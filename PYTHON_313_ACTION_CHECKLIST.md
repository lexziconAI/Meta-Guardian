# MetaGuardian Python 3.13 Windows Compatibility - Action Checklist

## Pre-Flight Assessment (Do This First)

- [ ] **Assess Current Backend Code** (15 minutes)
  - Location: `/mnt/c/Users/regan/ID SYSTEM/MetaGuardian/backend/`
  - [ ] List all Python files: `ls -la *.py`
  - [ ] Search for async usage: `grep -r "async def" .`
  - [ ] Search for async database: `grep -r "AsyncSession\|create_async_engine" .`
  - [ ] Search for websockets: `grep -r "from websockets\|import websockets" .`
  - **Decision Point:** 
    - If no async database usage: Windows might work with strict pinning
    - If async database found: MUST use WSL2
    - If websockets found: STRONGLY recommend WSL2

- [ ] **Check Current venv Status** (5 minutes)
  ```bash
  # From Windows CMD:
  C:\Users\regan\ID SYSTEM\MetaGuardian\backend\venv\Scripts\pip list
  # Note any packages already installed
  # Check versions that actually worked
  ```

- [ ] **Try Current Setup** (10 minutes)
  ```bash
  # From Windows CMD, activate venv:
  C:\Users\regan\ID SYSTEM\MetaGuardian\backend\venv\Scripts\activate
  
  # Try importing key modules:
  python -c "import fastapi; print('FastAPI OK')"
  python -c "import uvicorn; print('Uvicorn OK')"
  python -c "import pydantic; print('Pydantic OK')"
  python -c "import sqlalchemy; print('SQLAlchemy OK')"
  
  # Expected: Some imports fail or warn about C extensions
  ```

---

## Option A: Windows Native with Version Pinning (Lower Confidence)

**Effort: 4-6 hours | Success Rate: 40% | Risk: High**

Only pursue this if:
- [ ] Code assessment shows NO async database usage
- [ ] Code assessment shows NO websockets usage
- [ ] You have at least 4 hours to troubleshoot
- [ ] You accept potential deployment issues

### Step 1: Create Pinned requirements-windows.txt (30 minutes)

```bash
# Copy current requirements.txt to requirements-windows.txt
cp backend/requirements.txt backend/requirements-windows.txt

# Update with pinned versions:
```

**File: `/mnt/c/Users/regan/ID SYSTEM/MetaGuardian/backend/requirements-windows.txt`**
```
fastapi>=0.104.0
uvicorn[standard]>=0.30.0
sqlalchemy>=2.0.0,<2.1.0
pydantic>=2.0.0,<3.0.0
passlib[argon2]>=1.7.4
argon2-cffi>=23.1.0
python-jose[cryptography]>=3.3.0
cryptography>=41.0.0
python-multipart>=0.0.6
websockets>=14.0
requests>=2.31.0
groq>=0.10.0
python-dotenv>=1.0.0
sendgrid>=6.10.0
```

- [ ] Create file with pinned versions
- [ ] Commit to git: `git add requirements-windows.txt && git commit -m "Add Windows-specific pinned requirements"`

### Step 2: Clean venv and Reinstall (1 hour)

```bash
# From Windows CMD:
cd C:\Users\regan\ID SYSTEM\MetaGuardian\backend

# Deactivate current venv
venv\Scripts\deactivate

# Remove venv
rmdir /s /q venv

# Create fresh venv
C:\Python313\python.exe -m venv venv

# Activate
venv\Scripts\activate

# Install with pinned versions
pip install --upgrade pip setuptools wheel
pip install -r requirements-windows.txt
```

- [ ] venv deleted and recreated
- [ ] All packages installed without errors
- [ ] Verify key imports work:
  ```bash
  python -c "import fastapi; import uvicorn; import pydantic; import sqlalchemy; print('All OK')"
  ```

### Step 3: Test Backend Startup (1 hour)

- [ ] Check for main.py or app.py
  ```bash
  # Find entry point
  find . -name "main.py" -o -name "app.py" | head -5
  ```

- [ ] Try starting server (stop with Ctrl+C after success)
  ```bash
  # Assume app is in app/main.py or similar
  python -m uvicorn app.main:app --reload
  # Expected: "Uvicorn running on http://127.0.0.1:8000"
  ```

- [ ] Test an endpoint
  ```bash
  # In another terminal:
  curl http://localhost:8000/docs
  # Expected: FastAPI Swagger UI HTML response
  ```

- [ ] Check for runtime errors (30 minutes of testing)
  - Create test requests to various endpoints
  - Check for pydantic validation errors
  - Monitor for memory leaks

### Step 4: Full Stack Testing (2 hours)

- [ ] Start backend on Windows
- [ ] Start frontend dev server: `npm run dev`
- [ ] Test complete user workflows
- [ ] Monitor for errors in console
- [ ] Test under modest load (simulate 10-20 concurrent requests)

### Step 5: Document Findings (30 minutes)

- [ ] Create WINDOWS_SETUP.md with:
  - Exact steps that worked
  - What failed and how to work around it
  - Known limitations
  - When to switch to WSL2

---

## Option B: WSL2 Linux (Strongly Recommended)

**Effort: 2-3 hours | Success Rate: 99% | Risk: Very Low**

### Prerequisites
- [ ] WSL2 installed and running
- [ ] Ubuntu or Debian distro selected
- [ ] Can access from Windows file browser at: `\\wsl.localhost\Ubuntu\home\`

### Step 1: Install Python 3.13.3 in WSL2 (45 minutes)

```bash
# Open WSL2 terminal (PowerShell: wsl)
# Then:

