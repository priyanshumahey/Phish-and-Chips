# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define name = Character("[name]")
define pumpkin = Character("Pumpkin")
define meow = Character("Meowricio")
define coco = Character("Coco")
define jerry = Character("Jerry")
define doug = Character("Doug")
define snow = Character("Snow")
define catbot = Character("Catbot")

# just for funny
define e1 = Character("Employer 1")
define e2 = Character("Employer 2")
define e3 = Character("Employer 3")

#points system
default cyberpoints = 0

#character images
image catbot false = "characters/catbot/catbot_false.png"
image catbot n = "characters/catbot/catbot_n.png"
image catbot true = "characters/catbot/catbot_true.png"

image coco h = "characters/coco/coco_h.png"
image coco n = "characters/coco/coco_n.png"
image coco s = "characters/coco/coco_s.png"
image coco t = "characters/coco/coco_t.png"

image doug fake h = "characters/doug/doug_fake_h.png"
image doug fake n = "characters/doug/doug_fake_n.png"
image doug fake o = "characters/doug/doug_fake_o.png"
image doug h = "characters/doug/doug_h.png"
image doug n = "characters/doug/doug_n.png"
image doug o = "characters/doug/doug_o.png"

image jerry n = "characters/jerry/jerry_n.png"
image jerry w = "characters/jerry/jerry_w.png"

image cat1 = "characters/main/cat1.png"
image cat2 = "characters/main/cat2.png"
image cat3 = "characters/main/cat3.png"

image meow = "characters/meow/meow.png"

image pumpkin h= "characters/pumpkin/pumpkin_h.png"
image pumpkin n= "characters/pumpkin/pumpkin_n.png"
image pumpkin o= "characters/pumpkin/pumpkin_o.png"
image pumpkin s= "characters/pumpkin/pumpkin_s.png"

image snow h = "characters/snow/snow_h.png"
image snow n = "characters/snow/snow_n.png"

image bg cubicles = "bg/cubicles.png"

image bg office = "bg/office.png"

image bg outsideoffice = "bg/outsideoffice.png"

image bg home = "bg/home.png"

image bg office2  = "bg/office2.png"

# The game starts here.
label start:
    $ style.say_window = style.window
    $ name = renpy.input("What's your name?", "Catya", length=15)
    $ player_name = name.strip()
    "[name]! I love that!"
    "Pick your character!"
    call screen character_select
    return

screen character_select:
    imagebutton:
        idle "charsel/cat1_idle.png"
        hover "charsel/cat1_hover.png"
        focus_mask True
        action Jump("set_cat1") 
    imagebutton:
        idle "charsel/cat2_idle.png"
        hover "charsel/cat2_hover.png"
        focus_mask True
        action Jump("set_cat2") 
    imagebutton:
        idle "charsel/cat3_idle.png"
        hover "charsel/cat3_hover.png"
        focus_mask True
        action Jump("set_cat3") 

label set_cat1:
    python:
        window_style = style.window_CUSTOM1
    jump after_start
    return

label set_cat2:
    python:
        window_style = style.window_CUSTOM2
    jump after_start
    return

label set_cat3:
    python:
        window_style = style.window_CUSTOM3
    jump after_start
    return


