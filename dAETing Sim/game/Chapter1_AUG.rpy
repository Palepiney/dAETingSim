label chapter01:
# Chapter 1

menu start_menu:

    "Are you really ready for this?"

    "Go inside.":
        "Here goes nothing..."

    "Go back home.":
        # Returns to the main menu.
         $ MainMenu(confirm=False)()



label after_start:

    # Shows the foundry.
    scene foundry entrance with fade

    # Starts the background music.
    play music "audio/Idle_Theme_v1_by_John_T_Chambers.mp3" fadein 1.0

    # These display lines of dialogue. {w} means wait for player input or for seconds.

    "You’ve only seen pictures of the inside of DFA until now, and it does not
        disappoint."

    "A large screen in the center of the room showcases various projects from
        across the department."

    "Behind it, a variety of workstations rest against the floor-to-ceiling
        windows."

    "There’s everything from 3D printers to embroidery machines back there…"

    "You scan the booths and tables students can work at. A handful of people are
    already settled in with a coffee or water bottle, despite the early hour."

    "There’s a motorbike made out of feathers sitting on top of a low-rise
        bookcase. Seems right."

    "{w=1.0}You’re stalling."

    "Your first class is in a couple of minutes, and you don’t want to be late.
        First impressions, after all, are very important.{w} First semesters are
        important too.{w} First class."

    "Oh geez."

    "Your classroom is waiting for you at the top of the stairs. No time to think
    about how overwhelming this all is, just gotta go for it."

    # Switch to classroom scene.
    scene classroom with fade

    "First ever AET class.{w} Starting right now.{w} In this room.{w} Holy cow."

    "You go inside and a smattering of freshmen are already waiting inside,
        having polite albeit awkward conversations."

    "No thanks, you’re not in the mood for small talk. {w}You take a seat by the back corner."

    "Eventually an older-looking guy walks in and directly over to a standing
        desk, setting up his laptop and connecting it to the projector.{w} Clearly
        the professor."

    st "Hey everyone, let’s settle in. I’m Professor Steve Watson, but you don’t
    ever have to call me that, Steve is fine."

    st "Welcome to AET 101!"

    "He paused like he expected you to react.  Besides the scattered awkward smile,
    no one reacted as strongly as Steve intended."

    # Play cough SFX.
    play sound "audio/THE_dATEingSim_Cough-005.WAV"
    "With an awkward cough, he moved on."

    st "Alright,{w=0.3} uh,{w=0.3} so you have to take this course before entering into any other
        class for AET. There’s a reason for that.{w} We are all individually amazing
        and talented artists,{w=0.1} but together{w=0.1} we can make even cooler stuff!"

    st "This first class is just as much about honing those teamwork skills as it is
        testing the waters of what AET has to offer."

    "A few people around the room shifted in their seats uncomfortably. {w}Clearly,
        group projects were not everyone’s favorite way to meet new people, even if
        they were all super cool and talented new people."

    st "So! {w=0.3}Who here knows what Austin Design Week is?"

    # Play shuffling sound.
    play sound "audio/THE_dATEingSim_ShufflingOfPeopleAndChairs.WAV" fadein 1.0
    "Silence."

    st "Geez y’all are quiet."

    "Steve takes a moment to pull up something to project on the whiteboard at the front."

    "A modern and trendy-looking website appears with a variety of photos on it.
        {w} Most of them are strangers standing around exhibits, {w=0.2}but there are
        also a few pictures with AET students in them."

    "All the students were photographed candidly, adorned in matching shirts and
        bright smiles while they worked some event."

    st "I’m gonna read this straight off the website for a second,{w=0.5} uh,{w=0.3} ahem."

    st "{i}\"Founded in 2016, Austin Design Week’s (ADW) mission is to build an
        inclusive community that is a source of empowerment and inspiration for
        Austin’s creative problem solvers.\"{/i}"

    st "{i}\"Every year, ADW invites designers, organizations, agencies, and companies
        to host free workshops, studio tours, panels, talks, installations, and
        interactive events centered around a theme that challenges us to consider
        the role of design in improving our communities and ourselves.\"{/i}"

    st "{i}\" From graphic design to architecture, digital design to fashion, and
        more, ADW brings together creatives across disciplines and across Austin
        to share their talents, projects, ideas, and workspaces while inviting in
        the larger community (in Austin and beyond).\"{/i}"

    st "Sounds a lot like what we’re trying to accomplish too, doesn’t it?{w} So
        here’s your project:"

    st "Every winter, as the semester comes to a close, we host a student showcase
        on campus to close out ADW.{w} You, in teams of five or six, will be
        making something to showcase at this event."

    st "You could make a game, a sculpture, an audio experience, anything you want!
     I’d advise checking the course list for inspiration."

    "You let the professor's words sink in."

    "You’ve only ever made things for yourself, and you have no idea if you’re
        even actually all that good."

