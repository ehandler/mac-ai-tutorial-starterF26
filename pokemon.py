"""Pokemon partners: their evolution lines, types and friendship."""

# Friendship needed to reach each stage: stage 1 at 2 points, stage 2 at 4 points.
EVOLVE_AT = [2, 4]


class Pokemon:
    def __init__(self, line, types, hug):
        self.line = line        # three names, e.g. ["Spheal", "Sealeo", "Walrein"]
        self.types = types      # e.g. ["Water", "Ice"]
        self.hug = hug          # how this Pokemon reacts to a hug
        self.stage = 0          # index into self.line
        self.friendship = 0

    @property
    def name(self):
        return self.line[self.stage]

    def has_type(self, type_name):
        return type_name in self.types

    def add_friendship(self, points=1):
        """Grow friendship, and evolve if it reaches the next threshold."""
        self.friendship += points
        print(f"{self.name}'s friendship grew! (friendship: {self.friendship})")
        while self.stage < len(EVOLVE_AT) and self.friendship >= EVOLVE_AT[self.stage]:
            old_name = self.name
            self.stage += 1
            print(f"\nWhat? {old_name} is glowing...")
            print(f"Your bond is so strong that {old_name} evolved into {self.name}!")

    def __str__(self):
        return f"{self.name} ({'/'.join(self.types)})"


def make_trio():
    """Return a fresh copy of the three partner Pokemon, keyed by main type."""
    return {
        "Water": Pokemon(
            ["Spheal", "Sealeo", "Walrein"], ["Water", "Ice"],
            "It's soft, fuzzy and squishy, and it claps its flippers happily!",
        ),
        "Grass": Pokemon(
            ["Seedot", "Nuzleaf", "Shiftry"], ["Grass", "Dark"],
            "Its leaves rustle happily and it smells like fresh pine.",
        ),
        "Fire": Pokemon(
            ["Litwick", "Lampent", "Chandelure"], ["Fire", "Ghost"],
            "Its flame glows warm and gentle, just for you.",
        ),
    }