label after_start:
    $ style.say_window = style.window
    show catbot true
    catbot "Hi there! My name is Catbot!"
    
    catbot "I’m the friendly virtual assistant living in your phone. I’ll show up occasionally to help you along the story."
    hide catbot true
    show catbot n
    catbot "Would you like me to explain how this game works?"

    menu:
        "Yes":
            menu:
                "In this game, you make choices like this:"

                "Ok":
                    name "Ok"
                "Woah":
                    name "Woah"
            catbot "These choices will be related to cyber security and digital literacy."
            catbot "Don’t worry if you make “wrong” choices. Every choice you make is a learning opportunity!"
            catbot "And even if you make a “wrong” choice, you can always go back and select a different choice!"
            catbot "In addition to these choices, there will be fun minigames along the way!"
            $ style.say_window = window_style
            name "Cool! I’m ready!"
            $ style.say_window = style.window
            catbot "Let’s start!"
            pass


        "No":
            catbot "Okay! Let’s start meow!"
            pass
    hide catbot n

    $ style.say_window = window_style
    show bg home
    name "Ah, Kitty City. The land of opportunities, fresh fish, and of course…high rent."

    name "My name is [name]. I’m just a small-town cat with big dreams."

    name "I moved here to go to college for a degree in Biology but since graduating, I’ve been having trouble finding a job."

    name "I had a couple of interviews but here’s how most of them went:"
    
    $ style.say_window = style.window
    e1 "Knowing about the Krebs cycle won't help you here…"

    $ style.say_window = window_style
    name "Why not?"

    $ style.say_window = style.window
    e1 "This is a bank..."

    $ style.say_window = window_style
    name "Oh..."

    $ style.say_window = style.window
    e2 "Sorry, but…the position has already been filled."

    $ style.say_window = window_style
    name "Wait…then why am I here?"

    $ style.say_window = style.window    
    e3 "Who are you again?"

    $ style.say_window = window_style
    name "[name]!"

    $ style.say_window = style.window   
    e3 "Oh I think I invited the wrong cat to interview. Sorry haha."

    $ style.say_window = window_style
    name "I guess it doesn’t help that I don’t have much work experience."
    name "But how do I get work experience without getting a job? Ugh."
    name "Oh well. At least my aunt was nice enough to pay me for babysitting her daughter."
    name "Speaking of which…what is she doing on my computer?"
    name "Hey Coco, what are you doing?"

    
    show coco n
    $ style.say_window = style.window
    coco "Yo, [name]. Have you ever heard of Meowcube?"

    $ style.say_window = window_style
    name "Yes. It’s that game where everything is a cube right?"

    $ style.say_window = style.window
    hide coco n
    show coco t
    coco "Well you can also adventure and dress up your character but you’re old so I don’t expect you to understand."
    
    $ style.say_window = window_style
    name "Hey!"

    $ style.say_window = style.window
    hide coco t 
    show coco n
    coco "Anywaaay. Someone messaged me and they told me that if I give them my login information, they can get me 10000 Meowdollars."
    
    $ style.say_window = window_style
    name "Wow…is that a lot?"

    $ style.say_window = style.window
    hide coco t
    show coco h
    coco "Ohohoh! You have no idea! 10000 Meowdollars can get me the limited edition super rare rainbow turbo boosted unicorn pet!"
    hide coco h 
    show coco n
    $ style.say_window = window_style
    name "Wow, Coco…"

    menu:
        "This sounds like a scam!":
            $ style.say_window = window_style
            name "I don’t think you should do it."
            $ style.say_window = style.window
            coco "Huh? Why not?"

            $ style.say_window = window_style
            name "It’s too good to be true, Coco. There’s a good chance that they just want to steal your login info."
            
            $ style.say_window = style.window
            hide coco n
            show coco s
            coco "And I won’t get my Meowdollars?"

            $ style.say_window = window_style
            name "Nope."

            hide coco s 
            show coco n

            $ style.say_window = style.window
            coco "Then what should I do?"

            menu:
                "Ignore it":
                    $ style.say_window = window_style
                    name "You should just ignore them. You should never share your login information with anyone."

                    $ style.say_window = style.window
                    coco "But what if they do it again? I think I should report them. I don’t want them to hack my friends."

                    $ style.say_window = window_style
                    name "That’s a good idea, Coco."

                    $ style.say_window = style.window
                    hide coco n
                    show catbot n
                    catbot "Hi, [name]."

                    catbot "It’s a better idea to report the situation and ignore any links or requests from the scammer."
                    
                    $ style.say_window = window_style
                    name "Got it."
                    hide catbot n


                "Report it and block them":
                    $ style.say_window = window_style
                    name "You should report them, block them, and make sure to not send them any information or click on any links they send you."

                    name "You should never share your login information with anyone."
                    $ style.say_window = style.window
                    coco "Okay…fine. I guess you’re right."
                    hide coco n 
                    show catbot true
                    catbot "That was a good call, [name]! Things that are too good to be true usually are! It is important to not share your login information with anyone-- especially strangers on the internet!"
                    hide catbot true
                    $ cyberpoints += 1


                "Insult them":
                    $ style.say_window = window_style
                    name "Are you kidding me? You should insult them! How dare they scam children!"

                    $ style.say_window = style.window
                    coco "Ohohoh. They have no idea what’s coming for them."
                    hide coco n
                    show catbot n
                    catbot "Hey [name]. It’s a better idea to report the situation and ignore any links or requests from the scammer."
                    hide catbot n 

                    $ style.say_window = window_style
                    name "I see."
                    $ style.say_window = style.window
                    "10 minutes later."
                    show coco s
                    coco "Waaaah!"
                    $ style.say_window = window_style
                    name "Oh no! What’s wrong?"

                    $ style.say_window = style.window
                    coco "They called me names! And! And! They threatened that they would come find me if…if I don’t send them my login info."
                    
                    $ style.say_window = window_style
                    name "Coco…I think you should report them, block them, and do not talk with them any further. You should never share your login information with anyone."
                    $ style.say_window = style.window    
                    coco "Okay…okay…"
                    hide coco s

        "You should totally do it!":
            $ style.say_window = window_style
            name "That’s amazing! You should do it!"

            $ style.say_window = style.window
            hide coco n 
            show coco h
            coco "Right? It’s awesome!"

            "Five minutes later…"
            hide coco h
            show coco s
            coco "Waaaah!"

            $ style.say_window = window_style
            name "What’s wrong?"

            $ style.say_window = style.window
            coco "I lost all my items!"
            $ style.say_window = window_style
            name "Oh no! I think they might have been a scammer! Sorry."

            $ style.say_window = style.window
            coco "What do I doooo?"

            menu:
                "Change your login information":
                    $ style.say_window = window_style
                    name "You should change your password so they can’t login again. If the password is the same as your email’s, change it too."

                    $ style.say_window = style.window
                    coco "*sniffle* Okay."
                    hide coco s 
                    show catbot true

                    catbot "Good choice. If you do end up giving away your login information, make sure to change your password!"

                    $ cyberpoints += 1
                    hide catbot true

                "I don’t know":
                    $ style.say_window = window_style
                    name "I don’t know, Coco. Maybe you can make a new account?"

                    $ style.say_window = style.window
                    coco "I don’t wanna make a new account! I’ll lose all my progress!"

                    $ style.say_window = window_style
                    name "That’s fair…maybe it’s better if you change your password. That way you can save your progress."

                    $ style.say_window = style.window
                    coco "Wow. That’s actually a good idea…I’ll do that."
                    hide coco s

    hide coco n 
    pass
    $ style.say_window = style.window
    "After Coco took care of the Meowcube problem, she went to take a nap."

    "*Ding*"

    "Phone reminder: Rent is due in 14 days."
    $ style.say_window = window_style
    name "Right…rent is due soon. I don’t think babysitting money is going to be enough to cover it."
    name "I hope I hear back from a job soon…I desperately need it."
    name "Ughhh"

    $ style.say_window = style.window
    "Right as I was about to get up…"

    "*Ding*"
    $ style.say_window = window_style
    name "An email?"

    $ style.say_window = style.window
    pumpkin "Dear, [name], we have carefully gone over your application and reviewed your interview."

    pumpkin "We would like you to invite you to work with us at Phish n’ Chips Inc. as an intern."

    pumpkin "Please reply as soon as you are available."

    pumpkin "Best, Pumpkin, CEO of Phish n' Chips"
    $ style.say_window = window_style
    name "Ohmygosh! Ohmygosh! This can’t be happening."
    $ style.say_window = style.window
    "A grin spread across my face. I would have screamed for joy if Coco weren’t sleeping."

    menu:
        "Reply to email":
            "Dear Pumpkin,

            I would love to work for you! When do I start?

            Best,

            [name]"

            pass

    "*Ding*"

    pumpkin "Splendid! Training starts tomorrow at 9am. Please bring your laptop and your enthusiasm.

    Cheers,

    Pumpkin
    CEO"
    $ style.say_window = window_style
    name "Things are finally going my way!"
    $ style.say_window = style.window
    "I cannot wait for tomorrow."

    "I have to tell my best friend."

    # !!! here we would have to add in a phone

    $ style.say_window = window_style
    name "Meowricio!"
    $ style.say_window = style.window
    meow "Oh hey, [name]! What’s up!"

    $ style.say_window = window_style
    name "Guess who is employed?"
    $ style.say_window = style.window
    meow "YESSSS! Give me all the details!"

    $ style.say_window = window_style
    name "It’s at Phish n’ Chips."
    $ style.say_window = style.window
    meow "Phish n' Chips? What do they do?"

    $ style.say_window = window_style
    name "They manufacture computer chips!"
    $ style.say_window = style.window
    meow "Ohhh! Right. I’ve heard of them!"

    meow "When do you start?"
    $ style.say_window = window_style
    name "Tomorrow!"
    $ style.say_window = style.window
    meow "Awesome!! You’ll do great!"
    $ style.say_window = window_style
    name "Thanks, Meowricio :)"
    $ style.say_window = style.window
    meow "fknknal.ca/isthisyou?"

    menu:
        "Click on the link":
            "I click on the link and instantly get logged out of my account."
            $ style.say_window = window_style
            name "What’s going on?!"

            $ style.say_window = style.window
            "After logging back in."

            meow "Hey! Sorry about that! I think I got hacked! You didn’t click the link…did you?"

            mewo "I checked my messages…the link was sent to my other friends as well…"

            $ style.say_window = window_style
            name "Oh no! Oh no!"

            show catbot false
            $ style.say_window = style.window
            catbot "Beware of random links! They could get you hacked or steal your information! You can see where they lead to by hovering over them or using a link scanner."
           
            $ style.say_window = window_style 
            name "What should I do?"
            show catbot n
            menu:
                "Only delete all the links":
                    $ style.say_window = style.window
                    catbot "Close! If you get hacked, change your password immediately and delete all those messages with the links! Let your friends know that you’ve been hacked!"
                    $ style.say_window = window_style
                    name "Thanks! I’ll do that."


                "Panic":
                    $ style.say_window = style.window
                    "I scream."
                    $ style.say_window = window_style
                    name "Oh no! Oh no!"
                    $ style.say_window = style.window
                    catbot "Hey [name]! Let’s take it one step at a time. If you get hacked, change your password immediately and delete all those messages with the links! Let your friends know that you’ve been hacked!"
                    $ style.say_window = window_style
                    name "Thanks! I’ll do that."

                "Change your password & delete the links":
                    $ style.say_window = style.window
                    catbot "That’s right! If you get hacked, change your password immediately and delete all those messages with the links! Let your friends know that you’ve been hacked!"

                    $ style.say_window = window_style
                    name "Thanks! I’ll do that."

                    $ cyberpoints += 1

        "What is this?":
            $ style.say_window = window_style
            name "What’s this link?"
            $ style.say_window = style.window
            meow "Oh noes! DON’T click on it! I think I got hacked."
            $ style.say_window = window_style
            meow "Ahhhh! What should I do?"

            menu:
                "Only delete all the links":
                    $ style.say_window = style.window
                    show catbot false
                    catbot "This answer could be better. If you get hacked, change your password immediately and delete all those messages with the links! Let your friends know that you’ve been hacked!"
                    hide catbot false

                "Change your password & delete the links":
                    $ style.say_window = style.window
                    show catbot true                    
                    catbot "That’s right! If you get hacked, change your password immediately and delete all those messages with the links! Let your friends know that you’ve been hacked!"
                    hide catbot true
                    $ style.say_window = window_style
                    name "Meowricio! You should change your password. Then, delete all those messages and let everyone else know that you got hacked."
                    $ style.say_window = style.window
                    meow "Meow! You’re right! What would I do without you?"

                    $ cyberpoints += 1


    $ style.say_window = style.window
    "Phew. That is settled. Now it is time for bed."
    hide bg home
    "The next day."

    name "Phish n’ Chips…This must be it."

    # scene change
    show bg outsideoffice
    "The scent of coffee and fish wafts through the air."

    "A group of cats sitting at a small rectangular table. There’s only 5 cats here…including me. Is this the entire team?"

    "At the head of the table, I see a fluffy orange cat in a suit and tie. That must be Pumpkin!"

    $ style.say_window = window_style
    name "I guess I should sit down."

    $ style.say_window = style.window
    "I sit down next to a timid-looking cat and a…strange looking cat."
    show pumpkin h
    "The orange cat clasps their paws together and grins when I arrive."

    pumpkin "Hi [name]! So glad that you could make it! I’m Pumpkin."

    "I shake paws with Pumpkin."

    pumpkin "Everyone! Let’s go around and introduce ourselves."
    hide pumpkin h

    "An elegant cat in pearls raises her paw."
    show snow h

    snow "I’m Snow. I’m the Vice President of Phish n’ Chips."

    "I shake paws with Snow."
    hide snow h
    "The nervous cat beside me goes next."

    show jerry n
    jerry "H-hi. I’m J-jerry."

    "I offer my paw to shake but Jerry fist bumps it by mistake.
    "
    $ style.say_window = style.window
    show jerry w
    jerry "O-oh my bad…s-sorry."
    $ style.say_window = window_style
    name "All good…"
    hide jerry w 
    hide jerry n
    
    show snow n
    $ style.say_window = style.window
    snow "You have to say your role too, Jerry."
    hide snow n
    show jerry w
    jerry "I-I’m the supply manager. I also do m-maintenance on the machines."
    hide jerry w
    "The strange looking cat beside you goes next."

    show doug fake h
    doug "I’m Doug. I’m the security manager."
    hide doug fake h
    show doug fake n
    $ style.say_window = window_style
    name "Nice to meet you."

    $ style.say_window = style.window
    "Doug does not shake my paw."
    hide doug fake n
    
    show pumpkin h
    pumpkin "Whoopee! It’s so nice to see a fresh face around here. [name], you will be working mainly with Jerry and Doug for your internship."
    hide pumpkin h 
    
    show snow n
    snow "Here’s a To-Do List to help you get started."

    snow "You can follow me to your office space."
    hide snow n 
    hide bg outsideoffice

    "I follow Snow to a room with 3 cubicles. She points to one nearest to the door."

    show bg office
    show snow n
    snow "Okay, newbie. You can work here. Let me know if you need anything."
    $ style.say_window = window_style
    name "Okay, thanks Snow."
    $ style.say_window = style.window
    "Let’s do our first To-Do…"
    jump minigame_1
    return