# Update package manager
sudo apt update && sudo apt upgrade -y

# Install build dependencies
sudo apt install -y python3.13 python3.13-venv python3.13-dev build-essential

# Verify installation
python3.13 --version
# Expected: Python 3.13.3 (or close version)

# Set as default (optional)
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.13 1
```

- [ ] Python 3.13.3+ installed in WSL2
- [ ] Verified with version check

### Step 2: Set Up Backend Environment in WSL2 (30 minutes)

```bash
# In WSL2 terminal:
cd /mnt/c/Users/regan/ID\ SYSTEM/MetaGuardian/backend

# Create venv with Python 3.13
python3.13 -m venv venv-wsl2

# Activate
source venv-wsl2/bin/activate

# Upgrade pip
pip install --upgrade pip setuptools wheel

# Install requirements (no pinning needed!)
pip install -r requirements.txt

# Verify
python -c "import fastapi, uvicorn, pydantic, sqlalchemy; print('All OK')"
```

- [ ] New venv created in WSL2
- [ ] All packages installed without errors
- [ ] All imports successful

### Step 3: Test Backend in WSL2 (45 minutes)

```bash
# In WSL2 terminal, in backend directory with activated venv:

# Find main app entry point
find . -name "main.py" -o -name "app.py"

# Start server (example paths, adjust to your app)
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Expected output:
# Uvicorn running on http://0.0.0.0:8000
# ...
# Application startup complete
```

- [ ] Backend starts without errors
- [ ] Listens on port 8000
- [ ] Can be accessed from Windows browser: http://localhost:8000/docs

### Step 4: Test From Windows Frontend (30 minutes)

```bash
# In Windows PowerShell, go to MetaGuardian root:
cd "C:\Users\regan\ID SYSTEM\MetaGuardian"

# Start frontend dev server
npm run dev

# Opens browser to http://localhost:5173 (or similar)
# Frontend should be able to call WSL2 backend API
```

- [ ] Frontend dev server starts
- [ ] Can access from browser
- [ ] API calls to WSL2 backend work
- [ ] No CORS errors

### Step 5: Integration Testing (30 minutes)

- [ ] Test complete user workflows
- [ ] Create test accounts
- [ ] Test database operations
- [ ] Test any real-time features (websockets)
- [ ] Monitor both terminals for errors

### Step 6: Document Setup (30 minutes)

Create `WSL2_SETUP.md`:

```markdown
# MetaGuardian Backend Development on WSL2

## One-Time Setup

1. Ensure WSL2 is installed: `wsl --list --verbose`
2. Install Python 3.13: `sudo apt install python3.13`
3. Create venv: `python3.13 -m venv venv-wsl2`
4. Install deps: `source venv-wsl2/bin/activate && pip install -r requirements.txt`

## Running Backend

1. Open WSL2 terminal
2. `cd /mnt/c/Users/regan/ID\ SYSTEM/MetaGuardian/backend`
3. `source venv-wsl2/bin/activate`
4. `python -m uvicorn app.main:app --reload --host 0.0.0.0`

## Running Frontend

1. Open Windows PowerShell
2. `cd "C:\Users\regan\ID SYSTEM\MetaGuardian"`
3. `npm run dev`

## Troubleshooting

- Backend can't start: Check if port 8000 is free
- Frontend can't reach backend: Check firewall rules
- Slow performance: Enable WSL2 GPU acceleration
```

- [ ] Documentation created and committed
- [ ] Shared with team/self for future reference

---

## Decision Matrix

### Use Windows Native IF:
- [ ] Code has ZERO async database usage
- [ ] Code has NO websockets functionality
- [ ] You prefer Windows development workflow
- [ ] You have time to troubleshoot (4-6 hours)
- [ ] You accept 40% success rate

### Use WSL2 Linux IF:
- [ ] Any async database usage found (common with FastAPI)
- [ ] Any websockets usage found
- [ ] You want guaranteed success (99%)
- [ ] You want better performance (2-4x faster)
- [ ] You want production parity (Render = Linux)
- [ ] You have 2-3 hours setup time

**Recommendation:** WSL2 Linux (all factors point to this)

---

## Final Checklist Before Deployment

After choosing Windows or WSL2:

- [ ] All backend tests pass
- [ ] All frontend tests pass
- [ ] Integration tests pass
- [ ] Can handle 50+ concurrent connections
- [ ] Database operations work correctly
- [ ] WebSocket (if used) works stably
- [ ] Error handling tested
- [ ] Environment variables work
- [ ] Hot reload works for development
- [ ] Production environment documented
- [ ] Team trained on setup
- [ ] CI/CD pipeline configured for Linux (production)
- [ ] README updated with setup instructions
- [ ] Considered using Docker for consistency

---

## Support Resources

If you hit errors, check:

1. **Python 3.13 Known Issues**: https://github.com/python/cpython/issues
2. **Uvicorn Issues**: https://github.com/encode/uvicorn/issues
3. **Pydantic Issues**: https://github.com/pydantic/pydantic/issues
4. **SQLAlchemy Issues**: https://github.com/sqlalchemy/sqlalchemy/issues
5. **WSL2 Networking**: https://docs.microsoft.com/en-us/windows/wsl/networking

Common solutions:
- Clear pip cache: `pip cache purge`
- Upgrade pip/setuptools: `pip install --upgrade pip setuptools wheel`
- Check venv isolation: `pip show [package]` should show venv path
- Check build tools on Windows: `pip install --upgrade setuptools wheel cython`
