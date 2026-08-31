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