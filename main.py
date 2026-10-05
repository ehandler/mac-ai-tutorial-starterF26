"""Hoenn Puzzle Adventure: a Pokemon text game about friendship and problem solving."""

from pokemon import make_trio
from puzzles import ACT1, ACT2, ACT3, MEETINGS

# The order you meet the others depends on your starter: Water -> Grass -> Fire -> Water.
TYPE_ORDER = ["Water", "Grass", "Fire"]

HELP = "Commands: type a number to choose, 'team' to see your friends, 'hug' to hug them, 'quit' to stop."

# Counts for the journey recap at the end.
stats = {"steps": 0, "ideas_tried": 0, "missed": 0}


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


def choose_number(prompt, count, team, allow_back=False):
    """Ask for a number from 1 to count. Returns None if the player types 'back'."""
    while True:
        answer = ask(prompt, team)
        if allow_back and answer.lower() == "back":
            return None
        if answer.isdigit() and 1 <= int(answer) <= count:
            return int(answer)
        extra = " (or 'back')" if allow_back else ""
        print(f"Please type a number from 1 to {count}{extra}.")


def pick_move(team, question="Who can help?", exclude=None):
    """Pick a Pokemon, then one of its moves. Returns (pokemon, move)."""
    while True:
        if len(team) == 1:
            helper = team[0]
        else:
            print(question)
            for number, pokemon in enumerate(team, start=1):
                print(f"  {number}. {pokemon}")
            helper = team[choose_number("> ", len(team), team) - 1]
        if helper is exclude:
            print(f"{helper.name} is already helping! Pick a different friend.\n")
            continue
        print(f"What should {helper.name} do?")
        for number, move in enumerate(helper.moves, start=1):
            print(f"  {number}. {move['name']}")
        choice = choose_number("> ", len(helper.moves), team, allow_back=len(team) > 1)
        if choice is None:
            continue
        return helper, helper.moves[choice - 1]


def solve_step(step, team, misses, first_time=True):
    """Play one step. Returns True if solved, or the step index to go back to after a setback.

    Friendship only grows the first time a step is solved, not when redoing it after a setback.
    """
    solution = step["solution"]
    if isinstance(solution, list):
        print("This needs teamwork! Pick two friends to work together.")
        first = pick_move(team, "Who goes first?")
        second = pick_move(team, "Who helps them?", exclude=first[0])
        helpers = [first, second]
        tried = sorted(move["type"] for _, move in helpers)
        solved = tried == sorted(solution)
    else:
        helpers = [pick_move(team)]
        move = helpers[0][1]
        tried = move["type"]
        solved = solution in (move["type"], move["name"])
    stats["ideas_tried"] += 1

    if solved:
        if len(helpers) == 1:
            pokemon, move = helpers[0]
            print(step["success"].format(name=pokemon.name, move=move["name"]))
        else:
            (p1, m1), (p2, m2) = helpers
            print(step["success"].format(name1=p1.name, move1=m1["name"], name2=p2.name, move2=m2["name"]))
        if first_time:
            for pokemon, _ in helpers:
                pokemon.add_friendship()
            stats["steps"] += 1
        return True

    # A miss: show a fun reaction, maybe a setback, and a hint if the player seems stuck.
    names = " and ".join(f"{pokemon.name} uses {move['name']}" for pokemon, move in helpers)
    mistakes = step.get("mistakes", {})
    if isinstance(tried, str):
        key = helpers[0][1]["name"]
        mistake = mistakes.get(key) or mistakes.get(tried)
    else:
        key = "+".join(tried)
        mistake = mistakes.get(key)
    if mistake:
        print(f"{names}! " + mistake["text"].format(name=helpers[0][0].name))
    else:
        print(f"{names}! ...but nothing changes.")

    stats["missed"] += 1
    misses["total"] = misses.get("total", 0) + 1
    misses[key] = misses.get(key, 0) + 1
    if misses[key] >= 2 or misses["total"] >= 3:
        print(f"Your friends huddle close and think together. Hint: {step['hint']}")

    if mistake and "reset_to" in mistake:
        return mistake["reset_to"]
    return False


def play_puzzle(puzzle, team):
    """Play a puzzle step by step. Setbacks can send the player back to an earlier step."""
    print("\n" + puzzle["intro"])
    misses = {}     # one tally per step, kept even after a setback
    solved = set()  # steps solved at least once
    i = 0
    while i < len(puzzle["steps"]):
        step = puzzle["steps"][i]
        print("\n" + step["scene"])
        result = False
        while result is False:
            result = solve_step(step, team, misses.setdefault(i, {}), i not in solved)
        if result is True:
            solved.add(i)
            i += 1
        else:
            print("Oh no! You'll have to try that part again.")
            i = result


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
    print(f"\nYou solved {stats['steps']} puzzle steps and tried {stats['ideas_tried']} ideas.")
    extra = stats["missed"]
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
    play_puzzle(ACT1[starter_type], team)

    # Work out who you meet 2nd and 3rd, based on your starter.
    start = TYPE_ORDER.index(starter_type)
    second = trio[TYPE_ORDER[(start + 1) % 3]]
    third = trio[TYPE_ORDER[(start + 2) % 3]]

    meet(second, team)

    # Act 2: a puzzle that needs your new friend's type.
    print("\n--- Act 2: New Friends ---")
    play_puzzle(ACT2[second.types[0]], team)
    meet(third, team)

    # Act 3: two-step puzzles that need the whole team.
    print("\n--- Act 3: The Road to Shoal Cave ---")
    print("With all three friends together, you set off for Shoal Cave.")
    for puzzle in ACT3:
        play_puzzle(puzzle, team)

    # Finale: everyone shares the moment, and everyone's friendship grows.
    print("\nAt the bottom of Shoal Cave, the ice sparkles like stars.")
    print("Your team huddles close around you. You did it together!\n")
    for pokemon in team:
        pokemon.add_friendship()

    recap(team)
    print("\nThe End... of this chapter. Thanks for playing!")


if __name__ == "__main__":
    main()