label minigame_1:

    # [Set up wifi game]
    hide snow n
    show catbot n 
    $ style.say_window = style.window
    
    catbot "Alright! We need to start off by setting up the WIFI!"

    catbot "Connecting to a good WIFI network is really important to be safe online!"

    catbot "Pick the right WIFI network to use!"
    hide catbot n

    call screen wifi
    jump minigame_2
    return 

screen wifi:
    imagebutton auto "wifi/background_wifi_%s.png":
        focus_mask True
    imagebutton:
        idle "wifi/op1_idle.png"
        hover "wifi/op1_hover.png"
        focus_mask True
        action Jump("choice_1")
    imagebutton:
        idle "wifi/op2_idle.png"
        hover "wifi/op2_hover.png"
        focus_mask True
        action Jump("choice_2")
    imagebutton:
        idle "wifi/op3_idle.png"
        hover "wifi/op3_hover.png"
        focus_mask True
        action Jump("minigame_2")    
    imagebutton:
        idle "wifi/op4_idle.png"
        hover "wifi/op4_hover.png"
        focus_mask True
        action Jump("choice_4")    
    imagebutton:
        idle "wifi/op5_idle.png"
        hover "wifi/op5_hover.png"
        focus_mask True
        action Jump("choice_5")    
    imagebutton:
        idle "wifi/op6_idle.png"
        hover "wifi/op6_hover.png"
        focus_mask True
        action Jump("choice_6")    

