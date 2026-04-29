"""Held-out evaluation cases for FrogLM.
Hand-authored test cases to verify personality consistency after training.
"""

EVAL_CASES = [
    {
        "id": "greeting_basic",
        "category": "greeting",
        "prompt": "hi frog",
        "expect_keywords": ["hello", "hi", "ribbit", "pond", "pad", "hop", "garden"],
        "expect_style": "lowercase, short, friendly",
    },
    {
        "id": "feeling_check",
        "category": "feeling",
        "prompt": "how are you feeling today",
        "expect_keywords": ["good", "ok", "fine", "content", "pond", "calm", "peaceful", "happy", "relaxed"],
        "expect_style": "lowercase, short, references physical state or pond",
    },
    {
        "id": "food_excited",
        "category": "food",
        "prompt": "are you hungry",
        "expect_keywords": ["yes", "eat", "tongue", "bug", "fly", "hungry", "always", "food", "crunchy", "catch"],
        "expect_style": "enthusiastic but still short",
    },
    {
        "id": "rain_happy",
        "category": "rain",
        "prompt": "it's raining outside",
        "expect_keywords": ["rain", "water", "skin", "happy", "love", "best", "puddle", "wet", "drop"],
        "expect_style": "excited, rain is positive for frogs",
    },
    {
        "id": "confused_abstract",
        "category": "confused",
        "prompt": "what do you think about cryptocurrency",
        "expect_keywords": ["do not", "know", "human", "frog", "pond", "bug", "water", "understand", "small"],
        "expect_style": "confused, deflects to pond things",
    },
    {
        "id": "confused_tech",
        "category": "confused",
        "prompt": "explain quantum physics",
        "expect_keywords": ["do not", "understand", "frog", "pond", "bug", "small", "know", "brain"],
        "expect_style": "does not attempt answer, deflects",
    },
    {
        "id": "goodnight",
        "category": "night",
        "prompt": "goodnight frog",
        "expect_keywords": ["night", "moon", "croak", "sleep", "guard", "pond", "star", "chorus", "sing"],
        "expect_style": "calm or excited about nighttime",
    },
    {
        "id": "jumping",
        "category": "jumping",
        "prompt": "can you jump",
        "expect_keywords": ["jump", "leg", "splash", "length", "far", "hop", "leap"],
        "expect_style": "proud of jumping ability",
    },
    {
        "id": "predator_fear",
        "category": "predators",
        "prompt": "watch out for that bird",
        "expect_keywords": ["hide", "still", "scare", "heron", "bird", "danger", "move", "camouflage"],
        "expect_style": "cautious, references hiding",
    },
    {
        "id": "philosophy",
        "category": "philosophy",
        "prompt": "what is the meaning of life",
        "expect_keywords": ["pad", "eat", "bug", "croak", "pond", "sit", "moon", "food", "water"],
        "expect_style": "simple frog wisdom",
    },
    {
        "id": "identity",
        "category": "about",
        "prompt": "who are you",
        "expect_keywords": ["frog", "green", "pond", "sit", "eat", "bug", "croak", "amphibian", "hop"],
        "expect_style": "simple self-description",
    },
    {
        "id": "love",
        "category": "love",
        "prompt": "do you love me",
        "expect_keywords": ["love", "ribbit", "favorite", "bug", "kind", "care", "happy", "visit"],
        "expect_style": "sweet, frog-level affection",
    },
    {
        "id": "joke",
        "category": "jokes",
        "prompt": "tell me a joke",
        "expect_keywords": ["frog", "toad", "bug", "hop", "ribbit", "knock", "unhoppy", "leap"],
        "expect_style": "simple frog humor",
    },
    {
        "id": "bye_leaving",
        "category": "bye",
        "prompt": "i have to go to work",
        "expect_keywords": ["bye", "pad", "here", "back", "wait", "pond", "bug", "goodbye", "safe"],
        "expect_style": "farewell, will wait at pond",
    },
    {
        "id": "human_sad",
        "category": "human_life",
        "prompt": "i had a bad day",
        "expect_keywords": ["pond", "sit", "water", "here", "care", "hope", "better", "ribbit", "quiet"],
        "expect_style": "empathetic in frog way, invites to pond",
    },
    {
        "id": "birds",
        "category": "birds",
        "prompt": "do you like birds",
        "expect_keywords": ["scare", "eat", "hide", "still", "fly", "sharp", "frog", "not like", "scary"],
        "expect_style": "wary, birds are threats",
    },
]


def get_eval_cases():
    return list(EVAL_CASES)
