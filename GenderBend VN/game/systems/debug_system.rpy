# ============================================================
# DEVELOPER DEBUG SYSTEM
# ============================================================
# Development-only route/state testing tools.
# Press F8 while config.developer is enabled.
# ============================================================


# ============================================================
# DEBUG HOTKEY
# ============================================================

screen debug_hotkey_listener():

    if config.developer:
        key "K_F8" action ToggleScreen("debug_menu")
        


init python:

    if config.developer:
        if "debug_hotkey_listener" not in config.overlay_screens:
            config.overlay_screens.append("debug_hotkey_listener")


# ============================================================
# REUSABLE NORMAL ROUTE CONTROLS
# ============================================================

screen debug_route_controls(
    character_name,
    progress_variable,
    affection_variable,
    romance_lock_variable,
    route_lock_variable
):

    vbox:
        spacing 8

        text "[character_name]":
            size 25

        text "Progress: [getattr(store, progress_variable)] / 4"
        text "Affection: [getattr(store, affection_variable)]"
        text "Romance Locked: [getattr(store, romance_lock_variable)]"
        text "Route Locked: [getattr(store, route_lock_variable)]"

        hbox:
            spacing 8

            textbutton "P0":
                action SetVariable(progress_variable, 0)

            textbutton "P1":
                action SetVariable(progress_variable, 1)

            textbutton "P2":
                action SetVariable(progress_variable, 2)

            textbutton "P3":
                action SetVariable(progress_variable, 3)

            textbutton "P4":
                action SetVariable(progress_variable, 4)

        hbox:
            spacing 8

            textbutton "+20 Aff":
                action SetVariable(
                    affection_variable,
                    getattr(store, affection_variable) + 20
                )

            textbutton "Aff = 100":
                action SetVariable(affection_variable, 100)

            textbutton "Aff = 0":
                action SetVariable(affection_variable, 0)

            textbutton "Toggle Romance Lock":
                action ToggleVariable(romance_lock_variable)

            textbutton "Toggle Route Lock":
                action ToggleVariable(route_lock_variable)


# ============================================================
# MAIN DEBUG MENU
# ============================================================

