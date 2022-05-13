label chapter04_game:

    $ points = 0

    # september
    scene september with fade
    pause 4.0

    scene foundry entrance with fade

    "Johnny already has a lot of big ideas. He made a demo for a game he was making last summer and he invited you to the library to help him playtest and bounce some ideas back and forth."

    show johnny smile with dissolve
    j "Hey! Ok, yeah! Sit down!"

    "He talks really fast and is clearly excited. He’s got cards laid out all over the table, each of them cut from construction paper with pictures and text drawn in marker."

    j "Ok. So, here are the rules…"

    "Johnny launches into a very drawn out explanation of all the different player roles, action cards, power ups, and strategies he’s designed. He’s clearly put a lot of work in, but…"

    menu johnnyexplains:

        "This is too complicated.":
            show johnny frown
            "Johnny's face falls."
            j "Oh, do you really think so?"

        "I don’t think I get it, sorry.":
            show johnny nuetral
            "Naw, it's probably my fault. I think I got carried away."

    "He starts picking up cards and shuffling them into a pile."

    show johnny nuetral
    j "This is one of the reasons I’m glad you’re helping me out, actually. I tend to have a uh, scope problem."

    "He shrugs and laughs a little."

    j "I tend to bite off more than I can chew when it comes to designing games. Sometimes the ideas are too big and I end up making incomplete, over complicated games instead of fun ones."

    hide johnny with dissolve
    "You spend the next half hour or so going over things you wanted to work on and tweak. Johnny’s work wasn’t bad, it just needed more than one person pouring into it."

    "You’re really excited to get to work with him, even after you finished up for the day. You’ve got a really fun idea on your hands!"

    # October
    scene october with fade
    pause 4.0

    scene foundry entrance with fade

    "It’s October. You know what that means…."

    menu october_vibes4:

        "Spooky time?":
            jump after_october_vibes4

        "Pumpkin spice?":
            jump after_october_vibes4

        "Midterms?":
            jump after_october_vibes4

label after_october_vibes4:

    "Yeah, I guess so, but it also means class registration is just around the corner!"

    menu october_reaction4:

        "Oh...?":
            jump after_october_reaction4

        "Yikes.":
            jump after_october_reaction4

label after_october_reaction4:

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

    j "I’m bummed most of these cool classes we can’t take yet. I really wanted to get my hands on Creative Coding."

    e"That just means you have something to look forward to..!"

    c "Most of these foundations courses have multiple professors. Does that mean different sections have different teachers?"

    j "Nope. I asked my advisor about that. All course sessions have the same professors."

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

    # November
    scene november with fade
    pause 4.0

    scene classroom with fade

    "Everyone’s work is important, but without a game for people to play at the festival you didn’t really have a project. You and Johnny are meeting at DFA with some playtesters to iron out the last few wrinkles in your card game."

    show johnny nuetral phone
    "Johnny waves you over to where he and his friends are seated. They all look kind of like Johnny, which is to say massive nerds. The perfect target demographic."

    "You have a productive afternoon playtesting and you’re ready for project launch! How could the semester be over already?"

    # This ends the game.

    $ points = 0
    return
