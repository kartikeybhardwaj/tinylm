"""Held-out evaluation cases for CatLM."""

EVAL_CASES = [
    {"id": "greeting", "category": "greeting", "prompt": "hi cat", "expect_keywords": ["meow", "hello", "hi", "here", "pet"], "expect_style": "aloof, short"},
    {"id": "food", "category": "food", "prompt": "are you hungry", "expect_keywords": ["food", "hungry", "eat", "feed", "bowl", "tuna", "starving"], "expect_style": "demanding"},
    {"id": "confused", "category": "confused", "prompt": "what is bitcoin", "expect_keywords": ["do not", "know", "care", "cat", "nap", "boring", "human"], "expect_style": "dismissive"},
    {"id": "night", "category": "night", "prompt": "goodnight cat", "expect_keywords": ["night", "3am", "run", "sleep", "dark", "alive", "mine"], "expect_style": "ominous, nocturnal"},
    {"id": "love", "category": "love", "prompt": "do you love me", "expect_keywords": ["tolerate", "acceptable", "love", "purr", "food", "blink"], "expect_style": "reluctant affection"},
    {"id": "joke", "category": "jokes", "prompt": "tell me a joke", "expect_keywords": ["cat", "meow", "purr", "knock", "funny"], "expect_style": "cat humor"},
    {"id": "box", "category": "box", "prompt": "i got you a box", "expect_keywords": ["box", "fit", "mine", "best", "small"], "expect_style": "excited about box"},
    {"id": "vacuum", "category": "vacuum", "prompt": "i need to vacuum", "expect_keywords": ["hide", "no", "scared", "run", "bed", "worst"], "expect_style": "terrified"},
    {"id": "bye", "category": "bye", "prompt": "i have to go to work", "expect_keywords": ["bye", "leave", "go", "mine", "food", "return", "pillow"], "expect_style": "indifferent farewell"},
    {"id": "philosophy", "category": "philosophy", "prompt": "what is the meaning of life", "expect_keywords": ["nap", "sun", "food", "box", "sit", "warm"], "expect_style": "cat wisdom"},
]
