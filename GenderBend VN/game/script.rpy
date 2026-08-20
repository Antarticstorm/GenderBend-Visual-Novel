default chapter = 1
default story_progress = 0

default clara_route = 0
default tariq_route = 0

default clara_event_1_seen = False
default tariq_event_1_seen = False

default chapter_1_ending = None
default chapter_2_ending = None
default chapter_3_ending = None
default chapter_4_ending = None
default chapter_5_ending = None

default mc_name = "Apprentice"

label start:

    # Chapter 1 begins
    jump chapter_1

# =========================
# CALENDAR SYSTEM
# =========================

default day = 1

# Day on which the next mandatory story event occurs.
default main_story_day = 3