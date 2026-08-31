# ============================================================
# ITEM ACQUIRED SYSTEM
# ============================================================

transform item_acquire_pop:
    alpha 0.0
    zoom 0.75

    easeout 0.25 alpha 1.0 zoom 1.05
    easein 0.12 zoom 1.0

# ============================================================
# ITEM ACQUIRED SCREEN
# ============================================================

screen item_acquired(item_image, item_name):

    modal True

    add Solid("#00000088")

    frame:
        xalign 0.5
        yalign 0.5

        xsize 500
        ysize 500

        background Solid("#111318EE")
        padding (30, 25)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            text "◆ ITEM ACQUIRED ◆":
                xalign 0.5
                size 26
                color "#D7B56D"

            # ITEM IMAGE + POP ANIMATION
            add item_image:
                xalign 0.5
                xsize 250
                ysize 250
                at item_acquire_pop

            text item_name:
                xalign 0.5
                size 32
                color "#F4E8D0"

            textbutton "CONTINUE":
                xalign 0.5
                action Return()

# ============================================================
# ITEM 
# ============================================================

screen ingredient_tracker():

    frame:
        xalign 0.98
        yalign 0.03

        background Solid("#111318DD")
        padding (12, 10)

        vbox:
            spacing 5

            text "INGREDIENTS":
                xalign 0.5
                size 16
                color "#D7B56D"

            hbox:
                spacing 6

                if has_sunstone:
                    add "item sunstone":
                        xsize 45
                        ysize 45
                else:
                    text "?":
                        xsize 45
                        ysize 45
                        xalign 0.5
                        yalign 0.5

                if has_sea_gland:
                    add "item sea_gland":
                        xsize 45
                        ysize 45
                else:
                    text "?":
                        xsize 45
                        ysize 45

                if has_cinder_ash:
                    add "item cinder_ash":
                        xsize 45
                        ysize 45
                else:
                    text "?":
                        xsize 45
                        ysize 45

                if has_midnight_lotus:
                    add "item midnight_lotus":
                        xsize 45
                        ysize 45
                else:
                    text "?":
                        xsize 45
                        ysize 45

                if has_steel_core:
                    add "item steel_core":
                        xsize 45
                        ysize 45
                else:
                    text "?":
                        xsize 45
                        ysize 45

                if has_solar_bloom:
                    add "item solar_bloom":
                        xsize 45
                        ysize 45
                else:
                    text "?":
                        xsize 45
                        ysize 45

# ============================================================
# ITEM ACQUIRED HELPER
# ============================================================

label item_acquired(item_image, item_name):

    call screen item_acquired(item_image, item_name)

    return