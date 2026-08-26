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

        # New free-time period.
        # Everyone becomes visitable again.
        store.characters_visited_this_period = []
    
    def can_visit_character(character_id):

        # Chapter 4 is the catch-up / commitment period.
        # Repeat visits are allowed.
        if store.chapter == 4:
            return True

        # Chapters 1-3:
        # Character can only be selected once per period.
        return character_id not in store.characters_visited_this_period

    def finish_character_action(character_id):

        if character_id not in store.characters_visited_this_period:
            store.characters_visited_this_period.append(character_id)

        store.free_actions -= 1

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

    if clara_event_available() and can_visit_character("clara"):

        textbutton "Wanderlust Wheel - Clara":
            xpos 150
            ypos 320
            action Jump("clara_route_event")

    # =========================
    # TANSY
    # =========================

    if tansy_event_available() and can_visit_character("tansy"):

        textbutton "Solarium Sanctum - Tansy":
            xpos 900
            ypos 320
            action Jump("tansy_route_event")

    # =========================
    # TARIQ
    # =========================

    if tariq_event_available() and can_visit_character("tariq"):

        textbutton "Sun-Gilded Market - Tariq":
            xpos 600
            ypos 320
            action Jump("tariq_route_event")

    # =========================
    # BAO
    # =========================
    if bao_event_available() and can_visit_character("bao"):

        textbutton "The Laughing Anchor - Bao":
            xpos 150
            ypos 500
            action Jump("bao_route_event")
        
    # =========================
    # ELIANNA
    # =========================
    if elianna_event_available() and can_visit_character("elianna"):

        textbutton "Solarium Sanctum - Elianna":
            xpos 600
            ypos 500
            action Jump("elianna_route_event")

    # =========================
    # DOMITILLA
    # =========================
    if domitilla_event_available() and can_visit_character("domitilla"):

        textbutton "Crestward Bastion - Domitilla":
            xpos 900
            ypos 500
            action Jump("domitilla_route_event")

    # =========================
    # BAREK
    # =========================
    if barek_event_available() and can_visit_character("barek"):

    textbutton "Nautilus Point - Barek":
        xpos 150
        ypos 650
        action Jump("barek_route_event")

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

# =========================
# CHARACTER ACTION COMPLETE
# =========================

label complete_free_action:

    $ free_actions -= 1

    jump free_time


#=========================
# Checks for what chapter you're on
#========================= 
label complete_character_action(character_id):

    $ characters_visited_this_period.append(character_id)
    $ free_actions -= 1

    jump free_time