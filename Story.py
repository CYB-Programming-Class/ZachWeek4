import random

stories1 = [
    " walked into a bar, and then",
    " was strolling down the beach when",
    " found a peach and then",
    " opened a portal, then",
    " was a very grumpy man. then",
    " had a shiny ferarri when",
    " jumped out of a plane when",
    " was searching for treasure when",
    " had a heart attack when",
    " fantasised that"
]

stories2 = [
    " I was attacked by ",
    " my tummy felt funny after eating ",
    " I found ",
    " I suddenly realised that the world was inside ",
    " I called my parents to ask for ",
    " I wrote a song about ",
    " I dreamed of becoming ",
    " I became ",
    " I was the first human to come into contact with ",
    " I overturned the nefarious dictatorship of "
]

stories3 = [
    "a peanut.",
    "Kim Jong-un.",
    "a server farm.",
    "seven bald men.",
    "deep fried mac'n'cheese.",
    "the president.",
    "the national treasure.",
    "a superb owl.",
    "too many onion rings.",
    "my greatest fear."
]

stories4 = [
    " That is how I died.",
    " That is how I became president.",
    " I was never seen again.",
    " That was my awful no good very bad day.",
    " That was my origin story.",
    " Kids, this story has a lot of lessons to be learned.",
    " Buckle up, every time.",
    " Never again.",
    " This kills the Zach.",
    " The world changed that day..."
]

story1 = "Once I" + stories1[random.randint(0,9)]+ stories2[random.randint(0,9)]+ stories3[random.randint(0,9)]+ stories4[random.randint(0,9)]
story2 = "Once I" + stories1[random.randint(0,9)]+ stories2[random.randint(0,9)]+ stories3[random.randint(0,9)]+ stories4[random.randint(0,9)]
story3 = "Once I" + stories1[random.randint(0,9)]+ stories2[random.randint(0,9)]+ stories3[random.randint(0,9)]+ stories4[random.randint(0,9)]