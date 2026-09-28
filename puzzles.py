"""Puzzle data. Each puzzle is solved by a Pokemon with the right type."""

# Act 1: one puzzle per starter type, so the first puzzle always fits your starter.
ACT1 = {
    "Water": {
        "scene": "A campfire someone left burning has spread to the grass on Route 101.",
        "solution": "Water",
        "success": "{name} sprays a cool jet of water. The flames hiss and go out!",
        "hint": "What puts out a fire?",
    },
    "Grass": {
        "scene": "A small stream blocks Route 101. There is no bridge.",
        "solution": "Grass",
        "success": "{name} grows long vines across the stream. You walk over the vine bridge!",
        "hint": "Plants can grow across a gap.",
    },
    "Fire": {
        "scene": "A thick, tangled rope blocks the gate on Route 101.",
        "solution": "Fire",
        "success": "{name} glows brightly and burns through the rope. The gate swings open!",
        "hint": "What could burn a rope away?",
    },
}
