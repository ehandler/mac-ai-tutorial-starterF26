"""Hoenn Puzzle Adventure: a Pokemon text game about friendship and problem solving."""

from pokemon import make_trio
from puzzles import ACT1


def ask(prompt):
    """Read a line from the player. Typing 'quit' ends the game."""
    answer = input(prompt).strip()
    if answer.lower() == "quit":
        print("\nSee you next time, trainer!")
        raise SystemExit
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
            return starter
        print("Please type 1, 2 or 3.")


def solve_puzzle(puzzle, team):
    """Show a puzzle and keep asking until the player picks the right Pokemon."""
    print("\n" + puzzle["scene"])
    while True:
        print("Who can help?")
        for number, pokemon in enumerate(team, start=1):
            print(f"  {number}. {pokemon}")
        answer = ask("> ")
        if not answer.isdigit() or not 1 <= int(answer) <= len(team):
            print(f"Please type a number from 1 to {len(team)}.")
            continue
        helper = team[int(answer) - 1]
        if helper.has_type(puzzle["solution"]):
            print(puzzle["success"].format(name=helper.name))
            helper.add_friendship()
            return helper
        print(f"{helper.name} tries its best, but it doesn't work. Hint: {puzzle['hint']}")


def main():
    print("=== Hoenn Puzzle Adventure ===\n")
    print("You wake up in Littleroot Town. Today is the day you get your first Pokemon!\n")

    trio = make_trio()
    starter = choose_starter(trio)
    team = [starter]

    # Act 1: a puzzle that fits your starter's type.
    starter_type = starter.types[0]
    solve_puzzle(ACT1[starter_type], team)

    print("\nThe road ahead is open. Your adventure is just beginning...")
    print("(More coming soon!)")


if __name__ == "__main__":
    main()
