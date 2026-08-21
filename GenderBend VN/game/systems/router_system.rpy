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