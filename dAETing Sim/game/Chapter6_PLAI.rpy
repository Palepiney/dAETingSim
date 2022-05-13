label chapter06_plai:
# Projection and lighting path.

    $ points = 0

    # september
    scene september with fade
    pause 4.0

    scene foundry entrance with fade

    "The first September of your college career is almost over, and Champ texted
    you last night about meeting up in DFA to go over some of the finer details
    of your projection ideas for your ADW project."

    "You bought those programmable LED strips from that TikTok trend last year,
    and Champ owns a mini projector. Between the two of you, your final project
    is promises to be really progressive and immersive!"

    show champ nuetral with dissolve
    c"Heyo! How are you?"

    "Champ is already working when you walked up to meet him. He had what looked
    like an architectural program up on his laptop…"

    c "Oh, this? Have you not heard of Vectorworks before? It’s a professional-level program used by lighting and event designers, as well as a few other building professions."

    c "I still have a few months left on my student license from high school. Check it out!"

    "Elaine told him the kind of tailgate tent she was going to buy for the festival and Champ mocked up a model of it to scale in Vectorworks."

    menu model_react:

        "This looks complicated.":
            c "It's like riding a bike. You get used to it pretty fast."

        "This looks fun.":
            show champ smile
            c "It is! Maybe not perfect or easy, but definitely fun."

    hide champ with dissolve
    "You spent a little under an hour going over the math involved in setting up his projector, how many lumens it was capable of, and the throw distance he would need"

    "It was all very premature, and you could tell he was mostly looking for excuses to toss a couple buzz words around, but he was clearly passionate about his work."

    show champ nuetral with dissolve
    c "What about you? How long have you been interested in event production?"

    menu event_production:

        "Uh…10 minutes..?":
            show champ smile
            c "You know what, I'll take it. If working on this project with me means we have a class together later? Then mission accomplished!"

        "Since highschool!":
            show champ smile
            c "No way! Me too! Awesome!"

        "I can’t say I’m all that excited about it yet, but I still have a lot to learn.":
            c "That's fair. Part of what makes AET so great is the ability to try so many different fields all in one program!"

    hide champ with dissolve
    "You both have a lovely time working in the library and agree to check in later once Faith was done making your content. Champ was so excited about it, you couldn’t help but look forward to working on this again too."

    # October
    scene october with fade
    pause 4.0

    scene foundry entrance with fade

    "It’s October. You know what that means…."

    menu october_vibes6:

        "Spooky time?":
            jump after_october_vibes6

        "Pumpkin spice?":
            jump after_october_vibes6

        "Midterms?":
            jump after_october_vibes6

label after_october_vibes6:

    "Yeah, I guess so, but it also means class registration is just around the corner!"

    menu october_reaction6:

        "Oh...?":
            jump after_october_reaction6

        "Yikes.":
            jump after_october_reaction6

