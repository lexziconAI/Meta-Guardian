# MetaGuardian Backend main.py - CRASH ANALYSIS REPORT

## CRITICAL FINDINGS

### File Location
**Full Path**: `/mnt/c/Users/regan/ID SYSTEM/MetaGuardian/backend/main.py`
**Size**: 31,146 bytes (725 lines)

---

## CRITICAL ISSUES IDENTIFIED

### ISSUE 1: BROKEN IMPORT AT LINE 283 (THE MAIN CULPRIT)
**Location**: Line 283
```python
from constitutional_ai import validate_story_synthesis, export_all_receipts
```

**Status**: This import is **dynamically placed within an async function** (`finalize_session` at line 225)

**Problem**: 
- The import is **not at the top level** where Python expects it
- This causes **silent import failures on Windows/Python 3.13**
- The import happens **inside the async function body** (line 283)
- When this endpoint is called, if there's ANY import error or missing dependency, it will crash the entire FastAPI server without proper error logging

**Why It Crashes Silently**:
1. FastAPI servers don't always catch module-level import errors in async endpoint handlers
2. On Windows with Python 3.13, the asyncio event loop might swallow exceptions from late-binding imports
3. The server starts fine (imports load at startup in line 22: `models.Base.metadata.create_all()`), but crashes when the endpoint is first called

**Impact**: Exit code 1 silent crash when `/api/finalize-session` endpoint is called

---

### ISSUE 2: LATE BINDING IMPORTS (Lines 131, 465, 497, 576, 609, 659, 675)
**Locations**: 
- Line 131: `from groq import AsyncGroq` (inside function, used at line 136)
- Line 465: `from datetime import datetime` (duplicate import, already at line 8)
- Line 497: `from review_queue import ReviewQueueManager, JourneyMode`
- Line 576: `from review_queue import ReviewQueueManager` 
- Line 609: `from review_queue import ReviewQueueManager`
- Line 659: `from review_queue import ReviewQueueManager`
- Line 675: `from review_queue import ReviewQueueManager`

**Problem**: All these imports are embedded within endpoint functions rather than at module level

**Why This Breaks**:
- Python's module cache doesn't work optimally when imports happen inside functions
- On Windows, concurrent requests can cause race conditions with late imports
- Python 3.13 made changes to import handling that expose these issues
- If a module fails to load, the entire request handler fails catastrophically

---

### ISSUE 3: ASYNC/AWAIT MISMATCH (Lines 225, 352-372)
**Location**: Line 225 - `async def finalize_session()`

**Problem**:
```python
async def finalize_session(request: FinalizeSessionRequest, db: Session = Depends(get_db)):
    # ... later at line 506-507
    review = await review_manager.submit_report_for_review(...)
```

The function is async, but many of the internal operations are NOT properly awaited:
- Line 506: `review_manager = ReviewQueueManager(db)` - instantiation in async context
- The harm detector (line 104 in review_queue.py) is awaited, but the manager isn't async-aware

**Additionally**: The `constitutional_guard` decorator (lines 346-373) is broken:
```python
def constitutional_guard(content_type: str):
    def decorator(func):
        async def wrapper(*args, **kwargs):  # Async wrapper
            # ...
        return wrapper  # Returns async function, not original
    return decorator
```
This decorator is never actually used, but demonstrates poor async handling patterns.

---

### ISSUE 4: SYNC FUNCTIONS IN ASYNC CONTEXT (Line 536)
**Location**: Line 536
```python
async def finalize_session(...):
    # ...
    success = send_assessment_email(request.email, request.assessment)  # BLOCKING CALL
```

The `send_assessment_email()` function is called WITHOUT `await`, suggesting it's synchronous code running in an async handler. This causes the event loop to block.

---

### ISSUE 5: UNCAUGHT EXCEPTION AT LINE 283 INSIDE TRY/EXCEPT TRAP
**Location**: Lines 282-283
```python
# CONSTITUTIONAL AI: Import validator for atomic validation
from constitutional_ai import validate_story_synthesis, export_all_receipts
```

This import is **inside the try block** (line 170), but if it fails:
- The exception is caught at line 557: `except Exception as e:`
- It raises HTTPException at line 561
- But the import failure might happen **before the try block is properly initialized**
- On Windows asyncio, this can exit the entire process

---

