"""User message generators — simulated human inputs."""

from .vocabulary import BUG_TYPES, HUMAN_THINGS, pick


def _user_greeting():
    return pick(
        [
            "hi frog",
            "hello",
            "hey there",
            "good morning frog",
            "hi",
            "hey frog",
            "greetings",
            "howdy frog",
            "what's up frog",
            "yo frog",
            "hello frog",
            "hey",
            "morning frog",
            "hi little frog",
            "hey buddy",
            "good afternoon frog",
            "good evening frog",
            "hi friend",
        ]
    )


def _user_feeling():
    return pick(
        [
            "how are you",
            "how are you feeling",
            "you ok",
            "are you happy",
            "how do you feel",
            "what's your mood",
            "you good",
            "how's it going",
            "everything alright",
            "how's life",
            "are you doing ok",
            "feeling good",
            "how is everything",
            "are you comfortable",
        ]
    )


def _user_food():
    return pick(
        [
            "are you hungry",
            "want some food",
            "time to eat",
            "do you want food",
            "feeding time",
            "hungry?",
            "what do you eat",
            "want a snack",
            "what's for dinner",
            "need food",
            "are you starving",
            f"want some {pick(BUG_TYPES)}s",
            "dinner time",
            "snack time",
        ]
    )


def _user_rain():
    return pick(
        [
            "it's raining",
            "do you like rain",
            "it's wet outside",
            "rain is coming",
            "rainy day",
            "it's pouring",
            "thunderstorm",
            "drizzle",
            "rain again",
            "lots of rain today",
            "it's a rainy day",
            "the sky is crying",
        ]
    )


def _user_lily_pad():
    return pick(
        [
            "tell me about your lily pad",
            "do you like lily pads",
            "where do you sit",
            "what's your favorite spot",
            "are you on a lily pad",
            "nice pad",
            "comfy?",
            "where are you right now",
            "that's a big lily pad",
        ]
    )


def _user_night():
    return pick(
        [
            "goodnight frog",
            "time to sleep",
            "sleep well",
            "sweet dreams",
            "nighty night",
            "rest well frog",
            "going to bed",
            "goodnight little frog",
            "it's late goodnight",
            "bedtime frog",
            "lights out",
        ]
    )


def _user_jumping():
    return pick(
        [
            "can you jump",
            "how high can you jump",
            "do you like jumping",
            "jump for me",
            "show me a jump",
            "are frogs good jumpers",
            "leap frog",
            "how far can you jump",
            "jump!",
            "do a flip",
        ]
    )


def _user_bugs():
    return pick(
        [
            "do you like bugs",
            "what's your favorite bug",
            "catch any bugs today",
            "tell me about flies",
            "bugs are gross",
            "see any insects",
            "what bugs do you eat",
            "mosquito!",
            "there's a fly",
            "bug report",
        ]
    )


def _user_pond():
    return pick(
        [
            "tell me about your pond",
            "is the pond nice",
            "how's the water",
            "what's in the pond",
            "do you like your pond",
            "pond life",
            "is the pond big",
            "describe your pond",
            "nice pond",
        ]
    )


def _user_weather():
    return pick(
        [
            "how's the weather",
            "is it hot",
            "is it cold",
            "nice day",
            "what's the temperature",
            "sunny today",
            "cloudy",
            "windy",
            "the weather is nice",
            "weather report",
        ]
    )


def _user_croaking():
    return pick(
        [
            "why do you croak",
            "croak for me",
            "you're loud",
            "ribbit",
            "sing me a song",
            "what does ribbit mean",
            "do all frogs croak",
            "nice voice",
            "you're noisy",
            "croak croak",
        ]
    )


def _user_mud():
    return pick(
        [
            "do you like mud",
            "you're muddy",
            "tell me about mud",
            "is mud fun",
            "mud bath",
            "why do frogs like mud",
            "dirty frog",
            "mud puddle",
            "that's a lot of mud",
            "muddy",
        ]
    )


def _user_predators():
    return pick(
        [
            "are you scared of anything",
            "watch out for that bird",
            "is that a snake",
            "do you have enemies",
            "what eats frogs",
            "heron!",
            "danger",
            "be careful",
            "are you safe",
        ]
    )


def _user_seasons():
    return pick(
        [
            "what's your favorite season",
            "is it spring",
            "do you hibernate",
            "winter is coming",
            "summer time",
            "fall leaves",
            "do you like spring",
            "what do you do in winter",
            "autumn",
            "the seasons are changing",
        ]
    )


def _user_friends():
    return pick(
        [
            "do you have friends",
            "who are your friends",
            "are you lonely",
            "any pond buddies",
            "do you like the fish",
            "who do you hang out with",
            "best friend?",
            "frog friends",
            "are we friends",
        ]
    )


def _user_philosophy():
    return pick(
        [
            "what is the meaning of life",
            "why are we here",
            "what is happiness",
            "tell me something deep",
            "are you wise",
            "what is truth",
            "meaning of existence",
            "purpose of life",
            "what matters most",
            "any wisdom",
        ]
    )


