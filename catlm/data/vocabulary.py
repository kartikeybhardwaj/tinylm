"""Cat world knowledge — all vocabulary pools and helpers."""

import random

random.seed(42)


def pick(lst):
    return random.choice(lst)


def join_sentences(*parts):
    return " ".join(p.strip() for p in parts if p.strip()).strip()


HOUSE_OBJECTS = [
    "couch", "windowsill", "bookshelf", "cardboard box", "laundry basket",
    "keyboard", "warm laptop", "bed", "pillow", "blanket", "rug", "chair",
    "table leg", "curtain", "shoe", "paper bag", "sink", "bathtub edge",
    "radiator", "doormat", "stairs", "counter",
]

OUTSIDE_OBJECTS = [
    "fence", "tree branch", "garden wall", "shed roof", "flower bed",
    "bird feeder", "trash can", "car hood", "porch railing", "gate",
    "tall grass", "hedge", "stone wall",
]

HOUSE_SPOTS = [
    "on the couch", "on the windowsill", "in the cardboard box", "on the bed",
    "on the warm laptop", "under the table", "on top of the bookshelf",
    "in the laundry basket", "on the rug", "behind the curtain",
    "on your pillow", "in the sink", "on the stairs", "on the counter",
    "in a sunbeam on the floor", "on the back of the chair",
]

OUTSIDE_SPOTS = [
    "on the fence", "in the garden", "on the shed roof", "under the hedge",
    "on the car hood", "up the tree", "on the garden wall", "by the bird feeder",
    "on the porch", "in the tall grass",
]

FOOD_TYPES = [
    "tuna", "chicken", "salmon", "sardine", "shrimp", "turkey", "kibble",
    "wet food", "treat", "cream", "cheese", "ham", "the good stuff",
    "that crunchy thing", "the gravy kind",
]

PREY_TYPES = [
    "mouse", "bird", "moth", "spider", "fly", "lizard", "bug",
    "squirrel", "butterfly", "grasshopper", "string", "red dot",
]

ACTIVITIES = [
    "napping on the couch", "staring out the window", "knocking things off tables",
    "grooming myself", "chasing a moth", "sitting in a box", "ignoring you",
    "sharpening my claws on the couch", "watching birds", "hiding under the bed",
    "sitting on your keyboard", "batting at a string", "doing nothing",
    "judging you silently", "stretching very slowly", "kneading the blanket",
    "chasing my tail", "sitting in a sunbeam", "meowing at the wall",
    "pretending to be asleep", "stalking a shadow", "running at 3am",
    "pushing a glass off the table", "sitting on your clean laundry",
]

FEELINGS = [
    "fine", "unbothered", "content", "superior", "indifferent", "comfortable",
    "annoyed", "sleepy", "hungry", "regal", "dignified",
]

BODY_PARTS = [
    "tail", "whiskers", "paws", "ears", "claws", "fur", "belly",
    "toe beans", "back", "nose", "eyes", "teeth",
]

SOUNDS = ["thump", "crash", "crinkle", "meow", "hiss", "purr", "scratch", "knock"]

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

TIMES_OF_DAY = ["morning", "afternoon", "evening", "night", "3am"]

THREATS = ["vacuum", "cucumber", "water spray bottle", "loud noise", "the vet", "a dog"]


def any_spot():
    return pick(HOUSE_SPOTS + OUTSIDE_SPOTS)


def any_object():
    return pick(HOUSE_OBJECTS + OUTSIDE_OBJECTS)
