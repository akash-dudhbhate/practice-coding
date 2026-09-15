"""SOLUTION: Build Profile + Format (Hard)"""
def build_profile(name, **info):
    return {"name": name, **info}

def format_profile(profile):
    name = profile["name"]
    info_str = ", ".join(f"{k}={v}" for k, v in profile.items() if k != "name")
    return f"{name} ({info_str})"

if __name__ == "__main__":
    p = build_profile("Akash", role="dev", level=5)
    assert p["name"] == "Akash"
    assert p["role"] == "dev"
    f = format_profile(p)
    assert "Akash" in f and "role=dev" in f
    print("All tests passed!")
