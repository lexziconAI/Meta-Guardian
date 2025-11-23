import os
import sys
import traceback

# Add backend to path FIRST (before any imports)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from waitress import serve
from fastapi import FastAPI

print("🔍 Initializing Waitress Server...")

try:
    print("   - Importing main application...")
    from main import app as fastapi_app
    print("   - Main application imported successfully.")
except Exception as e:
    print(f"❌ CRITICAL ERROR importing main.py: {e}")
    traceback.print_exc()
    sys.exit(1)

if __name__ == "__main__":
    print("🚀 Starting MetaGuardian Backend (Waitress WSGI Mode)...")
    print("ℹ️  This is a production-grade WSGI server for maximum stability on Windows")
    
    try:
        # Use a2wsgi to convert ASGI to WSGI for Waitress
        from a2wsgi import ASGIMiddleware
        wsgi_app = ASGIMiddleware(fastapi_app)
        
        print(f"✅ Waitress server starting on http://0.0.0.0:8000 with app: {wsgi_app}")
        serve(wsgi_app, host='0.0.0.0', port=8000, threads=4)
        print("⚠️ Waitress serve() returned unexpectedly.")
        
    except ImportError:
        print("❌ Missing a2wsgi. Installing...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "a2wsgi"])
        
        from a2wsgi import ASGIMiddleware
        wsgi_app = ASGIMiddleware(fastapi_app)
        serve(wsgi_app, host='0.0.0.0', port=8000, threads=4)
        
    except KeyboardInterrupt:
        print("\n⚠️ Server stopped by user (Ctrl+C)")
        sys.exit(0)

    except Exception as e:
        print(f"❌ Server crashed: {e}")
        traceback.print_exc()
        sys.exit(1)
