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

label tansy_route_offer:

    $ tansy_route_offer_seen = True

    "A special opportunity has become available."

    "Tansy appears to have some free time at the Solarium Sanctum."

    menu:

        "Spend time with Tansy.":
            $ tansy_route_unlocked = True

            jump tansy_route_start


        "Ignore the opportunity.":
            $ tansy_route_locked = True

            "You decide not to pursue the opportunity."

            jump free_time