# Choice
menu adw_reaction:

    "This is going to be a trainwreck.":
        jump after_adw_reaction

    "This is going to be an adventure.":
        jump after_adw_reaction

    "You have no idea how it’s going to go.":
        jump after_adw_reaction

label after_adw_reaction:

    st "Now, you’re all freshmen and odds are you’ll be spending most of freshman
        year testing concepts and making some not-so-great stuff. Not that it’s
        bad, just not your best."

    st "Point is, don’t expect this to be hyper-polished or professional, and definitely
        don’t overload yourself and your team with pressure. Take this seriously,
        for sure, just not too serious."

    st "Have fun with it, learn something. Focus on the making, not the made. Got it?"

    st "Great. Now, I’ve sorted you randomly, when I call your last name, move to
        the table I point to."

    "Everyone slowly began to scatter around the room. You moved to your team’s table last."

    "Steve started talking again, but you were more focused on your new teammates."

    show todd nuetral with dissolve

    "One of them has a pair of headphones around his neck, and you remark that
        they look more heavy-duty than what you would normally see on the shelves of a tech store."

    "He’s tapping his face, and while you can’t hear it you can tell by watching
        he’s silently keeping a beat to a song no one else can hear."

    hide todd with dissolve
    show elaine nuetral with dissolve

    "One girl is writing furiously in a notebook, arrows and chicken-scratch handwriting
        dominating the page.{w} You genuinely can’t tell if she’s taking notes or writing
        something completely different."

    hide elaine with dissolve
    show champ nuetral with dissolve

    "Another guy has a laptop covered in stickers for theaters all over the state,
        from Bass Concert Hall to TUTS Houston."

    "He also has a yellow and black one more prominently displayed than the others
        that says “High End Systems” across the bottom edge."

    hide champ with dissolve
    show faith nuetral with dissolve

    "The student sitting next to you is writing notes with a drawing pencil. It might
        even be charcoal, you can’t tell."

    "She’s flipping back and forth between the scratch paper she has her notes on
        and the sketchbook underneath it where she has a portrait of Steve taking shape.
        {w} She’s really good."

    hide faith with dissolve
    show johnny nuetral phone with dissolve

    "The last boy at your table keeps staring at his lap. His backpack is drowning
        in keychains for various franchises you recognize, and when you drop your
        pencil you notice his phone is illuminating the underside of the table."

    "He might be texting in class, but he’s been at it for a while now; he’s probably
        playing a game of some kind."

    hide johnny with dissolve

    st "Alright, the rest of class is yours! Homework by next Monday is to turn in
        the worksheet posted on canvas. If I were you I’d start it now."

    st "One copy for your whole group is fine, just make sure everyone’s name makes
        it on there. And remember to turn in your loglines by end of class today."

    "You totally missed the rest of what he was saying.{w} Which worksheet?{w}
        What’s a logline?"

    show todd nuetral at left with dissolve
    show elaine nuetral at halfleft with dissolve
    show champ nuetral at center with dissolve
    show faith nuetral at halfright with dissolve
    show johnny nuetral phone at right with dissolve

    "You turn to your teammates. They all look as confused as you do. {w}Crap.
        {w=1.0} Now what?"

    hide todd with dissolve
    hide elaine with dissolve
    hide faith with dissolve
    hide johnny with dissolve

    "???" "There’s only one worksheet up right now, it’s us describing the project
        we want to do."

    "Laptop-stickers-guy is the first to speak up. He glances around between
        the other five of us."

    "Laptop Guy" "So,{w=0.2} uh,{w=0.2} names first, right? I’m Champ, and I’m from Houston."

    show faith nuetral at halfright with dissolve

    "???" "What part?"

    c "Dirty Cyp."

    "???" "Bummer."

    c "I know. You from Houston, too?"

    f "Yeah, I grew up in Spring. My name’s Faith."

    c " Cool, nice to meet you."

    show johnny nuetral phone at right with dissolve
    show elaine nuetral at halfleft with dissolve
    show todd nuetral at left with dissolve

    "Silence took over for a couple of awkward seconds."

    c "Sorry, uh, didn’t mean to derail us. Who’s next?"

    show johnny smile
    hide todd with dissolve
    hide elaine with dissolve

    "The boy with all the nerdy keychains on his bag leans back with a stretch
        and grins nonchalantly."

    j "I’m Johnny, I’m from DC and I have no idea what y’all are talking about."

    show faith frown

    "He gestured back and forth between Champ and Faith. Faith squinted at him."

    f "Houston is big. That’s really it."

    j "Hmph. Yeah ok."

    hide faith with dissolve
    hide johnny with dissolve
    hide champ with dissolve
    show elaine smile with dissolve

    e "If we’re going around in order, I guess I can go next..? I’m Elaine, it’s
        nice to meet you all. Oh, and I grew up here..! "

    hide elaine with dissolve
    show todd frown with dissolve

    "The boy with the headphones on Elaine’s left suddenly looked very uncomfortable
        now that it was his turn to talk."

    t "Hey, I’m Todd. I’m from Dallas."

    show todd nuetral at left with dissolve
    show elaine nuetral at halfleft with dissolve
    show champ nuetral at center with dissolve
    show faith nuetral at halfright with dissolve
    show johnny nuetral phone at right with dissolve

    "All eyes then turn to you as the last person to talk."

    "Oh boy."

    "A chorus of stinted nice-to-meet-you’s rang out. This is weird. Is it always
        this weird? Is it bad that it’s this weird? Are you just weird?"

    j " Let’s get into the thing so we don’t have to think about it after this
        class is over. Y’all got any ideas? What do we want our project to be?"

    # Choice
    menu project_idea:

        "Speak up right away.":
            "You offer up some ideas that have been floating around in your head for a while."

        "Wait for someone else.":
            "Not fully confident in talking to new people, you decide to give the stage to someone else."

    "Eventually, you all come up with an idea that gives everyone something to do that
        highlights their strengths."

    "You’re going to build a roleplaying card game booth, complete with mood
        lighting and backdrops."

    "Johnny is primarily pursuing game development so he’s going to be making the
        mechanics for the game itself by building off of a concept he already had."

    "Todd is going to work on a soundscape and music to listen to while patrons play."

    "Faith is going to digitally paint a backdrop that Champ would project on a
        screen in the back of our booth."

    "And Elaine, the storyteller, is going to help get the actual booth up and
        make sure that everyone’s work meshed together into one cohesive environment."

    "Wait, what are you gonna do?"

    # This specifies player's path choice.
    $ path_name = "0"

    menu path_choice:
        "Music":
            $ path_name = "Todd"
            hide champ with dissolve
            hide faith with dissolve
            hide elaine with dissolve
            hide johnny with dissolve

        "Storytelling":
            $ path_name = "Elaine"
            hide champ with dissolve
            hide faith with dissolve
            hide todd with dissolve
            hide johnny with dissolve

        "Games":
            $ path_name = "Johnny"
            hide champ with dissolve
            hide faith with dissolve
            hide todd with dissolve
            hide elaine with dissolve

        "Art":
            $ path_name = "Faith"
            hide champ with dissolve
            hide elaine with dissolve
            hide todd with dissolve
            hide johnny with dissolve

        "Projection":
            $ path_name = "Champ"
            hide elaine with dissolve
            hide faith with dissolve
            hide todd with dissolve
            hide johnny with dissolve

    "You tell [path_name] that you would like to help them with their part
        of the project, and they look happy to have you."

    hide elaine with dissolve
    hide faith with dissolve
    hide todd with dissolve
    hide johnny with dissolve

    "Everyone exchanges numbers and says their goodbyes as students shuffle out
        of the classroom."

    scene foundry entrance with fade

    "Day one, in the bag! See, that wasn’t so hard! Now, time to get to work and
        make this the best group project you can!"

    # Determines which chapter to jump to based on player's choice.

    if path_name == "Todd":
        jump chapter02_music
    elif path_name == "Elaine":
        jump chapter03_story
    elif path_name == "Champ":
        jump chapter06_plai
    elif path_name == "Faith":
        jump chapter05_art
    elif path_name == "Johnny":
        jump chapter04_game
    else:
        return
