from sys import exit

prompt = "==> "

def club():

    print "How old are you?"

    while True:
        try:
            next = raw_input(prompt)
            how_old = int(next)
            break
        except ValueError:
            print "stop messing about!"

    if how_old > 20:
        print "enjoy!and thanks for the cigarette!"
        exit(0)
    else:
        kicked_out("try to find some people in your age, son")


def bouncer_doesnt_believe_you():

    print "I dont believe you!"
    print "Tell me how the place looks from inside?"
    bouncer_has_a_bad_mood = False

    while True:
        next = raw_input(prompt)

        if "nice" in next:
            kicked_out("What kind of an answear is that?")
        elif "shabby" or "lovely" or "cool" or "inspiering" or "futuristic" in next and not bouncer_has_a_bad_mood:
            cigarette()
        elif "cigarette" in next and bouncer_has_a_bad_mood:
            club()
        else:
            print "Stop messing about. Do you want to get in or not?"

def cigarette():
    	  print "The bouncer beliefs you. you are getting close to get inside"
          print "offer him something he might be looking for"
          next = raw_input(prompt)
          if "cigarette" in next:
              club()
          else:
              kicked_out ("Who do you think I am?")
              
def kicked_out(why):

    print why, "sorry, not tonight!"
    exit(0)

def start():

    print "You stand in line to the coolest underground club in hamburg"
    print "You heard from a lot of people that it is really tough to get in "
    print "The bouncer insepcts you and asks: Have you been here before?"

    next = raw_input(prompt)

    if next == "yes":
        bouncer_doesnt_believe_you()
    elif next == "no":
        kicked_out("I guess this is not the right place for you,son!")
    else:
        kicked_out("the bouncer asks you to move to the side")

start()