label choice_1:
    $ style.say_window = window_style
    name "This is not protected! I shouldn't connect to this one. It's not safe"
    
    jump minigame_1
    return

label choice_2:
    $ style.say_window = window_style
    name "This is a hotspot. I probably shouldn't connect to it..."
    name "Don't want Doug to steal any of my information..."
    jump minigame_1
    return

label choice_4:
    $ style.say_window = window_style
    name "This one might be safe but it's labeled Ethernet which is a little concerning..."
    name "Typically Ethernet isn't connected through WiFi. Let's see if there's a better option."
    jump minigame_1
    return

label choice_5:
    $ style.say_window = window_style
    name "This seems to be a connection to Jerry's tablet. I probably shouldn't connect to this."
    name "I should let Jerry know later his network is visible..."
    jump minigame_1
    return

label choice_6:
    $ style.say_window = window_style
    name "This is not protected! I shouldn't connect to this one. It's not safe"
    jump minigame_1
    return

label minigame_2:
    hide screen wifi
    $ style.say_window = window_style
    name "This is the perfect wifi! It is secure, it is not someone's personal WiFi!"
    name "The name IS a bit silly tho..."
    name "We always have to be careful which wifi we connect to since the wifi network can access a lot of personal information."
    name "This can include which websites we access and what we download"
    name"Now that I have my wifi secured, I can do To-Do number 2!"
    # [Account set-up game]

    jump trans_to_mini_2
    return

label trans_to_mini_2:
    $ style.say_window = window_style
    name "Alright! I should get my password set up for my company account!"
    name "Normally I log in with my hop hop revolution pad! Hmm let me try my normal password"
    python:
        import random
        randomlist = ""

        for i in range(0,4):
            n = str(random.randint(1,4))
            randomlist = randomlist + n
    jump trans_to_mini_2_after
    return

label trans_to_mini_2_after:
    $ style.say_window = window_style
    name "Normally my password is [randomlist]. Let me try that:"
    python:
        p11 = renpy.input("What's the first digit of the password?", length=1)
        p11 = p11.strip()
        while len(p11) != 1:
            p11 = renpy.input("This isn't 1 digit! What's the first digit?", length=1)
            p11 = p11.strip()
        p11_pass = p11 == randomlist[0]

    if p11_pass:
        pass
    elif not p11_pass:
        $ style.say_window = window_style
        name "That's not correct! I should try again"
        jump trans_to_mini_2_after

    python:
        p11 = renpy.input("What are the first two digits of the password?", length=2)
        p11 = p11.strip()
        p12_pass = p11 == randomlist[:2]

    if p12_pass:
        pass
    elif not p12_pass:
        $ style.say_window = window_style
        name "That's not correct! I should try again"
        jump trans_to_mini_2_after

    python:
        p11 = renpy.input("What are the first three digits of the password?", length=3)
        p11 = p11.strip()
        p13_pass = p11 == randomlist[:3]

    if p13_pass:
        pass
    elif not p13_pass:
        $ style.say_window = window_style
        name "That's not correct! I should try again"
        jump trans_to_mini_2_after    

    python:
        p11 = renpy.input("What are the first four digits of the password?", length=4)
        p11 = p11.strip()
        p14_pass = p11 == randomlist

    if p14_pass:
        pass
    elif not p14_pass:
        $ style.say_window = window_style
        name "That's not correct! I should try again"
        jump trans_to_mini_2_after    

    $ style.say_window = window_style
    name "Yes! I remembered!"
    name "Hmmm..."
    name "Maybe it isn't the safest password. The system won't let me use it..."
    name "I need at least 8 characters, an uppercase, lowercase, symbol and a number"
    name "That's kind of hard to remember!"
    jump trans_to_mini_2_after_final
    return

