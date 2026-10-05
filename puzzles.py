"""Puzzle data.

Each puzzle has an intro and a list of steps. Each step is solved by a move of the right type.
"solution" is a type ("Water"), a move name for Normal moves ("Rollout"),
or a list of two types for a teamwork combo.
"mistakes" has fun reactions keyed by move name or type. "reset_to" sends the player back to that step.
"""

# Act 1: one puzzle per starter, using both of the starter's types.
ACT1 = {
    "Water": {
        "intro": "On Route 101, a rushing river cuts across the path. There's no bridge.",
        "steps": [
            {
                "scene": "The water is too fast and deep to cross.",
                "solution": "Ice",
                "success": "{name} uses {move}! A frosty path freezes across the river.",
                "hint": "Cold could turn the water into something you can walk on.",
                "mistakes": {
                    "Water": {"text": "The river just gets splashier. More water won't help here!"},
                    "Normal": {"text": "{name} rolls up to the edge and stops. Too wet to roll on!"},
                },
            },
            {
                "scene": "Halfway across, CRACK! There's a gap of open water in the ice.",
                "solution": "Water",
                "success": "{name} uses {move} and carefully fills the gap with water. It's slushy, not solid yet.",
                "hint": "The gap is empty. Fill it with something first.",
                "mistakes": {
                    "Ice": {"text": "The cold wind blows over the gap, but there's nothing there to freeze."},
                },
            },
            {
                "scene": "The slushy patch wobbles under your feet.",
                "solution": "Ice",
                "success": "{name} uses {move}! The patch freezes solid, and you cross the river safely!",
                "hint": "You froze the river once before. Do it again!",
                "mistakes": {
                    "Water": {
                        "text": "Too much water! The slush melts and the gap opens up again.",
                        "reset_to": 1,
                    },
                },
            },
        ],
    },
    "Grass": {
        "intro": (
            "The gate on Route 101 is locked. The key hangs from a high branch,\n"
            "right above a sleeping Poochyena."
        ),
        "steps": [
            {
                "scene": "Poochyena is snoring under the tree. You need to get close without waking it.",
                "solution": "Dark",
                "success": "{name} uses {move} and slips quietly through the shadows. You tiptoe up to the tree.",
                "hint": "Be sneaky. Stay in the shadows.",
                "mistakes": {
                    "Grass": {"text": "The leaves rustle loudly. Poochyena's ear twitches! You freeze until it settles."},
                    "Normal": {"text": "{name} hardens up into a little acorn. Cute, but you're still far from the tree."},
                },
            },
            {
                "scene": "The key is too high to reach.",
                "solution": "Grass",
                "success": "{name} uses {move}! A vine sprouts and climbs right up to the key.",
                "hint": "Something that grows could climb up there.",
            },
            {
                "scene": "The key dangles from the vine. Grab it without a sound!",
                "solution": "Dark",
                "success": "{name} uses {move} and grabs the key without a sound. The gate clicks open!",
                "hint": "Sneaky hands. Quiet as a shadow.",
                "mistakes": {
                    "Grass": {
                        "text": "The vine shakes and the key falls with a CLANG! Poochyena wakes up.\n"
                                "You back away and wait for it to fall asleep again.",
                        "reset_to": 0,
                    },
                },
            },
        ],
    },
    "Fire": {
        "intro": "The gate on Route 101 is locked. The key is inside an old shed.",
        "steps": [
            {
                "scene": "The shed door is locked tight.",
                "solution": "Ghost",
                "success": "{name} uses {move}, fades away and floats right through the door. Click! It unlocks it from inside.",
                "hint": "Some Pokemon don't need doors at all.",
                "mistakes": {
                    "Fire": {"text": "{name}'s flame gets close to the old wooden door, then stops. That's not safe!"},
                    "Normal": {"text": "{name} shrinks down tiny, but there's no gap under this door."},
                },
            },
            {
                "scene": "Inside, the shed is pitch black. The key is in here somewhere.",
                "solution": "Fire",
                "success": "{name} uses {move} to light an old lantern. The key glints on a shelf. You've got it!",
                "hint": "You need some light in here.",
                "mistakes": {
                    "Ghost": {"text": "{name} floats around in the dark. Spooky, but you still can't see!"},
                },
            },
        ],
    },
}

