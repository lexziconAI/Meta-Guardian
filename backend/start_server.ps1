$env:PYTHONPATH = "C:\Users\regan\ID SYSTEM\MetaGuardian\backend"
Set-Location "C:\Users\regan\ID SYSTEM\MetaGuardian\backend"
Write-Host "Starting MetaGuardian Backend (Waitress Stability Mode)..." -ForegroundColor Cyan
& "venv\Scripts\python" run_waitress_server.py