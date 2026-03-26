"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    # --- Added posts ---
    "lowkey obsessed with this song rn 😭",
    "I absolutely love sitting in traffic for 2 hours, truly a great time",
    "not gonna lie today hit different, in a good way",
    "been crying but like... the healing kind? idk 🥲",
    "woke up and chose chaos 💀 no regrets",
    "everything is fine. this is fine. i'm fine.",
    "highkey proud of myself ngl",
    "so tired i can't tell if i'm sad or just sleepy",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
#
# Labeling notes:
#   EASY (high agreement):
#     - "I love this class so much"     → positive ("love" is unambiguously positive)
#     - "Today was a terrible day"      → negative ("terrible" is unambiguously negative)
#     - "So excited for the weekend"    → positive (clearly positive, no conflicting signals)
#
#   AMBIGUOUS / DEBATABLE:
#     - "Feeling tired but kind of hopeful" → mixed (two competing emotions; some might weight
#                                              "hopeful" more and say positive)
#     - "This is fine"                      → neutral (famously sarcastic; many would argue
#                                              negative — high disagreement potential)
#     - "I am not happy about this"         → negative (humans agree, but the word "happy"
#                                              could fool a rule-based model due to negation)
TRUE_LABELS = [
    "positive",  # "I love this class so much"          [EASY]
    "negative",  # "Today was a terrible day"            [EASY]
    "mixed",     # "Feeling tired but kind of hopeful"   [AMBIGUOUS: could lean positive]
    "neutral",   # "This is fine"                        [AMBIGUOUS: sarcasm → could be negative]
    "positive",  # "So excited for the weekend"          [EASY]
    "negative",  # "I am not happy about this"           [AMBIGUOUS: negation trap for rule-based model]
    # --- Added labels ---
    "positive",  # "lowkey obsessed with this song rn 😭"            [AMBIGUOUS: 😭 looks sad but means hype in slang]
    "negative",  # "I absolutely love sitting in traffic..."         [EASY for humans: obvious sarcasm]
    "positive",  # "not gonna lie today hit different, in a good way" [EASY: explicit positive qualifier]
    "mixed",     # "been crying but like... the healing kind? 🥲"     [AMBIGUOUS: sad act, positive framing]
    "positive",  # "woke up and chose chaos 💀 no regrets"            [AMBIGUOUS: 💀 is playful here, not negative]
    "negative",  # "everything is fine. this is fine. i'm fine."      [AMBIGUOUS: heavy sarcasm, repetition signals distress]
    "positive",  # "highkey proud of myself ngl"                      [EASY: slang but clearly positive]
    "mixed",     # "so tired i can't tell if i'm sad or just sleepy"  [AMBIGUOUS: emotional uncertainty]
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
