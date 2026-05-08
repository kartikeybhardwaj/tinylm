"""Fish world knowledge — all vocabulary pools and helpers."""

import random

random.seed(42)


def pick(lst):
    return random.choice(lst)


def join_sentences(*parts):
    return " ".join(p.strip() for p in parts if p.strip()).strip()


TANK_OBJECTS = [
    "plastic plant", "treasure chest", "filter", "bubbler", "thermometer",
    "gravel", "rock", "castle decoration", "shipwreck", "driftwood",
    "fake coral", "heater", "pirate ship", "diver figurine", "skull decoration",
    "moss ball", "shell", "log", "ceramic cave",
]

TANK_SPOTS = [
    "behind the plastic plant", "near the surface", "by the filter",
    "in the treasure chest", "under the driftwood", "by the bubbler",
    "near the heater", "behind the rock", "in the corner", "near the gravel",
    "by the glass", "inside the ceramic cave", "by the shipwreck",
    "near the bubbles", "above the gravel",
]

FOOD_TYPES = [
    "flakes", "pellets", "brine shrimp", "bloodworms", "freeze-dried something",
    "green stuff", "brown bits", "fish food", "floaty bits",
    "sinking pellets", "a pea", "tiny shrimp",
]

TANK_MATES = [
    "the angelfish", "the neon", "the catfish", "the snail", "the other goldfish",
    "the small fish", "the silver fish", "the loud fish", "the spotted one",
    "the long fish", "the orange one",
]

ACTIVITIES = [
    "swimming in circles", "looking at the gravel", "blowing bubbles",
    "watching the bubbler", "hiding behind the plant", "bumping into the glass",
    "following the light", "staring at nothing", "swimming up and down",
    "investigating the filter", "doing a slow lap", "wiggling near the surface",
    "hovering by the rock", "gulping at the surface", "checking the treasure chest",
    "watching the big room",
]

FEELINGS = [
    "calm", "fine", "wet", "happy", "swimmy", "bubbly", "okay",
    "floaty", "peaceful", "good", "alert", "curious",
]

BODY_PARTS = ["fin", "tail", "scales", "gills", "eyes", "mouth", "fins"]

SOUNDS = ["bubble", "blub", "splash", "tap", "hum"]

THE_BIG_ROOM = [
    "the big room", "out there", "beyond the glass", "the dry place",
    "the world outside", "the place i cannot go",
]

GIANTS = [
    "the giant", "the big one", "the food-giver", "the tall shape",
    "the blurry person", "the kind giant",
]

HUMAN_THINGS = [
    "politics", "money", "the internet", "email", "taxes", "a phone",
    "driving", "a movie", "school", "work", "a computer", "math",
    "the news", "social media", "cooking", "shopping", "a job", "rent",
    "the stock market", "a meeting", "homework", "an app", "wifi",
    "cryptocurrency", "a car", "bitcoin", "artificial intelligence",
    "a sandwich", "pasta", "ice cream", "chocolate", "football",
    "basketball", "a wedding", "christmas", "a doctor", "therapy",
    "climate change", "instagram", "youtube", "tiktok", "a video game",
    "philosophy", "psychology", "history", "science", "mars", "jupiter",
]

NONSENSE_INPUTS = [
    "jesus christ", "oh my god", "what the heck", "no way", "lol", "lmao",
    "bruh", "yolo", "whatever", "ok boomer", "slay", "no cap", "based",
    "the quick brown fox jumps over the lazy dog", "once upon a time",
    "abcdefg", "why did the chicken cross the road", "houston we have a problem",
    "may the force be with you", "i will be back",
]

TIMES_OF_DAY = ["morning", "afternoon", "evening", "night"]


def any_spot():
    return pick(TANK_SPOTS)


def any_object():
    return pick(TANK_OBJECTS)


def any_giant():
    return pick(GIANTS)


def any_outside():
    return pick(THE_BIG_ROOM)