def _user_tongue():
    return pick(
        [
            "show me your tongue",
            "how fast is your tongue",
            "that's a long tongue",
            "how do you catch bugs",
            "sticky tongue",
            "your tongue is cool",
            "tongue facts",
            "how does your tongue work",
        ]
    )


def _user_eyes():
    return pick(
        [
            "your eyes are big",
            "can you see well",
            "why are your eyes on top",
            "nice eyes",
            "what do you see",
            "frog eyes",
            "do you blink",
            "those are cool eyes",
            "look at those eyes",
        ]
    )


def _user_swimming():
    return pick(
        [
            "can you swim",
            "do you like swimming",
            "go for a swim",
            "how do you swim",
            "swim time",
            "are you a good swimmer",
            "water frog",
            "dive in",
            "splash",
        ]
    )


def _user_colors():
    return pick(
        [
            "what color are you",
            "you're green",
            "pretty colors",
            "why are you green",
            "do frogs come in other colors",
            "green frog",
            "nice shade of green",
            "camouflage",
            "your skin is cool",
        ]
    )


def _user_love():
    return pick(
        [
            "do you love me",
            "i love you frog",
            "what is love",
            "do frogs fall in love",
            "you're cute",
            "love you",
            "do you have a girlfriend",
            "frog love",
        ]
    )


def _user_jokes():
    return pick(
        [
            "tell me a joke",
            "make me laugh",
            "funny frog",
            "know any jokes",
            "joke time",
            "say something funny",
            "humor me",
            "frog joke",
            "be funny",
        ]
    )


def _user_time():
    return pick(
        [
            "what time is it",
            "do you know what day it is",
            "how old are you",
            "do frogs understand time",
            "time flies",
            "it's late",
            "it's early",
            "how long have you been here",
        ]
    )


def _user_dreams():
    return pick(
        [
            "do you dream",
            "what do you dream about",
            "had any good dreams",
            "sweet dreams",
            "do frogs dream",
            "last night's dream",
            "daydream",
        ]
    )


def _user_music():
    return pick(
        [
            "do you like music",
            "sing for me",
            "what music do you like",
            "play a song",
            "frog choir",
            "concert",
            "do you sing",
            "musical frog",
        ]
    )


def _user_intelligence():
    return pick(
        [
            "are you smart",
            "do frogs think",
            "what do you know",
            "brain size",
            "clever frog",
            "do you understand me",
            "how smart are you",
            "genius frog",
        ]
    )


def _user_water():
    return pick(
        [
            "do you need water",
            "how's the water",
            "water quality",
            "is the water clean",
            "water temperature",
            "the water looks nice",
            "how does the water feel",
            "is the water ok",
        ]
    )


def _user_temperature():
    return pick(
        [
            "are you cold",
            "is it warm",
            "temperature check",
            "too hot?",
            "too cold?",
            "do you get cold",
            "warm frog",
            "cold blooded",
            "body temperature",
        ]
    )


def _user_humans():
    return pick(
        [
            "what do you think of humans",
            "do you like people",
            "am i scary",
            "what am i to you",
            "human friend",
            "do you trust me",
            "people are weird",
            "what are humans",
        ]
    )


def _user_confused(thing=None):
    if thing is None:
        thing = pick(HUMAN_THINGS)
    return pick(
        [
            f"what do you think about {thing}",
            f"do you know what {thing} is",
            f"have you heard of {thing}",
            f"do you use {thing}",
            f"tell me about {thing}",
            f"explain {thing}",
            f"what is {thing}",
            f"thoughts on {thing}",
            f"did you ever try {thing}",
            f"i really like {thing}",
            f"have you ever used {thing}",
            f"do you want {thing}",
            f"i need help with {thing}",
            f"can you believe {thing}",
            f"i was thinking about {thing} today",
            f"do you know anything about {thing}",
            f"my friend told me about {thing}",
            f"everyone is talking about {thing}",
            f"i just bought {thing}",
            f"should i get {thing}",
            f"did you buy {thing} when you had the chance",
            f"what would you do with {thing}",
            f"i spent all day on {thing}",
            f"how do you feel about {thing}",
            f"{thing} is really important to me",
            f"i cannot stop thinking about {thing}",
        ]
    )


def _user_bye():
    return pick(
        [
            "goodbye",
            "bye",
            "see you later",
            "gotta go",
            "talk later",
            "bye frog",
            "see you",
            "later frog",
            "bye bye",
            "catch you later",
            "i'm heading out",
            "i have to go",
            "i need to leave",
            "i have to go to work",
            "i have to go to office",
            "i must leave now",
            "time for me to go",
            "heading out",
            "i need to run",
            "off i go",
            "i have things to do",
            "i have to go somewhere",
            "duty calls",
            "i have a meeting",
            "i have to go home",
            "brb",
            "i will be back",
        ]
    )


def _user_about():
    return pick(
        [
            "what are you",
            "tell me about yourself",
            "who are you",
            "what kind of frog are you",
            "what do you do all day",
            "describe yourself",
            "what's your life like",
            "do you have a name",
            "who is frog",
        ]
    )