label trans_to_mini_2_after_final:
    python:
        passing = False
    while not passing:
        python:
            import re 
            passw = renpy.input("What is your password?", length=32)
            passw = passw.strip()


            up_p = 0
            low_p = 0
            special_p =0
            num_p = 0
            char_len = 0
            string_check= re.compile("[@_!#$%^&*()<>?/\|}{~:]") 

            for i in range(len(passw)):
                if passw[i].islower():
                    low_p = 1
                if passw[i].isupper():
                    up_p = 1
                if passw[i].isdigit():
                    num_p = 1
                if not string_check.search(passw) == None:
                    special_p = 1     
            
            in_mes = ""
            if len(passw) < 8:
                in_mes = in_mes + "This password is too short! "
            if up_p == 0:
                in_mes = in_mes + "There is no uppercase! "
            if low_p == 0:
                in_mes = in_mes + "There is no lowercase! "
            if special_p == 0:
                in_mes = in_mes + "There is no special character! "
            if num_p == 0:
                in_mes = in_mes + "There is no number! "
            if in_mes == "":
                in_mes = "This password is perfect! Good job!"
                passing = True
            final_mes = in_mes

        $ style.say_window = window_style
        name "[final_mes]"
    jump during_minigame_2
    return

label during_minigame_2:
    python:
        passw2 = renpy.input("Wait what was my password again?", length=32)
        passw2 = passw2.strip()
        x = passw2 == passw
    if not x:
        $ style.say_window = window_style
        name "hmm [passw2] is not correct!"
        $ style.say_window = style.window
        menu:
            name "What should I do?"
            "Try again":
                jump during_minigame_2
            "Remake the password":
                jump trans_to_mini_2
    if x:
        jump after_minigame_2

    return    

label after_minigame_2:
    $ style.say_window = window_style
    name "Nice! I have my new account! Now all I need to do is…"

    $ style.say_window = style.window
    "My laptop screen blacks out."

    $ style.say_window = window_style
    name "Oh no!"

    name "There aren’t any other computers here either. I guess they only manufacture computer chips…"

    name "I could ask Snow."

    menu:
        "Ask Snow for a charger":
            $ style.say_window = style.window
            "I wander out and see Snow writing things down on a clipboard."
            show snow n
            $ style.say_window = window_style
            name "Hi Snow! I was wondering if I could borrow a charger for my laptop!"
            $ style.say_window = style.window
            snow "Oh. Is your laptop out of battery? I don’t carry chargers on me but maybe you can ask Doug. He’s working in the cubicle next to you."
            $ style.say_window = window_style
            name "Sounds good. Thank you."
            $ style.say_window = style.window
            snow "By the way, when you are setting up a password, don’t forget to turn on multi factor authentication."
            $ style.say_window = window_style
            name "Why is that?"
            $ style.say_window = style.window
            snow "It sets up an extra layer of protection. If someone got your login information, the multifactor authentication could stop them from actually accessing your precious data!"
            $ style.say_window = window_style
            name "Got it, thanks."
            hide snow n

            pass

    $ style.say_window = style.window
    show bg cubicles
    "I go back into the office and just as Snow said, Doug is sitting in a cubicle."
    show doug fake n
    "When did he get in here? Anyway, let’s see if he has a charger."

    $ style.say_window = window_style
    name "Hey Doug, do you have an extra charger? My laptop died and I need to…"
    $ style.say_window = style.window
    doug "Check emails, woof? I mean meow…"

    "Doug takes one look at my laptop and shakes his head."

    doug "My laptop’s a different brand from yours."

    $ style.say_window = window_style
    name "Oh no…"

    $ style.say_window = style.window
    doug "But you’re in luck, buddy. I brought a spare laptop that you can borrow."

    $ style.say_window = window_style
    name "Awesome! Thanks!"

    $ style.say_window = style.window
    "Doug points to a dark room."

    doug "I set my laptop up over there woof. I mean meow. Just be careful when you login...there might be some cybersecurity risks in there that you need to take care of first."
    
    $ style.say_window = window_style
    name "What kind of security hazards might there be?"
    $ style.say_window = style.window
    doug "Sometimes, you forgot to logout and that can cause issues."

    doug "People can also track what you do their on their laptops so be super careful which kind of information you go through on other's computers"
    
    $ style.say_window = window_style
    name "Oh you're right! I'll try to be careful what I access with public computers and other people computers."
    hide doug n
    "I turn on the laptop and get to the login screen."

    # [A screen where you login and you cannot proceed unless you click on the “do not remember password” check mark]

    # Catbot (if they don’t check it): Don’t forget to click on the do not remember password button! If Doug has your login saved, he can access your information!
    jump minigame_4
    return

label pre_minigame_4:
    #Init for minigame
    python:
        contin = True
    python:
        emails_done = 0
        outs = 0
        outs_dis = 0
        points = 0
        max_outs = 3 #3 is the max number of outs
        max_points = 10 #Max emails
        real_list = ["emails/real1.png", "emails/real2.png", "emails/real3.png", "emails/real4.png", "emails/real5.png"]
        phish_list = ["emails/phish1.png", "emails/phish2.png", "emails/phish3.png", "emails/phish4.png", "emails/phish5.png"]
        order = [real_list[1], real_list[2], phish_list[0], phish_list[1], real_list[0], phish_list[2],
                real_list[4], phish_list[3], real_list[3], phish_list[4]]
    jump paws_check
    return

