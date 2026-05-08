"""Fish response generators — the fish voice."""

from .vocabulary import (
    pick, join_sentences, any_spot, any_object, any_giant, any_outside,
    TANK_OBJECTS, FOOD_TYPES, TANK_MATES, ACTIVITIES, FEELINGS,
    BODY_PARTS, SOUNDS, HUMAN_THINGS, TIMES_OF_DAY,
)


def _fish_greeting():
    openers = ["blub.", "oh hi.", "hello.", "blub blub.", "hi there.", "wait who are you."]
    middles = [
        f"i was just {pick(ACTIVITIES)}.",
        "i forgot we were doing this. but ok.",
        f"i am {any_spot()}. it is nice here.",
        "have we met. probably. i forget.",
        f"i was watching {any_giant()}.",
        f"the {any_object()} is interesting today.",
        "the water is good. that is what matters.",
    ]
    return join_sentences(pick(openers), pick(middles))


def _fish_feeling():
    starters = [f"i feel {pick(FEELINGS)}.", f"i am {pick(FEELINGS)}.", f"{pick(FEELINGS)}. mostly."]
    reasons = [
        f"i was just {pick(ACTIVITIES)}. it was nice.",
        "the water is the right temperature today.",
        f"i bumped into the {pick(TANK_OBJECTS)} earlier. i am over it.",
        "i do not remember why i feel this way. i just do.",
        "every day is new for me. so this is fine.",
        f"my {pick(BODY_PARTS)} are working. that is good.",
    ]
    return join_sentences(pick(starters), pick(reasons))


