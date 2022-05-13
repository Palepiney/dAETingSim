label chapter05_art:

    $ points = 0

    scene september with fade
    pause 4.0

    scene foundry entrance with fade

    "Faith had already been chatting with Elaine about what kind of background she wanted. It sounds like the bulk of the work you have to do for this semester would be that projected landscape for the back of your event space, with maybe some additional posters if you have time."

    scene computer lab with fade
    "Faith wants to meet you in the DFA to talk about a production schedule, so meet up in DFA you do. She’s sitting at a table with a large sketchbook when you walk up."

    show faith nuetral with dissolve
    f"Hey."

    "You sit down. She tips her sketchbook out of her lap and onto the table. It's filled with doodles of trees and short-hand notes. There are even a couple of spots covered by sticky notes and washi tape."

    f"So I’ve already been getting some ideas down…"

    "She immediately launches into what she’s drawn so far. You knew that the plan is to digitally paint a forest, but you weren’t expecting to see a forest so early in the design process. Faith is clearly well-practiced."

    menu art_react:

        "I can’t draw like this, what else can I do?":
            "Faith stares at you."
            f "What do you mean 'what else'? You're gonna help me paint all this."

        "You’re really good!":
            show faith smile
            "Faith shows the ghost of a smile."
            f "Thanks. Don't expect me to cover all the work though, you have to create some of this stuff too."

    show faith nuetral
    f"I’m really excited to see what your drawing style is, even if it looks a little different than mine. Would you rather 3D model some stuff? Or maybe work on sketches and layout?"

    "As you get into the bulk of your work schedule, you think back to applying to AET. You didn’t have to have a portfolio for the program, and you’re confident enough in your abilities to chase your career dreams, but now that you’re here…"

    "Also, you don’t get to take any AET coursework until you finish the intro class. You can try learning different photoshop tricks over the internet, but will that be enough for a semester-long project like this?"

    "You decide to ask Faith."

    menu faith_question:

        "Are you worried about the technical part of this project?":
            "Faith shrugs."
            f "I've dabbled in GIMP before, but I'm sure I can figure it out by the time the semester is over."

        "Are you worried about the fine arts part of this project?":
            "I mean, I've been drawing all my life, so not really, but I can appreciate where you're coming from."

    show faith frown
    f"I almost didn’t go to UT because AET is so new and weird. It’s a bachelor of science, so it’s really heavy on teaching students the software side of things depending on what you’re here for. You don’t even need a portfolio to get into the program."

    f"If you’re a game developer, that’s great, because you need to know how to code. Digital artists end up working a little harder to hit that balance between artistic and technical skills, at least in the classroom."

    show faith nuetral
    f"But that’s the cool thing about working with the professors and even the other students in AET; they’re here because they love what they’re doing. You can email professors you don’t have and ask if they have the office hour time to explain stuff to you. Most of them love it when students go out of their way to learn."

    f"I wouldn’t worry about learning what you need to. You’ve got the time, drive, and community around you to make it happen."

    hide faith with dissolve
    "You leave Faith a little while later to make it to your next class. It’s nice that you met someone so encouraging so quickly after you got here."

    # october
    scene october with fade
    pause 4.0

    scene foundry entrance with fade

    "It’s October. You know what that means…."

    menu october_vibes5:

        "Spooky time?":
            jump after_october_vibes5

        "Pumpkin spice?":
            jump after_october_vibes5

        "Midterms?":
            jump after_october_vibes5

label after_october_vibes5:

    "Yeah, I guess so, but it also means class registration is just around the corner!"

    menu october_reaction5:

        "Oh...?":
            jump after_october_reaction5

        "Yikes.":
            jump after_october_reaction5

label after_october_reaction5:

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

    e"Any classes catch your eye, Faith?"

    "It’ll be cool in a semester or two when I have the chance to take Principles of Animation, but for now I’m gonna try and get a spot in Art and Content."

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

    # november
    scene november with fade
    pause 4.0

    scene foundry entrance with fade

    "You and Faith had been hard at work all semester. She ended up doing most of the background work, and you designed the posters. You have just a little work left, but first, you had to return the drawing pad you rented from the library."

    menu dfa:

        "The DFA has technology any student can rent out.":
            "Pretty cool, actually."
            $ points += 3

        "You need special permission to rent out supplies from DFA.":
            "Yeah... wait, really? Do you? That may not be right..."
            $ points += 1

    scene computer lab with fade

    "After returning the drawing pad, you meet faith upstairs in the classroom you had been using together. The MacBooks upstairs and down have complete adobe suites on them. They are perfect for both you and faith, using Illustrator and Photoshop respectively."

    show faith nuetral with dissolve
    "You peer over Faith’s shoulder while you sit down next to her. She has a very detailed scene of a forest at sunset she’s putting the finishing touches on. It looks great! You log in to the MacBook in front of you and pull up your work."

    hide faith with dissolve

    menu macbook:

        "Your student profile saves your work on every computer.":
            "Oh yikes. No, it doesn't. The desktop of this mac is blank. Good thing you brought your flash drive..."
            $ points += 1

        "You need to save your work on your flash drive when working at DFA or you’ll lose it.":
            "Flash drive is love, flash drive is life. You plug yours in and get to work."
            $ points += 2

    "You just need to add some text to your poster explaining your game to people waiting for their turn at the table. What kind of typography to use…"

    menu typography:

        "What the heck is typography?":
            "Typography is the art of designing clear, legible text. If you had known, you might not have chosen papyrus as your font for this project."
            $ points += 1

        "Use a serif font.":
            "It's a little hard to read, but still looks good."
            $ points += 2

        "Use a sanserif font.":
            "The clear, bold font you chose looks great!"
            $ points += 3

    if points > 5:
        "Your poster looks freaking amazing. You did that! You! Well done!"

    else:
        "It… looks ok…? It looks like you just learned how to use Illustrator this semester, which you did. There are worse things in the world."

    scene foundry entrance with fade
    "You and Faith save your work. She emails hers to Champ while you pack your flash drive and prepare to go downstairs and print a few flyers. You say goodbye and end your last workday of the semester. The festival is just around the corner. Time flys…"

    # This ends the game.

    $ points = 0
    return
