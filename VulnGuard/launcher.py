import subprocess
import webbrowser
import time
import os
import sys

# =====================
# 📦 BASE PATH FIX
# =====================
def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

BASE_DIR = get_base_path()

# =====================
# 🚀 START BACKEND
# =====================
def start_backend():
    backend_path = os.path.join(BASE_DIR, "backend", "main.py")

    if not os.path.exists(backend_path):
        print("❌ Backend not found:", backend_path)
        return

    python_exe = sys.executable if getattr(sys, 'frozen', False) else sys.executable

    subprocess.Popen(
        [python_exe, backend_path],
        cwd=os.path.join(BASE_DIR, "backend")
    )

# =====================
# 🌐 OPEN FRONTEND
# =====================
def open_frontend():
    time.sleep(2)

    frontend_path = os.path.join(BASE_DIR, "frontend", "index.html")

    if not os.path.exists(frontend_path):
        print("❌ Frontend not found:", frontend_path)
        return

    webbrowser.open("file://" + frontend_path)

# =====================
# 🚀 MAIN
# =====================
if __name__ == "__main__":
    print("VulnGuard starting...")

    print("Base DIR:", BASE_DIR)

    start_backend()
    open_frontend()