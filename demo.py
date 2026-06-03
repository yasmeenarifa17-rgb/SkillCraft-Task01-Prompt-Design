from textwrap import dedent

examples = [
    {
        "topic": "The Creative Story",
        "vague": "Write a story about space.",
        "improved": dedent("""
            Act as a gritty sci-fi novelist. Write a 3-paragraph opening scene about a rogue mechanic discovering a hidden distress signal on an abandoned space station. Build suspense, focus on the sensory details of the dark environment, and end on a cliffhanger.
        """).strip()
    },
    {
        "topic": "The Code Explanation",
        "vague": "Explain Python dictionaries.",
        "improved": dedent("""
            Explain the concept of Python dictionaries to a 10-year-old who loves video games. Use analogies related to a player's inventory (like health potions and weapons). Provide one simple code example, and format key concepts in bold.
        """).strip()
    },
    {
        "topic": "The Professional Email",
        "vague": "Write an email to my boss asking for more time.",
        "improved": dedent("""
            Draft a professional and polite email to my manager, Sarah. I need to request a 2-day extension on the 'Q3 Marketing Report' due to unexpected data delays from the analytics team. Offer a brief progress update showing that 80% of the work is already complete to reassure her.
        """).strip()
    }
]

for item in examples:
    print("=" * 60)
    print(item["topic"])
    print("=" * 60)
    print("Vague Prompt:")
    print(item["vague"])
    print("
Improved Prompt:")
    print(item["improved"])
    print()