screen debug_menu():

    modal True
    zorder 500

    key "K_F8" action Hide("debug_menu")

    add Solid("#000000E8")

    frame:
        xalign 0.5
        yalign 0.5

        xsize 1200
        ysize 900

        padding (40, 30)

        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                spacing 20

                # ====================================================
                # HEADER
                # ====================================================

                text "DEVELOPER DEBUG MENU":
                    size 38
                    xalign 0.5

                text "Chapter: [chapter]"
                text "Free Actions: [free_actions]"
                text "Committed Routes: [len(committed_routes)] / [max_committed_routes]"

                null height 10


                # ====================================================
                # MAIN CHAPTER
                # ====================================================

                text "JUMP TO MAIN CHAPTER":
                    size 25

                hbox:
                    spacing 10

                    textbutton "Chapter 1":
                        action [
                            Hide("debug_menu"),
                            Jump("chapter_1")
                        ]

                    textbutton "Chapter 2":
                        action [
                            Hide("debug_menu"),
                            Jump("chapter_2")
                        ]

                    textbutton "Chapter 3":
                        action [
                            Hide("debug_menu"),
                            Jump("chapter_3")
                        ]

                    textbutton "Chapter 4":
                        action [
                            Hide("debug_menu"),
                            Jump("chapter_4")
                        ]

                    textbutton "Chapter 5":
                        action [
                            Hide("debug_menu"),
                            Jump("chapter_5")
                        ]

                    # ====================================================
                    # SET CHAPTER STATE WITHOUT JUMPING
                    # ====================================================

                    null height 10

                    text "SET CHAPTER STATE ONLY":
                        size 22

                    hbox:
                        spacing 10

                        textbutton "1":
                            action SetVariable("chapter", 1)

                        textbutton "2":
                            action SetVariable("chapter", 2)

                        textbutton "3":
                            action SetVariable("chapter", 3)

                        textbutton "4":
                            action SetVariable("chapter", 4)

                    null height 15


                # ====================================================
                # NORMAL ROUTES
                # ====================================================

                text "ROUTE CONTROLS":
                    size 30


                use debug_route_controls(
                    "CLARA",
                    "clara_route_progress",
                    "clara_affection",
                    "clara_romance_locked",
                    "clara_route_locked"
                )

                null height 20


                # use debug_route_controls(
                #     "TARIQ",
                #     "tariq_route_progress",
                #     "tariq_affection",
                #     "tariq_romance_locked",
                #     "tariq_route_locked"
                # )

                # null height 20


                # use debug_route_controls(
                #     "BAO",
                #     "bao_route_progress",
                #     "bao_affection",
                #     "bao_romance_locked",
                #     "bao_route_locked"
                # )

                #null height 20


                use debug_route_controls(
                    "ELIANNA",
                    "elianna_route_progress",
                    "elianna_affection",
                    "elianna_romance_locked",
                    "elianna_route_locked"
                )

                null height 20


                use debug_route_controls(
                    "DOMITILLA",
                    "domitilla_route_progress",
                    "domitilla_affection",
                    "domitilla_romance_locked",
                    "domitilla_route_locked"
                )

                null height 20


                # use debug_route_controls(
                #     "BAREK",
                #     "barek_route_progress",
                #     "barek_affection",
                #     "barek_romance_locked",
                #     "barek_route_locked"
                # )

                # null height 25


                # ====================================================
                # TANSY SECRET ROUTE
                # ====================================================

                text "TANSY — SECRET ROUTE":
                    size 30

                text "Progress: [tansy_route_progress]"
                text "Affection: [tansy_affection]"
                text "Triggered: [tansy_route_triggered]"
                text "Offer Seen: [tansy_route_offer_seen]"
                text "Unlocked: [tansy_route_unlocked]"
                text "Romance Locked: [tansy_romance_locked]"
                text "Route Locked: [tansy_route_locked]"

                hbox:
                    spacing 10

                    textbutton "Trigger Route":
                        action [
                            SetVariable("tansy_route_triggered", True),
                            SetVariable("tansy_route_locked", False)
                        ]

                    textbutton "Ready for Ch.3":
                        action [
                            SetVariable("tansy_route_triggered", True),
                            SetVariable("tansy_route_unlocked", True),
                            SetVariable("tansy_route_offer_seen", True),
                            SetVariable("tansy_route_progress", 3),
                            SetVariable("tansy_route_locked", False)
                        ]

                    textbutton "Ready for Ch.4":
                        action [
                            SetVariable("tansy_route_triggered", True),
                            SetVariable("tansy_route_unlocked", True),
                            SetVariable("tansy_route_offer_seen", True),
                            SetVariable("tansy_route_progress", 4),
                            SetVariable("tansy_route_locked", False)
                        ]

                hbox:
                    spacing 10

                    textbutton "Aff = 100":
                        action SetVariable("tansy_affection", 100)

                    textbutton "Aff = 0":
                        action SetVariable("tansy_affection", 0)

                    textbutton "Toggle Romance Lock":
                        action ToggleVariable("tansy_romance_locked")

                    textbutton "Toggle Route Lock":
                        action ToggleVariable("tansy_route_locked")

                null height 25


                # ====================================================
                # CHAPTER 4 COMMITMENTS
                # ====================================================

                text "CHAPTER 4 COMMITMENTS":
                    size 30

                text "Committed: [committed_routes]"
                text "Slots: [len(committed_routes)] / [max_committed_routes]"

                textbutton "Clear Commitments":
                    action SetVariable("committed_routes", [])

                hbox:
                    spacing 8

                    textbutton "Clara":
                        action Function(commit_character, "clara")

                    # textbutton "Tariq":
                    #     action Function(commit_character, "tariq")

                    # textbutton "Bao":
                    #     action Function(commit_character, "bao")

                    textbutton "Elianna":
                        action Function(commit_character, "elianna")

                hbox:
                    spacing 8

                    textbutton "Domitilla":
                        action Function(commit_character, "domitilla")

                    # textbutton "Barek":
                    #     action Function(commit_character, "barek")

                    textbutton "Tansy":
                        action Function(commit_character, "tansy")

                null height 25


                # ====================================================
                # GLOBAL DEBUG ACTIONS
                # ====================================================

                text "GLOBAL DEBUG ACTIONS":
                    size 30

                hbox:
                    spacing 10

                    textbutton "Give 2 Free Actions":
                        action SetVariable("free_actions", 2)

                    textbutton "Reset Visits":
                        action SetVariable(
                            "characters_visited_this_period",
                            []
                        )

                    textbutton "Clear Commitments":
                        action SetVariable(
                            "committed_routes",
                            []
                        )

                hbox:
                    spacing 10

                    textbutton "Open Free Time":
                        action [
                            SetVariable(
                                "characters_visited_this_period",
                                []
                            ),
                            Hide("debug_menu"),
                            Jump("free_time")
                        ]

                    textbutton "Close Debug Menu":
                        action Hide("debug_menu")
