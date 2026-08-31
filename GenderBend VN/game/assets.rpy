# =========================
# BACKGROUND ASSETS
# =========================

image bg crestward_bastion = "images/backgrounds/Crestward_Bastion.PNG"
image bg iron_ring = "images/backgrounds/Iron_Ring.PNG"
image bg laughing_anchor = "images/backgrounds/Laughing_Anchor.PNG"
image bg market = "images/backgrounds/Market.PNG"
image bg nautilus_point = "images/backgrounds/Nautilus_Point.PNG"
image bg solarium_sanctum = "images/backgrounds/Solarium_Sanctum.PNG"
image bg furnace_pier = "images/backgrounds/The_Furnace_Pier.PNG"
image bg nurse = "images/backgrounds/Nurse_Office.PNG"

# =========================
# ITEM ASSETS
# =========================
image item sunstone = "images/items/sunstone_powder.png"
image item sea_gland = "images/items/sea_gland.png"
image item cinder_ash = "images/items/cinder_ash.png"
image item midnight_lotus = "images/items/midnight_lotus.png"
image item steel_core = "images/items/steel_core_marrow.png"
image item solar_bloom = "images/items/solar_bloom_essence.png"

# ============================================================
# BACKGROUND PRESENTATION
# ============================================================

transform bg_normal:
    blur 1.0

transform bg_character_focus:
    blur 8.0
    matrixcolor BrightnessMatrix(-0.10)

# =========================
# CHARACTER ASSETS
# =========================

# ============================================================
# TANSY
# ============================================================

image tansy normal = "images/characters/tansy/idle.png"

image tansy happy = "images/characters/tansy/laugh.png"

image tansy frown = "images/characters/tansy/sad.png"

image tansy surprised = "images/characters/tansy/surprised.png"

image tansy confused = "images/characters/tansy/surprised_alt.png"

image tansy worried = "images/characters/tansy/worry.png"

image tansy teasing = "images/characters/tansy/tease.png"

image tansy talking = "images/characters/tansy/talk.png"
# ============================================================
# CLARA VANE
# ============================================================

image clara normal:
    "images/characters/clara/idle.png"
    zoom 0.37

image clara happy:
    "images/characters/clara/laugh.png"
    zoom 0.37

image clara sad:
    "images/characters/clara/sad.png"
    zoom 0.37

image clara surprised:
    "images/characters/clara/surprised.png"
    zoom 0.37

image clara talking:
    "images/characters/clara/talk.png"
    zoom 0.37

image clara teasing:
    "images/characters/clara/tease1.png"
    zoom 0.37

image clara flirty:
    "images/characters/clara/tease2.png"
    zoom 0.37

# ============================================================
# DOMITILLA
# ============================================================

image domitilla normal = "images/characters/domitilla/idle.png"

image domitilla happy = "images/characters/domitilla/smile.png"

image domitilla angry = "images/characters/domitilla/angry.png"

image domitilla surprised = "images/characters/domitilla/surprised.png"

image domitilla talking = "images/characters/domitilla/talk.png"

image domitilla happy_talking = "images/characters/domitilla/happy_talk.png"


# ============================================================
# ELIANNA
# ============================================================

image elianna normal = "images/characters/elianna/idle.png"

image elianna happy = "images/characters/elianna/smile.png"

image elianna laughing = "images/characters/elianna/laugh.png"

image elianna sad = "images/characters/elianna/sad_talk.png"

image elianna angry = "images/characters/elianna/angry.png"

image elianna talking = "images/characters/elianna/talk.png"

image elianna happy_talking = "images/characters/elianna/smile_talk.png"

image elianna smug = "images/characters/elianna/smug1.png"

image elianna very_smug = "images/characters/elianna/smug2.png"


# ============================================================
# MAP CHARACTER TOKENS
# ============================================================

image token clara = "images/ui/tokens/Clara_Token.png"
image token elianna = "images/ui/tokens/Ellie_Token.png"
image token domitilla = "images/ui/tokens/Domitilla_Token.png"
image token tansy = "images/ui/tokens/Tansy_Token.png"

# ============================================================
# CHARACTER POSITIONS
# ============================================================

transform char_left:
    xanchor 0.5
    xpos 0.18
    yalign 1.0

transform char_center:
    xanchor 0.5
    xpos 0.50
    yalign 1.0

transform char_right:
    xanchor 0.5
    xpos 0.82
    yalign 1.0

transform char_far_left:
    xanchor 0.5
    xpos 0.12
    yalign 1.0

transform char_mid_left:
    xanchor 0.5
    xpos 0.37
    yalign 1.0

transform char_mid_right:
    xanchor 0.5
    xpos 0.63
    yalign 1.0

transform char_far_right:
    xanchor 0.5
    xpos 0.88
    yalign 1.0
# ============================================================
# CHARACTER SIZES
# ============================================================

transform tansy_size:
    zoom 0.42

transform elianna_size:
    zoom 0.16

transform domitilla_size:
    zoom 0.28

# ============================================================
# CHARACTER ENTRANCE ANIMATIONS
# ============================================================

transform enter_from_left:
    xoffset -300
    alpha 0.0

    easeout 0.35 xoffset 0 alpha 1.0

transform enter_from_right:
    xoffset 300
    alpha 0.0

    easeout 0.35 xoffset 0 alpha 1.0

transform enter_from_bottom:
    yoffset 300
    alpha 0.0

    easeout 0.45 yoffset 0 alpha 1.0

transform expression_pop:
    yoffset 0

    easeout 0.06 yoffset -18
    easein 0.10 yoffset 0


transform expression_squish:
    yoffset 0

    linear 0.05 yoffset 8
    linear 0.07 yoffset -10
    easeout 0.10 yoffset 0