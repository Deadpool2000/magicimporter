import subprocess
import sys

def ensure_package_installed(package_name, install_args=None):
    install_args = install_args or []
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name, *install_args])