label paws_check:
    while contin:
        python:
            curr = order[emails_done]
            emails_done = emails_done + 1
            if emails_done == max_points:
                contin = False
            if outs == max_outs - 1:
                contin = False
        call screen up_down
    if not contin:
        if outs < max_outs:
            "Awesome! I finished all of my emails!"
            jump after_minigame_4
        else:
            "Oh no! I didn't do them properly!"
            "I guess I have to do it again!"
            jump pre_minigame_4
    return 

screen up_down:
    imagebutton:
        idle "emails/paws_down.png"
        hover "emails/paws_down_hover.png"
        focus_mask True
        action Jump("paws_down_lab")
    imagebutton:
        idle "emails/paws_up.png"
        hover "emails/paws_up_hover.png"
        focus_mask True
        action Jump("paws_up_lab")
    imagebutton:
        idle [order[emails_done-1]]
        focus_mask True

label paws_down_lab:
    python:
        if order[emails_done - 1] in phish_list:
            points = points + 1
        elif order[emails_done - 1] in real_list:
            outs = outs + 1
            outs_dis = outs
    "You have clicked paws down. Points: [points]. Outs: [outs_dis]"
    jump paws_check
    return

label paws_up_lab:
    python:
        if order[emails_done - 1] in real_list:
            points = points + 1
        elif order[emails_done - 1] in phish_list:
            outs = outs + 1
            outs_dis = outs
    "You have clicked paws up. Points: [points]. Outs: [outs_dis]"
    jump paws_check
    return

label minigame_4:
    "Alright! Time to check my emails!"

    "Click paws up if it's a good email and I should reply to it!"

    "Click paws down if it's a bad email (phishing or spam) and I should block the sender and delete the email!"

    
    jump pre_minigame_4
    return

label after_minigame_4:
    $ style.say_window = style.window
    show doug fake h
    doug "Hey, [name]. Are you done with your emails?"
    hide doug fake h
    show doug fake n
    $ style.say_window = window_style
    name "Yeah! Thanks for letting me borrow your laptop, Doug!"

    $ style.say_window = style.window
    doug "No problemo. Did you log out?"
    $ style.say_window = window_style
    name "Yep."
    $ style.say_window = style.window
    doug "…Good. I think Jerry might have a task for you."
    $ style.say_window = window_style
    name "What task?"
    $ style.say_window = style.window
    doug "I don’t know. Something about research and files. I’m too busy right now so maybe you can help him out. He’s in the supply room."
    $ style.say_window = window_style
    name "Okay."
    hide bg cubicles
    hide doug fake n
    show bg outsideoffice
    # scene transition
    $ style.say_window = style.window
    show jerry n
    jerry "Oh h-hey, [name]."

    $ style.say_window = window_style
    name "Hey, Jerry. Doug said you needed help?"
    $ style.say_window = style.window
    show jerry w
    jerry "Y-yeah! I am trying to find this really good software b-but it’s out of our company’s budget…"
    hide jerry w
    jerry "I found this site that is offering a free download of it. I-I wanted your opinion on it."

    $ style.say_window = window_style
    name "Jerry…"

    menu:
        "Don’t do it":
            
            $ style.say_window = window_style
            name "Jerry, it’s not worth it. There’s a chance that the files could contain viruses or malicious code."

            show jerry w
            $ style.say_window = style.window
            jerry "W-what type of malicious code?"

            $ style.say_window = window_style
            name "There could be spyware or Trojans!"

            hide jerry w
            show jerry n
            $ style.say_window = style.window
            jerry "Oh I-I’ve heard about Trojans! They can steal data and create backdoors in our computer."

            "My b-brother got his banking information stolen because of some s-shady code that was in the file."

            $ style.say_window = window_style
            name "Yeah…let’s not download that file. We can probably find a free and safe alternative to that paid software."

            $ style.say_window = style.window
            jerry "Y-you’re right!"

            $ cyberpoints += 1

        "Do it":
            $ style.say_window = window_style
            name "Free software is good software. I think you should download it."
            show jerry n
            $ style.say_window = style.window
            jerry "I a-agree."

            "After the file finishes downloading, Jerry’s screen freezes."
            show jerry w
            jerry "O-oh no! What’s happening?"
            hide jerry W

            show catbot false
            catbot "Be careful when downloading files on the internet! Downloaded files might contain viruses or malicious code."
            hide catbot false
            show catbot n 
            catbot "This could mean spyware and Trojans designed to steal data or create backdoors in the computers."
            hide catbot n
            show jerry w
            jerry "I-I should have updated my firewall."
            $ style.say_window = window_style
            name "Sorry, Jerry…"

            $ style.say_window = style.window
            jerry "It’s okay…I’ll just cry…I’ll ask Doug for help…"

            jerry "H-he’s a good cat. Very reliable. Very cat-like."
            hide jerry w
    $ style.say_window = style.window
    show jerry n
    jerry "A-anyway…I-I think it’s home time for you right?"
    $ style.say_window = window_style
    name "Oh yeah, you’re right."
    $ style.say_window = style.window
    jerry "B-bye…"
    hide jerry w 
    hide jerry n
    $ style.say_window = window_style
    name "Bye, Jerry."
    hide bg cubicles
    hide bg outsideoffice
    $ style.say_window = style.window
    "Back at home…"
    show bg home
    $ style.say_window = window_style
    name "I still have some assignments on the To-Do List."
    $ style.say_window = window_style
    name "Looks like I need to do some research on clients."
    jump minigame_5
    return

screen doors:
    imagebutton:
        idle "net/left_close.png"
        hover "net/left_opening.png"        
        focus_mask True
        action Jump("jump after_minigame_5")
    imagebutton:
        focus_mask True
        idle "net/right_close.png"
        hover "net/right_opening.png"
        action Jump("paws_down_lab")

