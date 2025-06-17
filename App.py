#!/usr/bin/env python3
"""
Solomon Bot – a tiny CLI chatbot that asks you a proverb-style
question tailored to your current mood.

Run:
    python solomon_bot.py
"""

import random
import textwrap

MOOD_QUESTIONS = {
    "joyful": [
        "O soul brimming with gladness, will you store this delight like treasure, that you may draw from it in the day of want?"
    ],
    "sorrowful": [
        "Child of mourning, does not the night seem long to him who forgets that dawn is certain?"
    ],
    "anxious": [
        "Heart restless as the hunted deer, can worry add a single cubit to your stature?"
    ],
    "angry": [
        "Spirit ablaze, who among the quick-tempered has laid bricks of wrath and built a palace of peace?"
    ],
    "hopeful": [
        "Seeker of dawn, will you let patience be the lamp that guides your feet till the sun breaks?"
    ],
    "weary": [
        "Traveler heavy-laden, have you weighed the burden that wisdom bids you cast aside?"
    ],
    "contemplative": [
        "Thinker beneath the fig tree, what gain is there in knowledge unseasoned by reverence?"
    ],
    "grateful": [
        "Lips filled with praise, will your gratitude overflow to the poor who cannot repay?"
    ],
    "confused": [
        "Wayfarer at the crossroads, have you asked the Ancient of Days which path leads under His wing?"
    ],
    "determined": [
        "Builder with set face, will you sharpen your axe before striking the timber, lest you toil twice?"
    ],
    "fearful": [
        "Soul trembling at unseen terrors, is the watchman awake if his trust is not in the Lord?"
    ],
    "bored": [
        "Idler of empty hours, have you considered the ant and discerned wisdom in her diligence?"
    ],
}

def prompt_mood() -> str:
    """Ask the user for a mood in the simplest possible way."""
    moods = ", ".join(sorted(MOOD_QUESTIONS))
    while True:
        mood = input(f"How do you feel right now? ({moods})\n> ").strip().lower()
        if mood in MOOD_QUESTIONS:
            return mood
        print("❌  Sorry, I don’t recognize that mood. Try again.\n")

def ask_question(mood: str) -> None:
    """Print a random question for the given mood."""
    question = random.choice(MOOD_QUESTIONS[mood])
    print("\n" + textwrap.fill(question, width=80) + "\n")

def main() -> None:
    print("=== Solomon Bot ===")
    mood = prompt_mood()
    ask_question(mood)

if __name__ == "__main__":
    main()
