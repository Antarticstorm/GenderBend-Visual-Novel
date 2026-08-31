# ============================================================
# ROUTE SYSTEM
# ============================================================

init python:

    def romance_available(affection, romance_locked):

        return affection >= 80 and not romance_locked


    def route_available(unlocked, locked):

        return unlocked and not locked


    def normal_route_event_available(progress, unlocked, locked):

        if not unlocked or locked:
            return False

        # Event 1
        if progress == 0 and store.chapter >= 1:
            return True

        # Event 2
        if progress == 1 and store.chapter >= 2:
            return True

        # Event 3
        if progress == 2 and store.chapter >= 3:
            return True

        # Event 4
        if progress == 3 and store.chapter >= 4:
            return True

        return False


    def tansy_event_available():

        if not store.tansy_route_unlocked:
            return False

        if store.tansy_route_locked:
            return False

        return (
            store.tansy_route_progress == 4
            and store.chapter >= 4
        )
        
# ============================================================
# CLARA EVENT RESOLVER
# ============================================================

label clara_route_event:

    # Entire route unavailable.
    if not clara_route_unlocked or clara_route_locked:
        jump free_time

    # Chapter 4 commitment.
    if chapter == 4:
        $ commit_character("clara")

    # Clara Chapter 1
    if clara_route_progress == 0 and chapter >= 1:
        jump clara_chapter_1

    # Clara Chapter 2
    elif clara_route_progress == 1 and chapter >= 2:
        jump clara_chapter_2

    # Clara Chapter 3
    elif clara_route_progress == 2 and chapter >= 3:
        jump clara_chapter_3

    # Clara Chapter 4
    elif clara_route_progress == 3 and chapter >= 4:
        jump clara_chapter_4

    # Nothing currently available.
    jump free_time

# ============================================================
# TANSY EVENT RESOLVER
# ============================================================

label tansy_route_event:

    if not tansy_route_unlocked or tansy_route_locked:
        jump free_time

    # Tansy's Chapter 3 is entered through her secret
    # interlude, so the map only routes Chapter 4.
    if tansy_route_progress == 4 and chapter >= 4:
        jump tansy_chapter_4

    jump free_time

# =========================
# FINISH TANSY CHAPTER 3
# =========================

label finish_tansy_chapter_3:

    hide tansy

    $ tansy_route_progress = 4
    $ finish_character_action("tansy")

    call route_end_transition("Tansy") from _call_route_end_transition

    jump free_time

# =========================
# YOU FAILED TANSY 
# =========================

label finish_tansy_failed_event:

    $ tansy_route_progress = 5
    $ finish_character_action("tansy")

    jump free_time  

# =========================
# FINISH TANSY CHAPTER 4
# =========================

label finish_tansy_chapter_4:

    hide tansy

    $ tansy_route_progress = 5
    $ finish_character_action("tansy")

    call route_end_transition("Tansy") from _call_route_end_transition_1

    jump free_time


# ============================================================
# TARIQ EVENT RESOLVER
# ============================================================

# label tariq_route_event:

#     if not tariq_route_unlocked or tariq_route_locked:
#         jump free_time

#     # Chapter 4 commitment.
#     if chapter == 4:
#         $ commit_character("tariq")

#     if tariq_route_progress == 0 and chapter >= 1:
#         jump tariq_chapter_1

#     elif tariq_route_progress == 1 and chapter >= 2:
#         jump tariq_chapter_2

#     elif tariq_route_progress == 2 and chapter >= 3:
#         jump tariq_chapter_3

#     elif tariq_route_progress == 3 and chapter >= 4:
#         jump tariq_chapter_4

#     jump free_time

# ============================================================
# BAO EVENT RESOLVER
# ============================================================

# label bao_route_event:

#     if not bao_route_unlocked or bao_route_locked:
#         jump free_time

#     # Chapter 4 commitment.
#     if chapter == 4:
#         $ commit_character("bao")

#     if bao_route_progress == 0 and chapter >= 1:
#         jump bao_chapter_1

#     elif bao_route_progress == 1 and chapter >= 2:
#         jump bao_chapter_2

#     elif bao_route_progress == 2 and chapter >= 3:
#         jump bao_chapter_3

#     elif bao_route_progress == 3 and chapter >= 4:
#         jump bao_chapter_4

#     jump free_time

# ============================================================
# ELIANNA EVENT RESOLVER
# ============================================================

label elianna_route_event:

    if not elianna_route_unlocked or elianna_route_locked:
        jump free_time

    # Chapter 4 commitment.
    if chapter == 4:
        $ commit_character("elianna")

    if elianna_route_progress == 0 and chapter >= 1:
        jump elianna_chapter_1

    elif elianna_route_progress == 1 and chapter >= 2:
        jump elianna_chapter_2

    elif elianna_route_progress == 2 and chapter >= 3:
        jump elianna_chapter_3

    elif elianna_route_progress == 3 and chapter >= 4:
        jump elianna_chapter_4

    jump free_time

# ============================================================
# DOMITILLA EVENT RESOLVER
# ============================================================

label domitilla_route_event:

    if not domitilla_route_unlocked or domitilla_route_locked:
        jump free_time
    
    # Chapter 4 commitment.
    if chapter == 4:
        $ commit_character("domitilla")

    if domitilla_route_progress == 0 and chapter >= 1:
        jump domitilla_chapter_1

    elif domitilla_route_progress == 1 and chapter >= 2:
        jump domitilla_chapter_2

    elif domitilla_route_progress == 2 and chapter >= 3:
        jump domitilla_chapter_3

    elif domitilla_route_progress == 3 and chapter >= 4:
        jump domitilla_chapter_4

    jump free_time

# ============================================================
# BAREK EVENT RESOLVER
# ============================================================

# label barek_route_event:

#     if not barek_route_unlocked or barek_route_locked:
#         jump free_time

#     # Chapter 4 commitment.
#     if chapter == 4:
#         $ commit_character("barek")

#     if barek_route_progress == 0 and chapter >= 1:
#         jump barek_chapter_1

#     elif barek_route_progress == 1 and chapter >= 2:
#         jump barek_chapter_2

#     elif barek_route_progress == 2 and chapter >= 3:
#         jump barek_chapter_3

#     elif barek_route_progress == 3 and chapter >= 4:
#         jump barek_chapter_4

#     jump free_time
# ============================================================
# COMPLETION HELPER
# ============================================================

label finish_clara_event:

    hide clara

    $ clara_route_progress += 1
    $ finish_character_action("clara")

    call route_end_transition("Clara Vane") from _call_route_end_transition_2

    jump free_time


# label finish_tariq_event:

#     hide tariq

#     $ tariq_route_progress += 1
#     $ finish_character_action("tariq")

#     call route_end_transition("Tariq Vane")

#     jump free_time

# label finish_bao_event:

#     hide bao

#     $ bao_route_progress += 1
#     $ finish_character_action("bao")

#     call route_end_transition("Bao Shen")

#     jump free_time

label finish_elianna_event:

    hide elianna

    $ elianna_route_progress += 1
    $ finish_character_action("elianna")

    call route_end_transition("Elianna Sylvane") from _call_route_end_transition_3

    jump free_time

label finish_domitilla_event:

    hide domitilla

    $ domitilla_route_progress += 1
    $ finish_character_action("domitilla")

    call route_end_transition("Domitilla Bruni") from _call_route_end_transition_4

    jump free_time
    
# label finish_barek_event:

#     hide barek

#     $ barek_route_progress += 1
#     $ finish_character_action("barek")

#     call route_end_transition("Barek Tidejaw")

#     jump free_time