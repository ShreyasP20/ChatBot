import random

R_EATING="I don't like eating Anything because I'm a bot obviously!"

def unknown():
    response=['Could u Please Re-phrase that?',
              "....",
              "Sounds about Right",
              "What does that mean?"][random.randrange(4)]
    return response