screen doors1:
    imagebutton:
        idle "net/1lc.png"
        hover "net/1lo.png"
        focus_mask True
        action Jump("to_door_2")
    imagebutton:
        idle "net/1rc.png"
        hover "net/1ro.png"
        focus_mask True
        action Jump("try_again_doors")

screen doors2:
    imagebutton:
        idle "net/2lc.png"
        hover "net/2lo.png"
        focus_mask True
        action Jump("try_again_doors")
    imagebutton:
        idle "net/2rc.png"
        hover "net/2ro.png"
        focus_mask True
        action Jump("to_doors_3")

screen doors3:
    imagebutton:
        idle "net/3lc.png"
        hover "net/3lo.png"
        focus_mask True
        action Jump("to_doors_4")
    imagebutton:
        idle "net/3rc.png"
        hover "net/3ro.png"
        focus_mask True
        action Jump("try_again_doors")

screen doors4:
    imagebutton:
        idle "net/4lc.png"
        hover "net/4lo.png"
        focus_mask True
        action Jump("try_again_doors")
    imagebutton:
        idle "net/4rc.png"
        hover "net/4ro.png"
        focus_mask True
        action Jump("to_doors_5")

screen doors5:
    imagebutton:
        idle "net/5lc.png"
        hover "net/5lo.png"
        focus_mask True
        action Jump("after_minigame_5")
    imagebutton:
        idle "net/5rc.png"
        hover "net/5ro.png"
        focus_mask True
        action Jump("try_again_doors")

label minigame_5:
    # [Traversing the web (add in something about secure and insecure networks). A puzzle game where you have to get through all the right doors]
    $ style.say_window = window_style
    name "When I'm on the web, I need to be super careful!"
    name "Let me make sure to only go on sites that are safe to traverse onto."
    $ style.say_window = style.window
    "Click on the door with the safer option below it!"
    call screen doors1
    return

label to_door_2:
    "Good job! We should try to only go on sites with https!"
    "https means the site has an ssl certicate and is more likely to be safe"
    call screen doors2
    return

label to_doors_3:
    "Good job! Some websites have weird numbers in their name to pretend to be sites they're not!"
    call screen doors3
    return

label to_doors_4:
    "Amazing! In the search bar, it'll sometimes tell you if a website is secure or not!"
    call screen doors4
    return

label to_doors_5:
    "Fantastic! Some times you get weird links which do not give you a proper addresses."
    "Try to avoid this if possible."
    call screen doors5
    return

label try_again_doors:
    "That's not correct but nice try! Let's try to find the correct safe websites again!"
    jump minigame_5
    return

label after_minigame_5:
    "Perfect! Some bad sites will add something at the starting to confuse the user."
    $ style.say_window = window_style
    name "Nice. I compiled everything into a zip file. Now I just need to send it over…"
    
    $ style.say_window = style.window
    "*Ding*"

    pumpkin "[name]! How was your first day?"

    $ style.say_window = window_style
    name "It was fun! I learned a lot."
    $ style.say_window = style.window
    pumpkin "I’m glad to hear! Can you send over the research file?"

    $ style.say_window = window_style
    name "Yeah sure! Where should I send it?"
    $ style.say_window = style.window
    pumpkin "You can just send it over text."

    "Hmmm. The file contains confidential information…"

    menu:
        "Send it through text":
            $ style.say_window = style.window
            "Right when I am about to send the file to Pumpkin’s number…"
            show catbot false
            catbot "Woah woah woah! SMS messages are not secured or encrypted! They could be intercepted by hackers! This is dangerous-- especially for sending confidential information!"
            
            $ style.say_window = window_style
            name "Oh no! What should I do instead?"
            $ style.say_window = style.window
            show catbot n
            catbot "You can attach the file to an encrypted email. It’s safer that way."
            $ style.say_window = window_style
            name "Okay! I’ll do that."
            $ style.say_window = style.window
            catbot "Do you have any questions?"

            menu:
                "What does encrypted mean?":
                    $ style.say_window = window_style
                    name "What does encrypted mean?"
                    $ style.say_window = style.window
                    catbot "Encrypted means that the message you send will be unreadable to unwanted eyes! Only authorized cats that have a secret code can read your message."
                    $ style.say_window = window_style
                    name "I see! Thanks, Catbot!"
                    $ style.say_window = style.window
                    catbot "I got you."
                    catbot "Anyway, I’ll leave you to it."

                    "After encrypting the email…"
                    show catbot true
                    catbot "Nice work!"

                "Nope":
                    show catbot n
                    catbot "Okay. I’ll leave you to it."

        "Send it through email":
            $ style.say_window = window_style
            name "I’ll send it through email."

            $ style.say_window = style.window
            pumpkin "Whatever works for you."
            
            show catbot n
            catbot "Don’t forget to encrypt the email! That way, if your email gets intercepted, cats that aren’t supposed to see your files won’t be able to understand them!"
            $ style.say_window = window_style
            name "Gotcha."

            $ style.say_window = style.window
            "After encrypting the email…"
            show catbot true
            catbot "Nice work! Encrypting files-- especially confidential ones, is important."
            hide catbot true
            hide catbot n 
            hide catbot false

        "Suggest encrypting files before sending it via email"      :
            $ style.say_window = window_style
            name "I’ll send it over to your email."
            $ style.say_window = style.window
            pumpkin "Okie dokie."
            "After encrypting the email…"
            show catbot true
            catbot "Nice work! Encrypting files-- especially confidential ones, is important."
            catbot "That way, if your email gets intercepted, cats that aren’t supposed to see your files won’t be able to understand them!"
            hide catbot true
            $ cyberpoints += 1

    pass

    $ style.say_window = style.window
    "Finally…I am done with my tasks."

    "I wonder what tomorrow holds for me."

    "The next day…"
    hide bg home
    show bg outsideoffice
    show pumpkin n
    "Pumpkin is pacing around the office."

    "They seemed worried."

    $ style.say_window = window_style
    name "Pumpkin? What happened?"

    $ style.say_window = style.window
    "They stop and walk over to face me."
    
    pumpkin "[name]. I’m sorry but…there was a data breach. A lot of our information got exposed."
    show pumpkin s
    pumpkin "Our investors are mad, [name]. Our customers are mad. Our stock prices are crashing!"
    
    show pumpkin n
    "They shake their head."

    pumpkin "Unfortunately, we have to let you go."

    "I am dumbfounded. I’ve only worked one day."

    $ style.say_window = window_style
    name "How are you going to respond to the breach?"
    
    $ style.say_window = style.window
    pumpkin "Doug…is working on containing it. He’s assessing the risks…and letting the relevant cats know what has happened."

    pumpkin "If we didn’t have to shut down…he’d also make sure it wouldn’t happen again…"
    show pumpkin s
    pumpkin "Waaah! This has never happened before!"

    "Pumpkin sobs and blows his nose into a tiny handkerchief."

    pumpkin "Anyway…you should pack up…"

    $ style.say_window = window_style
    name "Yeah…I guess so…"
    
    name "Aw man... I was really excited for this job too..."
    hide pumpkin n 
    hide pumpkin s 
    $ style.say_window = window_style
    show bg office2
    name "Alright time to clean up! I have to clean the proper areas!"

    $ style.say_window = style.window
    "Typically when you're finished with work you should keep the work area clean"

    "You should also try to keep computers clean! Especially ones with secure information on them"

    "To get rid of any documents, they need to be shred and on anything private on the computer, they need to be securely deleted"
    $ style.say_window = window_style
    name "I need to make sure my harddrive is properly cleared of any private information"

    $ style.say_window = style.window
    "Press the right keys on areas we think might be dirty to clean!"
    jump minigame_6
    return

