import uvicorn
import os
import sys

# Add backend to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    print("🚀 Starting MetaGuardian Backend via Python Script...")
    try:
        # Force compatibility settings for Python 3.13
        uvicorn.run(
            "main:app", 
            host="127.0.0.1", 
            port=8000, 
            workers=1, 
            loop="asyncio", 
            http="h11", 
            ws="wsproto",
            log_level="info"
        )
    except Exception as e:
        print(f"❌ Server crashed with error: {e}")
    
    print("⚠️ Server process exited.")
