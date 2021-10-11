from differently.renderers.html import HtmlRenderer
from differently.change import Change


def test() -> None:
    renderer = HtmlRenderer([
        Change("foo", "foo"),
        Change("delete delete delete", None),
        Change("1 simple change", "a simple change"),
        Change(None, "new new new"),
    ])
    print(renderer.render())
    with open("foo.html", "w") as f:
        f.write(renderer.render())
    assert False