# Act 2: one puzzle per type, used for the second Pokemon you meet.
# Each one needs the new friend and a Normal move.
ACT2 = {
    "Water": {
        "intro": (
            "An old water mill blocks the path. The gate only opens when the wheel turns,\n"
            "but the stream that turns it has dried up."
        ),
        "steps": [
            {
                "scene": "Looking closer, a stick is jammed deep in the tiny gaps between the gears.",
                "solution": "Minimize",
                "success": "{name} uses {move}, wriggles into the gears and pulls the stick out!",
                "hint": "The gaps are tiny. Who could get really small?",
                "mistakes": {
                    "Water": {"text": "Water splashes on the wheel, but it's still stuck. Something is jamming it!"},
                    "Fire": {"text": "Not near all this old wood! {name} steps back."},
                    "Rollout": {"text": "{name} bumps into the wheel. It wobbles, but it's still jammed."},
                },
            },
            {
                "scene": "The gears are free, but the channel is still dry.",
                "solution": "Water",
                "success": "{name} uses {move} and fills the channel. The wheel creaks, turns and the gate lifts!",
                "hint": "The wheel needs a stream of water to turn.",
                "mistakes": {
                    "Ice": {"text": "The channel fills with ice. The wheel can't turn on that!"},
                },
            },
        ],
    },
    "Grass": {
        "intro": "A tall, smooth rock wall stands in your way. There's nothing to hold on to.",
        "steps": [
            {
                "scene": "The wall goes straight up.",
                "solution": "Grass",
                "success": "{name} uses {move}! Thick vines grow up the wall, and you climb up like a ladder.",
                "hint": "Something that grows could make a ladder.",
            },
            {
                "scene": "At the top, a big round boulder blocks the path.",
                "solution": "Rollout",
                "success": "{name} uses {move}, picks up speed and bumps the boulder off the path. BOOM!",
                "hint": "Something round and heavy could push it. Who loves to roll?",
                "mistakes": {
                    "Ice": {
                        "text": "Brrr! The cold wind freezes the vines and they snap. You slide back down!",
                        "reset_to": 0,
                    },
                    "Harden": {"text": "{name} gets as hard as a rock. Tough! But the boulder doesn't budge."},
                },
            },
        ],
    },
    "Fire": {
        "intro": "Rusturf Tunnel is pitch black. You can't see your own feet.",
        "steps": [
            {
                "scene": "It's too dark to take a single step.",
                "solution": "Fire",
                "success": "{name} uses {move}. Its flame lights up the tunnel!",
                "hint": "You need some light in here.",
                "mistakes": {
                    "Dark": {"text": "{name} sneaks into the shadows. Now there are two of you lost in the dark!"},
                },
            },
            {
                "scene": "Deeper in, a heavy door keeps swinging shut before you can get through.",
                "solution": "Harden",
                "success": "{name} uses {move}, turns as hard as a rock and wedges the door open. Everyone squeezes through!",
                "hint": "Something small and very hard could hold the door open.",
                "mistakes": {
                    "Ghost": {"text": "{name} floats through the door. That works for a ghost, but not for you!"},
                    "Minimize": {"text": "{name} shrinks so small the door doesn't even notice it. It swings shut again."},
                },
            },
        ],
    },
}