label after_october_reaction6:

    "OH YIKES INDEED."

    "You, justifiably, make your peace with the reality that most of the classes
    you want will not be the ones you get. So is the way of the freshman. {w}However…{w}
    you can start taking AET foundations courses next semester with your intro class out of the way…"

    show todd nuetral at left with dissolve
    show elaine nuetral at halfleft with dissolve
    show champ nuetral at center with dissolve
    show faith nuetral at halfright with dissolve
    show johnny nuetral phone at right with dissolve
    "You and your friends all gather around a table in DFA, laptops out to peruse the class schedule."

    t "What classes are you looking at?"

    c "I’m really excited for Sound and Space for the next semester, but after that I’m gonna take Live Event Engineering as soon as I can!"

    j "Most of these foundations courses have multiple professors. Does that mean different sections have different teachers?"

    c "Nope. I asked my advisor about that. All course sessions have the same professors."

    t "Why have two teachers for the same course?"

    f "To get two specialists in the same classroom. One of the main goals of the
    program is to promote collaboration and build skills that are applicable across
    multiple fields of media."

    f "One of the best ways to do that is by putting multiple, unique professionals
    at the head of a class, so students have better odds of connecting the dots with
    other fields than their own."

    "AET foundations courses are a lot easier than other lower division courses
    to get into, since they are just for AET students. As October came to a close,
    you and all your friends each got your desired foundations courses."

    hide todd nuetral with dissolve
    hide elaine nuetral with dissolve
    hide champ nuetral with dissolve
    hide faith nuetral with dissolve
    hide johnny nuetral with dissolve
    "You feel a lot better now that registration is over, and you know what you’re
    doing next spring. Time to finish this semester strong to get ready for the next one!"

    # november
    scene november with fade
    pause 4.0

    scene foundry entrance with fade

    "Champ tells you it’s time to test the screen in the PLAI Lab now that Elaine has the tailgate tent, and Faith is done drawing the background."

    menu plai_lab:

        "You have no idea where the PLAI Lab is.":
            scene plai lab with fade
            "You spend a few minutes scrambling around before you discover the staircase leading up to the PLAI lab. It's right by the Hatchery, over some workshop and storage space for Bass Concert Hall."

        "You know exactly where the PLAI Lab is.":
            scene plai lab with fade
            "You confidently navigate up to the PLAI lab."

    "Upon entry, you see Champ already tying his projector to one of the beams of the tent, which he has set up in the center of the room."

    "Trellises full of lights hang from the ceiling. MacBooks line the back wall and PCs are set up at desks in front of the whiteboard. There’s one additional desk with a light board on it and a couple adjacent monitors"

    "That’s a lot of buttons…."

    show champ nuetral
    c"Hey! Glad you’re here. What do you think?"

    "The room is mostly dark, with the only lighting coming from the cracks in the window blinds and the lit projector. Champ has managed to perfectly fill the space on the back wall of the tent, brightly displaying the forest scene Faith made in Photoshop."

    "It looks freaking amazing. Champ killed it; it’s insane how talented he is."

    c "Ok, you can turn the lights back on out here if you want. Hog board is already active."

    hide champ with dissolve
    "You sit down at the lighting board. The Hog4 logo took up most of the screen. You were hoping that something else would have been on it to remind you how this thing works. What keys do you press again?"

    menu keys:

        "1 thru full":
            scene plai lights
            "You easily turn the lights on."

        "1 all on":
            show champ frown
            "Champ sees you looking for buttons that don't exist and walks over to turn the spot lights on for you."
            pause 0.1
            scene plai lights

        "How do you use this thing?!":
            show champ frown
            "Champ sees you looking for buttons that don't exist and walks over to turn the spot lights on for you."
            pause 0.1
            scene plai lights

    show champ smile
    c"I love it in here so much. It’s kinda tucked away into its own corner of campus, and there are so many fixtures to work with…"

    "Champ waxes poetic about lighting design for a little while while you test the LEDs you brought from home. He managed to get some work on a few events around town with some AET upperclassmen. There aren’t many PLAI students as focused as he is, so when special events roll around he’s already one of the first names that comes to mind."

    "It makes you wonder…"

    menu ask_champ:

        "Don’t you ever get tired?":
            show champ nuetral
            c "Yeah sometimes."
            c "It's hard work, and sometimes it's tedious work, but programming lights or designing stage projection is special to me."
            c "It's immersive and adaptive. And, most importantly, I'm patient enough to pour into something that isn't immediately rewarding. It's just kind of perfect for the creator I want to be. So I guess I don't mind the difficulty as much."

        "Do you ever get bored?":
            show champ nuetral
            c "Yeah sometimes."
            c "It's hard work, and sometimes it's tedious work, but programming lights or designing stage projection is special to me."
            c "It's immersive and adaptive. And, most importantly, I'm patient enough to pour into something that isn't immediately rewarding. It's just kind of perfect for the creator I want to be. So I guess I don't mind the difficulty as much."

        "How did you know this was what you wanted to do?":
            show champ nuetral
            c "Yeah, I guess I am pretty confident."
            c "It's hard work, and sometimes it's tedious work,  but programming lights or designing stage projection is special to me."
            c "It's immersive and adaptive. And, most importantly, I'm patient enough to pour into something that isn't immediately rewarding. It's just kind of perfect for the creator I want to be."

    hide champ with dissolve
    "Even when you both wrap up your work for the night, Champ wants to stay and fiddle with the Hog board for a little while. Considering how passionate he and your friends are now, you can’t wait to see what the rest of your time in AET holds."

    $ points = 0
    jump chapter07_dec
