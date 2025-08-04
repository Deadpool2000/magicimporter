import importlib
import types

class LazyModule(types.ModuleType):
    def __init__(self, name):
        super().__init__(name)
        self._module = None
        self._name = name

    def _load(self):
        if self._module is None:
            print(f"[magicimporter] Lazy-loading module: {self._name}")
            self._module = importlib.import_module(self._name)

    def __getattr__(self, item):
        self._load()
        return getattr(self._module, item)

    def __dir__(self):
        self._load()
        return dir(self._module)

def lazy_import(module_name):
    return LazyModule(module_name)
