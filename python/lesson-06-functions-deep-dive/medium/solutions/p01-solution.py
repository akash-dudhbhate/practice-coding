"""SOLUTION: Make HTML Tag (Medium)"""
def make_tag(tag, text, **attrs):
    attr_str = ""
    for k, v in attrs.items():
        attr_str += f' {k}="{v}"'
    return f"<{tag}{attr_str}>{text}</{tag}>"

if __name__ == "__main__":
    assert make_tag("a", "link", href="x.com") == '<a href="x.com">link</a>'
    assert make_tag("p", "hi") == "<p>hi</p>"
    print("All tests passed!")