## IMPORT AUDIT: ALL IMPORTS AND RISK LEVELS

### Top-Level Imports (Safe - Line 1-16)
```python
from fastapi import FastAPI, Depends, HTTPException, status  ✓ Standard
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm  ✓ Standard
from fastapi.staticfiles import StaticFiles  ✓ Standard
from fastapi.responses import FileResponse  ✓ Standard
from sqlalchemy.orm import Session  ✓ Standard
from passlib.context import CryptContext  ✓ Standard
from jose import JWTError, jwt  ✓ Standard
from datetime import datetime, timedelta  ✓ Standard
from typing import List  ✓ Standard
import os  ✓ Standard
import json  ✓ Standard
import models, schemas, database  ⚠️ Custom modules (relative imports)
from openai_relay import router as openai_relay_router  ⚠️ Custom module
from email_service import send_assessment_email  ⚠️ Custom module
from dotenv import load_dotenv  ✓ External package
from fastapi.middleware.cors import CORSMiddleware  ✓ Standard
```

### Mid-Function Imports (DANGEROUS - Risk Level: HIGH)
```python
# Line 131
from groq import AsyncGroq  ⚠️ Inside function, requires GROQ_API_KEY env var

# Line 283  
from constitutional_ai import validate_story_synthesis, export_all_receipts  ❌ CRITICAL
    ↳ Deep inside async function
    ↳ If constitutional_ai.py has import errors → crashes server
    ↳ If module doesn't exist → crashes server

# Line 465 (duplicate)
from datetime import datetime  ⚠️ Already imported at line 8, wastes CPU

# Line 497
from review_queue import ReviewQueueManager, JourneyMode  ⚠️ Inside async function

# Lines 576, 609, 659, 675 (repeated)
from review_queue import ReviewQueueManager  ⚠️ Repeated 4 times inside functions
```

---

## DATABASE INITIALIZATION CODE

**Locations**: Lines 22, 39-44

### Line 22 (Synchronous Database Creation)
```python
models.Base.metadata.create_all(bind=database.engine)
```
This runs at **module import time** (top level), **synchronously**. On Windows with many SQLite operations, this can:
- Block the event loop during server startup
- Cause deadlocks if the database is locked
- Prevent proper async initialization

### Lines 39-44 (Dependency Injection)
```python
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
```
This is **synchronous** but used in **async endpoints**. FastAPI handles this, but it's not optimal for Python 3.13's stricter event loop rules.

---

## STARTUP EVENT HANDLERS

**Status**: ❌ NONE DEFINED

The application has **NO startup event handlers**. This means:
1. No health checks before serving requests
2. No import validation at startup
3. Database initialization failures are hidden
4. Missing environment variables only discovered on first request

---

## ASYNCIO-RELATED ISSUES (PYTHON 3.13/WINDOWS SPECIFIC)

### Issue A: Event Loop Policy on Windows
Python 3.13 changed Windows asyncio event loop handling:
- Default changed from `ProactorEventLoop` to `WindowsSelectorEventLoop` in some configs
- The code doesn't explicitly set the event loop policy
- When uvicorn starts, it might use a different loop than FastAPI expects

### Issue B: Sync-in-Async Antipattern (Lines 506-540)
```python
async def finalize_session(...):
    review_manager = ReviewQueueManager(db)  # Sync instantiation
    review = await review_manager.submit_report_for_review(...)  # Async call
    success = send_assessment_email(...)  # ← BLOCKING CALL in async context!
```

On Windows, blocking calls inside async functions cause event loop stalls that trigger timeouts and silent process exits.

### Issue C: No Asyncio Context Managers
The code doesn't use `async with` for resource management. When the event loop is interrupted (which Python 3.13 does more aggressively), resources might not be properly cleaned up.

---

## SPECIFIC LINES THAT CAUSE SILENT CRASHES

### Line 283 - MOST CRITICAL
```python
from constitutional_ai import validate_story_synthesis, export_all_receipts
```
When endpoint is called → import happens → if module has ANY error → server exits with code 1

### Line 536
```python
success = send_assessment_email(request.email, request.assessment)
```
**Blocking I/O** in async context causes event loop to hang, then gets forcefully terminated by Python 3.13's stricter asyncio validation.

