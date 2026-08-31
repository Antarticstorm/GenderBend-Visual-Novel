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
    alpha 0.80

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
# OBTAINED ITEM GLOW
# ============================================================

transform item_obtained_glow:

    alpha 1.0

    linear 0.8 matrixcolor BrightnessMatrix(0.30)
    linear 0.8 matrixcolor BrightnessMatrix(0.10)

    repeat
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
    character_token,
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
        ysize 350

        background Solid(accent_color)
        padding (2, 2)

        frame:
            xfill True
            yfill True

            background Solid("#111318F5")
            padding (20, 20)

            vbox:

                if not card_available:
                    at map_card_unavailable

                xalign 0.5
                yalign 0.5
                spacing 10


                # ====================================================
                # TOKEN
                # ====================================================

                add character_token:
                    xalign 0.5
                    xsize 90
                    ysize 90


                # ====================================================
                # CHARACTER
                # ====================================================

                text character_name:
                    xalign 0.5
                    size 40
                    color accent_color

                text location_name:
                    xalign 0.5
                    size 21
                    color "#C8B99B"


                # ====================================================
                # PROGRESS
                # ====================================================

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
                                
                # ====================================================
                # CHAPTERS 1–3
                # ====================================================

                if chapter < 4:

                    if character_id in characters_visited_this_period:

                        text "VISITED":
                            xalign 0.5
                            size 25
                            color "#7FD18B"


                    elif normal_route_event_available(
                        progress,
                        unlocked,
                        locked
                    ):

                        textbutton "◆  VISIT  ◆":
                            xalign 0.5

                            at map_card_hover

                            text_color accent_color
                            text_hover_color "#FFFFFF"
                            text_size 22

                            background Solid("#322817CC")
                            hover_background Solid("#6A5124EE")

                            padding (30, 10)

                            action Jump(route_label)


                    elif locked:

                        text "LOCKED":
                            xalign 0.5
                            size 25
                            color "#777777"


                    else:

                        text "UNAVAILABLE":
                            xalign 0.5
                            size 25
                            color "#555555"


                # ====================================================
                # CHAPTER 4
                # ====================================================

                else:

                    if progress >= 4:

                        text "ROUTE COMPLETE":
                            xalign 0.5
                            size 25
                            color "#7FD18B"


                    elif route_is_committed(character_id):

                        text "COMMITTED":
                            xalign 0.5
                            size 20
                            color accent_color

                        textbutton "◆  CONTINUE ROUTE  ◆":
                            xalign 0.5

                            at map_card_hover

                            text_size 21
                            text_color accent_color
                            text_hover_color "#FFFFFF"

                            background Solid("#322817CC")
                            hover_background Solid("#6A5124EE")

                            padding (20, 8)

                            action Jump(route_label)


                    elif (
                        progress >= 1
                        and not locked
                        and can_commit_character(character_id)
                    ):

                        text "FINAL ROUTE AVAILABLE":
                            xalign 0.5
                            size 17
                            color accent_color



                        textbutton "◆  COMMIT  ◆":
                            xalign 0.5

                            at map_card_hover

                            text_color accent_color
                            text_hover_color "#FFFFFF"
                            text_size 22

                            background Solid("#322817CC")
                            hover_background Solid("#6A5124EE")

                            padding (25, 8)

                            action Jump(route_label)


                    elif progress >= 1 and not locked:

                        text "NOT CHOSEN":
                            xalign 0.5
                            size 25
                            color "#888888"


                    else:

                        text "UNAVAILABLE":
                            xalign 0.5
                            size 25
                            color "#555555"
# ============================================================
# INGREDIENT TRACKER
# ============================================================

screen ingredient_tracker():

    frame:
        xalign 0.98
        yalign 0.03

        background Solid("#111318DD")
        padding (15, 12)

        vbox:
            spacing 8

            text "ALKAHEST INGREDIENTS":
                xalign 0.5
                size 16
                color "#D7B56D"

            hbox:
                spacing 8

                # SUNSTONE POWDER
                if has_sunstone:
                    add "item sunstone":
                        xsize 50
                        ysize 50
                        at item_obtained_glow
                else:
                    add "item sunstone":
                        xsize 50
                        ysize 50
                        alpha 0.18

                # SEA-GLAND
                if has_sea_gland:
                    add "item sea_gland":
                        xsize 50
                        ysize 50
                        at item_obtained_glow
                else:
                    add "item sea_gland":
                        xsize 50
                        ysize 50
                        alpha 0.18

                # CINDER-ASH
                if has_cinder_ash:
                    add "item cinder_ash":
                        xsize 50
                        ysize 50
                        at item_obtained_glow
                else:
                    add "item cinder_ash":
                        xsize 50
                        ysize 50
                        alpha 0.18

                # MIDNIGHT LOTUS
                if has_midnight_lotus:
                    add "item midnight_lotus":
                        xsize 50
                        ysize 50
                        at item_obtained_glow
                else:
                    add "item midnight_lotus":
                        xsize 50
                        ysize 50
                        alpha 0.18

                # STEEL-CORE MARROW
                if has_steel_core:
                    add "item steel_core":
                        xsize 50
                        ysize 50
                        at item_obtained_glow
                else:
                    add "item steel_core":
                        xsize 50
                        ysize 50
                        alpha 0.18

                # SOLAR BLOOM
                if has_solar_bloom:
                    add "item solar_bloom":
                        xsize 50
                        ysize 50
                        at item_obtained_glow
                else:
                    add "item solar_bloom":
                        xsize 50
                        ysize 50
                        alpha 0.18
# ============================================================
# MIRTHHAVEN MAP
# ============================================================

screen mirthhaven_map():

    tag menu

    add "images/backgrounds/Crestward_Bastion.PNG":
        blur 15.0
        
    add Solid("#00000055")

    use ingredient_tracker

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
            "Meet up with Clara",
            clara_route_progress,
            clara_route_unlocked,
            clara_route_locked,
            "clara_route_event",
            "#E5BC68",
            "token clara",
            0.20
        )


        # =========================
        # ELIANNA
        # =========================

        use map_character_button(
            "Elianna",
            "elianna",
            "Meet up with Elianna",
            elianna_route_progress,
            elianna_route_unlocked,
            elianna_route_locked,
            "elianna_route_event",
            "#A9D8B2",
            "token elianna",
            0.30
        )


        # =========================
        # DOMITILLA
        # =========================

        use map_character_button(
            "Domitilla",
            "domitilla",
            "Meet up with Domitilla",
            domitilla_route_progress,
            domitilla_route_unlocked,
            domitilla_route_locked,
            "domitilla_route_event",
            "#D98282",
            "token domitilla",
            0.40
        )

    # ============================================================
    # TANSY — SECRET ROUTE
    # ============================================================

    if chapter >= 3 and tansy_route_offer_seen:

        frame:
            at secret_card_enter

            xalign 0.5
            ypos 700

            xsize 380
            ysize 240

            background Solid("#9C55D8")
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

                    add "token tansy":
                        xalign 0.5
                        xsize 80
                        ysize 80

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
                            color "#292929"


    # ============================================================
    # REST / CONTINUE
    # ============================================================

    if chapter < 4:

        textbutton "Spend Time Alone":
            xalign 0.5
            ypos 950

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
            ypos 950

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
