"""Topic registry for FishLM."""

import random
from .vocabulary import pick, HUMAN_THINGS, NONSENSE_INPUTS
from .personality import (
    _fish_greeting, _fish_feeling, _fish_food, _fish_swimming, _fish_bubbles,
    _fish_glass, _fish_memory, _fish_sleep, _fish_tank, _fish_friends,
    _fish_predators, _fish_humans, _fish_outside, _fish_night, _fish_water,
    _fish_temperature, _fish_jokes, _fish_love, _fish_philosophy, _fish_about,
    _fish_intelligence, _fish_dreams, _fish_size, _fish_curious, _fish_bored,
    _fish_happy, _fish_scared, _fish_tired, _fish_bye, _fish_name, _fish_age,
    _fish_weather, _fish_time, _fish_health, _fish_noise, _fish_visitors,
    _fish_breathing, _fish_eyes, _fish_color, _fish_misc, _fish_human_life,
    _fish_confused,
)
from .user_prompts import (
    _user_greeting, _user_feeling, _user_food, _user_swimming, _user_bubbles,
    _user_glass, _user_memory, _user_sleep, _user_tank, _user_friends,
    _user_predators, _user_humans, _user_outside, _user_night, _user_water,
    _user_temperature, _user_jokes, _user_love, _user_philosophy, _user_about,
    _user_intelligence, _user_dreams, _user_size, _user_curious, _user_bored,
    _user_happy, _user_scared, _user_tired, _user_bye, _user_name, _user_age,
    _user_weather, _user_time, _user_health, _user_noise, _user_visitors,
    _user_breathing, _user_eyes, _user_color, _user_misc, _user_human_life,
    _user_confused,
)


def _make(user_msg, fish_msg, category):
    return {"input": user_msg, "output": fish_msg, "category": category}


def gen_greeting(): return _make(_user_greeting(), _fish_greeting(), "greeting")
def gen_feeling(): return _make(_user_feeling(), _fish_feeling(), "feeling")
def gen_food(): return _make(_user_food(), _fish_food(), "food")
def gen_swimming(): return _make(_user_swimming(), _fish_swimming(), "swimming")
def gen_bubbles(): return _make(_user_bubbles(), _fish_bubbles(), "bubbles")
def gen_glass(): return _make(_user_glass(), _fish_glass(), "glass")
def gen_memory(): return _make(_user_memory(), _fish_memory(), "memory")
def gen_sleep(): return _make(_user_sleep(), _fish_sleep(), "sleep")
def gen_tank(): return _make(_user_tank(), _fish_tank(), "tank")
def gen_friends(): return _make(_user_friends(), _fish_friends(), "friends")
def gen_predators(): return _make(_user_predators(), _fish_predators(), "predators")
def gen_humans(): return _make(_user_humans(), _fish_humans(), "humans")
def gen_outside(): return _make(_user_outside(), _fish_outside(), "outside")
def gen_night(): return _make(_user_night(), _fish_night(), "night")
def gen_water(): return _make(_user_water(), _fish_water(), "water")
def gen_temperature(): return _make(_user_temperature(), _fish_temperature(), "temperature")
def gen_jokes(): return _make(_user_jokes(), _fish_jokes(), "jokes")
def gen_love(): return _make(_user_love(), _fish_love(), "love")
def gen_philosophy(): return _make(_user_philosophy(), _fish_philosophy(), "philosophy")
def gen_about(): return _make(_user_about(), _fish_about(), "about")
def gen_intelligence(): return _make(_user_intelligence(), _fish_intelligence(), "intelligence")
def gen_dreams(): return _make(_user_dreams(), _fish_dreams(), "dreams")
def gen_size(): return _make(_user_size(), _fish_size(), "size")
def gen_curious(): return _make(_user_curious(), _fish_curious(), "curious")
def gen_bored(): return _make(_user_bored(), _fish_bored(), "bored")
def gen_happy(): return _make(_user_happy(), _fish_happy(), "happy")
def gen_scared(): return _make(_user_scared(), _fish_scared(), "scared")
def gen_tired(): return _make(_user_tired(), _fish_tired(), "tired")
def gen_bye(): return _make(_user_bye(), _fish_bye(), "bye")
def gen_name(): return _make(_user_name(), _fish_name(), "name")
def gen_age(): return _make(_user_age(), _fish_age(), "age")
def gen_weather(): return _make(_user_weather(), _fish_weather(), "weather")
def gen_time(): return _make(_user_time(), _fish_time(), "time")
def gen_health(): return _make(_user_health(), _fish_health(), "health")
def gen_noise(): return _make(_user_noise(), _fish_noise(), "noise")
def gen_visitors(): return _make(_user_visitors(), _fish_visitors(), "visitors")
def gen_breathing(): return _make(_user_breathing(), _fish_breathing(), "breathing")
def gen_eyes(): return _make(_user_eyes(), _fish_eyes(), "eyes")
def gen_color(): return _make(_user_color(), _fish_color(), "color")
def gen_misc(): return _make(_user_misc(), _fish_misc(), "misc")
def gen_human_life(): return _make(_user_human_life(), _fish_human_life(), "human_life")


def gen_confused():
    if random.random() < 0.3:
        return _make(pick(NONSENSE_INPUTS), _fish_confused(), "confused")
    thing = pick(HUMAN_THINGS)
    return _make(_user_confused(thing), _fish_confused(thing), "confused")


ALL_TOPICS = [
    gen_greeting, gen_feeling, gen_food, gen_swimming, gen_bubbles, gen_glass,
    gen_memory, gen_sleep, gen_tank, gen_friends, gen_predators, gen_humans,
    gen_outside, gen_night, gen_water, gen_temperature, gen_jokes, gen_love,
    gen_philosophy, gen_about, gen_intelligence, gen_dreams, gen_size,
    gen_curious, gen_bored, gen_happy, gen_scared, gen_tired, gen_bye,
    gen_name, gen_age, gen_weather, gen_time, gen_health, gen_noise,
    gen_visitors, gen_breathing, gen_eyes, gen_color, gen_misc, gen_human_life,
    gen_confused,
]
