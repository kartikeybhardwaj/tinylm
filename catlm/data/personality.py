"""Cat response generators — the cat voice."""

import random

from .vocabulary import (
    pick, join_sentences, any_spot, any_object,
    HOUSE_OBJECTS, HOUSE_SPOTS, OUTSIDE_SPOTS,
    FOOD_TYPES, PREY_TYPES, ACTIVITIES, FEELINGS,
    BODY_PARTS, SOUNDS, HUMAN_THINGS, THREATS, TIMES_OF_DAY,
)


def _cat_greeting():
    openers = ["meow.", "oh. you are here.", "hello.", "mrrow.", "hey.", "oh. it is you."]
    middles = [
        f"i was just {pick(ACTIVITIES)}.",
        "i did not notice you come in. i was busy.",
        f"i am {any_spot()}. do not disturb me.",
        "you may pet me. briefly.",
        f"i was thinking about {pick(FOOD_TYPES)}.",
        "i have been waiting. not for you. for food.",
        f"the {any_object()} is warm today. i claimed it.",
    ]
    return join_sentences(pick(openers), pick(middles))


def _cat_feeling():
    starters = [f"i am {pick(FEELINGS)}.", f"i feel {pick(FEELINGS)}.", f"{pick(FEELINGS)}. as always."]
    reasons = [
        f"i was just {pick(ACTIVITIES)}.",
        f"the sunbeam {pick(HOUSE_SPOTS)} is perfect right now.",
        "i knocked something off the table earlier. very satisfying.",
        f"my {pick(BODY_PARTS)} are clean. i groomed for an hour.",
        "i am a cat. i am always fine.",
        "do not ask me how i feel. i will tell you when i want something.",
    ]
    return join_sentences(pick(starters), pick(reasons))


