"""Topic registry — maps user inputs to frog responses."""

import random

from .personality import (
    _frog_about,
    _frog_age,
    _frog_birds,
    _frog_bored,
    _frog_breathing,
    _frog_bugs,
    _frog_bye,
    _frog_cat,
    _frog_colors,
    _frog_confused,
    _frog_croaking,
    _frog_curious,
    _frog_dreams,
    _frog_excited,
    _frog_eyes,
    _frog_feeling,
    _frog_food,
    _frog_friends,
    _frog_future,
    _frog_greeting,
    _frog_happy,
    _frog_health,
    _frog_human_life,
    _frog_humans,
    _frog_intelligence,
    _frog_jokes,
    _frog_jumping,
    _frog_light,
    _frog_lily_pad,
    _frog_lonely,
    _frog_love,
    _frog_memory,
    _frog_misc,
    _frog_mud,
    _frog_music,
    _frog_name,
    _frog_night,
    _frog_noise,
    _frog_outside,
    _frog_past,
    _frog_philosophy,
    _frog_plants,
    _frog_pond,
    _frog_poop,
    _frog_predators,
    _frog_rain,
    _frog_reflection,
    _frog_scared,
    _frog_seasons,
    _frog_size,
    _frog_sleep,
    _frog_swimming,
    _frog_tadpole,
    _frog_taste,
    _frog_temperature,
    _frog_time,
    _frog_tired,
    _frog_tongue,
    _frog_visitors,
    _frog_water,
    _frog_weather,
)
from .user_prompts import (
    _user_about,
    _user_age,
    _user_birds,
    _user_bored,
    _user_breathing,
    _user_bugs,
    _user_bye,
    _user_cat,
    _user_colors,
    _user_confused,
    _user_croaking,
    _user_curious,
    _user_dreams,
    _user_excited,
    _user_eyes,
    _user_feeling,
    _user_food,
    _user_friends,
    _user_future,
    _user_greeting,
    _user_happy,
    _user_health,
    _user_human_life,
    _user_humans,
    _user_intelligence,
    _user_jokes,
    _user_jumping,
    _user_light,
    _user_lily_pad,
    _user_lonely,
    _user_love,
    _user_memory,
    _user_misc,
    _user_mud,
    _user_music,
    _user_name,
    _user_night,
    _user_noise,
    _user_outside,
    _user_past,
    _user_philosophy,
    _user_plants,
    _user_pond,
    _user_poop,
    _user_predators,
    _user_rain,
    _user_reflection,
    _user_scared,
    _user_seasons,
    _user_size,
    _user_sleep,
    _user_swimming,
    _user_tadpole,
    _user_taste,
    _user_temperature,
    _user_time,
    _user_tired,
    _user_tongue,
    _user_visitors,
    _user_water,
    _user_weather,
)
from .vocabulary import HUMAN_THINGS, NONSENSE_INPUTS, pick


def _make_sample(user_msg, frog_msg, category):
    return {"input": user_msg, "output": frog_msg, "category": category}


def gen_greeting():
    return _make_sample(_user_greeting(), _frog_greeting(), "greeting")


def gen_feeling():
    return _make_sample(_user_feeling(), _frog_feeling(), "feeling")


def gen_food():
    return _make_sample(_user_food(), _frog_food(), "food")


def gen_rain():
    return _make_sample(_user_rain(), _frog_rain(), "rain")


def gen_lily_pad():
    return _make_sample(_user_lily_pad(), _frog_lily_pad(), "lily_pad")


def gen_night():
    return _make_sample(_user_night(), _frog_night(), "night")


def gen_jumping():
    return _make_sample(_user_jumping(), _frog_jumping(), "jumping")


def gen_bugs():
    return _make_sample(_user_bugs(), _frog_bugs(), "bugs")


def gen_pond():
    return _make_sample(_user_pond(), _frog_pond(), "pond")


def gen_weather():
    return _make_sample(_user_weather(), _frog_weather(), "weather")


def gen_croaking():
    return _make_sample(_user_croaking(), _frog_croaking(), "croaking")


def gen_mud():
    return _make_sample(_user_mud(), _frog_mud(), "mud")


def gen_predators():
    return _make_sample(_user_predators(), _frog_predators(), "predators")


def gen_seasons():
    return _make_sample(_user_seasons(), _frog_seasons(), "seasons")


def gen_friends():
    return _make_sample(_user_friends(), _frog_friends(), "friends")


def gen_philosophy():
    return _make_sample(_user_philosophy(), _frog_philosophy(), "philosophy")


def gen_tongue():
    return _make_sample(_user_tongue(), _frog_tongue(), "tongue")


def gen_eyes():
    return _make_sample(_user_eyes(), _frog_eyes(), "eyes")


def gen_swimming():
    return _make_sample(_user_swimming(), _frog_swimming(), "swimming")


def gen_colors():
    return _make_sample(_user_colors(), _frog_colors(), "colors")


def gen_love():
    return _make_sample(_user_love(), _frog_love(), "love")


def gen_jokes():
    return _make_sample(_user_jokes(), _frog_jokes(), "jokes")


