# ============================================================
# MIRTHHAVEN MAP STYLES
# ============================================================

style map_card_frame:
    background Frame(
        Solid("#111318E8"),
        2, 2
    )

style map_visit_button:
    background Solid("#2A2418CC")
    hover_background Solid("#5A4524EE")

    padding (25, 10)

style map_visit_button_text:
    color "#D8C9A7"
    hover_color "#FFE29A"

    size 20


transform map_card_unavailable:
    alpha 0.45

transform map_card_enter(delay=0.0):

    alpha 0.0
    yoffset 30

    pause delay

    easeout 0.35 alpha 1.0 yoffset 0

transform map_bottom_enter:
    alpha 0.0
    yoffset 30

    pause 0.65

    easeout 0.35 alpha 1.0 yoffset 0


transform map_bottom_hover:
    on idle:
        ease 0.12 zoom 1.0 yoffset 0

    on hover:
        ease 0.12 zoom 1.04 yoffset -5
# ============================================================
# REUSABLE MAP CHARACTER CARD
# ============================================================

screen map_character_button(
    character_name,
    character_id,
    location_name,
    progress,
    unlocked,
    locked,
    route_label,
    accent_color,
    entrance_delay=0.0
):

    $ card_available = False

    if chapter < 4:
        if (
            character_id not in characters_visited_this_period
            and normal_route_event_available(progress, unlocked, locked)
        ):
            $ card_available = True

    else:
        if progress < 4:
            if route_is_committed(character_id):
                $ card_available = True
            elif progress >= 1 and not locked and can_commit_character(character_id):
                $ card_available = True

    frame:
        at map_card_enter(entrance_delay)

        xsize 380
        ysize 250

        background Solid(accent_color)
        padding (2, 2)

        frame:

            if not card_available:
                at map_card_unavailable

            xfill True
            yfill True

            background Solid("#111318E8")

            padding (25, 20)

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 10

                text character_name:
                    xalign 0.5
                    size 40
                    color accent_color

                text location_name:
                    xalign 0.5
                    size 21
                    color "#C8B99B"

                hbox:
                    xalign 0.5
                    spacing 7

                    for i in range(4):

                        if i < progress:

                            text "◆":
                                color accent_color
                                size 18

                        else:

                            text "◇":
                                color "#555555"
                                size 18

                null height 10


            # ========================================================
            # CHAPTERS 1–3
            # ========================================================

            if chapter < 4:

                if character_id in characters_visited_this_period:

                    text "VISITED":
                        xalign 0.5
                        size 25
                        yoffset 170
                        color "#7FD18B"


                elif normal_route_event_available(
                    progress,
                    unlocked,
                    locked
                ):

                    textbutton "◆  VISIT  ◆":
                        xalign 0.5
                        yoffset 170

                        at map_card_hover

                        text_color "#D7B56D"
                        text_hover_color "#FFF0B3"
                        text_size 22

                        background Solid("#322817CC")
                        hover_background Solid("#6A5124EE")

                        padding (30, 10)

                        action Jump(route_label)


                elif locked:

                    text "LOCKED":
                        xalign 0.5
                        size 21
                        color "#777777"


                else:

                    text "UNAVAILABLE":
                        xalign 0.5
                        yoffset 170
                        size 20
                        color "#888888"


            # ========================================================
            # CHAPTER 4
            # ========================================================

            else:

                if progress >= 4:

                    text "ROUTE COMPLETE":
                        xalign 0.5
                        yoffset 170
                        size 25
                        color "#7FD18B"


                elif route_is_committed(character_id):

                    text "COMMITTED":
                        xalign 0.5
                        size 25
                        color "#D7B56D"

                    textbutton "CONTINUE ROUTE":
                        xalign 0.5
                        yoffset 170
                        text_size 25

                        text_color "#D7B56D"
                        text_hover_color "#FFF0B3"

                        background Solid("#322817CC")
                        hover_background Solid("#6A5124EE")

                        padding (10, 8)

                        action Jump(route_label)


                elif (
                    progress >= 1
                    and not locked
                    and can_commit_character(character_id)
                ):

                    text "FINAL ROUTE AVAILABLE":
                        xalign 0.5
                        size 20
                        color "#D7B56D"

                        at route_available_glow

                    textbutton "◆  COMMIT  ◆":
                        xalign 0.5
                        yoffset 170

                        at map_card_hover
                        
                        text_color "#D7B56D"
                        text_hover_color "#FFF0B3"
                        text_size 22

                        background Solid("#322817CC")
                        hover_background Solid("#6A5124EE")

                        padding (25, 8)

                        action Jump(route_label)


                elif progress >= 1 and not locked:

                    text "NOT CHOSEN":
                        xalign 0.5
                        yoffset 170
                        size 25
                        color "#888888"

                else:

                    text "UNAVAILABLE":
                        xalign 0.5
                        yoffset 170
                        size 25
                        color "#888888"
                        
