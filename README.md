# Coding with AI: Starter Project

This is the starter project for the Coding with AI tutorial at Macalester.
In about two hours, you'll build a small project with Claude Code.
You don't need an idea yet. Claude will help you find one.

## My project

**Hoenn Puzzle Adventure** is a Pokémon text adventure with no battles.
You pick Spheal, Seedot or Litwick from Professor Kestrel in Littleroot Town.
The other two join you along the way.
To get past each obstacle, you pick a Pokémon and then one of its moves.
Each Pokémon has a move for each of its two types plus one Normal move.
Water puts out fires, Ice freezes rivers, Dark sneaks past sleepers and Ghost slips through doors.
Puzzles take several steps, and the order matters. A wrong move can set you back a step.
Later puzzles need two friends working together, like Fire and Water making steam.
When your Pokémon help solve puzzles, your friendship grows and they evolve.
The goal is the journey: make friends and become a smart problem solver.

Professors are named after North American birds, not trees.

Run it with:

```
python3 main.py
```

While you play, type `team` to check on your friends, `hug` to hug them,
`help` to see the commands or `quit` to stop.

## Before you start

You need:

- Access to Claude. Accept the email invite from us before you start.
- A GitHub account.
- [VS Code](https://code.visualstudio.com/) and [GitHub Desktop]([https://git-scm.com/downloads](https://desktop.github.com/download/) on your laptop.

## Set up

1. Fork this repo. Click **Fork** at the top right of this page.
2. Clone this repo in GitHub desktop.
3. Open the repo in VS Code.
4. TOpen a terminal: **Terminal > New Terminal**.
5. Install Claude Code. You only do this once.
   - Mac or Linux: `curl -fsSL https://claude.ai/install.sh | bash`
   - Windows: `irm https://claude.ai/install.ps1 | iex`
6. Start up claude: `claude`

Stuck? Ask an instructor, or see the [setup guide](https://code.claude.com/docs/en/setup).

## Build your project

Say hi to Claude. It will walk you through four steps:

1. **Brainstorm** an idea that fits in two hours.
2. **Plan** it. Claude will ask you to turn on plan mode with **Shift+Tab**.
   Then it will ask you a few questions.
3. **Describe and sketch** it. Claude writes a short description under "My project" above.
   It also sets up a skeleton of your project. Then it helps you commit both.
4. **Build** it in small steps. Commit each time something works.

Press **Esc** to stop Claude at any time.

## Change Claude's personality

Claude talks like a pirate. Why? Open `CLAUDE.md` to find out.
Claude reads that file at the start of every session.

Once you get going, rewrite the "Personality" section of `CLAUDE.md`.
Then type `/exit` and run `claude` again to meet your new Claude.
