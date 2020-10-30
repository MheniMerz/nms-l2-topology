
class Link:
    def __init__(self, interfaces: ["Interface"]):
        self.interfaces = interfaces

    def to_string(self) -> str:
        return "<-->".join(i.name for i in self.interfaces)
