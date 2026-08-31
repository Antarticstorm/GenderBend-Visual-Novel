screen chapter_title(number, title):

    add Solid("#000")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        text "CHAPTER [number]":
            xalign 0.5
            size 40

        text title:
            xalign 0.5
            size 60
label chapter_transition(number, title):

    scene black
    with fade

    show screen chapter_title(number, title)

    $ renpy.pause(2.5, hard=True)

    hide screen chapter_title
    with fade

    return

# ============================================================
# CHARACTER ROUTE TITLE
# ============================================================

screen route_title(character_name, route_number, route_title):

    add Solid("#000")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 15

        text character_name.upper():
            xalign 0.5
            size 55

        text "ROUTE — CHAPTER [route_number]":
            xalign 0.5
            size 30

        text route_title:
            xalign 0.5
            size 42

label route_transition(character_name, route_number, route_title):

    scene black
    with fade

    show screen route_title(
        character_name,
        route_number,
        route_title
    )

    $ renpy.pause(2.0, hard=True)

    hide screen route_title
    with fade

    return

# ============================================================
# CHARACTER ROUTE ENDING
# ============================================================

screen route_end(character_name):

    add Solid("#000")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 15

        text character_name.upper():
            xalign 0.5
            size 45

        text "Free Time Event Complete":
            xalign 0.5
            size 30

label route_end_transition(character_name):

    scene black
    with fade

    show screen route_end(character_name)

    $ renpy.pause(1.5, hard=True)

    hide screen route_end
    with fade

    return

screen chapter_end_card(number, title):

    add Solid("#000")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        text "CHAPTER [number] COMPLETE":
            xalign 0.5
            size 38

        text title:
            xalign 0.5
            size 54

        null height 20

        text "MIRTHHAVEN":
            xalign 0.5
            size 24

label chapter_end(number, title):

scene black
with fade

show screen chapter_end_card(number, title)

$ renpy.pause(3.0, hard=True)

hide screen chapter_end_card
with fade

return

# ============================================================
# MAP CARD ANIMATIONS
# ============================================================

transform map_card_available:
    alpha 1.0
    zoom 1.0


transform map_card_unavailable:
    alpha 0.55
    zoom 1.0


transform map_card_hover:
    on idle:
        ease 0.15 zoom 1.0 yoffset 0

    on hover:
        ease 0.15 zoom 1.025 yoffset -8

# Header enters from above.
transform map_header_enter:
    alpha 0.0
    yoffset -25

    pause 0.05

    easeout 0.35 alpha 1.0 yoffset 0


# Normal route cards appear one after another.
transform map_card_enter(delay=0.0):
    alpha 0.0
    yoffset 25
    zoom 0.97

    pause delay

    easeout 0.30 alpha 1.0 yoffset 0 zoom 1.0


# Tansy appears separately from below.
transform secret_card_enter:
    alpha 0.0
    yoffset 25
    zoom 0.95

    pause 0.45

    easeout 0.35 alpha 1.0 yoffset 0 zoom 1.0


# Dim cards that cannot currently be selected.
transform map_card_unavailable:
    alpha 0.48


# Subtle pulse for an important available route.
transform route_available_glow:
    alpha 1.0

    linear 1.1 alpha 0.82
    linear 1.1 alpha 1.0

    repeat

# ============================================================
# END CREDITS
# ============================================================

screen end_credits():

    add Solid("#000")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 14

        text "MIRTHHAVEN":
            xalign 0.5
            size 52
            color "#F4E8D0"

        text "━━━━━━━━━━━━━━━━━━━━":
            xalign 0.5
            size 16
            color "#8A713E"

        null height 15


        text "GAME JAM LEADER":
            xalign 0.5
            size 20
            color "#D7B56D"

        text "Marby Blum":
            xalign 0.5
            size 26


        null height 10


        text "CHARACTER ARTISTS":
            xalign 0.5
            size 20
            color "#D7B56D"

        text "Marby Blum  •  Evening":
            xalign 0.5
            size 26


        null height 10


        text "BACKGROUND ARTIST":
            xalign 0.5
            size 20
            color "#D7B56D"

        text "Ashy":
            xalign 0.5
            size 26


        null height 10


        text "WRITER":
            xalign 0.5
            size 20
            color "#D7B56D"

        text "Yubelier":
            xalign 0.5
            size 26


        null height 10


        text "PROGRAMMER":
            xalign 0.5
            size 20
            color "#D7B56D"

        text "Arctix":
            xalign 0.5
            size 26