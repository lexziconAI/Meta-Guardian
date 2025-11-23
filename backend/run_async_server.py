import uvicorn
import os
import sys
import asyncio

# Add backend to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

async def main():
    config = uvicorn.Config(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
        loop="asyncio",
        http="h11",
        ws="wsproto"
    )
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    print("🚀 Starting MetaGuardian Backend (Asyncio Mode)...")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("⚠️ Server stopped by user")
    except Exception as e:
        print(f"❌ Server crashed: {e}")
