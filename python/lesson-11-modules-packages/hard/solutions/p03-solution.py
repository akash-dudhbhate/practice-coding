"""SOLUTION: Plugin System (Hard)"""
import importlib
import os

def load_plugins(plugins_dir):
    """Dynamically load all .py files from a directory as plugins."""
    plugins = []
    if not os.path.isdir(plugins_dir):
        return plugins
    for filename in os.listdir(plugins_dir):
        if filename.endswith(".py") and not filename.startswith("_"):
            modname = filename[:-3]
            spec = importlib.util.spec_from_file_location(
                modname, os.path.join(plugins_dir, filename)
            )
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            if hasattr(mod, "run"):
                plugins.append(mod)
    return plugins

# Example plugin (would be in plugins/hello.py):
# def run():
#     print("Hello from plugin!")

if __name__ == "__main__":
    # Create a test plugin
    import tempfile
    d = tempfile.mkdtemp()
    with open(os.path.join(d, "test_plugin.py"), "w") as f:
        f.write("def run():\n    return 'plugin ran'\n")
    plugins = load_plugins(d)
    assert len(plugins) == 1
    assert plugins[0].run() == "plugin ran"
    print("All tests passed!")
