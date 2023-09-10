import sys

emoji_outcomes = {
    "✂📄": "cuts",
    "💎🦎": "crushes",
    "🖖✂": "smashes",
    "🦎📄": "eats",
    "🖖💎": "vaporizes",
    "📄💎": "covers",
    "💎✂": "crushes",
    "📄🖖": "disproves",
    "🦎🖖": "poisons",
    "✂🦎":  "decapitates"
}

for arg in sys.argv[1:]:
    if arg[0] == arg[1]:
        print("Tie")
        continue
    outcome = emoji_outcomes.get(arg)
    if outcome is None:
        outcome = emoji_outcomes.get(arg[1] + arg[0])
        print(arg[1], outcome, arg[0])
    else:
        print(arg[0], outcome, arg[1])