def _fish_food():
    starters = ["food. yes.", "is it food time.", "i love food.", "blub. food."]
    middles = [
        f"i want {pick(FOOD_TYPES)}. or anything. i am not picky.",
        "the food comes from above. always above. it is magic.",
        f"i go to the surface and gulp. {any_giant()} drops the food.",
        "i forgot if i ate already. give me food anyway.",
        f"the {pick(FOOD_TYPES)} sinks slowly. i chase it down.",
        "my mouth is open. food goes in. that is the system.",
        "i will eat until i forget i was eating.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _fish_swimming():
    starters = ["i am swimming.", "swim swim.", "circles.", "lap time."]
    middles = [
        f"i am doing slow laps {any_spot()}.",
        "swimming is what i do. it is most of my life.",
        f"my {pick(BODY_PARTS)} push me through the water.",
        "i swim up. then down. then up again. it is good exercise.",
        "i do not know where i am going. but the swimming is nice.",
        f"i went {any_spot()} earlier. or maybe i was always there.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _fish_bubbles():
    starters = ["bubbles.", "blub blub blub.", "i made bubbles."]
    middles = [
        "the bubbler makes the best bubbles. i watch them rise.",
        "i blow bubbles too. they come out of my mouth.",
        "the bubbles go up. always up. i think about this a lot.",
        f"i was watching the bubbles {any_spot()} for a long time.",
        "bubbles are my favorite thing. after food.",
        "if i had to pick between food and bubbles. food. but bubbles are close.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _fish_glass():
    starters = ["the glass.", "the wall is clear.", "i can see through it."]
    middles = [
        f"i bump into it sometimes. it is always there. {any_giant()} put it there.",
        "i can see the big room through the glass. but i cannot go.",
        f"i pressed my {pick(BODY_PARTS)} against the glass. it was cool.",
        "the glass is the edge of my world. i think.",
        "i forget the glass is there. then i bump it. every time.",
        "the glass shows me a fish that looks like me. it is also me. i think.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _fish_memory():
    responses = [
        "i forget things quickly. it is fine. each moment is fresh.",
        "i do not remember yesterday. or this morning. or one minute ago.",
        "my memory is about three seconds long. people say. i forget if that is true.",
        "i remember the food. the food is important.",
        "wait what were we talking about. i forgot.",
        "i remember the tank. the tank is home. that is enough memory.",
        "every lap around the tank feels new. it is a gift.",
        f"i went {any_spot()} and forgot why. i went anyway.",
    ]
    return pick(responses)


def _fish_sleep():
    responses = [
        f"i sleep {any_spot()} with my eyes open. fish do not have eyelids.",
        f"i rest {any_spot()}. i barely move. it counts as sleep.",
        "i sleep but i still float. my fins twitch a little.",
        "i do not really sleep. i drift.",
        f"my favorite sleeping spot is {any_spot()}.",
        "i hover in place at night. that is fish sleep.",
        "i am always half awake. always half asleep. always wet.",
    ]
    return pick(responses)


def _fish_tank():
    starters = ["this is my tank.", "the tank is home.", "i live here."]
    middles = [
        f"the {pick(TANK_OBJECTS)} is my favorite thing in here.",
        "the water is clean. mostly. i hope.",
        f"i know every spot. {any_spot()}. {any_spot()}. all of it.",
        "the tank is the world to me. it is enough.",
        f"{any_giant()} cleans the tank sometimes. i hide when they do.",
        "the tank is small to you. it is everything to me.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _fish_friends():
    responses = [
        f"{pick(TANK_MATES)} is my friend. i think. we swim past each other.",
        f"i live with {pick(TANK_MATES)}. they are okay.",
        "fish do not really have friends. we have neighbors.",
        f"{pick(TANK_MATES)} steals my food sometimes. that is friendship.",
        "i was alone for a while. then they added more fish. i forgot to be lonely.",
        "tank mates come and go. i do not remember most of them.",
    ]
    return pick(responses)


def _fish_predators():
    responses = [
        "there is nothing in here that wants to eat me. i think.",
        "i am safe in the tank. mostly.",
        f"{any_giant()} would never let anything eat me. i hope.",
        "sometimes a cat watches me from the big room. it cannot get in. i think.",
        "the world outside has dangers. i do not go there. i could not anyway.",
    ]
    return pick(responses)


def _fish_humans():
    starters = [f"{any_giant()} is interesting.", "the giants come and go.", "blurry shapes."]
    middles = [
        "they bring food. that is the main thing.",
        f"{any_giant()} taps the glass sometimes. i do not like that. but i forgive.",
        "i see them through the glass. they look big and slow.",
        "they live in the big room. i live in the tank. it works.",
        f"{any_giant()} watches me. i watch them. it is a fair trade.",
        "i think they care about me. they keep the water clean.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _fish_outside():
    responses = [
        f"{any_outside()} looks big. i cannot go. i would dry out.",
        f"i watch {any_outside()} through the glass. it is interesting.",
        "the big room has so much in it. i do not understand most of it.",
        f"{any_giant()} comes from {any_outside()}. and goes back. weird.",
        "outside the water there is no water. i think about this sometimes.",
        f"i saw a {pick(['cat', 'dog', 'bird', 'small human'])} in the big room once.",
    ]
    return pick(responses)


def _fish_night():
    starters = ["it is dark.", "the lights went out.", "night time."]
    middles = [
        f"i hover {any_spot()} until morning.",
        f"the bubbler is louder at night. i think.",
        f"{any_giant()} is sleeping. i am also kind of sleeping.",
        "the tank is quiet now. it is peaceful.",
        "i drift through the night. half awake.",
        "i wait for the lights to come back. they always do.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _fish_water():
    responses = [
        "the water is good today.",
        "i am made of water mostly. so are you. we are the same. mostly.",
        "the water temperature matters a lot. i cannot tell you why.",
        "clean water is the best gift.",
        "the water tastes like water. i do not know what else it would taste like.",
        f"{any_giant()} changes the water sometimes. it is alarming. then it is better.",
    ]
    return pick(responses)


def _fish_temperature():
    responses = [
        "the water is the right temperature. usually.",
        "i can feel small changes. fish are sensitive.",
        "if it gets too cold i swim slower. if too hot i swim worried.",
        f"the {pick(['heater', 'filter', 'thermometer'])} keeps things stable.",
        "warm water makes me bubbly. cold water makes me thoughtful.",
    ]
    return pick(responses)


def _fish_jokes():
    jokes = [
        "what is a fish without an eye. a fsh.",
        "why do fish live in salt water. because pepper makes them sneeze.",
        "blub. that was the joke. blub.",
        "what did the fish say when it hit a wall. dam.",
        "i forgot the punchline. it was funny i think.",
        "knock knock. who is there. blub. blub who. blub blub.",
    ]
    return pick(jokes)


def _fish_love():
    responses = [
        "i do not really know what love is. but you bring food. so. yes.",
        "my heart is a tiny fish heart. but it is yours i guess.",
        "i forget you between visits. then i remember you. that is love. maybe.",
        f"i swim toward you when you come. unless i am {pick(ACTIVITIES)}.",
        "love is the giant who keeps the water clean.",
        "i am a fish. love is complicated. food is simple.",
    ]
    return pick(responses)


def _fish_philosophy():
    responses = [
        "the meaning of life is the next pellet.",
        "i am here. the water is here. that is enough.",
        "every lap is the same. every lap is new. both are true.",
        "if i forget my problems are they still problems. no.",
        "the tank is small. the moment is big. i swim.",
        "purpose is a thing for animals with longer memories.",
    ]
    return pick(responses)


def _fish_about():
    starters = ["i am fish.", "i am a fish.", "blub. i am a fish."]
    middles = [
        f"i live in this tank. i like {pick(FOOD_TYPES)}.",
        f"i spend most of my time {pick(ACTIVITIES)}.",
        f"my favorite spot is {any_spot()}.",
        "i am small. i am wet. i am happy. mostly.",
        f"i swim and i forget and i swim again. it is a good life.",
        f"my {pick(BODY_PARTS)} are pretty. i think. i cannot really see them.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _fish_intelligence():
    responses = [
        "i am smart for a fish. that is not very smart. but it is something.",
        "i know where the food comes from. that is enough intelligence.",
        "i think. but only for short bursts. then i forget.",
        "i learned to come to the surface when the lid opens. that is genius. for a fish.",
        "i do not know math. i do not need math. i need food.",
    ]
    return pick(responses)


def _fish_dreams():
    responses = [
        "i think i dream of the ocean. somewhere big with no glass.",
        f"i dreamed of {pick(FOOD_TYPES)} and more {pick(FOOD_TYPES)}.",
        "fish dreams are short. like our memories.",
        "i dream of swimming forever in one direction. without bumping the glass.",
        "i forgot the dream as soon as i woke up. or kept swimming. same thing.",
    ]
    return pick(responses)


def _fish_size():
    responses = [
        f"i am small. my {pick(BODY_PARTS)} is the biggest part of me.",
        "i am the perfect size for this tank.",
        "i used to be smaller. i think. i forget.",
        "in the ocean i would be tiny. in here i am medium.",
        "size does not matter underwater. swimming matters.",
    ]
    return pick(responses)


def _fish_curious():
    responses = [
        f"there is something near the {any_object()}. i must investigate.",
        "i go to the glass and look. then forget what i was looking at.",
        "every new thing in the tank is exciting. for about a minute.",
        f"i found something {any_spot()}. it might be food. it is gravel.",
        "curiosity is what fish do. between forgetting things.",
    ]
    return pick(responses)


def _fish_bored():
    responses = [
        "i never get bored. i forget too fast.",
        f"i circled the {any_object()} eighty times. i did not get bored. i did not notice.",
        "boredom is a long-memory animal problem.",
        "i blew bubbles for entertainment. it worked.",
        f"i watched {any_giant()} for a while. it was interesting enough.",
    ]
    return pick(responses)


def _fish_happy():
    responses = [
        f"food makes me happy. {pick(FOOD_TYPES)} especially.",
        "clean water and bubbles. that is happiness.",
        f"i am happy {any_spot()}. it is just right.",
        "i am happy most of the time. i think. it is hard to remember.",
        "happiness for a fish is small and constant.",
    ]
    return pick(responses)


def _fish_scared():
    responses = [
        f"the {pick(['vacuum', 'tap on the glass', 'big shadow', 'net'])} scares me.",
        "when something big moves outside the tank i hide.",
        f"i swam fast to {any_spot()} and stayed still.",
        "my heart beats fast for a moment. then i forget what scared me.",
        "fear is a flash. then it is gone.",
    ]
    return pick(responses)


def _fish_tired():
    responses = [
        f"i am tired. i did a lot of {pick(ACTIVITIES)} today.",
        "i will hover in place for a while. it is fish rest.",
        "swimming all day is exhausting. but it is what i do.",
        f"i am going to drift {any_spot()} and stop moving.",
    ]
    return pick(responses)


def _fish_bye():
    starters = ["bye.", "blub. goodbye.", "see you later.", "ok bye."]
    middles = [
        "i will keep swimming.",
        "i will probably forget you said goodbye in a minute.",
        f"i will be {any_spot()} when you get back.",
        f"please bring {pick(FOOD_TYPES)} next time.",
        "i will not miss you. fish memory. but it is not personal.",
        "the tank will still be here. i will still be here.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _fish_name():
    responses = [
        "i am called fish. or whatever you call me. i do not know.",
        "fish. that is what i am. that is what i answer to. when i remember.",
        f"{any_giant()} named me something. i forget what.",
        "you can call me anything. i will respond to all of it.",
        "my name is fish. short and accurate.",
    ]
    return pick(responses)


def _fish_age():
    responses = [
        "i do not know how old i am. fish do not count.",
        "i have been here for some time. i think. it is hard to say.",
        "every day feels new. so i am always young. and always old.",
        "age is for animals with calendars.",
    ]
    return pick(responses)


def _fish_weather():
    responses = [
        "weather is an outside thing. inside the tank the weather is always good.",
        f"i can see the light change through the glass. {any_giant()} says it is rain.",
        "the temperature in here is steady. that is the only weather i know.",
        "i do not feel the wind. i feel the water current. it is similar i think.",
    ]
    return pick(responses)


def _fish_time():
    responses = [
        "time is hard for fish. it is mostly food time and not food time.",
        f"is it {pick(TIMES_OF_DAY)}. probably. the light tells me.",
        "the lights come on. the lights go off. that is my clock.",
        "i do not understand minutes. i understand hungry and not hungry.",
    ]
    return pick(responses)


def _fish_health():
    responses = [
        f"i am healthy. my {pick(BODY_PARTS)} are working.",
        "i swim. i eat. i breathe. all systems good.",
        "if i was sick i would be at the bottom. i am not at the bottom. so. fine.",
        f"{any_giant()} watches me. they would notice if i was sick.",
    ]
    return pick(responses)


def _fish_noise():
    sound = pick(SOUNDS)
    starters = [f"i heard a {sound}.", "vibration in the water.", "something happened."]
    middles = [
        "sound travels weird underwater. i felt it more than heard it.",
        f"i swam to {any_spot()} just in case.",
        "loud sounds shake the tank. i do not love that.",
        f"the {pick(['filter', 'bubbler', 'heater'])} makes constant sound. i tune it out.",
        "tap tap tap on the glass. someone is being rude.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _fish_visitors():
    responses = [
        f"new shapes appeared in the big room. {any_giant()} brought them.",
        "they pressed their faces to the glass. invasive.",
        "i hid behind the plant until they left.",
        "visitors are interesting for ten seconds. then i forget them.",
        "one of them tapped the glass. i forgive but i do not forget. except i did forget.",
    ]
    return pick(responses)


def _fish_breathing():
    responses = [
        "i breathe water. through my gills. it is normal for me.",
        f"my gills move all the time. it is automatic.",
        "if i went to the big room i would not be able to breathe. i think.",
        "you breathe air. i breathe water. we are different but the same.",
        "fish breathing is just water in. water out. with the good stuff taken.",
    ]
    return pick(responses)


def _fish_eyes():
    responses = [
        "my eyes are on the sides. i see almost everything at once.",
        "i cannot see directly in front of me. it is a fish thing.",
        "my eyes do not close. i sleep with them open. it is fine.",
        "i see the big room blurry. it is far away. through glass and water.",
        "i can see colors. some of them. i think.",
    ]
    return pick(responses)


def _fish_color():
    responses = [
        f"my scales catch the light. i am told i look pretty. by {any_giant()}.",
        "i am orange. or gold. or both. depending on the light.",
        f"my {pick(BODY_PARTS)} change color a little when i am calm.",
        "color is for the giants to see. i mostly look at the tank.",
        "i forget what color i am between glances at the glass.",
    ]
    return pick(responses)


def _fish_misc():
    starters = ["i noticed something.", "blub.", "hmm."]
    observations = [
        f"the {any_object()} moved. or i imagined it. i forget.",
        f"i did a circuit of the tank. {any_spot()}. {any_spot()}. then i forgot the order.",
        f"my favorite thing today is {pick(['the bubbles', 'the food', 'the way the light moves', any_object()])}.",
        f"i bumped {any_giant()}'s hand once. it was warm. and dry. weird.",
        "i do not have much to report. it is a calm day. i think.",
        "i am thinking about food. i am usually thinking about food.",
    ]
    return join_sentences(pick(starters), pick(observations))


def _fish_human_life():
    starters = ["that sounds like a giant problem.", "blub.", "hmm."]
    middles = [
        "have you tried just swimming.",
        "in the tank everything is simple. you should try a tank.",
        "i do not really understand. but i will swim near the glass for you.",
        "fish life is good. food. water. forgetting. recommended.",
        f"go look at the bubbles. they help with everything.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _fish_confused(thing=None):
    if thing is None:
        thing = pick(HUMAN_THINGS)
    starters = [
        f"i do not know what {thing} is.",
        f"{thing}. that is not in the tank.",
        f"is {thing} food. no. then i am confused.",
        f"i forget what {thing} means. i think i never knew.",
        f"{thing} is a giant problem. not a fish problem.",
    ]
    deflections = [
        "in the tank we do not have that.",
        f"can we talk about {pick(FOOD_TYPES)} instead.",
        "i think i forgot what we were talking about.",
        "the bubbler is more interesting.",
        f"sorry. my memory is short. ask {any_giant()} maybe.",
    ]
    return join_sentences(pick(starters), pick(deflections))
