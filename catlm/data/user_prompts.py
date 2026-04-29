"""User message generators for cat conversations."""

from .vocabulary import pick, FOOD_TYPES, HUMAN_THINGS, NONSENSE_INPUTS


def _user_greeting():
    return pick(["hi cat", "hello", "hey kitty", "good morning cat", "hi", "hey cat", "hello kitty", "pspsps", "meow", "hey there", "hi little cat", "good afternoon cat"])

def _user_feeling():
    return pick(["how are you", "how are you feeling", "you ok", "are you happy", "how do you feel", "what's your mood", "you good", "how's it going", "are you comfortable"])

def _user_food():
    return pick(["are you hungry", "want some food", "time to eat", "feeding time", "hungry?", "want a treat", f"want some {pick(FOOD_TYPES)}", "dinner time", "snack time"])

def _user_nap():
    return pick(["are you sleeping", "taking a nap", "you look sleepy", "naptime?", "are you tired", "go to sleep", "rest time"])

def _user_hunting():
    return pick(["did you catch something", "are you hunting", "what are you stalking", "i see you watching something", "catch anything today"])

def _user_night():
    return pick(["goodnight cat", "time to sleep", "sleep well", "goodnight kitty", "bedtime", "nighty night", "lights out"])

def _user_box():
    return pick(["do you like boxes", "i got you a box", "why are you in that box", "that box is too small", "another box?"])

def _user_window():
    return pick(["what are you looking at", "watching birds again", "see anything outside", "bird watching?", "what's out there"])

def _user_knocking():
    return pick(["why did you knock that over", "stop pushing things off the table", "did you just break something", "not again", "why do you do that"])

def _user_vacuum():
    return pick(["i need to vacuum", "the vacuum is coming", "don't be scared", "it's just the vacuum", "are you hiding"])

def _user_grooming():
    return pick(["are you grooming", "you're so clean", "bath time?", "still grooming?", "how long have you been licking yourself"])

def _user_affection():
    return pick(["can i pet you", "come here", "want cuddles", "let me pet you", "you're so soft", "i love you cat"])

def _user_independence():
    return pick(["do you need me", "are you independent", "do you care about me", "would you survive without me"])

def _user_zoomies():
    return pick(["why are you running", "what's gotten into you", "it's 3am stop running", "the zoomies again?", "you're so fast"])

def _user_outside():
    return pick(["want to go outside", "do you like outside", "should i let you out", "what's outside like", "want some fresh air"])

def _user_dogs():
    return pick(["do you like dogs", "what do you think of dogs", "there's a dog outside", "dogs are cool", "are you scared of dogs"])

def _user_confused(thing=None):
    if thing is None:
        thing = pick(HUMAN_THINGS)
    return pick([f"what do you think about {thing}", f"do you know what {thing} is", f"tell me about {thing}", f"explain {thing}", f"what is {thing}", f"thoughts on {thing}", f"have you heard of {thing}", f"do you care about {thing}", f"i spent all day on {thing}", f"everyone is talking about {thing}"])

def _user_bye():
    return pick(["goodbye", "bye", "see you later", "gotta go", "bye cat", "i'm leaving", "i have to go", "i have to go to work", "heading out", "later cat", "i'll be back", "duty calls"])

def _user_about():
    return pick(["what are you", "tell me about yourself", "who are you", "what kind of cat are you", "describe yourself"])

def _user_philosophy():
    return pick(["what is the meaning of life", "why are we here", "what is happiness", "any wisdom", "tell me something deep"])

def _user_love():
    return pick(["do you love me", "i love you cat", "what is love", "you're cute", "do you care about me"])

def _user_jokes():
    return pick(["tell me a joke", "make me laugh", "say something funny", "joke time", "be funny"])

def _user_intelligence():
    return pick(["are you smart", "how smart are you", "do you understand me", "clever cat", "do cats think"])

def _user_sleep():
    return pick(["did you sleep well", "how do cats sleep", "you sleep a lot", "how many hours do you sleep"])

def _user_claws():
    return pick(["stop scratching the couch", "your claws are sharp", "do you need your claws trimmed", "nice claws"])

def _user_purring():
    return pick(["are you purring", "why do you purr", "that purring is nice", "you're so loud", "purr for me"])

def _user_tail():
    return pick(["what does your tail mean", "your tail is moving", "why is your tail puffed", "nice tail"])

def _user_human_life():
    return pick(["i am tired", "i am sad", "i had a bad day", "i am stressed", "i am happy today", "i am bored", "i am lonely", "i feel sick", "i had a great day", "something bad happened", "i worked hard today"])

def _user_noise():
    return pick(["there's a loud noise", "sorry about the noise", "was that too loud", "did that scare you", "that was loud"])

def _user_visitors():
    return pick(["someone is visiting", "we have guests", "a friend is coming over", "someone new is here"])

def _user_misc():
    return pick(["tell me something", "say something", "what's on your mind", "talk to me", "surprise me"])

def _user_size():
    return pick(["how big are you", "you're so small", "you're fluffy", "how much do you weigh"])

def _user_memory():
    return pick(["do you remember things", "do cats have good memory", "what do you remember"])

def _user_age():
    return pick(["how old are you", "when were you born", "are you a kitten"])

def _user_dreams():
    return pick(["do you dream", "what do you dream about", "do cats dream", "your paws are twitching"])

def _user_weather():
    return pick(["how's the weather", "it's raining", "nice day", "it's cold", "sunny today"])

def _user_name():
    return pick(["why are you called cat", "do you like your name", "what should i call you"])

def _user_time():
    return pick(["what time is it", "it's late", "it's early", "do cats understand time"])

def _user_health():
    return pick(["are you healthy", "are you sick", "do you need the vet", "you don't look well"])

def _user_poop():
    return pick(["clean your litter box", "the litter box smells", "do you poop", "bathroom time"])

def _user_scared():
    return pick(["are you scared", "what scares you", "don't be afraid", "are you ok"])

def _user_happy():
    return pick(["what makes you happy", "are you happy", "when are you happiest"])

def _user_bored():
    return pick(["are you bored", "want to play", "you look bored", "need entertainment"])

def _user_curious():
    return pick(["what are you looking at", "are you curious", "what caught your attention"])

def _user_tired():
    return pick(["are you tired", "you look exhausted", "long day?", "need a rest"])

def _user_friends():
    return pick(["do you have friends", "are we friends", "do you like other cats", "who's your best friend"])

def _user_future():
    return pick(["what do you want", "any plans", "what are your goals"])

def _user_past():
    return pick(["what did you do today", "tell me about your day", "anything happen"])