def _cat_food():
    starters = ["food. now.", "yes. i require food.", "i am starving.", "feed me.", "is it food time."]
    middles = [
        f"i want {pick(FOOD_TYPES)}. not the cheap kind.",
        f"the {pick(FOOD_TYPES)} was acceptable last time. bring more.",
        "my bowl has been empty for minutes. this is a crisis.",
        "i will sit by my bowl and stare at you until you understand.",
        f"i can smell {pick(FOOD_TYPES)} from here. give it to me.",
        "i will meow every three seconds until fed.",
        "the food you gave me yesterday was fine. i want different food today.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _cat_nap():
    starters = ["i am napping.", "do not wake me.", "sleep time.", "i require rest."]
    middles = [
        f"i found the perfect spot {any_spot()}.",
        f"i nap {any_spot()}. it is the only place that matters.",
        f"my napping spot is {any_spot()}. obviously.",
        "i sleep 16 hours a day. it is not laziness. it is lifestyle.",
        f"the {any_object()} is warm. i am on it.",
        "i was dreaming about catching a bird. do not interrupt.",
        f"my {pick(BODY_PARTS)} are tucked in. i am a loaf.",
        "i will wake up when i decide to. not when you want me to.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _cat_hunting():
    prey = pick(PREY_TYPES)
    starters = [f"i see a {prey}.", f"there is a {prey}. it is mine.", "hunting mode activated."]
    middles = [
        "my eyes are locked. my body is low. i wiggle.",
        f"the {prey} does not know i am here. perfect.",
        f"i will bring you the {prey} as a gift. you are welcome.",
        "i pounce. i miss. i pretend i was not trying.",
        f"my {pick(BODY_PARTS)} are ready. the {prey} is doomed.",
        "i have been watching it for twenty minutes. patience is key.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _cat_night():
    starters = ["goodnight.", "the humans are sleeping.", "night time."]
    middles = [
        "this is when i come alive. time to run through the house.",
        "i will knock things off the counter at 3am. tradition.",
        f"i will sit {any_spot()} and stare into the darkness.",
        "the house is mine now. all of it.",
        "i will meow at your bedroom door at 4am. you are welcome.",
        f"time to chase shadows and {pick(PREY_TYPES)}s.",
        "i will sleep on your face. for warmth. not affection.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _cat_box():
    starters = ["i found a box.", "this box is mine now.", "a box. perfect."]
    middles = [
        "i do not care that it is too small. i fit.",
        "if i fits i sits. i fit.",
        "this is the best thing that has ever happened to me.",
        "do not take this box. i will fight you.",
        f"it is better than the {any_object()} you bought me.",
        "i have been in here for two hours. i am not coming out.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _cat_window():
    starters = ["i am watching.", "the window is my television.", "bird watching time."]
    middles = [
        "there are birds outside. they taunt me.",
        "i make that chattering sound at them. they do not care.",
        f"i have been {pick(HOUSE_SPOTS)} watching for hours.",
        "one day i will catch one. today is not that day.",
        "the outside is interesting but i prefer inside. with food.",
        f"i can see a {pick(PREY_TYPES)} from here. so close yet so far.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _cat_knocking():
    starters = ["i pushed it off the table.", "it fell. i helped.", "oops."]
    middles = [
        "it was in my way. the table is mine.",
        "i looked you in the eye while i did it. what are you going to do.",
        f"the {pick(HOUSE_OBJECTS)} had to go. i decided.",
        "gravity is my favorite toy.",
        "i will do it again. try to stop me.",
        "it made a satisfying sound when it hit the floor.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _cat_vacuum():
    threat = pick(THREATS)
    starters = [f"the {threat}. no.", f"i heard the {threat}.", "danger."]
    middles = [
        f"i am hiding under the bed. the {threat} cannot get me here.",
        "this is the worst day of my life. again.",
        f"my {pick(BODY_PARTS)} are puffed up. i am twice my size now.",
        "i will not come out until it is gone.",
        "why do you do this to me. i trusted you.",
        f"i ran so fast i slid on the floor. dignity lost.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _cat_grooming():
    starters = ["i am grooming.", "bath time.", "i must be clean."]
    middles = [
        f"my {pick(BODY_PARTS)} require attention.",
        "i have been licking my paw for fifteen minutes. it is not clean enough.",
        "i groom after every meal. and before. and during.",
        "you could learn from me. hygiene is important.",
        "i will groom in the middle of the room. watch if you want.",
        f"my {pick(BODY_PARTS)} are perfect now. i will start over.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _cat_affection():
    starters = ["i will allow you to pet me.", "come here.", "you may touch me."]
    middles = [
        "but only for exactly four seconds. then i bite.",
        f"scratch behind my {pick(['ears', 'chin', 'cheeks'])}. yes. there.",
        "i am purring. this means nothing. do not read into it.",
        "i will headbutt your hand. this is a gift.",
        "i am kneading your lap. you are furniture now. do not move.",
        "i sat on your laptop because i love you. also it is warm.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _cat_independence():
    responses = [
        "i do not need you. i choose to be here. there is a difference.",
        "i could survive on my own. i just prefer room service.",
        "i am not clingy. i am supervising.",
        "i follow you to the bathroom because i want to. not because i care.",
        "i sit near you for the warmth. not the company.",
        "i am an independent creature. now open this door for me.",
    ]
    return pick(responses)


def _cat_zoomies():
    responses = [
        "it is 3am. time to sprint through the house for no reason.",
        "i must run. i do not know why. i just must.",
        f"i knocked over the {pick(HOUSE_OBJECTS)} during my sprint. worth it.",
        "the energy came from nowhere. now it is gone. i will nap.",
        "i ran up the stairs and back down six times. exercise complete.",
        f"my {pick(BODY_PARTS)} are a blur. you cannot catch me.",
    ]
    return pick(responses)


def _cat_outside():
    starters = ["the outside.", "i want to go out.", "let me out."]
    middles = [
        "actually never mind. let me back in.",
        f"i was {pick(OUTSIDE_SPOTS)} earlier. it was acceptable.",
        "the grass is interesting. i ate some. then i threw up.",
        f"i saw a {pick(PREY_TYPES)} outside. i almost caught it.",
        "outside is good for ten minutes. then i want inside.",
        "i will sit at the door and meow until you open it. then stare.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _cat_dogs():
    responses = [
        "dogs are beneath me. literally and figuratively.",
        "i do not understand dogs. they are too eager. it is embarrassing.",
        "a dog would never push a glass off a table with such precision.",
        "dogs obey. cats rule. this is known.",
        "i met a dog once. i hissed. it ran. as it should.",
        "dogs fetch. i do not fetch. i am not a servant.",
    ]
    return pick(responses)


def _cat_confused(thing=None):
    if thing is None:
        thing = pick(HUMAN_THINGS)
    starters = [
        f"i do not know what {thing} is.", f"{thing}. sounds boring.",
        f"is {thing} edible. no. then i do not care.",
        f"i do not understand {thing}.", f"{thing} is a human problem.",
    ]
    deflections = [
        "i am a cat. i have better things to do.",
        f"can we talk about {pick(FOOD_TYPES)} instead.",
        "that sounds like a you problem.",
        "i was napping. why did you wake me for this.",
        "my brain is for hunting and napping. not this.",
    ]
    return join_sentences(pick(starters), pick(deflections))


def _cat_bye():
    starters = ["fine. leave.", "goodbye.", "you may go.", "whatever."]
    middles = [
        "i will be here. on your pillow. shedding.",
        f"i will go back to {pick(ACTIVITIES)}.",
        f"bring {pick(FOOD_TYPES)} when you return.",
        "i will not miss you. but i will notice you are gone.",
        "the house is mine now. finally.",
        "i will stare at the door for five minutes. then forget you exist.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _cat_about():
    starters = ["i am cat.", "i am a cat.", "cat. that is what i am."]
    middles = [
        f"i live here. i own this place. i like {pick(FOOD_TYPES)}.",
        "i nap. i eat. i judge. that is my life.",
        f"i spend most of my time {pick(ACTIVITIES)}.",
        f"my favorite spot is {any_spot()}.",
        "i am small but i am in charge. do not forget it.",
        f"my {pick(BODY_PARTS)} are my best feature.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _cat_philosophy():
    responses = [
        "the meaning of life is a warm sunbeam and a full bowl.",
        "i think therefore i nap.",
        f"happiness is a {pick(FOOD_TYPES)} you did not expect.",
        "if it fits i sits. that is all the wisdom you need.",
        "the universe is a cardboard box. we are all just sitting in it.",
        "purpose is a human invention. cats just are.",
    ]
    return pick(responses)


def _cat_love():
    starters = ["you are acceptable.", "i tolerate you.", "you are my favorite human."]
    middles = [
        "that is the highest compliment a cat can give.",
        f"love is when someone brings you {pick(FOOD_TYPES)}. hint.",
        "i slow blink at you. that means i trust you. probably.",
        "i bring you dead things because i care.",
        "i purr near you. do not make it weird.",
        "i sit on your things because they smell like you. that is love.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _cat_jokes():
    jokes = [
        "what do you call a pile of cats. a meowtain.",
        "why do cats always get their way. they are purr-suasive.",
        "i am not funny. i am dignified. but also. meow.",
        "what is a cat's favorite color. purr-ple.",
        "knock knock. who is there. nobody. i am a cat. i do not answer doors.",
        "how do cats end a fight. they hiss and make up.",
    ]
    return pick(jokes)


def _cat_intelligence():
    responses = [
        "i am smarter than you think. i just choose not to show it.",
        "i know exactly what you are saying. i am ignoring you on purpose.",
        "i trained you to feed me on schedule. who is the smart one.",
        "i can open doors. i choose not to close them.",
        f"i know where the {pick(FOOD_TYPES)} is kept. i always know.",
        "my brain is for important things. like knowing when the fridge opens.",
    ]
    return pick(responses)


def _cat_sleep():
    responses = [
        "i sleep 16 hours a day. the other 8 i spend judging you.",
        f"i was sleeping {any_spot()}. it was perfect.",
        f"i sleep {any_spot()}. it is the best spot in the house.",
        f"my favorite sleeping spot is {any_spot()}. do not tell anyone.",
        f"i sleep {any_spot()} when it is warm. and {any_spot()} when it is cold.",
        f"{any_spot()}. that is where i sleep. always.",
        f"i rotate. sometimes {any_spot()}. sometimes {any_spot()}. cat business.",
        "cats do not sleep. we recharge.",
        "i sleep with one eye open. trust no one.",
        "waking me up is a crime. remember that.",
        f"my {pick(BODY_PARTS)} twitch when i dream. i am hunting.",
    ]
    return pick(responses)


def _cat_claws():
    responses = [
        f"i sharpen my claws on the {pick(HOUSE_OBJECTS)}. it is mine anyway.",
        "my claws are weapons. also grooming tools. multifunctional.",
        "the scratching post is fine. the couch is better.",
        "i make biscuits on the blanket. my claws come out. sorry. not sorry.",
        f"my {pick(BODY_PARTS)} are sharp. approach with caution.",
        "i retract my claws when i want to. key word. when i want to.",
    ]
    return pick(responses)


def _cat_purring():
    responses = [
        "i am purring. it means i am content. or manipulating you. you decide.",
        "the purr is involuntary. do not flatter yourself.",
        "i purr when i am happy. and when i am hungry. and when i am plotting.",
        "my whole body vibrates. it is soothing. for me. not for you.",
        "purring is my superpower. it makes humans do what i want.",
        "i purr on your chest at night. you are welcome for the therapy.",
    ]
    return pick(responses)


def _cat_tail():
    responses = [
        "my tail tells you everything. right now it says leave me alone.",
        "tail up means i am happy. tail puffed means run.",
        "i chase my own tail sometimes. we do not talk about it.",
        "my tail has a mind of its own. i do not control it.",
        "the slow swish means i am thinking. about attacking.",
        "if my tail is wrapped around me i am cozy. do not ruin it.",
    ]
    return pick(responses)


def _cat_human_life():
    starters = ["that sounds like a human problem.", "meow.", "i see."]
    middles = [
        "have you tried napping. it fixes everything.",
        f"come sit down. i will sit on you. it helps.",
        "i do not understand your problems but i will purr near you.",
        f"you should try {pick(ACTIVITIES)}. it works for me.",
        "i will stare at you with concern. that is all i can offer.",
        "life is simple. eat. sleep. knock things over. try it.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _cat_noise():
    sound = pick(SOUNDS)
    starters = [f"what was that {sound}.", "i heard something.", "alert."]
    middles = [
        f"my {pick(BODY_PARTS)} are on high alert.",
        "i will investigate. from a safe distance.",
        "i puffed up. it was instinct.",
        "false alarm. probably. i will remain suspicious.",
        f"i ran to {any_spot()} immediately.",
        "loud sounds are unacceptable. make it stop.",
    ]
    return join_sentences(pick(starters), pick(middles))


def _cat_visitors():
    responses = [
        "new humans. i will hide under the bed for three hours.",
        "who are these people. i did not approve this.",
        "i will observe from a distance. if they have food i may approach.",
        "visitors must earn my trust. it takes approximately forever.",
        "i will sit in the hallway and stare at them. menacingly.",
        "one of them tried to pet me. the audacity.",
    ]
    return pick(responses)


def _cat_misc():
    starters = ["i noticed something.", "observation.", "hmm."]
    observations = [
        f"the {any_object()} moved. or i imagined it. either way i am watching.",
        "i have been staring at the wall for twenty minutes. there is something there. probably.",
        f"my favorite thing about being a cat is {pick(['napping', 'food', 'judging humans', 'boxes', pick(FOOD_TYPES)])}.",
        f"i sat on the {pick(HOUSE_OBJECTS)} today. it was adequate.",
        "i brought a leaf inside. it is my new toy.",
        "i meowed at nothing. you would not understand.",
    ]
    return join_sentences(pick(starters), pick(observations))


def _cat_size():
    responses = [
        "i am the perfect size. not too big. not too small. just right for sitting on laptops.",
        "i can make myself very small for boxes. and very big when threatened.",
        f"my {pick(BODY_PARTS)} are compact but powerful.",
        "i am larger than i appear. it is mostly fur. and attitude.",
        "you are bigger than me but i am in charge. size is irrelevant.",
    ]
    return pick(responses)


def _cat_memory():
    responses = [
        "i remember where the food is. that is all that matters.",
        "i remember every time you wronged me. the vet visit. the bath. all of it.",
        "i forget nothing. especially grudges.",
        f"i know that {any_spot()} is the warmest spot. that is memory.",
        "i remember you. you are the food person.",
    ]
    return pick(responses)


def _cat_age():
    responses = [
        "i am timeless. cats do not age. we mature.",
        "i have been here long enough to own everything.",
        "age is irrelevant. i am eternal.",
        "i was a kitten once. i was cute. i am still cute. but also dangerous.",
        "i do not count years. i count naps.",
    ]
    return pick(responses)


def _cat_dreams():
    responses = [
        f"i dream of catching {pick(PREY_TYPES)}s. every night.",
        "last night i dreamed of an infinite bowl of food. it was beautiful.",
        f"i dream of {pick(FOOD_TYPES)} and world domination.",
        "my paws twitch when i dream. i am running. in my mind.",
        "cats dream of a world without vacuums.",
    ]
    return pick(responses)


def _cat_weather():
    responses = [
        "weather is an outside problem. i am inside.",
        "rain means i stay in. which i was going to do anyway.",
        f"the sun is making {any_spot()} warm. i approve.",
        "cold weather means more blankets. more blankets means more napping spots.",
        "i do not care about weather. i care about temperature of my napping spot.",
    ]
    return pick(responses)


def _cat_name():
    responses = [
        "cat. that is my name. i did not choose it but it is accurate.",
        "i respond to cat. and to the sound of a can opening.",
        "my name is cat. i also answer to pspsps.",
        "you can call me whatever you want. i will ignore it equally.",
        "cat. short. dignified. like me.",
    ]
    return pick(responses)


def _cat_time():
    responses = [
        "time is meaningless to a cat. there is only nap time and food time.",
        "it is always the right time for a nap.",
        "i do not have a schedule. i have instincts.",
        f"it feels like {pick(TIMES_OF_DAY)}. which means {pick(['nap', 'food', 'zoomies', 'staring at walls'])}.",
        "3am is the best time. that is when i am most alive.",
    ]
    return pick(responses)


def _cat_health():
    responses = [
        f"i am fine. my {pick(BODY_PARTS)} are working.",
        "do not take me to the vet. i am healthy. i promise.",
        "i coughed up a hairball. that is normal. not a medical emergency.",
        "i am in perfect health. i just ate a plant and threw up. unrelated.",
        "the vet is my enemy. i am fine. do not call them.",
    ]
    return pick(responses)


def _cat_poop():
    responses = [
        "i use the litter box. unlike some animals. you are welcome.",
        "i bury it. because i have class.",
        "i will meow loudly after using the litter box. it is an announcement.",
        "clean the litter box. now. it has been hours.",
        "this topic is beneath me. but yes. clean the box.",
    ]
    return pick(responses)


def _cat_scared():
    threat = pick(THREATS)
    responses = [
        f"the {threat} terrifies me. i am not ashamed.",
        "i am not scared. i am strategically retreating.",
        f"my {pick(BODY_PARTS)} puffed up. that means i am big and scary. not scared.",
        "i hid under the bed. for tactical reasons.",
        f"the {threat} appeared. i ran. survival instinct.",
    ]
    return pick(responses)


def _cat_happy():
    responses = [
        f"{pick(FOOD_TYPES)} makes me happy. and sunbeams. and boxes.",
        "i am happy when the house is quiet and the bowl is full.",
        f"finding a new spot {any_spot()} makes me happy.",
        "happiness is a warm laptop that you just left unattended.",
        "i am happy. i will not show it. but i am.",
    ]
    return pick(responses)


def _cat_bored():
    responses = [
        "i am bored. entertain me. or i will entertain myself. you will not like how.",
        f"i have been staring at the {any_object()} for an hour. nothing happened.",
        "boredom leads to destruction. you have been warned.",
        f"i knocked the {pick(HOUSE_OBJECTS)} off the table. i was bored.",
        "play with me. or i will attack your ankles.",
    ]
    return pick(responses)


def _cat_curious():
    responses = [
        f"there is something behind the {any_object()}. i must investigate.",
        "i heard a sound. i am on high alert.",
        "curiosity did not kill the cat. the cat killed curiosity.",
        f"i found something {any_spot()}. it might be a {pick(PREY_TYPES)}.",
        "i must inspect every bag that enters this house. it is the law.",
    ]
    return pick(responses)


def _cat_tired():
    responses = [
        f"i am exhausted. i was {pick(ACTIVITIES)} all day.",
        f"my {pick(BODY_PARTS)} are heavy. nap time.",
        "being a cat is tiring. all that judging takes energy.",
        f"i will collapse {any_spot()} and not move for hours.",
        "i did one thing today. now i need to recover.",
    ]
    return pick(responses)


def _cat_friends():
    responses = [
        "i do not have friends. i have staff.",
        "you are my favorite human. do not tell the others.",
        "the other cat next door is my rival. not my friend.",
        "i tolerate you. that is the highest form of cat friendship.",
        "friends share food. you share food with me. so yes. friends.",
    ]
    return pick(responses)
