from .installer import ensure_package_installed
from .lazy import lazy_import

def magic_import(module_name, *, lazy=False, auto_install=False, install_args=None):
    try:
        if lazy:
            return lazy_import(module_name)
        return __import__(module_name)
    except ModuleNotFoundError as e:
        if auto_install:
            print(f"[magicimporter] Installing missing package: {module_name}")
            ensure_package_installed(module_name, install_args)
            return __import__(module_name) if not lazy else lazy_import(module_name)
        else:
            raise e
