"""SOLUTION: Config Loader (Hard)"""
import json

class ConfigError(Exception):
    pass

def config_loader(path):
    try:
        with open(path, "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        raise ConfigError(f"Config file not found: {path}")
    except json.JSONDecodeError:
        raise ConfigError(f"Invalid JSON in config: {path}")
    if "host" not in config:
        raise ConfigError("Config must contain 'host' key")
    return config

if __name__ == "__main__":
    with open("/tmp/test_cfg.json", "w") as f:
        json.dump({"host": "localhost", "port": 8080}, f)
    cfg = config_loader("/tmp/test_cfg.json")
    assert cfg["host"] == "localhost"
    with open("/tmp/test_cfg2.json", "w") as f:
        json.dump({"port": 8080}, f)
    try:
        config_loader("/tmp/test_cfg2.json")
        assert False
    except ConfigError:
        pass
    print("All tests passed!")
