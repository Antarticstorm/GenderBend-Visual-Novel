label chapter_4:

    # =========================
    # SCENE 1 - Sparks & Tripping Hazards
    # =========================

    # Location: The Solarium Sanctum — Sunlit Wards (Infirmary & Botanical Annex)
    # (Sound Effect: Distant glass shattering, bubbling liquid hiss, frantic scurrying footsteps, smoke alarms chiming softly)

    "(You hurry down the arched white corridors of the Sunlit Wards, carrying the five rare ingredients secured from across Mirthhaven. As you push open the double oak doors to the infirmary annex, a cloud of pink and neon-green smoke billows past your face, smelling intensely of peppermint and sulfur.)"

    # [SPRITE: Ellie — Panicked, Flustered, Apron Smoldering]
    ellie "Eeeeek! No, no, no! Please don't explode! Oh dear, where is the neutralizing agent?!"

    "(Through the haze, you see Ellie scrambling across the polished marble floor. A heavy brass rack holding dozens of volatile restorative potions has tipped over onto an enchanted heating brazier. To make matters exponentially worse, Tansy is standing right beside her, arms raised, enthusiastically waving her wooden wand.)"

    # [SPRITE: Tansy — Excited, Carefree, Smirking]
    tansy "Don't worry, Ellie! A quick little Ignis-Expellior spell will burn off the excess vapor! Stand back!"

    # [SPRITE: Ellie — Terrified, Waving Hands]
    ellie "WAIT! TANSY, NO! THAT'S NITRATE-BASED—"

    # (Sound Effect: LOUD ARCANA FIZZING! Sparks shooting toward ceiling, bubbling froth expanding rapidly)
    mc "TANSY, STOP CASTING!"

    # CHOICE 1
    menu:
        "(Bark authoritative orders to establish immediate command over both witches)":
            mc "Ellie, grab the damp leather blankets! Tansy, lower your wand and don't touch another rune!"
            tansy "Ooh! Look at my apprentice taking charge! So authoritative!"
            ellie "Y-Yes! Right away!"

        "(Physically dash forward and pull Ellie out of the line of fire)":
            "(You spring across the room, wrapping your arm around Ellie's waist and pulling her clear just as a splash of boiling green foam hits the tile where she stood.)"
            ellie "Ah! S-Sorcerer! Oh goodness... thank you! My apron almost caught fire!"

        "(Grasp Tansy's raised wrist to forcefully cut off her spell focus)":
            "(You grab Tansy's hand mid-incantation, redirecting her wand tip safely toward the stone hearth.)"
            tansy "Party pooper! I had that totally under control... mostly! Well, 40% under control!"

    # (Sound Effect: Potion froth growing larger, deep rumbling arcana reaction)
    # [SPRITE: Ellie — Distressed, Trembling]
    ellie "If those spilling potions reach the greenhouse bed, they'll destroy the Solar Bloom garden! That's where the final catalyst grows!"

    # =========================
    # SCENE 2 - Containing the Reaction
    # =========================

    # Location: The Solarium Sanctum — Sunlit Wards

    "(The pool of volatile potion sludge on the floor begins to swirl, forming a bubbling, multi-colored arcana vortex that creeps rapidly toward the glass greenhouse doors.)"

    # [SPRITE: Tansy — Grinning, Watching Intently]
    tansy "Well, look at that chemical feedback! Pure alchemy in action! What's your move, apprentice?"

    mc "I'm not letting all our hard work go up in smoke!"

    # CHOICE 2
    menu:
        "(Weave a multi-layered Glacial Containment Field to instantly freeze the boiling sludge solid)":
            "(Frost spreads across the marble floor in glowing geometric circles, flash-freezing the boiling sludge into harmless blue ice crystals.)"
            ellie "Incredible! The temperature drop completely stabilized the volatile compounds!"

        "(Use precise herbal counter-agents from your pouch to alter the chemical pH directly)":
            "(You hurl a handful of powdered salt-bark into the center of the vortex, causing the acidic froth to instantly neutralize into plain water.)"
            tansy "A textbook chemical inversion! Look at you remembering your First-Year Theory!"

        "(Channel a Siphon Ward through your body to absorb the excess volatile energy)":
            "(You draw the raw magical heat into your palms, channeling it harmlessly down into the stone flooring. The sludge goes completely inert.)"
            bao "Bao's fire training really taught you how to handle raw energy!"

    # (Sound Effect: Hissing steam fading, quiet room restored, gentle dripping)
    "(Ellie lets out a massive sigh of relief, slumping against the counter before hurriedly wiping her soot-stained cheeks.)"

    # [SPRITE: Ellie — Tearful, Extremely Grateful]
    ellie "You saved the ward... and the flowers! Oh, sorcerer, I don't know what we would have done if you hadn't taken charge!"

    "(Ellie turns to the pristine golden bed of glowing flowers near the window. She carefully prunes a single, radiant blossom that emanates pure solar warmth, placing it into a silver crystal vial.)"

    # [SPRITE: Ellie — Soft Smile, Handing Item]
    ellie "Here... ingredient number six: Solar Bloom Essence. All six catalyst components are finally gathered!"

    # =========================
    # SCENE 3 - The Grand Alembic Ritual
    # =========================

    # Location: The Solarium Sanctum — Grand Alchemy Laboratory
    # (Sound Effect: Deep humming magical conduits, golden liquid bubbling in heavy glass, crackling hearth)

    "(The three of you move to the main laboratory. In the center of the room stands the Grand Alembic—a massive, ancient bronze and glass apparatus mounted over a glowing mana-furnace. The base liquid of the Alkahest of True Form boils gently.)"

    # [SPRITE: Tansy — Proud, Masterful Tone]
    tansy "Alright, apprentice. This is it. Sunstone Powder, Luminescent Sea-Gland, Draconic Cinder-Ash, Midnight Lotus Petal, Steel-Core Marrow, and Solar Bloom Essence."

    "(Tansy steps back, placing her hands on her hips while Ellie nervously checks the temperature gauges.)"

    # [SPRITE: Ellie — Focused, Watching Gauges]
    ellie "The Alkahest requires exact magical resonance. Combining six wildly opposing elemental forces—fire, water, solar, dark, earth, and light—is extremely delicate. One wrong move during the infusion will destroy the batch!"

    # [SPRITE: Tansy — Smirking, Encouraging]
    tansy "You brought us this far, kiddo. I'm stepping back. You weave the catalyst infusion. How are you balancing the six elements into the brew?"

    # CHOICE 3
    menu:
        "(Sequence the catalysts by elemental opposition—balancing Draconic Fire with Sea-Gland Water, bound by Steel-Core Earth and Lotus Shadow, sealed with Sunstone and Solar Essence)":
            $ chapter_4_ending = "perfect_equilibrium"
            jump chapter_4_ending_a

        "(Channel your own mana channels as a living bridge, harmonizing all six ingredients simultaneously into a unified golden nexus)":
            $ chapter_4_ending = "living_catalyst"
            jump chapter_4_ending_b

        "(Dump all six ingredients into the boiling chamber at once while forcing maximum magic pressure to speed up the brewing process)":
            $ chapter_4_ending = "alembic_explosion"
            jump chapter_4_ending_c


