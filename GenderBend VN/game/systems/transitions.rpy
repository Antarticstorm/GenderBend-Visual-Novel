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