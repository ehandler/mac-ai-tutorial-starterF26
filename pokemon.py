"""Pokemon partners: their evolution lines, types and friendship."""


class Pokemon:
    def __init__(self, line, types):
        self.line = line        # three names, e.g. ["Spheal", "Sealeo", "Walrein"]
        self.types = types      # e.g. ["Water", "Ice"]
        self.stage = 0          # index into self.line
        self.friendship = 0

    @property
    def name(self):
        return self.line[self.stage]

    def has_type(self, type_name):
        return type_name in self.types

    def __str__(self):
        return f"{self.name} ({'/'.join(self.types)})"


def make_trio():
    """Return a fresh copy of the three partner Pokemon, keyed by main type."""
    return {
        "Water": Pokemon(["Spheal", "Sealeo", "Walrein"], ["Water", "Ice"]),
        "Grass": Pokemon(["Seedot", "Nuzleaf", "Shiftry"], ["Grass", "Dark"]),
        "Fire": Pokemon(["Litwick", "Lampent", "Chandelure"], ["Fire", "Ghost"]),
    }
