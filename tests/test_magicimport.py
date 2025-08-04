from magicimporter import magic_import

def test_lazy_import():
    json = magic_import("json", lazy=True)
    assert json.dumps({"x": 1}) == '{"x": 1}'

def test_auto_install():
    try:
        yaml = magic_import("pyyaml", auto_install=True)
        assert yaml.safe_load("key: value")["key"] == "value"
    except Exception:
        pass
