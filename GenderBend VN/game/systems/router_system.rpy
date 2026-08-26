# ============================================================
# ROUTE SYSTEM
# ============================================================

init python:

    def romance_available(affection, romance_locked):
        """
        Returns True when the character's romantic ending
        is still obtainable.
        """

        return affection >= 80 and not romance_locked


    def route_available(unlocked, locked):
        """
        Returns True when the character's route can
        currently be pursued.
        """

        return unlocked and not locked
    
    #Is clara available?
    def clara_event_available():

        if not clara_route_unlocked:
            return False

        if clara_route_locked:
            return False

        if clara_route_progress == 0 and chapter >= 1:
            return True

        if clara_route_progress == 1 and chapter >= 2:
            return True

        if clara_route_progress == 2 and chapter >= 3:
            return True

        if clara_route_progress == 3 and chapter >= 4:
            return True

        return False

    #Is Tansy available?
    def tansy_event_available():

        # Tansy's route must have been accepted.
        if not tansy_route_unlocked:
            return False

        # Route was permanently closed.
        if tansy_route_locked:
            return False

        # Chapter 3 is launched directly by the special-route offer,
        # so the normal map only needs to expose Chapter 4.
        if tansy_route_progress == 4 and chapter >= 4:
            return True

        return False
    
    #Is tariq available?
    def tariq_event_available():

        if not tariq_route_unlocked:
            return False

        if tariq_route_locked:
            return False

        if tariq_route_progress == 0 and chapter >= 1:
            return True

        if tariq_route_progress == 1 and chapter >= 2:
            return True

        if tariq_route_progress == 2 and chapter >= 3:
            return True

        if tariq_route_progress == 3 and chapter >= 4:
            return True

        return False

    #Is bao available?
    def bao_event_available():

        if not bao_route_unlocked:
            return False

        if bao_route_locked:
            return False

        if bao_route_progress == 0 and chapter >= 1:
            return True

        if bao_route_progress == 1 and chapter >= 2:
            return True

        if bao_route_progress == 2 and chapter >= 3:
            return True

        if bao_route_progress == 3 and chapter >= 4:
            return True

        return False

    #Is elianna available?
    def elianna_event_available():

        if not elianna_route_unlocked:
            return False

        if elianna_route_locked:
            return False

        if elianna_route_progress == 0 and chapter >= 1:
            return True

        if elianna_route_progress == 1 and chapter >= 2:
            return True

        if elianna_route_progress == 2 and chapter >= 3:
            return True

        if elianna_route_progress == 3 and chapter >= 4:
            return True

        return False

    #Is domitilla available?
    def domitilla_event_available():

        if not domitilla_route_unlocked:
            return False

        if domitilla_route_locked:
            return False

        if domitilla_route_progress == 0 and chapter >= 1:
            return True

        if domitilla_route_progress == 1 and chapter >= 2:
            return True

        if domitilla_route_progress == 2 and chapter >= 3:
            return True

        if domitilla_route_progress == 3 and chapter >= 4:
            return True

        return False

    #Is barek available?   
    def barek_event_available():

        if not barek_route_unlocked:
            return False

        if barek_route_locked:
            return False

        if barek_route_progress == 0 and chapter >= 1:
            return True

        if barek_route_progress == 1 and chapter >= 2:
            return True

        if barek_route_progress == 2 and chapter >= 3:
            return True

        if barek_route_progress == 3 and chapter >= 4:
            return True

        return False
# ============================================================
# CLARA EVENT RESOLVER
# ============================================================

label clara_route_event:

    # Entire route unavailable.
    if not clara_route_unlocked or clara_route_locked:
        jump free_time

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

    $ tansy_route_progress = 4
    $ finish_character_action("tansy")

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

    $ tansy_route_progress = 5
    $ finish_character_action("tansy")

    jump free_time


# ============================================================
# TARIQ EVENT RESOLVER
# ============================================================

label tariq_route_event:

    if not tariq_route_unlocked or tariq_route_locked:
        jump free_time

    if tariq_route_progress == 0 and chapter >= 1:
        jump tariq_chapter_1

    elif tariq_route_progress == 1 and chapter >= 2:
        jump tariq_chapter_2

    elif tariq_route_progress == 2 and chapter >= 3:
        jump tariq_chapter_3

    elif tariq_route_progress == 3 and chapter >= 4:
        jump tariq_chapter_4

    jump free_time

# ============================================================
# BAO EVENT RESOLVER
# ============================================================

label bao_route_event:

    if not bao_route_unlocked or bao_route_locked:
        jump free_time

    if bao_route_progress == 0 and chapter >= 1:
        jump bao_chapter_1

    elif bao_route_progress == 1 and chapter >= 2:
        jump bao_chapter_2

    elif bao_route_progress == 2 and chapter >= 3:
        jump bao_chapter_3

    elif bao_route_progress == 3 and chapter >= 4:
        jump bao_chapter_4

    jump free_time

# ============================================================
# ELIANNA EVENT RESOLVER
# ============================================================

label elianna_route_event:

    if not elianna_route_unlocked or elianna_route_locked:
        jump free_time

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

label barek_route_event:

    if not barek_route_unlocked or barek_route_locked:
        jump free_time

    if barek_route_progress == 0 and chapter >= 1:
        jump barek_chapter_1

    elif barek_route_progress == 1 and chapter >= 2:
        jump barek_chapter_2

    elif barek_route_progress == 2 and chapter >= 3:
        jump barek_chapter_3

    elif barek_route_progress == 3 and chapter >= 4:
        jump barek_chapter_4

    jump free_time
# ============================================================
# COMPLETION HELPER
# ============================================================

label finish_clara_event:

    $ clara_route_progress += 1
    $ finish_character_action("clara")

    jump free_time


label finish_tariq_event:

    $ tariq_route_progress += 1
    $ finish_character_action("tariq")

    jump free_time

label finish_bao_event:

    $ bao_route_progress += 1
    $ finish_character_action("bao")

    jump free_time

label finish_elianna_event:

    $ elianna_route_progress += 1
    $ finish_character_action("elianna")

    jump free_time

label finish_domitilla_event:

    $ domitilla_route_progress += 1
    $ finish_character_action("domitilla")

    jump free_time
    
label finish_barek_event:

    $ barek_route_progress += 1
    $ finish_character_action("barek")

    jump free_time