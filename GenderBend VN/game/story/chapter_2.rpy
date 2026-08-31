# ============================================================
# MAIN CHAPTER 2 — AQUA-VAULTS & MILITARY STEEL
# Adjusted four-character version.
# ============================================================

label chapter_2:

    call chapter_transition(2, "Aqua-Vaults & Military Steel")

    # Scene 1: Bioluminescent Depths
    # Location: The Solarium Sanctum — Aquatic Botanical Wing
    scene bg nurse at bg_character_focus
    with fade
    # [SCENE START]
    # SFX: Sound Effect: Gentle water splashing, hum of underwater filtration wards, soft bioluminescent glow echoing off wet glass
    "(Following your checklist, you navigate down to the flooded glass arches of the Sanctum’s aquatic conservatories.)"
    "(Water tanks line the walls, shimmering with deep-sea flora.)"
    "(Near the central pool, Ellie Sylvane is struggling with a heavy iron aquatic mesh stuck beneath a submerged stone pedestal.)"
    # SFX: Sound Effect: Heavy splashing, straining metal, soft grunting
    # Source [SPRITE: Ellie — Strained, Flustered, Wet Sleeves]
    show elianna normal at elianna_size, char_center, enter_from_bottom
    elianna "Hnnrgh... Oh dear... come on, yield you stubborn iron mesh...!"
    "(Ellie has her sleeves rolled up, her pale arms wrapped around a heavy leviathan-net used to contain deep-sea specimens. The mesh is wedged tightly under a stone filter arch.)"
    # [MC]
    mc "Need a hand over there, Ellie?"
    "(Ellie glances up over her shoulder, her cheeks flushing as she takes in your transformed form and sorcerer robes.)"
    # Source [SPRITE: Ellie — Surprised, Embarrassed]
    show elianna angry at elianna_size, char_center, expression_squish
    elianna "Ah! Sorcerer! Oh goodness... I-I didn't expect anyone down here! This heavy specimen cage got snagged during the morning water siphon..."
    # [MC]
    mc "Watch me."

    menu:
        "Cast a kinetic lift spell while bracing yourself alongside her at the pool’s edge":
            "(Cast a kinetic lift spell while bracing yourself alongside her at the pool’s edge.)"
            show elianna happy at elianna_size, char_center, expression_pop
            elianna "My goodness! Look at that strength! You're much sturdier than you look in those robes!"
        "Channel a precise magic pulse directly into the snagged stone arch to shatter the obstruction":
            "(Channel a precise magic pulse directly into the snagged stone arch to shatter the obstruction.)"
            show elianna normal at elianna_size, char_center, expression_pop
            elianna "Oh! A clean kinetic pulse! That saved me hours of struggling with the levers!"
        "Use a levitation weave on the iron weights while instructing Ellie when to pull":
            "(Use a levitation weave on the iron weights while instructing Ellie when to pull.)"
            "(You weave a glowing blue harness around the sunken iron weights, lifting their mass as you call out the cadence for Ellie to hoist.)"
            show elianna happy at elianna_size, char_center, expression_pop
            elianna "Such smooth spellcraft! Working smart instead of straining—I really admire your focus!"


    # SFX: Sound Effect: Heavy net splashing onto the stone deck
    "(Ellie wipes sea-spray from her forehead, offering you a bright, relieved smile.)"
    # Source [SPRITE: Ellie — Gentle, Grateful]
    show elianna happy at elianna_size, char_center, expression_pop
    elianna "Thank you so much! Most scholars avoid getting their robes wet down here. Now, what brings you to the aquatic wing?"
    # [MC]
    mc "I'm looking for a catalyst for Tansy's reversal brew. We need a Luminescent Sea-Gland."
    # Source [SPRITE: Ellie — Smiling, Generous]
    show elianna happy_talking at elianna_size, char_center, expression_pop
    elianna "Oh, Tansy's cure! Of course! The net we just freed contained a deep-sea angler specimen."
    "(Ellie reaches into her velvet specimen pouch and pulls out a glowing, pearlescent orb that pulses with a calm, bioluminescent blue light. She presses it gently into your palm.)"
    # Source [SPRITE: Ellie — Warm, Encouraging]
    show elianna talking at elianna_size, char_center, expression_pop
    elianna "Ingredient number two: Luminescent Sea-Gland, perfectly preserved. Be careful heading out—your next stop is the Garrison armory for forge ingredients!"

    $ has_sea_gland = True
    call item_acquired("item sea_gland", "Luminescent Sea-Gland")

    # Scene 2: Forge-Fire & Dragon Steel
    hide elianna
    # Location: The Crestward Garrison — High Armory Forge (Dusk)
    scene bg furnace_pier at bg_character_focus
    with fade
    # [SCENE START]
    # SFX: Sound Effect: Heavy hammer strikes echoing, roaring forge bellows, crackling white-hot flames
    "(The Crestward Garrison armory is blazing with heat.)"
    "(Commander Domitilla Bruni stands near the central draconic blast-furnace, her dark plate armor reflecting the intense golden embers as she works a massive ingot of metal.)"
    # Source [SPRITE: Commander Bruni — Boisterous, Hammering]
    show domitilla happy at domitilla_size, char_center, enter_from_right
    domitilla "HA! Put some muscle into those bellows, recruits! Steel doesn't temper itself!"
    "(Domitilla turns her head, her sharp golden eyes catching sight of your sorcerer robes.)"
    # Source [SPRITE: Commander Bruni — Intrigued, Smirking]
    show domitilla surprised at domitilla_size, char_center, expression_squish
    domitilla "Well, well! A Sanctum scholar stepping right into my forge hall! What brings magic robes into the heat of military iron?"
    # SFX: Sound Effect: Pop of magic smoke, light laughter
    # Source [SPRITE: Tansy — Mischievous, Popping In]
    show tansy teasing at tansy_size, char_left, enter_from_left
    tansy "I brought them, Commander! We need a spark of your legendary draconic furnace to harvest Draconic Cinder-Ash! But I told my apprentice your forge fire has gotten a bit tame lately~"
    # Source [SPRITE: Commander Bruni — Booming Laugh, Fiery Eyes]
    show domitilla happy at domitilla_size, char_center, expression_pop
    domitilla "TAME?! MY FORGE FLAME?! Ha! Them's fighting words, alchemist! My hearth burns hot enough to melt dragon-scale!"
    "(Domitilla steps up to you, the intense heat radiating from her armor.)"

    menu:
        "Join in their rowdy martial banter with a bold grin":
            "(Join in their rowdy martial banter with a bold grin.)"
            mc "Don't hold back on my account, Commander! Show my mentor what real heat looks like!\" Bruni: \"BHAHA! I like this kid! You've got real garrison spirit!"
        "Use a small flame-shaping spell to dance sparks over your knuckles":
            "(Use a small flame-shaping spell to dance sparks over your knuckles.)"
            mc "Careful, Commander. If your forge slacks, I might just have to ignite the cinder-ash myself.\" Bruni: \"Oho! Showing off fire magic to a knight? Bold move, wizard! I respect it!"
        "Keep your cool and gently nudge Tansy back from the furnace blast":
            "(Keep your cool and gently nudge Tansy back from the furnace blast.)"
            mc "Tansy, stop poking the Commander. Bruni, we just need a controlled spark for the Alkahest.\" Bruni: \"Ha! Controlled? Fair enough, but where's the fun without a little show?!"

    # Source [SPRITE: Commander Bruni — Focused, Grinning]
    show domitilla talking at domitilla_size, char_center, expression_pop
    domitilla "Alright, apprentice! Hold up your enchanted collection vial! Let's see if you can hold steady when the Garrison forge unleashes true heat!"
    "(Domitilla yanks open the heavy iron blast-hatch of the main furnace.)"
    # SFX: Sound Effect: Deep rumbling heat, roaring flame ignition
    # Scene 3: Cinder & Steel
    # Location: The Crestward Garrison — Furnace Hearth
    # [SCENE START]
    "(The air in the armory turns scorchingly hot as a concentrated, brilliant stream of white-hot draconic flame rushes out from the open forge.)"
    "(The fire swaths directly toward the enchanted brass-lined flask in your hands.)"
    # SFX: Sound Effect: Roaring draconic fire, crackling magic wards
    # Source [SPRITE: Tansy — Excited, Watching Close]
    show tansy worried at tansy_size, char_left, expression_squish
    tansy "Hold it steady! Don't let the thermal shock crack the glass!"
    "(The intense heat radiates against your face, turning your cheeks flushed red. Glowing, crystalline ash begins to settle at the bottom of the flask, burning with embers of pure magic.)"

    menu:
        "Hold the vial steady without flinching.":
            "(You hold the glass dead steady right next to the blast hatch without flinching a single inch.)"
            # SFX: Sound Effect: Furnace hatch slamming shut
            # Source [SPRITE: Commander Bruni — Ceasing Flame, Deeply Impressed]
            show domitilla surprised at domitilla_size, char_center, expression_squish
            domitilla "BY THE ANCIENTS! Not a flinch! Not a single shake!"
            "(Bruni slaps her massive armored hand onto the anvil, making the iron tools jump.)"
            show domitilla happy at domitilla_size, char_center, expression_pop
            domitilla "You've got the heart of a true warrior, apprentice! Most scholars back away the second my forge glows! That Draconic Cinder-Ash in your flask is as pure as it gets!"
            # Source [SPRITE: Tansy — Raising Flask, Cheering]
            show tansy happy at tansy_size, char_left, expression_pop
            tansy "To the bravest apprentice in Mirthhaven! Two ingredients down!"
            "(You cork the glowing flask, holding two completed ingredients safely in hand.)"
            hide domitilla
            hide tansy
            call chapter_end(2, "Aqua-Vaults & Military Steel")
            $ story_progress += 1
            $ setup_free_time(2)
            jump free_time
        "Channel the ash with a heat-deflection ward.":
            "(You weave an elegant heat-deflection ward around your fingers to channel the ash cleanly.)"
            # Source [SPRITE: Tansy — Proud, Beaming]
            show tansy happy at tansy_size, char_left, expression_pop
            tansy "Flawless heat distribution! See that, Commander? That's Sanctum precision right there!"
            # Source [SPRITE: Commander Bruni — Nodding, Respectful]
            show domitilla happy at domitilla_size, char_center, expression_pop
            domitilla "Heh... slick work, kid. You handled my forge fire like a seasoned spell-smith tempering rare steel. Clean, sharp, and smart."
            "(Bruni pats your shoulder with a heavy, warm palm as you cap the shimmering flask.)"
            show domitilla talking at domitilla_size, char_center, expression_pop
            domitilla "Take that Draconic Cinder-Ash with pride. You earned it with real skill."
            $ has_cinder_ash = true
            call item_acquired("item cinder_ash", "Draconic Cinder-Ash")
            "(With your magic control praised by both your mentor and the Garrison Commander, you secure your third ingredient with complete composure.)"
            
            $ has_cinder_ash = true
            call item_acquired("item cinder_ash", "Draconic Cinder-Ash")
            hide domitilla
            hide tansy
            call chapter_end(2, "Aqua-Vaults & Military Steel")
            $ story_progress += 1
            $ setup_free_time(2)
            jump free_time
        "Tease Bruni about her furnace heat.":
            "(You laugh through the heat, teasing Bruni that her furnace feels like a cozy hearth fire.)"
            # Source [SPRITE: Commander Bruni — Thunderous Laugh, Flustered]
            show domitilla happy at domitilla_size, char_center, expression_pop
            domitilla "A HEARTH CANDLE?! BHAHAHA! Did you hear that, recruits?! This little wizard just called my draconic blast-furnace a candle!"
            # Source [SPRITE: Tansy — Grinning, Shaking Head]
            show tansy happy at tansy_size, char_left, expression_pop
            tansy "You've met your match, Commander! You can't intimidate this one!"
            # Source [SPRITE: Commander Bruni — Chuckling, Handing Over Cinder]
            domitilla "You've got some nerve, kid! I love it! Here—take your Draconic Cinder-Ash before you make fun of my anvils next!"

            $ has_cinder_ash = true
            call item_acquired("item cinder_ash", "Draconic Cinder-Ash")
            "(The armory fills with laughter as you cap the glowing vial, enjoying the lively energy of the Garrison as you prepare for the next leg of your quest.)"
            # [SCENE END]
            hide domitilla
            hide tansy
            call chapter_end(2, "Aqua-Vaults & Military Steel")
            $ story_progress += 1
            $ setup_free_time(2)
            jump free_time