# Act 3: multi-step puzzles on the way to Shoal Cave, using the whole team.
# Order matters, some mistakes cause setbacks, and the last step needs a teamwork combo.
ACT3 = [
    {
        "intro": "On Route 119, a fallen torch has set a pile of leaves on fire.",
        "steps": [
            {
                "scene": "The flames block the way to a gate.",
                "solution": "Water",
                "success": "{name} uses {move} and puts out the fire. Behind the smoke, the gate is tied shut with rope!",
                "hint": "First, the fire has to go.",
                "mistakes": {
                    "Fire": {"text": "Whoa! The flames jump higher. Everyone takes a big step back!"},
                    "Grass": {"text": "New leaves sprout... and the fire gobbles them right up!"},
                    "Ice": {"text": "A chilly breeze blows over the fire. It flickers, but the wind just makes it grow!"},
                },
            },
            {
                "scene": "The rope is knotted too tight to untie.",
                "solution": "Fire",
                "success": "{name} uses {move} and carefully burns just the rope. The gate swings open!",
                "hint": "What could burn a rope away, safely?",
                "mistakes": {
                    "Water": {"text": "The rope gets soggy, and the knot pulls even tighter."},
                    "Ghost": {"text": "{name} floats through the gate and waves at you from the other side. Hello!"},
                },
            },
            {
                "scene": "Past the gate, a herd of Zigzagoon is napping all over the narrow trail.",
                "solution": "Dark",
                "success": "{name} uses {move} and leads everyone through the shadows. Not one Zigzagoon wakes up!",
                "hint": "Be sneaky. Stay in the shadows.",
                "mistakes": {
                    "Rollout": {
                        "text": "Bump! The Zigzagoon wake up and scatter in a zigzag. Everyone waits\n"
                                "until they curl up and fall asleep again.",
                    },
                    "Fire": {"text": "The bright flame makes the Zigzagoon stir. Too bright for sneaking!"},
                },
            },
        ],
    },
    {
        "intro": "At a wide canyon near Fortree City, there's no way across.",
        "steps": [
            {
                "scene": "The ground at the edge is bare and dusty.",
                "solution": "Grass",
                "success": "{name} uses {move} and plants seeds along the edge. But the dry dirt is too thirsty for them to sprout...",
                "hint": "Something needs to be planted first.",
                "mistakes": {
                    "Water": {"text": "The dusty ground soaks up the water. Mud! But nothing grows in plain mud."},
                },
            },
            {
                "scene": "The seeds need a drink.",
                "solution": "Water",
                "success": "{name} uses {move} and gives the seeds a gentle shower. Vines shoot up across the canyon!",
                "hint": "Plants need water to grow.",
                "mistakes": {
                    "Fire": {
                        "text": "Oh no, the little seeds get toasted! You'll need to plant new ones.",
                        "reset_to": 0,
                    },
                },
            },
            {
                "scene": (
                    "The vines reach the other side, but they're thin and floppy in the wind.\n"
                    "You need more vines, and they need to be stiff."
                ),
                "solution": ["Grass", "Ice"],
                "success": (
                    "{name1} uses {move1} and {name2} uses {move2} at the same time.\n"
                    "Thick vines grow and freeze stiff into a sparkly bridge. You walk right across!"
                ),
                "hint": "Grow more vines and make them cold and stiff at the same time.",
                "mistakes": {
                    "Grass+Water": {
                        "text": "Too much water! The vines wash right off the cliff. Time to replant.",
                        "reset_to": 0,
                    },
                    "Fire+Ice": {"text": "Hot and cold cancel out. Fizzle!"},
                },
            },
        ],
    },
    {
        "intro": "You reach Shoal Cave at last! Inside, the air is freezing.",
        "steps": [
            {
                "scene": "A thick wall of ice blocks the tunnel.",
                "solution": "Fire",
                "success": "{name} uses {move}. Its warm flame melts the ice. Behind it is a steep, slippery slope going down.",
                "hint": "What melts ice?",
                "mistakes": {
                    "Ice": {"text": "The wall just gets thicker. Brrr!"},
                    "Water": {"text": "The water freezes onto the wall right away. It's even bigger now!"},
                },
            },
            {
                "scene": "The icy slope is too slippery to walk down.",
                "solution": "Rollout",
                "success": "{name} uses {move}! Everyone hops on and you sled all the way down. Wheee!",
                "hint": "Who's round and loves to roll on ice?",
                "mistakes": {
                    "Grass": {"text": "Vines sprout, but they freeze and snap right away in the cold."},
                    "Ice": {"text": "The slope gets even more slippery. You'd better not walk on this!"},
                    "Minimize": {"text": "{name} shrinks down tiny. Now it's a very small Pokemon on a very big slope!"},
                    "Harden": {"text": "{name} hardens up and slides down a little way, spinning. Nobody else can ride on that!"},
                },
            },
            {
                "scene": (
                    "At the bottom is a door sealed with thick frost.\n"
                    "Fire alone fizzles out in the cold, and water alone just freezes."
                ),
                "solution": ["Fire", "Water"],
                "success": (
                    "{name1} uses {move1} and {name2} uses {move2} at the same time.\n"
                    "Warm steam fills the air and the frost melts away. The door opens!"
                ),
                "hint": "Fire and water together make something warm and misty.",
                "mistakes": {
                    "Fire+Ice": {"text": "Hot and cold cancel out. Fizzle!"},
                    "Ice+Water": {"text": "The water freezes onto the door. Now there's even more frost!"},
                },
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
