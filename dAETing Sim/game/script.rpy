# The script of the game goes in this file.

# Declared characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Elaine", color = "#ff9770")
define st = Character("Steve", color = "#ffffff")
define c = Character("Champ", color = "#f15bb5")
define f = Character("Faith", color = "#00bbf9")
define j = Character("Johnny", color = "#9b5de5")
define t = Character("Todd", color = "#cdf3a0")

# A custom position variable for sprites on the screen.

transform halfleft:
    xpos 0.2 ypos 0.2

# A custom position variable for sprites on the screen.

transform halfright:
    xpos 0.6 ypos 0.2

# The game starts here.

label start:
    # Points variable for path choices.
    $ points = 0

    jump chapter01
