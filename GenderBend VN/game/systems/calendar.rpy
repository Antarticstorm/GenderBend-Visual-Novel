# =========================
# FREE-TIME CALENDAR
# =========================

label free_time:

    # Check whether we've reached
    # the next mandatory story date.

    if day >= main_story_day:
        jump main_story_event

    # Otherwise open the map.
    call screen mirthaven_map

    # Safety fallback.
    jump free_time

screen mirthaven_map():

    tag menu

    text "Mirthhaven" xalign 0.5 ypos 40 size 50

    text "Day [day]" xalign 0.5 ypos 110 size 35

    text "Next Main Story: Day [main_story_day]" xalign 0.5 ypos 155


    # Clara
    textbutton "Wanderlust Wheel - Clara":
        xpos 150
        ypos 300
        action Jump("visit_clara")


    # Tariq
    textbutton "Sun-Gilded Market - Tariq":
        xpos 600
        ypos 300
        action Jump("visit_tariq")


    # Barek
    textbutton "Nautilus Point - Barek":
        xpos 150
        ypos 500
        action Jump("visit_barek")


    # Ellie
    textbutton "Solarium Sanctum - Ellie":
        xpos 600
        ypos 500
        action Jump("visit_ellie")

label visit_clara:

    clara "Oh! It's good to see you again, [mc_name]."

    clara "How is your search progressing?"

    mc "Slowly, but I'm getting there."

    clara "Then make sure you don't exhaust yourself."

    $ clara_route += 1

    $ day += 1

    jump free_time

label visit_tariq:

    tariq "Back already, little wizard?"

    mc "Don't sound so disappointed."

    tariq "Quite the opposite."

    $ tariq_route += 1

    $ day += 1

    jump free_time

label visit_barek:

    barek "Back at the docks, wizard?"

    mc "I had some free time."

    barek "Then you're always welcome here!"

    $ day += 1

    jump free_time


label visit_ellie:

    ellie "Oh! Hello, [mc_name]!"

    mc "Busy?"

    ellie "Always..."

    $ day += 1

    jump free_time

label main_story_event:

    if chapter == 1:
        jump chapter_2

    elif chapter == 2:
        jump chapter_3

    elif chapter == 3:
        jump chapter_4

    elif chapter == 4:
        jump chapter_5

    return