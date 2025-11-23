import uvicorn
import sys
import os

# Ensure we can import main
sys.path.append(os.getcwd())

if __name__ == "__main__":
    print("Starting Uvicorn programmatically...")
    try:
        uvicorn.run("main:app", host="127.0.0.1", port=8002, log_level="debug")
    except Exception as e:
        print(f"Uvicorn crashed: {e}")
    print("Uvicorn run finished.")
