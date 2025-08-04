# 🪄 magicimporter

**Smart Python import wrapper** that makes your imports lazier, safer, and smarter.

> Written by a developer who's tired of writing `try: import ... except: install ...` everywhere.

---

## 🚀 What It Does

magicimporter is a tiny utility that helps you:

✅ **Lazy-load modules** - defer importing until first access  
✅ **Auto-install missing packages** - no more `pip install` errors  
✅ **Avoid clutter** - wrap your imports cleanly and clearly  
✅ **Support optional dependencies** - without breaking your app

Perfect for:
- Notebooks and prototyping
- Reducing startup time (e.g., in CLI tools)
- Handling optional packages gracefully
- Plug-and-play with any Python script

---

## 📦 Installation

### From PyPI (soon):
```bash
pip install magicimporter
```

### From source:
```bash
git clone https://github.com/Deadpool2000/magicimporter
cd magicimporter
pip install -e .
```

---

## 🔧 How to Use

### Basic Usage

```python
from magicimporter import magic_import

json = magic_import("json")  # Just works like import
print(json.dumps({"hello": "world"}))
```

---

### Lazy Import (delay loading until accessed)

```python
np = magic_import("numpy", lazy=True)

# numpy isn’t imported until this line:
print(np.array([1, 2, 3]))
```

---

### Auto-Install Missing Packages

```python
requests = magic_import("requests", auto_install=True)

res = requests.get("https://httpbin.org/get")
print(res.status_code)
```

---

### Lazy + Auto-Install Together

```python
pandas = magic_import("pandas", lazy=True, auto_install=True)

# Nothing is loaded yet...
print("About to create DataFrame")

df = pandas.DataFrame({"a": [1, 2, 3]})  # Now pandas loads
print(df)
```

---

### Import Submodules

```python
os_path = magic_import("os.path", lazy=True)
print(os_path.basename("/foo/bar.txt"))
```

---

### Optional Dependencies Pattern

```python
try:
    yaml = magic_import("pyyaml", auto_install=False)
    config = yaml.safe_load(open("config.yaml"))
except ModuleNotFoundError:
    print("Skipping YAML config support: dependency missing")
```

---

## 📁 Directory Structure

```txt
magicimporter/
├── magicimporter/
│   ├── __init__.py
│   ├── core.py          # main logic
│   ├── lazy.py          # lazy loader
│   └── installer.py     # auto-installer
├── examples/
│   └── demo.py
├── tests/
│   └── test_magicimporter.py
├── setup.py
├── pyproject.toml
└── README.md
```

---

## 🧪 Running Tests

```bash
pytest tests/
```

You can also test individual features manually from `examples/demo.py`.

---

## 🧠 Why This Exists

You're writing a script or notebook and hit this:

```python
import somepackage  # ModuleNotFoundError
```

Then you type:

```bash
pip install somepackage
```

And do it again. And again.  
What if your code just handled that?  
That's what magicimporter does.

It’s especially useful when:
- Building CLI tools with optional features
- Using heavy modules only in specific branches
- Rapid prototyping in notebooks or scripts

---

## 📌 Notes & Caveats

- Auto-install uses `subprocess` to call pip - no fancy API yet.
- Lazy import doesn't delay sub-imports inside a module (standard Python behavior).
- Use responsibly in production: implicit installs may surprise your users.

---

## 🛠️ Roadmap Ideas

- [ ] Async import support
- [ ] Config file or env variable overrides
- [ ] Warnings and logging customization
- [ ] Module-level caching

---

## 👨‍💻 Author

Made with care by Deadpool2000 – feel free to fork, extend, or PR ideas!

---

## 📄 License

MIT – use it, hack it, ship it.
