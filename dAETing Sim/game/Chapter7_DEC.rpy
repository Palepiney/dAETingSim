label chapter07_dec:
# ADW and final Chapter.

    $ points = 0
    play music "audio/showcase_theme_moc2_by_John_T._Chambers.mp3"

    # december
    scene december with fade
    pause 4.0

    scene black
    "It's time..."

    scene foundry entrance with fade

    "The ADW student night is officially starting in a couple hours. Everyone is running around in matching T-shirts, getting final preparations in order."

    if path_name == "Todd":
        show todd smile with dissolve
        "Because all tech needed to be loaded in the day of, you and Todd are spending the afternoon setting up your speakers. They’re just bluetooth, they don’t need to be fancy."

        "Todd is running your sound effects through two small speakers hidden on either side of the game table, while the music will be coming through his speaker hiding behind Johnny’s chair for the night."
    elif path_name == "Elaine":
        show elaine smile with dissolve
        "You and Elaine are the first to arrive, setting up the tent and helping everyone else get ready."

        "One by one, your group members trickle in to help finalize your project. It’s like, actually here. In person. A whole, free standing thing. Whoa."
    elif path_name == "Champ":
        show champ smile with dissolve
        "Setting up the projector is easy since you tested it in the PLAI lab. It looked good before, but it looks even better now."
    elif path_name == "Faith":
        show faith smile with dissolve
        "You and Faith arrive last since all you have to do for set up is just hang your posters. Faith looks at the projected wall and smiles at her work."
        "It’s a different experience looking at it projected instead of just having it on a screen."
    else:
        show johnny smile with dissolve
        "Johnny wastes no time setting up the cards for play in the center of the tent. He’s giddy, bouncing up and down while he waits for people to come play his game."

    hide todd
    hide johnny
    hide elaine
    hide faith
    hide johnny


    show elaine smile at halfleft with dissolve
    e"It feels so good to be done."

    show faith smile at halfright with dissolve
    f"Understatement of the century."

    show champ smile at center with dissolve
    c"What, did y’all not have fun?"

    e "No, it was a blast! I’m just happy to have created something so unique."

    f"Maybe when I’m less tired I’ll be just as excited as you are…"

    show johnny smile at right with dissolve
    show todd smile at left with dissolve
    "Todd gave her a reassuring pat on the shoulder. Elaine and Faith both had a point. The work was good, but it was still work."

    "Everything went perfect. No matter where people were coming from, whether they were creatives from around Austin or fellow students on a break, everyone had fun under your tailgate tent."

    "By the time the night was over, you were exhausted. But hey, everything went great!{w} And this was only your first semester…"

    scene black with fade
    pause (2.0)
    scene end with fade
    $ renpy.pause()

    # This ends the game.
    return