label chapter_4_ending_a:

    # (Sound Effect: Harmonious musical chiming, brilliant golden light illuminating room)
    "(As you feed the ingredients in perfect opposing pairs, the violent magic reactions cancel each other out seamlessly. The liquid inside the Grand Alembic turns into a pristine, shimmering liquid gold that glows like a miniature sun.)"

    # [SPRITE: Tansy — Stunned, Deeply Impressed]
    tansy "By the Higher Mages... Perfect elemental balance on the first attempt! That is Grandmaster-level alchemy control!"

    # [SPRITE: Ellie — Beaming, Clapping Hands]
    ellie "It's flawless! Look at the clarity of the Alkahest! Not a single impurity!"

    "(The golden potion settles into a crystal goblet, radiating pure reversal magic. You stand over the completed cure with total mastery.)"

    $ story_progress += 1
    $ chapter = 5

    jump chapter_5


label chapter_4_ending_b:

    # (Sound Effect: Deep resonant hum, warm pulse of magic radiating through floor)
    "(You extend your hands, weaving your personal magic aura around the six catalysts. As they dissolve into the alembic, the brew pulses in exact rhythm with your own heartbeat, turning into a rich, honey-golden nectar attuned specifically to your body.)"

    # [SPRITE: Tansy — Laughing Proudly]
    tansy "A living soul-bind infusion! You attuned the cure directly to your own mana signature! Brilliant thinking!"

    # [SPRITE: Ellie — Warm Smile]
    ellie "It's so warm and gentle... The transformation back to your true self will be completely painless now."

    "(The glowing potion fills the goblet, perfectly matched to your personal spell-weave.)"

    $ story_progress += 1
    $ chapter = 5

    jump chapter_5


label chapter_4_ending_c:

    # (Sound Effect: VOLATILE SHOCKWAVE! HEAVY GLASS SHATTERING! SCALDING LIQUID SLOSH!)
    "(The sudden, forced overload of opposing elemental forces violently ruptures the upper glass dome of the Grand Alembic! Scalding, corrupted sludge erupts in a violent burst, spraying across your hands and chest!)"

    mc "AAAAGH! IT BURNS!"

    # (Sound Effect: Sizzling arcana burn, glass crunching underfoot)
    # [SPRITE: Ellie — Screaming, Running Forward]
    ellie "SORCERER! NO!"

    "(Ellie rushes over, desperately applying cooling salve to your severely scorched hands as you collapse to your knees. The ruined alembic smokes darkly, coated in a thick, muddy brown sludge.)"

    # [SPRITE: Tansy — Furious, Scolding]
    tansy "WHAT WERE YOU THINKING?! Forcing maximum pressure on six unstable catalysts?! Alchemy isn't a battering ram!"

    "(Tansy spends ten grueling minutes using her own high-tier mana to manually salvage whatever degraded residue remains at the bottom of the shattered furnace.)"

    # [SPRITE: Tansy — Sighing, Handing Corrupted Potion]
    tansy "The main batch is completely ruined. I managed to condense a degraded, bitter sludge tincture from the residue... but because of the magic burn on your hands and the corrupted brew, the transformation back is going to be incredibly painful."

    "(You hold the dark, foul-smelling goblet with bandaged, throbbing hands. The cure is barely usable, leaving you injured and forced to drink an agonizingly flawed potion.)"

    $ story_progress += 1
    $ chapter = 5

    jump chapter_5
