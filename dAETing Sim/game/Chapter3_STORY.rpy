label chapter03_story:
# Storytelling path.

    $ points = 0

    # September
    scene september with fade
    pause 4.0

    scene foundry entrance with fade

    "You meet Elaine at the library to discuss a loose production schedule for
    your interactive gaming experience."

    "As creative leads on the project, it’s your job to work together and make
    sure that the team is working in tandem with one another and that all of the
    work meshes cleanly together into one final product."

    show elaine nuetral with dissolve
    e "Hey! Sit down, I’ve got an outline to show you."

    "Elaine has a huge coffee sitting next to her on the table, with notes taking
    up most of the available space."

    menu coffee_react:

        "Nice job being productive!":
            show elaine smile
            e "Thanks! I really appreciate it!"

        "That’s a ton of notes.":
            e "Heh, yeah. I tend to go a little overboard every now and then..."

    hide elaine with dissolve
    "You spend the next few minutes getting into the finer details of your ideal
    production schedule. Besides being co-producers, most of what you’re going to
    be doing will come into play much later in the semester."

    "It looks like you’re going to be constructing the actual booth that you’ll
    be hosting your players in on the night of the event, complete with a projection
    surface along the back wall and hidden speakers."

    "Do we really have time to build this? Or the skills?"

    show elaine nuetral with dissolve
    e "Hey, what’s up? You look pensive."

    menu pensive:

        "Have you ever built anything like this before?":
            show elaine smile
            "Elaine smiles a little wider."

        "Will we have enough time to build this?":
            show elaine smile
            "Elaine smiles a little wider."

    e "No, but that’s the fun part! It doesn’t have to be perfect, and
    we’re gonna cut adapt when we need to."

    e "It’ll be more like a stretch goal. There’s a lab in between this
    building and Bass Concert Hall that AET uses for fabrication projects
    like this all the time, and whatever we can’t learn, we’ll cut."

    e "As long as we’re here though, we might as well try new things, right? It
    would suck to let all of these resources go to waste!"

    menu about_elaine:

        "Didn’t you come to AET to be a games writer?":
            e "I came to AET to be a narrative designer, so this is totally still
            in my wheelhouse. Fabrication makes me better at placemaking."
            e "That's just a fancy word for designing public spaces. Narrative design isn't
            just for games, it's for museums and festivals and even theme parks!"

        "I didn’t realize AET had a fabrication side to it.":
            e "Oh yeah totally! It was one of the things that attracted me to the program."
            e "Most of the hard skills AET advertises are software related, but
            technically fabrication falls under hardware skills. I heard some Game Dev
            kids built an arcade machine together!"
            e "Working with your hands in this degree is totally an option."

    "She looks really passionate about this project. You’re glad her excitement is so infectious."

    # october
    scene october with fade
    pause 4.0

    scene foundry entrance with fade

    hide elaine with dissolve
    "It’s October. You know what that means…."

    menu october_vibes3:

        "Spooky time?":
            jump after_october_vibes3

        "Pumpkin spice?":
            jump after_october_vibes3

        "Midterms?":
            jump after_october_vibes3

label after_october_vibes3:

    "Yeah, I guess so, but it also means class registration is just around the corner!"

    menu october_reaction3:

        "Oh...?":
            jump after_october_reaction3

        "Yikes.":
            jump after_october_reaction3

