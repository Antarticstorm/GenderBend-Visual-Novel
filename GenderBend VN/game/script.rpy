default chapter = 1
default story_progress = 0

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
default time_slot = "morning"

default main_story_day = 3

default free_time_active = False

# =========================
# ROUTE SYSTEM
# =========================

# =========================
# CLARA ROUTE

default clara_route_unlocked = True
default clara_route_progress = 0

# Relationship / performance
default clara_affection = 0
default clara_kid_warning = False
default clara_romance_locked = False

# Tansy prerequisite
default tansy_route_triggered = False

# Clara route ending
default clara_ending = None


# =========================
# TARIQ ROUTE

default tariq_route_unlocked = True
default tariq_route_progress = 0
default tariq_affection = 0

default tariq_romance_locked = False
default tariq_route_locked = False

# =========================
# TANSY SPECIAL ROUTE

default tansy_route_triggered = False
default tansy_route_unlocked = False
default tansy_route_progress = 0
default tansy_affection = 0

default tansy_romance_locked = False
default tansy_route_locked = False

# Has the player already been offered the special route?
default tansy_route_offer_seen = False