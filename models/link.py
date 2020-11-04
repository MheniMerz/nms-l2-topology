
class Link:
    def __init__(self, ltps: ["Ltp"]):
        self.ltps = ltps

    def to_string(self) -> str:
        return "<-->".join(i.name for i in self.ltps)
