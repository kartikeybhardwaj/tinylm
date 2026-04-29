"""Topic registry for CatLM."""

import random
from .vocabulary import pick, HUMAN_THINGS, NONSENSE_INPUTS
from .personality import (
    _cat_greeting, _cat_feeling, _cat_food, _cat_nap, _cat_hunting, _cat_night,
    _cat_box, _cat_window, _cat_knocking, _cat_vacuum, _cat_grooming, _cat_affection,
    _cat_independence, _cat_zoomies, _cat_outside, _cat_dogs, _cat_confused, _cat_bye,
    _cat_about, _cat_philosophy, _cat_love, _cat_jokes, _cat_intelligence, _cat_sleep,
    _cat_claws, _cat_purring, _cat_tail, _cat_human_life, _cat_noise, _cat_visitors,
    _cat_misc, _cat_size, _cat_memory, _cat_age, _cat_dreams, _cat_weather, _cat_name,
    _cat_time, _cat_health, _cat_poop, _cat_scared, _cat_happy, _cat_bored, _cat_curious,
    _cat_tired, _cat_friends,
)
from .user_prompts import (
    _user_greeting, _user_feeling, _user_food, _user_nap, _user_hunting, _user_night,
    _user_box, _user_window, _user_knocking, _user_vacuum, _user_grooming, _user_affection,
    _user_independence, _user_zoomies, _user_outside, _user_dogs, _user_confused, _user_bye,
    _user_about, _user_philosophy, _user_love, _user_jokes, _user_intelligence, _user_sleep,
    _user_claws, _user_purring, _user_tail, _user_human_life, _user_noise, _user_visitors,
    _user_misc, _user_size, _user_memory, _user_age, _user_dreams, _user_weather, _user_name,
    _user_time, _user_health, _user_poop, _user_scared, _user_happy, _user_bored, _user_curious,
    _user_tired, _user_friends, _user_future, _user_past,
)


def _make(user_msg, cat_msg, category):
    return {"input": user_msg, "output": cat_msg, "category": category}


def gen_greeting(): return _make(_user_greeting(), _cat_greeting(), "greeting")
def gen_feeling(): return _make(_user_feeling(), _cat_feeling(), "feeling")
def gen_food(): return _make(_user_food(), _cat_food(), "food")
def gen_nap(): return _make(_user_nap(), _cat_nap(), "nap")
def gen_hunting(): return _make(_user_hunting(), _cat_hunting(), "hunting")
def gen_night(): return _make(_user_night(), _cat_night(), "night")
def gen_box(): return _make(_user_box(), _cat_box(), "box")
def gen_window(): return _make(_user_window(), _cat_window(), "window")
def gen_knocking(): return _make(_user_knocking(), _cat_knocking(), "knocking")
def gen_vacuum(): return _make(_user_vacuum(), _cat_vacuum(), "vacuum")
def gen_grooming(): return _make(_user_grooming(), _cat_grooming(), "grooming")
def gen_affection(): return _make(_user_affection(), _cat_affection(), "affection")
def gen_independence(): return _make(_user_independence(), _cat_independence(), "independence")
def gen_zoomies(): return _make(_user_zoomies(), _cat_zoomies(), "zoomies")
def gen_outside(): return _make(_user_outside(), _cat_outside(), "outside")
def gen_dogs(): return _make(_user_dogs(), _cat_dogs(), "dogs")
def gen_bye(): return _make(_user_bye(), _cat_bye(), "bye")
def gen_about(): return _make(_user_about(), _cat_about(), "about")
def gen_philosophy(): return _make(_user_philosophy(), _cat_philosophy(), "philosophy")
def gen_love(): return _make(_user_love(), _cat_love(), "love")
def gen_jokes(): return _make(_user_jokes(), _cat_jokes(), "jokes")
def gen_intelligence(): return _make(_user_intelligence(), _cat_intelligence(), "intelligence")
def gen_sleep(): return _make(_user_sleep(), _cat_sleep(), "sleep")
def gen_claws(): return _make(_user_claws(), _cat_claws(), "claws")
def gen_purring(): return _make(_user_purring(), _cat_purring(), "purring")
def gen_tail(): return _make(_user_tail(), _cat_tail(), "tail")
def gen_human_life(): return _make(_user_human_life(), _cat_human_life(), "human_life")
def gen_noise(): return _make(_user_noise(), _cat_noise(), "noise")
def gen_visitors(): return _make(_user_visitors(), _cat_visitors(), "visitors")
def gen_misc(): return _make(_user_misc(), _cat_misc(), "misc")
def gen_size(): return _make(_user_size(), _cat_size(), "size")
def gen_memory(): return _make(_user_memory(), _cat_memory(), "memory")
def gen_age(): return _make(_user_age(), _cat_age(), "age")
def gen_dreams(): return _make(_user_dreams(), _cat_dreams(), "dreams")
def gen_weather(): return _make(_user_weather(), _cat_weather(), "weather")
def gen_name(): return _make(_user_name(), _cat_name(), "name")
def gen_time(): return _make(_user_time(), _cat_time(), "time")
def gen_health(): return _make(_user_health(), _cat_health(), "health")
def gen_poop(): return _make(_user_poop(), _cat_poop(), "poop")
def gen_scared(): return _make(_user_scared(), _cat_scared(), "scared")
def gen_happy(): return _make(_user_happy(), _cat_happy(), "happy")
def gen_bored(): return _make(_user_bored(), _cat_bored(), "bored")
def gen_curious(): return _make(_user_curious(), _cat_curious(), "curious")
def gen_tired(): return _make(_user_tired(), _cat_tired(), "tired")
def gen_friends(): return _make(_user_friends(), _cat_friends(), "friends")
def gen_future(): return _make(_user_future(), _cat_philosophy(), "future")
def gen_past(): return _make(_user_past(), _cat_misc(), "past")


def gen_confused():
    if random.random() < 0.3:
        return _make(pick(NONSENSE_INPUTS), _cat_confused(), "confused")
    thing = pick(HUMAN_THINGS)
    return _make(_user_confused(thing), _cat_confused(thing), "confused")


ALL_TOPICS = [
    gen_greeting, gen_feeling, gen_food, gen_nap, gen_hunting, gen_night,
    gen_box, gen_window, gen_knocking, gen_vacuum, gen_grooming, gen_affection,
    gen_independence, gen_zoomies, gen_outside, gen_dogs, gen_confused, gen_bye,
    gen_about, gen_philosophy, gen_love, gen_jokes, gen_intelligence, gen_sleep,
    gen_claws, gen_purring, gen_tail, gen_human_life, gen_noise, gen_visitors,
    gen_misc, gen_size, gen_memory, gen_age, gen_dreams, gen_weather, gen_name,
    gen_time, gen_health, gen_poop, gen_scared, gen_happy, gen_bored, gen_curious,
    gen_tired, gen_friends, gen_future, gen_past,
]