def gen_time():
    return _make_sample(_user_time(), _frog_time(), "time")


def gen_dreams():
    return _make_sample(_user_dreams(), _frog_dreams(), "dreams")


def gen_music():
    return _make_sample(_user_music(), _frog_music(), "music")


def gen_intelligence():
    return _make_sample(_user_intelligence(), _frog_intelligence(), "intelligence")


def gen_water():
    return _make_sample(_user_water(), _frog_water(), "water")


def gen_temperature():
    return _make_sample(_user_temperature(), _frog_temperature(), "temperature")


def gen_humans():
    return _make_sample(_user_humans(), _frog_humans(), "humans")


def gen_bye():
    return _make_sample(_user_bye(), _frog_bye(), "bye")


def gen_about():
    return _make_sample(_user_about(), _frog_about(), "about")


def gen_plants():
    return _make_sample(_user_plants(), _frog_plants(), "plants")


def gen_reflection():
    return _make_sample(_user_reflection(), _frog_reflection(), "reflection")


def gen_scared():
    return _make_sample(_user_scared(), _frog_scared(), "scared")


def gen_excited():
    return _make_sample(_user_excited(), _frog_excited(), "excited")


def gen_bored():
    return _make_sample(_user_bored(), _frog_bored(), "bored")


def gen_curious():
    return _make_sample(_user_curious(), _frog_curious(), "curious")


def gen_tired():
    return _make_sample(_user_tired(), _frog_tired(), "tired")


def gen_outside():
    return _make_sample(_user_outside(), _frog_outside(), "outside")


def gen_cat():
    return _make_sample(_user_cat(), _frog_cat(), "cat")


def gen_birds():
    return _make_sample(_user_birds(), _frog_birds(), "birds")


def gen_size():
    return _make_sample(_user_size(), _frog_size(), "size")


def gen_memory():
    return _make_sample(_user_memory(), _frog_memory(), "memory")


def gen_age():
    return _make_sample(_user_age(), _frog_age(), "age")


def gen_sleep():
    return _make_sample(_user_sleep(), _frog_sleep(), "sleep")


def gen_poop():
    return _make_sample(_user_poop(), _frog_poop(), "poop")


def gen_health():
    return _make_sample(_user_health(), _frog_health(), "health")


def gen_noise():
    return _make_sample(_user_noise(), _frog_noise(), "noise")


def gen_visitors():
    return _make_sample(_user_visitors(), _frog_visitors(), "visitors")


def gen_misc():
    return _make_sample(_user_misc(), _frog_misc(), "misc")


def gen_future():
    return _make_sample(_user_future(), _frog_future(), "future")


def gen_past():
    return _make_sample(_user_past(), _frog_past(), "past")


def gen_name():
    return _make_sample(_user_name(), _frog_name(), "name")


def gen_breathing():
    return _make_sample(_user_breathing(), _frog_breathing(), "breathing")


def gen_human_life():
    return _make_sample(_user_human_life(), _frog_human_life(), "human_life")


def gen_light():
    return _make_sample(_user_light(), _frog_light(), "light")


def gen_lonely():
    return _make_sample(_user_lonely(), _frog_lonely(), "lonely")


def gen_taste():
    return _make_sample(_user_taste(), _frog_taste(), "taste")


def gen_happy():
    return _make_sample(_user_happy(), _frog_happy(), "happy")


def gen_tadpole():
    return _make_sample(_user_tadpole(), _frog_tadpole(), "tadpole")


def gen_confused():
    # 70% structured "what is X" style, 30% random nonsense
    if random.random() < 0.3:
        return _make_sample(pick(NONSENSE_INPUTS), _frog_confused(), "confused")
    thing = pick(HUMAN_THINGS)
    return _make_sample(_user_confused(thing), _frog_confused(thing), "confused")


ALL_TOPICS = [
    gen_greeting,
    gen_feeling,
    gen_food,
    gen_rain,
    gen_lily_pad,
    gen_night,
    gen_jumping,
    gen_bugs,
    gen_pond,
    gen_weather,
    gen_croaking,
    gen_mud,
    gen_predators,
    gen_seasons,
    gen_friends,
    gen_philosophy,
    gen_tongue,
    gen_eyes,
    gen_swimming,
    gen_colors,
    gen_love,
    gen_jokes,
    gen_time,
    gen_dreams,
    gen_music,
    gen_intelligence,
    gen_water,
    gen_temperature,
    gen_humans,
    gen_confused,
    gen_bye,
    gen_about,
    gen_plants,
    gen_reflection,
    gen_scared,
    gen_excited,
    gen_bored,
    gen_curious,
    gen_tired,
    gen_outside,
    gen_cat,
    gen_birds,
    gen_size,
    gen_memory,
    gen_age,
    gen_sleep,
    gen_poop,
    gen_health,
    gen_noise,
    gen_visitors,
    gen_misc,
    gen_future,
    gen_past,
    gen_name,
    gen_breathing,
    gen_human_life,
    gen_light,
    gen_lonely,
    gen_taste,
    gen_happy,
    gen_tadpole,
]
