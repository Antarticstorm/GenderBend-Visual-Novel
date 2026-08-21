# =========================
# FREE-TIME CALENDAR
# =========================

label free_time:

    $ free_time_active = True

    # ==================================
    # MAIN STORY DEADLINE
    # ==================================

    if day >= main_story_day:

        $ free_time_active = False
        jump main_story_event


    # ==================================
    # SPECIAL ROUTE EVENTS
    # ==================================

    if (
        chapter >= 3
        and chapter <= 4
        and tansy_route_triggered
        and not tansy_route_offer_seen
        and not tansy_route_locked
    ):

        jump tansy_route_offer


    # ==================================
    # NORMAL FREE ACTION
    # ==================================

    call screen mirthhaven_map

    jump free_time

# =========================
# TIME ADJUSTMENT
# =========================
label advance_time:

    if time_slot == "morning":

        $ time_slot = "afternoon"

    elif time_slot == "afternoon":

        $ time_slot = "evening"

    elif time_slot == "evening":

        $ time_slot = "morning"
        $ day += 1

    jump free_time

#PLACE HOLDER SYSTEM
screen mirthhaven_map():

    tag menu

    text "Mirthhaven":
        xalign 0.5
        ypos 40
        size 50

    text "Day [day]":
        xalign 0.5
        ypos 110
        size 35

    text "[time_slot!c]":
        xalign 0.5
        ypos 155
        size 28

    text "Main Story: Day [main_story_day]":
        xalign 0.5
        ypos 195
        size 24

    textbutton "Wanderlust Wheel - Clara":
        xpos 150
        ypos 320
        action Jump("label clara_route_event:")

        
    textbutton "Rest / Pass Time":
        xalign 0.5
        ypos 750
        action Jump("pass_time")

label pass_time:

    "You decide to spend some time resting."

    jump advance_time

label clara_route_event:

    if clara_route_locked:
        jump free_time

    if clara_route_progress == 0:
        jump clara_chapter_1

    elif clara_route_progress == 1:
        jump clara_chapter_2

    elif clara_route_progress == 2:
        jump clara_chapter_3

    elif clara_route_progress == 3:
        jump clara_chapter_4

    else:
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