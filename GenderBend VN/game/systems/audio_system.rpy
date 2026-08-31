# ============================================================
# AUDIO SYSTEM
# ============================================================
init python:
    renpy.music.register_channel(
        "ambient",
        mixer="sfx",
        loop=True
    )