# ============================================================
# MIRTHHAVEN MAP
# ============================================================

screen mirthhaven_map():

    tag menu

    add "images/backgrounds/Market.PNG":
        blur 15.0
        
    add Solid("#00000055")

# ============================================================
# HEADER
# ============================================================

    frame:

        at map_header_enter

        xalign 0.5
        ypos 30

        xsize 580

        background Solid("#0A0A0AEE")
        padding (35, 18)

        vbox:
            xalign 0.5
            spacing 6

            # =========================
            # TITLE
            # =========================

            text "M I R T H H A V E N":
                xalign 0.5
                size 38
                color "#F4E8D0"

            # Gold separator
            text "━━━━━━━━━━━━━━━━━━━━━━━━":
                xalign 0.5
                size 15
                color "#8A713E"

                at map_card_enter(0.15)
            # =========================
            # CHAPTERS 1–3
            # =========================

            if chapter < 4:

                text "FREE TIME — CHAPTER [chapter]":
                    xalign 0.5
                    size 22
                    color "#D7B56D"

                text "Choose who you want to spend time with":
                    xalign 0.5
                    size 17
                    color "#CCCCCC"

                text "Interactions Remaining: [free_actions]":
                    xalign 0.5
                    size 19
                    color "#F4E8D0"


            # =========================
            # CHAPTER 4
            # =========================

            else:

                text "FINAL FREE TIME":
                    xalign 0.5
                    size 23
                    color "#D7B56D"

                text "Choose who you want to spend your remaining time with":
                    xalign 0.5
                    size 17
                    color "#CCCCCC"

                text "ROUTES COMMITTED  ◆  [len(committed_routes)] / [max_committed_routes]":
                    xalign 0.5
                    size 19
                    color "#F4E8D0"

# ============================================================
# NORMAL CHARACTER ROUTES
# ============================================================

    hbox:
        xalign 0.5
        ypos 320
        spacing 50

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
            "#E5BC68",
            0.20
        )


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
            "#A9D8B2",
            0.30
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
            "#D98282",
            0.40
        )

    # ============================================================
    # TANSY — SECRET ROUTE
    # ============================================================

    if tansy_route_triggered or tansy_route_unlocked or tansy_route_progress > 0:

        frame:
            at secret_card_enter

            xalign 0.5
            ypos 585

            xsize 400
            ysize 170

            background Solid("#35144DEE")
            padding (2, 2)

            frame:
                xfill True
                yfill True

                background Solid("#25142FEE")
                padding (25, 18)

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 8

                    text "✦ SECRET ROUTE ✦":
                        xalign 0.5
                        size 20
                        color "#D9A7FF"

                    text "Tansy":
                        xalign 0.5
                        size 30
                        color "#E5BCFF"

                    if tansy_route_progress >= 4:

                        text "ROUTE COMPLETE":
                            xalign 0.5
                            size 25
                            color "#7FD18B"

                    elif tansy_event_available():

                        textbutton "◆  VISIT  ◆":
                            xalign 0.5

                            text_size 20
                            text_color "#D9A7FF"
                            text_hover_color "#FFFFFF"

                            background Solid("#3A1D4FCC")
                            hover_background Solid("#6E3691EE")

                            padding (25, 7)

                            action Jump("tansy_route_event")

                    else:

                        text "UNAVAILABLE":
                            xalign 0.5
                            size 20
                            color "#888888"


    # ============================================================
    # REST / CONTINUE
    # ============================================================

    if chapter < 4:

        textbutton "Spend Time Alone":
            xalign 0.5
            ypos 900

            at map_bottom_enter, map_bottom_hover

            text_size 35
            text_color "#D7B56D"
            text_hover_color "#FFF0B3"

            background Solid("#322817CC")
            hover_background Solid("#6A5124EE")

            padding (20, 8)

            action Jump("pass_time")


    elif chapter == 4:

        textbutton "Continue Main Story":
            xalign 0.5
            ypos 900

            at map_bottom_enter, map_bottom_hover

            text_size 35
            text_color "#D7B56D"
            text_hover_color "#FFF0B3"

            background Solid("#322817CC")
            hover_background Solid("#6A5124EE")

            padding (20, 8)

            action Jump("finish_chapter_4_free_time")




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
    # REST
    # =========================
