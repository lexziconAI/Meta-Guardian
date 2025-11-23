import uvicorn
import os
import sys
import asyncio
import signal

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
    
    # Override signal handlers to prevent premature exit
    loop = asyncio.get_running_loop()
    
    # Windows doesn't support add_signal_handler for SIGINT/SIGTERM in the same way as Unix
    # But we can try to catch KeyboardInterrupt in the run loop
    
    await server.serve()

if __name__ == "__main__":
    print("🚀 Starting MetaGuardian Backend (Fractal Robust Mode)...")
    try:
        # Use WindowsProactorEventLoopPolicy if on Windows
        if sys.platform == 'win32':
            asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
            
        asyncio.run(main())
    except KeyboardInterrupt:
        print("⚠️ Server stopped by user")
    except Exception as e:
        print(f"❌ Server crashed: {e}")