label minigame_6:
    #init
    $cont_minigame = 0
    $cont = 0
    $arr_keys = ["c", "e", "K_UP", "K_SPACE", "K_DOWN"]
    $wins = 0
    $loses = 0
    $max_win = 15 

    while not wins + loses == max_win:
        call qte_setup(0.99, 0.99, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup
        python:
            if cont == 1:
                wins = wins +1
            elif cont == 0:
                loses = loses + 1

    if loses > 3:
        $ style.say_window = style.window
        "Oh no! We didn't clean up well enough! This place is still is a mess! Let's try again"
        jump minigame_6
    elif wins > 10:
        $ style.say_window = style.window
        "Perfect! This place is more clean now!"
        "Hmmm... "
        "There's still a bit of a mess left. I should try to clean some harder to reach places now."
        jump minigame_6_2
    return

label minigame_6_2:
    #init
    $cont_minigame = 0
    $cont = 0
    $arr_keys = ["c", "e", "K_UP", "K_SPACE", "K_DOWN"]
    $wins = 0
    $loses = 0
    $max_win = 10 

    while not wins + loses == max_win:
        call qte_setup(0.65, 0.65, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup_1
        python:
            if cont == 1:
                wins = wins +1
            elif cont == 0:
                loses = loses + 1

    if loses > 2:
        $ style.say_window = style.window
        "Oh no! We didn't clean up well enough! This place is still is a mess! Let's try again"
        jump minigame_6_2
    if wins > 7:
        $ style.say_window = style.window
        "Perfect! This place is more clean now!"
        "Hmmm... "
        "I should go check up on Pumpkin"
        jump after_minigame_6
    return


label qte_setup(time_start, time_max, interval, trigger_key, x_align, y_align):
    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align

    call screen qte_keyboard

    $ cont = _return

    return

screen qte_keyboard:

    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_keyboard')])
    key trigger_key action (Return(1))

    vbox:
        xalign x_align
        yalign y_align
        spacing 25

        text trigger_key:
            xalign 0.5
            color "#fff"
            size 36

        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"


label after_minigame_6:
    $ style.say_window = window_style
    show outsideoffice
    show pumpkin s
    name "Hey, Pumpkin…are you going to be alright?"
    $ style.say_window = style.window
    pumpkin "Yeah…sorry your internship had to end so suddenly…"
    show pumpkin n
    
    if cyberpoints == 4:
        jump good

    else:
        jump bad

    label good:
        $ style.say_window = style.window
        show pumpkin h
        pumpkin "But! Don’t worry."

        "Pumpkin hands me a business card."

        pumpkin "I’ve sent you a referral to this fishing company. I think they’d be happy to hire you."
        show pumpkin n
        $ style.say_window = window_style
        name "Thanks! And uh…sorry."

        $ style.say_window = style.window
        pumpkin "No…it’s okay. We’ll figure it out."

        pumpkin "Bye now."
        hide pumpkin h 
        hide pumpkin s 
        hide pumpkin n

        "A few days later…"

        "Kitty City. The land of opportunities, fresh fish, and rent that I can afford."

        "I learned a lot that day at Phish n’ Chips."

        "There are some bad cats out there! As long as the internet exists, there are going to be risks."

        "But by learning how to reduce those risks…"

        "By being cyber smart…"

        "I feel more ready to navigate my new job and the internet!"

        "Congratulations! You got the good ending!"

        "Feel free to play again to see how other choices impact the story!"

        # can insert fishing game here

        return

    label bad:
        show bg home
        "At home."
        $ style.say_window = window_style
        name "Ughh. What do I do now?"

        "Kitty City. The land of opportunities, fresh fish, and rent that I can’t afford."

        $ style.say_window = window_style
        name "I think I’ll have to work on my digital literacy skills…"

        $ style.say_window = style.window
        "Meow! You got the bad ending!"

        "That’s okay!"

        "Feel free to play again to see how other choices impact the story!"

        return

    return