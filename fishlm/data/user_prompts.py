"""User message generators for fish conversations."""

from .vocabulary import pick, FOOD_TYPES, HUMAN_THINGS


def _user_greeting():
    return pick(["hi fish", "hello", "hey fish", "good morning fish", "hi", "hey", "hello little fish", "blub blub", "hi there", "good afternoon"])

def _user_feeling():
    return pick(["how are you", "how are you feeling", "you ok", "are you happy", "how do you feel", "what's your mood", "you good", "how's it going"])

def _user_food():
    return pick(["are you hungry", "want some food", "time to eat", "feeding time", "hungry?", f"want some {pick(FOOD_TYPES)}", "dinner time", "snack time", "food time"])

def _user_swimming():
    return pick(["are you swimming", "what are you doing", "swim around", "show me your swimming", "are you exercising", "lots of laps today"])

def _user_bubbles():
    return pick(["i see bubbles", "the bubbler is on", "are you blowing bubbles", "do you like bubbles", "bubbles are nice"])

def _user_glass():
    return pick(["can you see me", "do you bump the glass", "do you know there is glass", "are you stuck in there", "what is the glass like"])

def _user_memory():
    return pick(["do you remember me", "what do you remember", "do you remember yesterday", "do fish forget things", "is your memory short", "do you remember things"])

def _user_sleep():
    return pick(["do you sleep", "where do you sleep", "how do fish sleep", "do you close your eyes", "are you sleeping", "do fish dream"])

def _user_tank():
    return pick(["do you like your tank", "tell me about your tank", "is your tank nice", "what is in your tank", "is the tank big enough"])

def _user_friends():
    return pick(["do you have friends", "are we friends", "do you like the other fish", "who is your favorite fish"])

def _user_predators():
    return pick(["are you safe", "what eats fish", "are you scared of being eaten", "is anything dangerous"])

def _user_humans():
    return pick(["what do you think of me", "do you see me", "what do humans look like to you", "do you like the people", "we are humans"])

def _user_outside():
    return pick(["what do you see out there", "what is outside the tank", "do you want to come out", "do you see the room", "tell me about the world outside"])

def _user_night():
    return pick(["goodnight fish", "time to sleep", "sleep well", "lights out", "nighty night", "bedtime"])

def _user_water():
    return pick(["how is the water", "is the water clean", "do you like the water", "is the water nice today"])

def _user_temperature():
    return pick(["is the water warm", "is the water cold", "what is the temperature", "is it too hot in there"])

def _user_jokes():
    return pick(["tell me a joke", "make me laugh", "say something funny", "joke time", "be funny"])

def _user_love():
    return pick(["do you love me", "i love you fish", "what is love", "do you care about me", "you are cute"])

def _user_philosophy():
    return pick(["what is the meaning of life", "why are we here", "what is happiness", "any wisdom", "tell me something deep"])

def _user_about():
    return pick(["what are you", "tell me about yourself", "who are you", "what kind of fish are you", "describe yourself"])

def _user_intelligence():
    return pick(["are you smart", "how smart are you", "do you understand me", "are fish smart"])

def _user_dreams():
    return pick(["do you dream", "what do you dream about", "do fish dream", "what is in your dreams"])

def _user_size():
    return pick(["how big are you", "you're so small", "are you a small fish", "how much do you weigh"])

def _user_curious():
    return pick(["what are you looking at", "are you curious", "what caught your attention", "what's interesting today"])

def _user_bored():
    return pick(["are you bored", "you look bored", "need entertainment", "want to play"])

def _user_happy():
    return pick(["what makes you happy", "are you happy", "when are you happiest"])

def _user_scared():
    return pick(["are you scared", "what scares you", "don't be afraid", "are you ok"])

def _user_tired():
    return pick(["are you tired", "you look exhausted", "long day?", "need a rest"])

def _user_bye():
    return pick(["goodbye", "bye", "see you later", "gotta go", "bye fish", "i'm leaving", "i have to go", "heading out", "later", "i'll be back"])

def _user_name():
    return pick(["what is your name", "do you have a name", "what should i call you", "why are you called fish"])

def _user_age():
    return pick(["how old are you", "when were you born", "are you a baby fish"])

def _user_weather():
    return pick(["how's the weather", "it's raining", "nice day", "it's cold", "sunny today"])

def _user_time():
    return pick(["what time is it", "it's late", "it's early", "do fish know what time it is"])

def _user_health():
    return pick(["are you healthy", "are you sick", "do you feel ok", "you don't look well"])

def _user_noise():
    return pick(["was that loud", "did you hear that", "sorry about the noise", "did that scare you"])

def _user_visitors():
    return pick(["someone is visiting", "we have guests", "a friend is here", "someone new is here"])

def _user_breathing():
    return pick(["how do you breathe", "do you breathe water", "do fish breathe air", "how do gills work"])

def _user_eyes():
    return pick(["can you see well", "are your eyes open", "do you have good eyesight", "what do you see"])

def _user_color():
    return pick(["what color are you", "you are pretty", "your scales are shiny", "you are orange"])

def _user_misc():
    return pick(["tell me something", "say something", "what's on your mind", "talk to me", "surprise me", "tell me a story"])

def _user_human_life():
    return pick(["i am tired", "i am sad", "i had a bad day", "i am stressed", "i am happy today", "i am bored", "i feel sick", "i had a great day", "something bad happened"])

def _user_confused(thing=None):
    if thing is None:
        thing = pick(HUMAN_THINGS)
    return pick([f"what do you think about {thing}", f"do you know what {thing} is", f"tell me about {thing}", f"explain {thing}", f"what is {thing}", f"thoughts on {thing}", f"have you heard of {thing}", f"do you care about {thing}", f"i spent all day on {thing}"])
