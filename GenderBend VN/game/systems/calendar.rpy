# =========================
# FREE-TIME CALENDAR
# =========================

label free_time:

    $ free_time_active = True

    if chapter < 4 and free_actions <= 0:

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

        store.free_time_active = True
        store.characters_visited_this_period = []

        # Chapters 1-3 use normal free actions.
        if completed_chapter < 4:
            store.free_actions = store.max_free_actions

        # Chapter 4 uses route commitments instead.
        elif completed_chapter == 4:
            store.free_actions = 0
            store.committed_routes = []
    
    def can_visit_character(character_id):

        # ========================================================
        # CHAPTERS 1-3
        # One interaction with each character per free-time period.
        # ========================================================

        if store.chapter < 4:

            return character_id not in store.characters_visited_this_period


        # ========================================================
        # CHAPTER 4
        # Only committed characters remain available once
        # both commitment slots are occupied.
        # ========================================================

        if store.chapter == 4:

            return can_commit_character(character_id)


        return False

    def finish_character_action(character_id):

        # ========================================================
        # CHAPTERS 1-3
        # ========================================================

        if store.chapter < 4:

            if character_id not in store.characters_visited_this_period:
                store.characters_visited_this_period.append(character_id)

            store.free_actions -= 1


        # ========================================================
        # CHAPTER 4
        # ========================================================

        elif store.chapter == 4:

            commit_character(character_id)

    def route_is_committed(character_id):

        return character_id in store.committed_routes


    def commitment_slots_full():

        return len(store.committed_routes) >= store.max_committed_routes


    def can_commit_character(character_id):

        # Already committed.
        if character_id in store.committed_routes:
            return True

        # Still have an empty slot.
        return len(store.committed_routes) < store.max_committed_routes


    def commit_character(character_id):

        # Don't add duplicates.
        if character_id in store.committed_routes:
            return

        # Add character if a slot exists.
        if len(store.committed_routes) < store.max_committed_routes:
            store.committed_routes.append(character_id)

    def normal_route_event_available(progress, unlocked, locked):

        if not unlocked or locked:
            return False


        # ========================================================
        # CHAPTERS 1-3
        # ========================================================

        if store.chapter < 4:

            if progress == 0 and store.chapter >= 1:
                return True

            if progress == 1 and store.chapter >= 2:
                return True

            if progress == 2 and store.chapter >= 3:
                return True

            return False


        # ========================================================
        # CHAPTER 4
        # ========================================================

        if store.chapter == 4:

            # Player must have interacted with this
            # character at least once before Chapter 4.
            #
            # Progress 1-3 can catch up.
            # Progress 4 is already finished.

            return progress >= 1 and progress < 4


        return False
# =========================
# PASS TIME EVENT
# =========================

label pass_time:

    "You decide to spend your free time alone and get some rest."

    jump complete_free_action
    
# ============================================================
# FINISH CHAPTER 4 FREE TIME
# ============================================================

label finish_chapter_4_free_time:

    $ free_time_active = False
    $ characters_visited_this_period = []

    jump chapter_5

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
