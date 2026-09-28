"""Hoenn Puzzle Adventure: a Pokemon text game about friendship and problem solving."""

from pokemon import make_trio
from puzzles import ACT1, ACT2, ACT3, MEETINGS

# The order you meet the others depends on your starter: Water -> Grass -> Fire -> Water.
TYPE_ORDER = ["Water", "Grass", "Fire"]

HELP = "Commands: type a number to choose, 'team' to see your friends, 'hug' to hug them, 'quit' to stop."

# Counts for the journey recap at the end.
stats = {"puzzles": 0, "ideas_tried": 0}


def show_team(team):
    if not team:
        print("You don't have any Pokemon yet!")
        return
    print("\nYour team:")
    for pokemon in team:
        hearts = "<3 " * pokemon.friendship
        print(f"  {pokemon}  friendship: {pokemon.friendship}  {hearts}")
    print()


def hug_team(team):
    if not team:
        print("There's no one to hug yet. Soon!")
        return
    for pokemon in team:
        print(f"You give {pokemon.name} a big hug. {pokemon.hug}")
    print()


def ask(prompt, team=None):
    """Read a line from the player. Handles 'team', 'hug', 'help' and 'quit' along the way."""
    team = team or []
    while True:
        answer = input(prompt).strip()
        command = answer.lower()
        if command == "quit":
            print("\nSee you next time, trainer!")
            raise SystemExit
        elif command == "team":
            show_team(team)
        elif command == "hug":
            hug_team(team)
        elif command == "help":
            print(HELP)
        else:
            return answer


def choose_starter(trio):
    print("Professor Kestrel smiles. \"Every trainer needs a partner. Who will you choose?\"\n")
    choices = list(trio.values())
    for number, pokemon in enumerate(choices, start=1):
        print(f"  {number}. {pokemon}")
    while True:
        answer = ask("\nPick 1, 2 or 3: ")
        if answer in ("1", "2", "3"):
            starter = choices[int(answer) - 1]
            print(f"\nYou chose {starter.name}! It looks up at you happily.")
            print("Professor Kestrel nods. \"Remember: every problem has a clue. Look for it!\"")
            return starter
        print("Please type 1, 2 or 3.")


def solve_puzzle(puzzle, team):
    """Show a puzzle and keep asking until the player picks the right Pokemon."""
    print("\n" + puzzle["scene"])
    while True:
        print("Who can help?")
        for number, pokemon in enumerate(team, start=1):
            print(f"  {number}. {pokemon}")
        answer = ask("> ", team)
        if not answer.isdigit() or not 1 <= int(answer) <= len(team):
            print(f"Please type a number from 1 to {len(team)}.")
            continue
        stats["ideas_tried"] += 1
        helper = team[int(answer) - 1]
        if helper.has_type(puzzle["solution"]):
            print(puzzle["success"].format(name=helper.name))
            helper.add_friendship()
            stats["puzzles"] += 1
            return helper
        print(f"{helper.name} tries its best, but it doesn't work. Hint: {puzzle['hint']}")


def meet(pokemon, team):
    """Play a meeting scene. When the player chooses kindly, the Pokemon joins the team."""
    scene = MEETINGS[pokemon.types[0]]
    print("\n" + scene["scene"])
    while True:
        print("What do you do?")
        for number, choice in enumerate(scene["choices"], start=1):
            print(f"  {number}. {choice}")
        answer = ask("> ", team)
        if not answer.isdigit() or not 1 <= int(answer) <= len(scene["choices"]):
            print(f"Please type a number from 1 to {len(scene['choices'])}.")
            continue
        if int(answer) == scene["correct"]:
            print(scene["success"])
            team.append(pokemon)
            print(f"\n{pokemon.name} joined your team!")
            return
        print(scene["wrong"][int(answer)] + " Try something kinder.\n")


def recap(team):
    """Look back on the journey at the end of the game."""
    print("\n=== Your Journey ===")
    for pokemon in team:
        if pokemon.stage > 0:
            print(f"  {pokemon.line[0]} grew into {pokemon.name}.  friendship: {pokemon.friendship}")
        else:
            print(f"  {pokemon.name} is still growing.  friendship: {pokemon.friendship}")
    print(f"\nYou solved {stats['puzzles']} puzzles and tried {stats['ideas_tried']} ideas.")
    extra = stats["ideas_tried"] - stats["puzzles"]
    if extra == 0:
        print("You got every one on the first try. What a sharp problem solver!")
    else:
        ideas = "idea" if extra == 1 else "ideas"
        print(f"{extra} {ideas} didn't work, and each one taught you something. That's how smart trainers learn!")


def main():
    print("=== Hoenn Puzzle Adventure ===\n")
    print(HELP + "\n")
    print("You wake up in Littleroot Town. Today is the day you get your first Pokemon!\n")

    trio = make_trio()
    starter = choose_starter(trio)
    team = [starter]

    # Act 1: a puzzle that fits your starter's type.
    print("\n--- Act 1: First Steps ---")
    starter_type = starter.types[0]
    solve_puzzle(ACT1[starter_type], team)

    # Work out who you meet 2nd and 3rd, based on your starter.
    start = TYPE_ORDER.index(starter_type)
    second = trio[TYPE_ORDER[(start + 1) % 3]]
    third = trio[TYPE_ORDER[(start + 2) % 3]]

    meet(second, team)

    # Act 2: a puzzle that needs your new friend's type.
    print("\n--- Act 2: New Friends ---")
    solve_puzzle(ACT2[second.types[0]], team)
    meet(third, team)

    # Act 3: two-step puzzles that need the whole team.
    print("\n--- Act 3: The Road to Shoal Cave ---")
    print("With all three friends together, you set off for Shoal Cave.")
    for puzzle in ACT3:
        print("\n" + puzzle["intro"])
        for step in puzzle["steps"]:
            solve_puzzle(step, team)

    # Finale: everyone shares the moment, and everyone's friendship grows.
    print("\nAt the bottom of Shoal Cave, the ice sparkles like stars.")
    print("Your team huddles close around you. You did it together!\n")
    for pokemon in team:
        pokemon.add_friendship()

    recap(team)
    print("\nThe End... of this chapter. Thanks for playing!")


if __name__ == "__main__":
    main()