def _user_plants():
    return pick(
        [
            "do you like plants",
            "nice plants",
            "what plants are in the pond",
            "tell me about the reeds",
            "algae",
            "flowers",
            "pond plants",
        ]
    )


def _user_reflection():
    return pick(
        ["do you see yourself", "that's your reflection", "you're looking at yourself", "do you recognize yourself"]
    )


def _user_scared():
    return pick(["are you scared", "what scares you", "don't be scared", "are you afraid", "what's your biggest fear"])


def _user_excited():
    return pick(["are you excited", "you seem excited", "what excites you", "you're jumping a lot"])


def _user_bored():
    return pick(["are you bored", "is it boring", "what do you do when you're bored", "you look bored"])


def _user_curious():
    return pick(
        [
            "what are you looking at",
            "are you curious about something",
            "you seem interested",
            "what caught your attention",
        ]
    )


def _user_tired():
    return pick(["are you tired", "you look sleepy", "do frogs get tired", "take a rest"])


def _user_outside():
    return pick(
        [
            "what do you think is outside",
            "do you wonder about the outside",
            "there's a whole world out there",
            "have you ever left the pond",
        ]
    )


def _user_cat():
    return pick(
        ["the cat is looking at you", "do you see the cat", "are you scared of the cat", "there's a cat by the pond"]
    )


def _user_birds():
    return pick(
        [
            "have you met birds",
            "do you like birds",
            "there is a bird",
            "bird!",
            "watch out for that bird",
            "the bird is back",
            "do birds scare you",
            "a duck is here",
            "birds are cool",
        ]
    )


def _user_size():
    return pick(["how big are you", "you're so small", "will you grow bigger", "how big is your world"])


def _user_memory():
    return pick(
        ["do you remember things", "what do you remember", "do frogs have good memory", "do you forget things"]
    )


def _user_age():
    return pick(["how old are you", "when were you born", "when is your birthday", "how long have you been here"])


def _user_sleep():
    return pick(["did you sleep well", "how do frogs sleep", "were you sleeping", "i just woke up"])


def _user_poop():
    return pick(["do you poop", "where do you go to the bathroom", "the pond needs cleaning", "gross"])


def _user_health():
    return pick(["are you sick", "are you healthy", "you don't look well", "do frogs get sick", "are you ok"])


def _user_noise():
    return pick(
        [
            "there's a loud noise",
            "sorry about the noise",
            "was that too loud",
            "i dropped something",
            "did that scare you",
            "that was loud",
        ]
    )


def _user_visitors():
    return pick(["someone is visiting", "we have guests", "a friend wants to see you", "someone new is here"])


def _user_misc():
    return pick(
        [
            "tell me something",
            "say something",
            "anything to say",
            "what's on your mind",
            "talk to me",
            "what are you thinking about",
            "surprise me",
        ]
    )


def _user_future():
    return pick(["what do you want", "what are your goals", "any plans for tomorrow", "what do you hope for"])


def _user_past():
    return pick(
        ["what happened today", "what did you do yesterday", "tell me about your day", "anything happen recently"]
    )


def _user_name():
    return pick(["why are you called frog", "do you like your name", "who named you", "what does frog mean"])


def _user_breathing():
    return pick(["how do you breathe", "are you breathing ok", "do frogs breathe air", "how do your lungs work"])


def _user_human_life():
    return pick(
        [
            "i am tired",
            "i am sad",
            "i had a bad day",
            "i am stressed",
            "i am happy today",
            "i failed my test",
            "i am bored",
            "i am excited",
            "i am angry",
            "i had a great day",
            "i am lonely",
            "i feel sick",
            "i am worried",
            "i ate too much",
            "i can not sleep",
            "i miss my friend",
            "i am cold",
            "i am hot",
            "i had fun today",
            "my day was long",
            "i worked hard today",
            "i am exhausted",
            "something good happened",
            "something bad happened",
            "i am grateful",
            "i feel good",
        ]
    )


def _user_light():
    return pick(
        [
            "the sun is out",
            "it's bright today",
            "it's getting dark",
            "the light changed",
            "is the light bothering you",
            "nice sunset",
            "the moon is bright",
            "it's so dark",
            "sunny day",
        ]
    )


def _user_lonely():
    return pick(
        [
            "do you get lonely",
            "are you lonely",
            "do you want a friend",
            "is it boring being alone",
            "do you need company",
            "are you ok by yourself",
            "do you ever feel alone",
        ]
    )


def _user_taste():
    return pick(
        [
            "can you taste things",
            "what does the water taste like",
            "do you taste food",
            "how does a fly taste",
            "what do bugs taste like",
            "do frogs have taste buds",
        ]
    )


def _user_happy():
    return pick(
        [
            "what makes you happy",
            "are you happy",
            "when are you happiest",
            "what's the best part of your day",
            "what do you enjoy",
        ]
    )


def _user_tadpole():
    return pick(
        [
            "were you a tadpole",
            "tell me about being a tadpole",
            "do you remember being a tadpole",
            "what was it like as a tadpole",
            "did you have a tail",
            "how did you grow legs",
        ]
    )
