# ============================================================
# MAIN CHAPTER 4 — THE DOUBLE-WITCH LAB PANIC
# Adjusted four-character version.
# ============================================================

label chapter_4:

    call chapter_transition(4, "The Double-Witch Lab Panic")

    show elianna angry at elianna_size, char_left
    show tansy teasing at tansy_size, char_right
    # Scene 1: Sparks & Tripping Hazards
    # Location: The Solarium Sanctum — Sunlit Wards (Infirmary & Botanical Annex)
    # [SCENE START]
    # SFX: Sound Effect: Distant glass shattering, bubbling liquid hiss, frantic scurrying footsteps, smoke alarms chiming softly
    "(You hurry down the arched white corridors of the Sunlit Wards, carrying the five rare ingredients secured from across Mirthhaven.)"
    "(As you push open the double oak doors to the infirmary annex, a cloud of pink and neon-green smoke billows past your face, smelling intensely of peppermint and sulfur.)"
    # Source [SPRITE: Ellie — Panicked, Flustered, Apron Smoldering]
    show elianna angry
    elianna "Eeeeek! No, no, no! Please don't explode! Oh dear, where is the neutralizing agent?!"
    "(Through the haze, you see Ellie scrambling across the polished marble floor.)"
    "(A heavy brass rack holding dozens of volatile restorative potions has tipped over onto an enchanted heating brazier.)"
    "(To make matters exponentially worse, Tansy is standing right beside her, arms raised, enthusiastically waving her wooden wand.)"
    # Source [SPRITE: Tansy — Excited, Carefree, Smirking]
    show tansy teasing
    tansy "Don't worry, Ellie! A quick little Ignis-Expellior spell will burn off the excess vapor! Stand back!"
    # Source [SPRITE: Ellie — Terrified, Waving Hands]
    show elianna talking
    elianna "WAIT! TANSY, NO! THAT'S NITRATE-BASED—"
    # SFX: Sound Effect: LOUD ARCANA FIZZING! Sparks shooting toward ceiling, bubbling froth expanding rapidly
    # [MC]
    mc "TANSY, STOP CASTING!"

    menu:
        "Take command of the situation.":
            "(Bark authoritative orders to establish immediate command over both witches)"
            mc "Ellie, grab the damp leather blankets! Tansy, lower your wand and don't touch another rune!\" Tansy: \"Ooh! Look at my apprentice taking charge! So authoritative!\" Ellie: \"Y-Yes! Right away!"
        "Pull Ellie out of the line of fire.":
            "(Physically dash forward and pull Ellie out of the line of fire)"
            "(You spring across the room, wrapping your arm around Ellie’s waist and pulling her clear just as a splash of boiling green foam hits the tile where she stood.)"
            show elianna happy
            elianna "Ah! S-Sorcerer! Oh goodness... thank you! My apron almost caught fire!"
        "Stop Tansy's spellcasting.":
            "(Grasp Tansy's raised wrist to forcefully cut off her spell focus)"
            "(You grab Tansy's hand mid-incantation, redirecting her wand tip safely toward the stone hearth.)"
            show tansy teasing
            tansy "Party pooper! I had that totally under control... mostly! Well, 40% under control!"

    # SFX: Sound Effect: Potion froth growing larger, deep rumbling arcana reaction
    # Source [SPRITE: Ellie — Distressed, Trembling]
    show elianna angry
    elianna "If those spilling potions reach the greenhouse bed, they'll destroy the Solar Bloom garden! That's where the final catalyst grows!"
    # Scene 2: Containing the Reaction
    # Location: The Solarium Sanctum — Sunlit Wards
    # [SCENE START]
    "(The pool of volatile potion sludge on the floor begins to swirl, forming a bubbling, multi-colored arcana vortex that creeps rapidly toward the glass greenhouse doors.)"
    # Source [SPRITE: Tansy — Grinning, Watching Intently]
    show tansy happy
    tansy "Well, look at that chemical feedback! Pure alchemy in action! What's your move, apprentice?"
    # [MC]
    mc "I'm not letting all our hard work go up in smoke!"

    menu:
        "Freeze the sludge with a Glacial Containment Field.":
            "(Weave a multi-layered Glacial Containment Field to instantly freeze the boiling sludge solid)"
            "(Frost spreads across the marble floor in glowing geometric circles, flash-freezing the boiling sludge into harmless blue ice crystals.)"
            show elianna happy
            elianna "Incredible! The temperature drop completely stabilized the volatile compounds!"
        "Neutralize the sludge with herbal counter-agents.":
            "(Use precise herbal counter-agents from your pouch to alter the chemical pH directly)"
            "(You hurl a handful of powdered salt-bark into the center of the vortex, causing the acidic froth to instantly neutralize into plain water.)"
            show tansy happy
            tansy "A textbook chemical inversion! Look at you remembering your First-Year Theory!"
        "Absorb the volatile energy with a Siphon Ward.":
            "(Channel a Siphon Ward through your body to absorb the excess volatile energy)"
            "(You draw the raw magical heat into your palms, channeling it harmlessly down into the stone floorings. The sludge goes completely inert.)"
            show tansy talking
            tansy "Oho! Commander Bruni's fire training really taught you how to handle raw energy!"

    # SFX: Sound Effect: Hissing steam fading, quiet room restored, gentle dripping
    "(Ellie lets out a massive sigh of relief, slumping against the counter before hurriedly wiping her soot-stained cheeks.)"
    # Source [SPRITE: Ellie — Tearful, Extremely Grateful]
    show elianna talking
    elianna "You saved the ward... and the flowers! Oh, sorcerer, I don't know what we would have done if you hadn't taken charge!"
    "(Ellie turns to the pristine golden bed of glowing flowers near the window. She carefully prunes a single, radiant blossom that emanates pure solar warmth, placing it into a silver crystal vial.)"
    # Source [SPRITE: Ellie — Soft Smile, Handing Item]
    show elianna happy
    elianna "Here... ingredient number six: Solar Bloom Essence. All six catalyst components are finally gathered!"
    # Scene 3: The Grand Alembic Ritual
    # Location: The Solarium Sanctum — Grand Alchemy Laboratory
    # [SCENE START]
    # SFX: Sound Effect: Deep humming magical conduits, golden liquid bubbling in heavy glass, crackling hearth
    "(The three of you move to the main laboratory.)"
    "(In the center of the room stands the Grand Alembic—a massive, ancient bronze and glass apparatus mounted over a glowing mana-furnace.)"
    "(The base liquid of the Alkahest of True Form boils gently.)"
    # Source [SPRITE: Tansy — Proud, Masterful Tone]
    show tansy talking
    tansy "Alright, apprentice. This is it. Sunstone Powder, Luminescent Sea-Gland, Draconic Cinder-Ash, Midnight Lotus Petal, Steel-Core Marrow, and Solar Bloom Essence."
    "(Tansy steps back, placing her hands on her hips while Ellie nervously checks the temperature gauges.)"
    # Source [SPRITE: Ellie — Focused, Watching Gauges]
    show elianna angry
    elianna "The Alkahest requires exact magical resonance."
    elianna "Combining six wildly opposing elemental forces—fire, water, solar, dark, earth, and light—is extremely delicate."
    elianna "One wrong move during the infusion will destroy the batch!"
    # Source [SPRITE: Tansy — Smirking, Encouraging]
    show tansy talking
    tansy "You brought us this far, kiddo. I'm stepping back. You weave the catalyst infusion. How are you balancing the six elements into the brew?"

    menu:
        "Balance the catalysts through elemental opposition.":
            "(You sequence the catalysts by elemental opposition—balancing Draconic Fire with Sea-Gland Water, bound by Steel-Core Earth and Lotus Shadow, sealed with Sunstone and Solar Essence.)"
            # SFX: Sound Effect: Harmonious musical chiming, brilliant golden light illuminating room
            "(As you feed the ingredients in perfect opposing pairs, the violent magic reactions cancel each other out seamlessly.)"
            "(The liquid inside the Grand Alembic turns into a pristine, shimmering liquid gold that glows like a miniature sun.)"
            # Source [SPRITE: Tansy — Stunned, Deeply Impressed]
            show tansy happy
            tansy "By the Higher Mages... Perfect elemental balance on the first attempt! That is Grandmaster-level alchemy control!"
            # Source [SPRITE: Ellie — Beaming, Clapping Hands]
            show elianna happy
            elianna "It's flawless! Look at the clarity of the Alkahest! Not a single impurity!"
            "(The golden potion settles into a crystal goblet, radiating pure reversal magic. You stand over the completed cure with total mastery.)"
            hide elianna
            hide tansy
            $ story_progress += 1
            jump finish_chapter_4_free_time
        "Use your mana as a living bridge between all six catalysts.":
            "(You channel your own mana channels as a living bridge, harmonizing all six ingredients simultaneously into a unified golden nexus.)"
            # SFX: Sound Effect: Deep resonant hum, warm pulse of magic radiating through floor
            "(You extend your hands, weaving your personal magic aura around the six catalysts.)"
            "(As they dissolve into the alembic, the brew pulses in exact rhythm with your own heartbeat, turning into a rich, honey-golden nectar attuned specifically to your body.)"
            # Source [SPRITE: Tansy — Laughing Proudly]
            show tansy happy
            tansy "A living soul-bind infusion! You attuned the cure directly to your own mana signature! Brilliant thinking!"
            # Source [SPRITE: Ellie — Warm Smile]
            show elianna sad
            elianna "It’s so warm and gentle... The transformation back to your true self will be completely painless now."
            "(The glowing potion fills the goblet, perfectly matched to your personal spell-weave.)"
            hide elianna
            hide tansy
            $ story_progress += 1
            jump finish_chapter_4_free_time
        "Force all six catalysts into the alembic at maximum pressure.":
            "(You dump all six ingredients into the boiling chamber at once while forcing maximum magic pressure to speed up the brewing process.)"
            $ chapter_4_bad_outcome = True
            # SFX: Sound Effect: VOLATILE SHOCKWAVE! HEAVY GLASS SHATTERING! SCALDING LIQUID SLOSH!
            "(The sudden, forced overload of opposing elemental forces violently ruptures the upper glass dome of the Grand Alembic!)"
            "(Scalding, corrupted sludge erupts in a violent burst, spraying across your hands and chest!)"
            # [MC]
            mc "AAAAGH! IT BURNS!"
            # SFX: Sound Effect: Sizzling arcana burn, glass crunching underfoot
            # Source [SPRITE: Ellie — Screaming, Running Forward]
            show elianna angry
            elianna "SORCERER! NO!"
            "(Ellie rushes over, desperately applying cooling salve to your severely scorched hands as you collapse to your knees. The ruined alembic smokes darkly, coated in a thick, muddy brown sludge.)"
            # Source [SPRITE: Tansy — Furious, Scolding]
            show tansy surprised
            tansy "WHAT WERE YOU THINKING?! Forcing maximum pressure on six unstable catalysts?! Alchemy isn't a battering ram!"
            "(Tansy spends ten grueling minutes using her own high-tier mana to manually salvage whatever degraded residue remains at the bottom of the shattered furnace.)"
            # Source [SPRITE: Tansy — Sighing, Handing Corrupted Potion]
            show tansy frown
            tansy "The main batch is completely ruined."
            tansy "I managed to condense a degraded, bitter sludge tincture from the residue... but because of the magic burn on your hands and the corrupted brew, the transformation back is going to be incredibly painful."
            "(You hold the dark, foul-smelling goblet with bandaged, throbbing hands. The cure is barely usable, leaving you injured and forced to drink an agonizingly flawed potion.)"
            # [SCENE END]
            hide elianna
            hide tansy
            $ story_progress += 1
            jump finish_chapter_4_free_time