label after_october_reaction3:

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

    e "It’s a bummer that you can’t take any upper-division classes yet."

    f "Which one were you looking at?"

    e "Intro to Narrative is an upper-division course. There’s another one in here
    called Themed Entertainment Design that also looks so cool..! Guess I have to wait a little longer."

    j "Most of these foundations courses have multiple professors. Does that mean
    different sections have different teachers?"

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

    "The semester is coming to a close."

    "The due date for your final project in AET 101 is almost a month away, and you
    and Elaine were going to meet in the Hatchery to discuss building the booth for
    your project. You decide to use a tailgate tent as your main structure."

    "The bulk of your work for the next couple of weeks is mostly making sure that the
    projection surface at the back of the tent is well secured, and that there are places
    for speakers on the support poles."

    "The Hatchery is technically a part of Bass Concert Hall occupying a space directly
    above some backstage workshops and other tech storage for the theater."

    "You got here by…"

    menu got_here:

        "Asking any AET professor.":
            "Yeah close enough... you think... Should you have done something differently?"
            $ points += 2

        "Asking an AET professor that you knew had a class in the Hatchery.":
            "It was the best way to make sure no one else was using the space while
            also asking permission to utilize lab materials."
            $ points = 3

        "Just showing up when there wasn’t class.":
            "Yeah close enough... you think... Should you have done something differently?"
            $ points = 1

    "Once inside the Hatchery, You notice Elaine already hard at work on something
    on one of the tables. She also has half of your tailgate tent assembled and leaning
    against the wall to test tapes and string lights for final assembly."

    "You’re very impressed with the amount of materials available for AET students
    to use in the space, from cardboard, to paper, to glue guns and soldering irons.
    It really does feel like the sky’s the limit in a workspace like this."

    show elaine smile with dissolve
    "Elaine pauses her music and smiles at you."

    e"Hey, ready to get started?"

    "She is making something out of cardboard. You peer around her to get a better look."

    show elaine nuetral
    e"Oh this? I was making something to hold the speakers that we could probably tape or
    something to the top of our tent! I just had a Fabrications Workshop in here for fun,
    and I thought I'd use the skills I learned to make something unique!"

    "Following Elaine's advice, you had also taken a certification course or two in the library."

    menu cert:

        "You did the whole thing online.":
            "Yeah close enough... you think... Should you have done something differently?"
            $ points += 1

        "You did the whole thing in person.":
            "Yeah close enough... you think... Should you have done something differently?"
            $ points += 2

        "You did half of the certification in person and half online.":
            "You finished the canvas portions and the in-person instruction, so
            now you can proudly use the 3D printer and the embroidery machine!"
            $ points += 3

    e"Ok! Todd has a speaker for us to test with downstairs. I’m gonna go meet him,
    you make a replica speaker box while I’m gone."

    hide elaine with dissolve
    "You grab the hot glue and box cutter she left for you and started working."

    menu cut:

        "Cut in the direction of the flutes.":
            "You sliced through your cardboard like hot butter. Cutting with the
            flutes is so much easier!"
            $ points += 3

        "Cut against the flutes.":
            "Not the easiest thing in the world, but you cut everything alright."
            $ points += 2

        "What the heck is a flute?":
            "A fancy word for the ripples inside cardboard is 'flutes'. Now you
            can say with authority that you ignored the flutes of the cardboard
            and shredded the edges where you cut the board to size."
            "Aren't you smart? :)"
            $ points += 1

    if points > 6:
        show elaine smile with dissolve
        "It looks great! You even took time to strengthen the edges with bamboo
        skewers. You really know your stuff!"

        e"Wow! Yours is better than mine! Are you sure you’ve never been up here before?"

        "She places Todd’s speaker in the cardboard case. It’s a perfect fit! With
        some tape and a little willpower, the box secures firmly to a tent support pole."

        show elaine nuetral
        e"I can’t believe assembly is just in a couple weeks. We’ve done some really good work together. Thanks for helping me out all semester."

    else:

        "It… doesn’t look great."

        "Hot glue is seeping out of a corner of your box because you didn’t line
        up the walls right. Oh well, no one is supposed to see it. Three cheers
        for beginning mastery of a new skill!"

        show elaine frown with dissolve
        "Elaine comes back and smiles weakly upon seeing your work."

        e "I might remake yours, I just don’t want anything expensive to fall, you know?"

        "She places Todd’s speaker in the box she already made to test her design.
        It fit perfectly, and with some tape and a little willpower, the cardboard
        case kept the speaker well-secured to the tent supports."

        show elaine nuetral
        e"I can’t believe assembly is just in a couple weeks. We’ve done some
        really good work together. Thanks for helping me out all semester."


    menu will_like:

        "Do you think people are going to like it?":
            show elaine smile
            e "Yeah, I think so! I mean, we like what the rest of our team is
            doing, right? People are sure to enjoy it"

        "Do you think we’re gonna get a good grade?":
            show elaine smile
            e "We worked really hard on this, I don't see why not. More
            importantly, we learned a lot and we made something people are
            going to enjoy. Why wouldn't that reflect in our grades?"

    hide elaine with dissolve
    "You nod and help Elaine with clean up. All you had left was the freshman
    showcase itself, and your first semester at UT would be in the books. Where has the time gone?"

    $ points = 0
    jump chapter07_dec
