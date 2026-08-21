# =========================
# FREE-TIME CALENDAR
# =========================

label free_time:

    $ free_time_active = True

    # Both free actions have been used.
    if free_actions <= 0:

        $ free_time_active = False
        jump main_story_event


    # =========================
    # SPECIAL ROUTE CHECKS
    # =========================

    if (
        chapter == 3
        and tansy_route_triggered
        and not tansy_route_offer_seen
        and not tansy_route_locked
    ):

        jump tansy_route_offer


    # Show map.
    call screen mirthhaven_map

    jump free_time

# =========================
# CHARACTER ACTION COMPLETE
# =========================

label complete_free_action:

    $ free_actions -= 1

    jump free_time

# =========================
# START FREE-TIME PERIOD
# =========================

label start_free_time(completed_chapter):

    $ story_progress += 1
    $ chapter = completed_chapter

    $ free_actions = max_free_actions
    $ time_slot = "morning"

    jump free_time

# =========================
# SET UP FREE-TIME
# =========================
init python:

    def setup_free_time(completed_chapter):
        store.story_progress += 1
        store.chapter = completed_chapter
        store.free_actions = store.max_free_actions
        store.free_time_active = True

#PLACE HOLDER MAP LAYOUT SYSTEM
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


    text "Character Interactions: [free_actions] / [max_free_actions]":
        xalign 0.5
        ypos 195
        size 24


    # =========================
    # CLARA
    # =========================

    if clara_event_available():

        textbutton "Wanderlust Wheel - Clara":
            xpos 150
            ypos 320
            action Jump("clara_route_event")

    # =========================
    # TANSY
    # =========================

    if tansy_event_available():

        textbutton "Solarium Sanctum - Tansy":
            xpos 600
            ypos 320
            action Jump("tansy_route_event")

    # =========================
    # TARIQ
    # =========================

    if tariq_event_available():

        textbutton "Sun-Gilded Market - Tariq":
            xpos 600
            ypos 320
            action Jump("tariq_route_event")
            
    # =========================
    # PASS TIME
    # =========================

    textbutton "Spend Free Time Alone":
        xalign 0.5
        ypos 750
        action Jump("pass_time")

# =========================
# PASS TIME EVENT
# =========================

label pass_time:

    "You decide to spend your free time alone and get some rest."

    jump complete_free_action
    
#=========================
# Checks for what chapter you're on
#========================= 

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