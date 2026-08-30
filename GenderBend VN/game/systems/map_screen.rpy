# ============================================================
# REUSABLE MAP-CHARACTER COMPONENT
# ============================================================
screen map_character_button(
    character_name,
    character_id,
    location_name,
    progress,
    unlocked,
    locked,
    route_label,
    xpos_value,
    ypos_value
):

    # ========================================================
    # CHAPTERS 1-3
    # ========================================================

    if chapter < 4:

        # Already interacted during this free-time period.
        if character_id in characters_visited_this_period:

            textbutton "[character_name]\n✓ Visited":
                xpos xpos_value
                ypos ypos_value
                sensitive False


        # Character has an event available.
        elif normal_route_event_available(
            progress,
            unlocked,
            locked
        ):

            textbutton "[character_name]\n[location_name]":
                xpos xpos_value
                ypos ypos_value
                action Jump(route_label)


    # ========================================================
    # CHAPTER 4 — FINAL COMMITMENT
    # ========================================================

    elif chapter == 4:

        # --------------------------------
        # ROUTE ALREADY COMPLETED
        # --------------------------------

        if progress >= 4:

            textbutton "[character_name]\n✓ Route Complete":
                xpos xpos_value
                ypos ypos_value
                sensitive False


        # --------------------------------
        # ALREADY COMMITTED
        # --------------------------------

        elif route_is_committed(character_id):

            textbutton "[character_name]\n♥ Committed":
                xpos xpos_value
                ypos ypos_value
                action Jump(route_label)


        # --------------------------------
        # ELIGIBLE FOR COMMITMENT
        # --------------------------------

        elif (
            progress >= 1
            and not locked
            and can_commit_character(character_id)
        ):

            textbutton "[character_name]\nFinal Route Available":
                xpos xpos_value
                ypos ypos_value
                action Jump(route_label)


        # --------------------------------
        # INVESTED, BUT COMMITMENT FULL
        # --------------------------------

        elif progress >= 1 and not locked:

            textbutton "[character_name]\n🔒 Not Chosen":
                xpos xpos_value
                ypos ypos_value
                sensitive False

# ============================================================
# MIRTHHAVEN MAP
# ============================================================

screen mirthhaven_map():

    tag menu

    # Temporary background.
    # Replace this later with:
    # add "images/map/mirthhaven_map.webp"

    add Solid("#18202a")


    # =========================
    # HEADER
    # =========================

    frame:
        xalign 0.5
        ypos 25

        padding (35, 15)

        vbox:
            spacing 5

            text "MIRTHHAVEN":
                xalign 0.5
                size 42

            text "Free Time — Chapter [chapter]":
                xalign 0.5
                size 24

            if chapter < 4:

                text "Interactions Remaining: [free_actions]":
                    xalign 0.5
                    size 22

            else:

                text "Final Free Time — Choose who you want to spend your remaining time with":
                    xalign 0.5
                    size 20

                text "Committed Routes: [len(committed_routes)] / [max_committed_routes]":
                    xalign 0.5
                    size 22


    # =========================
    # CLARA
    # =========================

    use map_character_button(
        "Clara",
        "clara",
        "Wanderlust Wheel",
        clara_route_progress,
        clara_route_unlocked,
        clara_route_locked,
        "clara_route_event",
        120,
        260
    )


    # =========================
    # TARIQ
    # =========================

    # use map_character_button(
    #     "Tariq",
    #     "tariq",
    #     "Sun-Gilded Market",
    #     tariq_route_progress,
    #     tariq_route_unlocked,
    #     tariq_route_locked,
    #     "tariq_route_event",
    #     520,
    #     240
    # )


    # =========================
    # BAO
    # =========================

    # use map_character_button(
    #     "Bao",
    #     "bao",
    #     "The Laughing Anchor",
    #     bao_route_progress,
    #     bao_route_unlocked,
    #     bao_route_locked,
    #     "bao_route_event",
    #     950,
    #     280
    # )


    # =========================
    # ELIANNA
    # =========================

    use map_character_button(
        "Elianna",
        "elianna",
        "Solarium Sanctum",
        elianna_route_progress,
        elianna_route_unlocked,
        elianna_route_locked,
        "elianna_route_event",
        300,
        520
    )


    # =========================
    # DOMITILLA
    # =========================

    use map_character_button(
        "Domitilla",
        "domitilla",
        "Crestward Bastion",
        domitilla_route_progress,
        domitilla_route_unlocked,
        domitilla_route_locked,
        "domitilla_route_event",
        720,
        520
    )


    # =========================
    # BAREK
    # =========================

    # use map_character_button(
    #     "Barek",
    #     "barek",
    #     "Nautilus Point",
    #     barek_route_progress,
    #     barek_route_unlocked,
    #     barek_route_locked,
    #     "barek_route_event",
    #     1100,
    #     520
    # )
    # =========================
    # TANSY
    # Secret Route
    # =========================

    if tansy_event_available() and can_visit_character("tansy"):

        textbutton "Tansy\nAlchemy Wing":

            xpos 300
            ypos 700

            action Jump("tansy_route_event")


    # =========================
    # REST
    # =========================

    if chapter < 4:

        textbutton "Spend Time Alone":

            xalign 0.5
            ypos 900

            action Jump("pass_time")


    elif chapter == 4:

        textbutton "Continue Main Story":

            xalign 0.5
            ypos 900

            action Jump("finish_chapter_4_free_time")