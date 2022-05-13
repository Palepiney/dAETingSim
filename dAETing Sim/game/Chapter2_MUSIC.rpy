label chapter02_music:

    $ points = 0

    scene september with fade
    pause 4.0

    scene foundry entrance with fade

    "It’s the first week of September."

    "You and Todd have chatted with the group, and together, the work has been
    broken up accordingly."

    "Todd has experience producing music that you don’t, so you’re gonna focus on the soundscape and Todd is going to focus on a backing soundtrack for your booth."

    "You’ve been texting with Todd, and you’re going to go to the library together to go over a rough production schedule."

    show todd nuetral with dissolve

    "He was waiting for you at one of the tables in the DFA."

    t "You find any good sound bites yet? Or maybe just an idea of what you want to put together?"

    menu any_ideas:

        "You were pretty confident so far.":
            show todd smile
            "Nice! That's great to hear!"

        "You had no idea what you were doing":
            "Hey, that's ok. You're allowed to take time to figure stuff out."

    show todd nuetral

    "Todd had a lot of good expertise. He showed you a couple of websites that
    offered free mp3 downloads, like Freesound and Filmstro."

    "He’s been making music since he was in high school and even had an album out
    on Spotify. It’s pretty good; you listened to it on the walk over."

    t "Would you ever produce your own stuff? Maybe even release it on Soundcloud or Spotify?"

    menu produce:

        "Oh absolutely!":
            show todd smile
            t "Awesome! You should go for it while I'm still around to throw you a launch party!"

        "I don’t have the skills for that…":
            t "Well maybe not yet, but you're never gonna learn unless you go for it.
            DO THE THING. LEARN THE MUSIC STUFF. SHARE YOUR SOUND."

        "That’s not really my dream":
            t "That's cool, at least you know what you want. Not everyone does."

    show todd nuetral
    t "I got really lucky when releasing my stuff, I didn’t have to wait around
    until I had a career. The entry barrier is so low nowadays anyway…"

    menu barrier:

        "What’s an entry barrier..?":
            t "An entry barrier is basically the minimum requirement for people to
            start doing a thing."
            t "The entry barrier for music is super low because of how easy it is
            to get the programs to make music and also how easy it is to self-publish."

        "It’s the miracle of the internet":
            show todd smile
            "Todd laughs."

    hide todd
    "You and Todd go over the rest of your work schedule and have a lovely time
    working in the library together."

    # October
    scene october with dissolve
    pause 4.0

    scene foundry entrance with fade

    "It’s October. You know what that means…."

    menu october_vibes2:

        "Spooky time?":
            jump after_october_vibes2

        "Pumpkin spice?":
            jump after_october_vibes2

        "Midterms?":
            jump after_october_vibes2

label after_october_vibes2:

    "Yeah, I guess so, but it also means class registration is just around the corner!"

    menu october_reaction2:

        "Oh...?":
            jump after_october_reaction2

        "Yikes.":
            jump after_october_reaction2

label after_october_reaction2:

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

    c "What classes are you looking at?"

    t "If only I was upper-division, I’d be taking Immersive Audio or Digital Musicianship.
     I’m still really excited for Sound and Space though!"

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

    # November

    scene november with fade
    pause 4.0

    scene foundry entrance with fade

    "Todd was certified to use the recording booth on the first floor of DFA recently
    for your project. He’s going to play guitar for the backing track he is making,
    and he asked you to help."

    menu booth_cert:

        "You needed to be certified to be in the recording booth at all.":
            "Wait, is that right? You're not certified, are you breaking the rules
            right now? No, You're just wrong."
            $ points += 1

        "You only need to be certified to reserve your time.":
            "It's really nice to have a friend who knows what they're doing to reserve
            a time and help you out, assuming you can't just reserve your own spot by
            the next time you need the booth."
            $ points += 3

    scene booth with fade
    show todd smile with dissolve
    "You meet Todd at the door. He smiles and opens the door for you."

    t "Time to get set up. Make yourself at home at the desk."

    hide todd with dissolve
    "Todd goes into the recording room and shuts the door. You can barely hear him
    in there setting up his guitar; that thick glass and foam paneling are really
    effective. The desk you sat down at just has one MacBook on it. It’s a small,
    comforting space for sound and music students to record everything from voice
    acting to self-released albums."

    show todd nuetral with dissolve
    "Todd gives you a nod and a thumbs up and you boot up Logic Pro."

    t "Ok, we’re gonna do a few takes if that’s all right. I was thinking a minute
    long or so? What do you think? Is that long enough for a good loop?"

    menu booth_time:

        "Sounds good!":
            $ points += 2

        "Maybe two minutes?":
            show todd smile
            $ points += 3

        "Maybe just 30 seconds?":
            show todd frown
            $ points += 1

    "Todd nods and you both get to work. He’s really good at playing guitar."
    hide todd with dissolve

    menu track:

        "You record each take on a separate track in Logic.":
            "You even color-coded all of the guitar tracks as you finished recording
            them. You nailed it!"
            $ points += 3

        "You record each take on the same Logic track.":
            "You accidentally record all of your takes on the same track, meaning
            only the last one saved. Oh well, at least it was the best take."
            $ points += 2

        "What’s a track…?":
            "Tracks in Logic Pro are individual recordings or compositions inside
            a larger piece to help organize and master your project. If you knew
            that you would have been more careful about not recording over all of
            yours..."
            $ points += 1


    if points > 6:

        show todd smile with dissolve
        "You and Todd listen through and pick your favorite track when you’re done
        recording. It sounds amazing! You’re both so excited to listen to the final
        song when Todd’s done with it."

    else:

        show todd frown with dissolve
        "You and Todd listen to what you recorded and agree that it could have been done better."
        t "No one’s probably going to notice but us. It’s still a little frustrating…"

    scene foundry entrance with fade
    show todd nuetral
    "On your way out of DFA, Todd stops and turns to you."

    t "You found some really good sounds for the ambiance side of our project, I’m
    wondering if we should just cut my song altogether and focus on that. It’s just{w=0.2}
    not as good as I want it to be…"

    menu todds_song:

        "You should ask the rest of the team":
            t "Champ just listened to it for the first time today, and he loved it.
            Faith told me she had it on loop for a few minutes while she studied..."
            t "If everyone liked it that much, I shouldn't be as hard on my work.
            Never mind, forget I said anything."

        "Well, if you’re worried about our grade…":
            t "Yeah, I kind of am. Maybe... actually no. The rest of the team really
            likes my song."
            t "I need to be a little more optimistic about my work,
            especially since I worked so hard on it."

        "Are you kidding? The song is amazing!":
            "Todd smiles."
            t "Thanks. That makes me feel a lot better. Ok, we'll keep it."

    hide todd with dissolve
    "You both walk home after a productive afternoon in the DFA recording studio."

    "The semester is almost over. Didn’t you just get here?"

    # Move to last chapter.

    $ points = 0
    jump chapter07_dec