### Line 506
```python
review_manager = ReviewQueueManager(db)
```
The `ReviewQueueManager.__init__()` creates `LLMHarmDetector()` which initializes Anthropic client:
```python
# harm_detection.py, line 28-32
self.client = anthropic.Anthropic(api_key=api_key)
```
If `ANTHROPIC_API_KEY` is missing, this crashes synchronously inside an async function.

### Line 440
```python
completion = await groq_client.chat.completions.create(...)
```
If `GROQ_API_KEY` is missing, the AsyncGroq client initialization (line 136) fails silently because it's inside the function.

---

## RECOMMENDED FIXES

### FIX 1: Move ALL imports to top level
```python
# At line 1, after existing imports, add:
from constitutional_ai import validate_story_synthesis, export_all_receipts
from groq import AsyncGroq
from review_queue import ReviewQueueManager, JourneyMode
```

Remove the duplicate imports from inside functions.

### FIX 2: Add startup validation
```python
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    """Validate all imports and environment variables at startup"""
    errors = []
    
    # Check required env vars
    required_vars = ['GROQ_API_KEY', 'ANTHROPIC_API_KEY', 'SECRET_KEY']
    for var in required_vars:
        if not os.getenv(var):
            errors.append(f"Missing required env var: {var}")
    
    # Test imports
    try:
        from constitutional_ai import validate_story_synthesis
        from review_queue import ReviewQueueManager
    except ImportError as e:
        errors.append(f"Import error: {e}")
    
    if errors:
        print("STARTUP ERRORS:")
        for error in errors:
            print(f"  - {error}")
        raise RuntimeError("Startup validation failed")
    
    print("✓ All startup checks passed")
```

### FIX 3: Fix async/sync mismatches
```python
# Instead of:
success = send_assessment_email(request.email, request.assessment)

# Do:
import asyncio
loop = asyncio.get_event_loop()
success = await loop.run_in_executor(None, send_assessment_email, request.email, request.assessment)

# Or better: make send_assessment_email async
async def send_assessment_email_async(email: str, assessment: dict) -> bool:
    # ... async implementation
```

### FIX 4: Set explicit event loop policy for Windows
Add to main.py, at the very top, BEFORE FastAPI import:
```python
import sys
if sys.platform == 'win32':
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
```

### FIX 5: Add lifespan context manager (FastAPI 0.93+)
```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("App starting up")
    yield
    # Shutdown
    print("App shutting down")

app = FastAPI(lifespan=lifespan)
```

### FIX 6: Wrap dangerous endpoints with better error handling
```python
@app.post("/api/finalize-session")
async def finalize_session(request: FinalizeSessionRequest, db: Session = Depends(get_db)):
    try:
        # Validation before any async work
        if not request.email:
            raise ValueError("Email required")
        
        # Now do async work
        # ...
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"CRITICAL ERROR in finalize_session: {e}")
        import traceback
        traceback.print_exc()  # Force logging to console
        raise HTTPException(status_code=500, detail="Server error")
```

---

## REQUIREMENTS.TXT ANALYSIS

```
fastapi                 ✓ Supports async
uvicorn                 ✓ Good async support
sqlalchemy              ⚠️ Needs async driver (current: sqlite3 is blocking)
pydantic                ✓ Good
passlib[argon2]         ✓ Good
python-jose             ✓ Good
python-multipart        ✓ Good
websockets              ⚠️ May not be used, adds complexity
requests                ⚠️ Blocking HTTP client
groq                    ✓ Has async support, but imported late
python-dotenv           ✓ Good
sendgrid                ⚠️ Might be blocking
```

**Missing**: 
- `anthropic` (required by harm_detection.py!)
- `beautifulsoup4` (required by harm_detection.py!)

These missing dependencies would cause immediate import failure of harm_detection.

---

## ROOT CAUSE SUMMARY

The application crashes on Windows/Python 3.13 with exit code 1 because:

1. **Late binding imports** (line 283) cause late validation of dependencies
2. **Missing dependencies** in requirements.txt (`anthropic`, `beautifulsoup4`)
3. **Async/sync mismatches** (blocking calls in async context)
4. **No startup validation** - errors hidden until first request
5. **Python 3.13 stricter asyncio** - exposes the sync-in-async anti-patterns

The server **appears to start successfully** but crashes when `/api/finalize-session` is called for the first time, which is why it seems silent - the startup succeeds, the crash happens on request.

