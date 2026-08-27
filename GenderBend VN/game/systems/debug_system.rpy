# ============================================================
# DEVELOPER DEBUG SYSTEM
# ============================================================

# This screen should only be used during development.


# ============================================================
# DEBUG HOTKEY
# ============================================================

screen debug_hotkey_listener():

    if config.developer:

        key "K_F8" action Show("debug_menu")


init python:

    if config.developer:

        if "debug_hotkey_listener" not in config.overlay_screens:
            config.overlay_screens.append("debug_hotkey_listener")

# ============================================================
# MAIN DEBUG MENU
# ============================================================

screen debug_menu():

    modal True
    zorder 500

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

                text "DEVELOPER DEBUG MENU":
                    size 42
                    xalign 0.5

                text "Chapter: [chapter]"

                text "Free Actions: [free_actions]"

                text "Committed Routes: [len(committed_routes)] / [max_committed_routes]"

                null height 10

                                null height 25

                text "ROUTE CONTROLS":
                    size 32


                use debug_route_controls(
                    "CLARA",
                    "clara_route_progress",
                    "clara_affection",
                    "clara_romance_locked",
                    "clara_route_locked"
                )

                null height 20


                use debug_route_controls(
                    "TARIQ",
                    "tariq_route_progress",
                    "tariq_affection",
                    "tariq_romance_locked",
                    "tariq_route_locked"
                )

                null height 20


                use debug_route_controls(
                    "BAO",
                    "bao_route_progress",
                    "bao_affection",
                    "bao_romance_locked",
                    "bao_route_locked"
                )

                null height 20


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


                use debug_route_controls(
                    "BAREK",
                    "barek_route_progress",
                    "barek_affection",
                    "barek_romance_locked",
                    "barek_route_locked"
                )

                # ============================================
                # CHAPTER CONTROLS
                # ============================================

                text "MAIN CHAPTER":
                    size 28

                hbox:

                    spacing 10

                    textbutton "Chapter 1":
                        action SetVariable("chapter", 1)

                    textbutton "Chapter 2":
                        action SetVariable("chapter", 2)

                    textbutton "Chapter 3":
                        action SetVariable("chapter", 3)

                    textbutton "Chapter 4":
                        action SetVariable("chapter", 4)


                null height 15

# ============================================================
# NORMAL ROUTE DEBUG COMPONENT
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
            size 28

        text "Progress: [getattr(store, progress_variable)] / 4"

        text "Affection: [getattr(store, affection_variable)]"

        text "Romance Locked: [getattr(store, romance_lock_variable)]"

        text "Route Locked: [getattr(store, route_lock_variable)]"


        hbox:

            spacing 8

            textbutton "P0":
                action SetVariable(
                    progress_variable,
                    0
                )

            textbutton "P1":
                action SetVariable(
                    progress_variable,
                    1
                )

            textbutton "P2":
                action SetVariable(
                    progress_variable,
                    2
                )

            textbutton "P3":
                action SetVariable(
                    progress_variable,
                    3
                )

            textbutton "P4":
                action SetVariable(
                    progress_variable,
                    4
                )


        hbox:

            spacing 8

            textbutton "+20 Aff":
                action SetVariable(
                    affection_variable,
                    getattr(store, affection_variable) + 20
                )

            textbutton "Aff = 100":
                action SetVariable(
                    affection_variable,
                    100
                )

            textbutton "Aff = 0":
                action SetVariable(
                    affection_variable,
                    0
                )

            textbutton "Toggle Romance Lock":
                action ToggleVariable(
                    romance_lock_variable
                )

            textbutton "Toggle Route Lock":
                action ToggleVariable(
                    route_lock_variable
                )
            
                            null height 25

                text "TANSY — SECRET ROUTE":
                    size 28

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
                            SetVariable(
                                "tansy_route_triggered",
                                True
                            ),

                            SetVariable(
                                "tansy_route_locked",
                                False
                            )
                        ]


                    textbutton "Ready for Ch.3":

                        action [
                            SetVariable(
                                "tansy_route_triggered",
                                True
                            ),

                            SetVariable(
                                "tansy_route_unlocked",
                                True
                            ),

                            SetVariable(
                                "tansy_route_offer_seen",
                                True
                            ),

                            SetVariable(
                                "tansy_route_progress",
                                3
                            ),

                            SetVariable(
                                "tansy_route_locked",
                                False
                            )
                        ]


                    textbutton "Ready for Ch.4":

                        action [
                            SetVariable(
                                "tansy_route_triggered",
                                True
                            ),

                            SetVariable(
                                "tansy_route_unlocked",
                                True
                            ),

                            SetVariable(
                                "tansy_route_offer_seen",
                                True
                            ),

                            SetVariable(
                                "tansy_route_progress",
                                4
                            ),

                            SetVariable(
                                "tansy_route_locked",
                                False
                            )
                        ]
                    hbox:

                        spacing 10

                        textbutton "Aff = 100":
                            action SetVariable(
                                "tansy_affection",
                                100
                            )

                        textbutton "Toggle Romance Lock":
                            action ToggleVariable(
                                "tansy_romance_locked"
                            )

                        textbutton "Toggle Route Lock":
                            action ToggleVariable(
                                "tansy_route_locked"
                            )
                                    null height 25

                text "CHAPTER 4 COMMITMENTS":
                    size 28

                text "Committed: [committed_routes]"

                textbutton "Clear Commitments":

                    action SetVariable(
                        "committed_routes",
                        []
                    )
                                hbox:

                    spacing 10

                    textbutton "Commit Clara":
                        action Function(
                            commit_character,
                            "clara"
                        )

                    textbutton "Commit Bao":
                        action Function(
                            commit_character,
                            "bao"
                        )

                    textbutton "Commit Elianna":
                        action Function(
                            commit_character,
                            "elianna"
                        )

                    textbutton "Commit Domitilla":
                        action Function(
                            commit_character,
                            "domitilla"
                        )
                                    null height 30

                text "GLOBAL DEBUG ACTIONS":
                    size 28


                hbox:

                    spacing 10


                    textbutton "Give 2 Free Actions":

                        action SetVariable(
                            "free_actions",
                            2
                        )


                    textbutton "Reset Visits":

                        action SetVariable(
                            "characters_visited_this_period",
                            []
                        )


                    textbutton "Open Free Time":

                        action [
                            SetVariable(
                                "characters_visited_this_period",
                                []
                            ),

                            Hide("debug_menu"),

                            Jump("free_time")
                        ]


                textbutton "CLOSE DEBUG MENU":

                    xalign 0.5

                    action Hide("debug_menu")