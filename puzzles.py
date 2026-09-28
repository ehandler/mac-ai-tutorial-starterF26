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

# Act 2: one puzzle per type, used for the second Pokemon you meet.
ACT2 = {
    "Water": {
        "scene": (
            "An old water mill blocks the path. The gate only opens when the wheel turns,\n"
            "but the stream that turns it has dried up."
        ),
        "solution": "Water",
        "success": "{name} fills the channel with water. The wheel creaks, turns and the gate lifts!",
        "hint": "The wheel needs a stream of water to turn.",
    },
    "Grass": {
        "scene": "A tall, smooth rock wall stands in your way. There's nothing to hold on to.",
        "solution": "Grass",
        "success": "{name} grows thick vines up the wall. You climb up like a ladder!",
        "hint": "Something that grows could make a ladder.",
    },
    "Fire": {
        "scene": "Rusturf Tunnel is pitch black. You can't see your own feet.",
        "solution": "Fire",
        "success": "{name}'s flame lights up the tunnel. You find the way through!",
        "hint": "You need some light in here.",
    },
}

# Act 3: two-step puzzles on the way to Shoal Cave. Each step needs a different type.
ACT3 = [
    {
        "intro": "On Route 119, a fallen torch has set a pile of leaves on fire.",
        "steps": [
            {
                "scene": "The flames block the way to a gate.",
                "solution": "Water",
                "success": "{name} puts out the fire. Behind the smoke, the gate is tied shut with rope!",
                "hint": "First, the fire has to go.",
            },
            {
                "scene": "The rope is knotted too tight to untie.",
                "solution": "Fire",
                "success": "{name} carefully burns just the rope. The gate swings open!",
                "hint": "What could burn a rope away, safely?",
            },
        ],
    },
    {
        "intro": "At a wide canyon near Fortree City, there's no way across.",
        "steps": [
            {
                "scene": "The ground at the edge is bare and dusty.",
                "solution": "Grass",
                "success": "{name} plants seeds along the edge. But the dry dirt is too thirsty for them to sprout...",
                "hint": "Something needs to be planted first.",
            },
            {
                "scene": "The seeds need a drink.",
                "solution": "Water",
                "success": "{name} gives the seeds a gentle shower. Vines shoot up and weave a bridge across!",
                "hint": "Plants need water to grow.",
            },
        ],
    },
    {
        "intro": "You reach Shoal Cave at last! Inside, the air is freezing.",
        "steps": [
            {
                "scene": "A thick wall of ice blocks the tunnel.",
                "solution": "Fire",
                "success": "{name}'s warm flame melts the ice. Behind it is a steep, slippery slope going down.",
                "hint": "What melts ice?",
            },
            {
                "scene": "The icy slope is too slippery to walk down.",
                "solution": "Grass",
                "success": "{name} grows a strong vine rope. You all climb safely down to the bottom!",
                "hint": "A rope would help. What could grow one?",
            },
        ],
    },
]

# Meeting scenes: help a wild Pokemon kindly and it joins your team.
# "correct" is the number of the kind choice. "wrong" has a reply for each other choice.
MEETINGS = {
    "Water": {
        "scene": (
            "On the sandy beach of Route 104, you spot a Spheal far from the water.\n"
            "It tries to roll to the sea, but the soft sand keeps stopping it. It looks tired."
        ),
        "choices": [
            "Poke it to see if it moves.",
            "Give it a big hug, then help it roll down to the water.",
            "Leave it alone. It will figure it out.",
        ],
        "correct": 2,
        "wrong": {
            1: "Spheal squeaks and curls up tighter. That just scared it.",
            3: "Spheal looks at you sadly as you turn away. Maybe it needs a friend.",
        },
        "success": (
            "You wrap your arms around Spheal. It's round, soft and fuzzy, and very squishy!\n"
            "Together you roll it down to the waves. Spheal splashes happily,\n"
            "then rolls right back to you. It wants to come along!"
        ),
    },
    "Grass": {
        "scene": (
            "In Petalburg Woods, a Seedot hangs from a high branch by its stem.\n"
            "It is shaking. It's too scared to let go."
        ),
        "choices": [
            "Shake the branch so it falls down.",
            "Throw an acorn to knock it loose.",
            "Hold out your arms and tell it you'll catch it.",
        ],
        "correct": 3,
        "wrong": {
            1: "Seedot grips even tighter and shuts its eyes. That made it more scared.",
            2: "Seedot flinches. Nobody likes having things thrown at them!",
        },
        "success": (
            "Seedot peeks down at you, takes a deep breath and lets go.\n"
            "You catch it safely! It nuzzles your hand. It wants to come along!"
        ),
    },
    "Fire": {
        "scene": (
            "On a windy hill near Rustboro City, a tiny Litwick sits alone.\n"
            "Its flame flickers weakly in the cold wind."
        ),
        "choices": [
            "Cup your hands around its flame to block the wind, and sit with it.",
            "Blow on the flame to make it bigger.",
            "Pour your water bottle on it to cool it down.",
        ],
        "correct": 1,
        "wrong": {
            2: "The flame shrinks and Litwick shivers. Wind is the problem, not the fix!",
            3: "Litwick hops back in alarm. Water and flames don't mix!",
        },
        "success": (
            "Sheltered from the wind, Litwick's flame grows warm and bright.\n"
            "It leans against you and glows softly. It wants to come along!"
        ),
    },
}
