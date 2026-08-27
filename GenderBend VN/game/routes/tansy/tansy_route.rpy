# ============================================================
# TANSY SECRET ROUTE — FULL DOCUMENT CONVERSION
# ============================================================
# Source: "Tansy Chapters"
# All unique narrative/dialogue/choice content from the source is preserved.
# Source SFX and unavailable sprite directions are retained as comments.
# Chapter 4 appears twice verbatim in the source document; it is implemented
# once here so the player does not replay the identical chapter twice.
# ============================================================


# ============================================================
# SECRET INTERLUDE TRIGGER
# Location: The Sanctum — Hallway outside the Alchemy Wing
# Late Night
# ============================================================

label tansy_route_offer:

    $ tansy_route_offer_seen = True

    # SFX: Muffled BOOM! Heavy metallic rattling, violet ether smoke
    # leaking under the heavy oak door, frantic coughing.

    "(You stand in the quiet hallway between main story events. Suddenly, the floor beneath your boots vibrates as a plume of sparkling, foul-smelling purple smoke pours into the corridor.)"

    "{color=#B76CFF}{b}SYSTEM NOTIFICATION: SECRET ROUTE CHOICE UNLOCKED!{/b}{/color}"

    menu:

        "Tansy! What did you blow up this time?!":

            "(You kick the lab door open and yell through the violet smoke.)"

            $ tansy_route_unlocked = True
            $ tansy_route_progress = 3

            jump tansy_chapter_3


        "Ignore the explosion and continue on.":

            "(You cough once, turn on your heel, and walk out to the main city.)"

            $ tansy_route_locked = True

            jump free_time


# ============================================================
# CHAPTER 3 — THE GREMLIN'S CATALYST
# ============================================================

label tansy_chapter_3:

    call route_transition(
        "Tansy",
        3,
        "The Gremlin's Catalyst"
    )


    # ========================================================
    # SCENE 1 — CAFFEINATED ETHER-SMOKE
    # Location: The Sanctum — Alchemy Wing (Late Night)
    # ========================================================

    # SFX: Loud hiss of steam, glass retorts clinking wildly,
    # chaotic cackling through coughing fits.

    "(You burst into the lab. Violet ether-smoke fills the room.)"
    "(Standing on a stool in front of a bubbling, neon-pink crucible is Tansy.)"
    "(She wears oversized protective goggles crooked on her forehead, soot smeared across her nose, and holds a steaming beaker of raw, unrefined mana-coffee in one hand and a stirring rod in the other.)"

    "(She turns toward the door, her wide amber eyes twitching with pure, unhinged academic madness.)"

    # Source sprite direction:
    # Tansy — Disheveled Gremlin, Caffeinated Twitch, Goggles Crooked
    show tansy surprised at tansy_size, char_center

    tansy "HOLD YOUR BREATH, WIZARD! Unless you want your lungs to taste like bubblegum and wild magic for three business days!"

    "(She grabs a brass lever and yanks it down. An overhead exhaust pipe rattles violently, sucking the purple smoke up into the rafters.)"

    "(Tansy drops off her stool, landing with an ungraceful thud, taking a massive swig of her black mana-coffee, and pointing her glass stirring rod directly at your face.)"

    # Source sprite direction:
    # Tansy — Pointing Stirring Rod, Suspicious 4th-Wall Glare
    show tansy confused

    tansy "Wait... hold on. Pause the scene! Why are you here?!"
    tansy "Isn't it late Chapter 3 right now?"
    tansy "Aren't you supposed to be at the harbor flirt-fighting with the Garrison Commander or doing adult paperwork with Clara?!"


    # ========================================================
    # CHOICE 1 — MATCHING THE GREMLIN ENERGY
    # ========================================================

    menu:

        "I saw purple smoke and smelled an OSHA violation. How could I resist?":

            "(You grab a pair of spare goggles off a shelf, strap them on, and smirk.)"

            $ tansy_affection += 20

            "(Tansy lets out a sharp, delighted cackle, slapping her knee.)"

            show tansy happy

            tansy "OSHA?! In the Sanctum?! We don't have health codes here, scholar! We have raw ambition and exploding glassware!"


        "The game UI gave me a glowing secret option. I picked you, Tansy.":

            "(You cross your arms, leaning against a worktable.)"

            $ tansy_affection += 20

            "(Tansy blinks, her amber eyes widening in shock as she looks up at the sky.)"

            show tansy surprised

            tansy "Wait—the UI gave you a glowing choice?! You bypassed the main story content for me?! Do you know what kind of route-flags we just broke?!"


        "First of all, you've had way too much caffeine.":

            "(You gently snatch her mana-coffee.)"

            $ tansy_affection += 15

            show tansy teasing

            tansy "(Hisses like a startled feral cat as you take her coffee) Hey! Give that back! That brewed potion is forty percent caffeine and sixty percent pure magic! It's the only reason my heart is still beating!"


    "(Tansy hops onto a nearby cluttered table, sitting cross-legged among parchment scrolls, half-eaten apples, and glowing reagents.)"

    # Source sprite direction:
    # Tansy — Sitting Cross-Legged, Wild Smirk
    show tansy teasing

    tansy "Okay, look. If you're staying in here, you're helping me."
    tansy "I'm trying to synthesize the secondary catalyst for your curse cure."
    tansy "But the thermal density keeps spiking every time I add the Midnight Lotus!"

    "(Behind her, the neon-pink potion in the crucible begins to rumble ominously, bubbling up toward the brim!)"


    # ========================================================
    # SCENE 2 — BREAKING THE FOURTH WALL
    # Location: The Sanctum — Alchemy Wing
    # ========================================================

    # SFX: Ominous bubbling getting louder, sparks flying
    # from the crucible.

    "(Tansy panics, scrambling across the table, knocking over three inkwells and a brass scale in the process.)"

    # Source sprite direction:
    # Tansy — Flustered Scramble, Grabbing Reagents
    show tansy worried

    tansy "Ngh! It's critical! Quick! Hand me the stabilizing salt! No, the blue jar! Not the green one unless you want to turn us both into frogs!"


    # ========================================================
    # CHOICE 2 — STABILIZING THE BREW
    # ========================================================

    menu:

        "Stabilize the brew with the blue salt.":

            "(You grab the blue salt jar, channel a quick cooling kinetic freeze spell into the rim of the crucible, and dump the salt in.)"

            $ tansy_affection += 20

            # SFX: CRISP FROST HISS!

            "(Your kinetic frost instantly cools the boiling mixture. The pink liquid calms down, shifting into a serene, glowing crystalline blue.)"

            show tansy surprised

            tansy "(Gasps, staring at the crucible in awe) Woah... Perfect thermal stabilization! You... you actually know what you're doing!"


        "Pull Tansy out of the splash zone.":

            "(You grab Tansy by her waist, lift her off the table out of the splash zone, and toss a blanket over the crucible.)"

            $ tansy_affection += 20

            "(You scoop her up off the table. Tansy squeaks in surprise as the potion pops harmlessly under the heavy fireproof blanket.)"

            show tansy surprised

            tansy "(Blushing wildly, dangling in your arms) O-Oh. Physical intervention! That's... surprisingly effective. You can put me down now, wizard! Before my sprite gets any more flustered!"


        "Use the green jar on purpose.":

            "(You grab the green jar on purpose just to see what happens.)"

            $ tansy_affection += 15

            # SFX: MINI LOUD POP!

            "(A puff of green smoke erupts. Both of your robes sprout tiny, harmless green toadstool mushrooms.)"

            show tansy teasing

            tansy "(Stares at the mushroom on her shoulder, then looks at you) You did that on purpose. You're an absolute goblin. I love it."


    # ========================================================
    # SCENE 3 — THE GREMLIN'S CONFESSION
    # Location: The Sanctum — Alchemy Wing (Post-Experiment)
    # ========================================================

    "(The danger has passed. The lab is a complete mess—soot on the ceiling, glowing blue liquid in the crucible, and mushrooms on the floor.)"
    "(Tansy sits on the edge of her worktable, swinging her legs back and forth.)"
    "(Her face is covered in fresh soot, but her amber eyes shine with a rare, playful warmth as she looks at you.)"

    # Source sprite direction:
    # Tansy — Cheeky Smirk, Soot-Covered, Looking Up
    show tansy teasing

    tansy "You know... I skipped Chapters 1 and 2 of my own romance arc."
    tansy "I was supposed to just be the background alchemist NPC who gives you quest items and complains about grant funding."

    "(She leans forward, resting her hands on the edge of the table, creeping into your personal space with a mischievous smirk.)"

    # Source sprite direction:
    # Tansy — Leaning Close, Wild Sparkle in Eyes
    show tansy teasing

    tansy "But then you brought me Clara's lunch box. And then you kicked open my door tonight. You ruined my entire character script, wizard."

    mc "Are you complaining, Tansy?"

    show tansy happy

    tansy "(Grins, her cheeks turning a bright pink beneath her soot marks) Complaining?! I'm ecstatic! I get the sharpest, most reckless scholar in the Sanctum all to myself!"


    # ========================================================
    # CHOICE 3 — THE CHAOTIC BINDING DECISION
    # ========================================================

    menu:

        "Then let's break the rest of the script together, you adorable chaos-goblin.":

            "(You step right between her knees, wipe the soot off her nose with your thumb, and grin.)"

            $ tansy_affection += 30

            "(You step close, wiping the soot from her cheek. Tansy's sarcastic bravado instantly melts into a wide breathless, ridiculously happy smile.)"

            # Source sprite direction:
            # Tansy — Cheeks Bright Red, Overjoyed Gremlin
            show tansy happy

            tansy "Deal! But if the narrative crashes because we fell in love before Chapter 4... I'm blaming you!"

            "(She grabs your scholar's collar and pulls you down into a wild, messy, incredibly sweet kiss—nearly knocking over another rack of glass retorts in the process.)"


            hide tansy

            jump finish_tansy_chapter_3


        "You're a complete mess, Tansy... but you're my favorite mess in Mirthhaven.":

            "(You cross your arms and smirk back.)"

            $ tansy_affection += 20

            "(Tansy laughs loudly, hopping off the table and throwing her arm around your waist.)"

            # Source sprite direction:
            # Tansy — Laughing, Arm Around Waist
            show tansy happy

            tansy "Your favorite mess?! I'm framing that quote on the wall! Now come on, wizard—we have three more unstable potions to brew before dawn!"


            hide tansy

            jump finish_tansy_chapter_3


        "Honestly, this lab is a safety hazard.":

            "(You step back, looking around the ruined room with a scowl.)"

            $ tansy_route_locked = True
            $ tansy_romance_locked = True
            $ tansy_ending = "route_crash"

            "(Tansy's playful grin instantly drops. She rolls her eyes dramatically, pointing her stirring rod at the exit door.)"

            # Source sprite direction:
            # Tansy — Annoyed, Pointing at Door
            show tansy sad

            tansy "Boring! Absolute buzzkill! Go back to the main story if you can't handle a little ether-smoke! The door's behind you, scholar!"

            "(Tansy turns her back on you, diving back into her calculations. You leave the lab, permanently closing Tansy's secret route.)"


            hide tansy

            jump finish_tansy_failed_event


# ============================================================
# CHAPTER 4 — FORMULA FOR TWO CHAOS-GOBLINS
# ============================================================

label tansy_chapter_4:

    call route_transition(
        "Tansy",
        4,
        "Formula for Two Chaos-Goblins"
    )


    # ========================================================
    # SCENE 1 — THE RAINBOW EXPLOSION
    # Location: The Sanctum — Alchemy Wing (Dawn)
    # ========================================================

    # SFX: Loud fizzing pop, sparkling corks flying,
    # an out-of-tune magical gramophone blasting a victorious fanfare.

    "(The first light of dawn pierces through the stained-glass windows of the Sanctum Alchemy Wing, revealing a room that looks like a rainbow bomb detonated inside it.)"
    "(Iridescent gold glitter covers the stone ceiling and glowing neon-blue bubbles float lazily through the air.)"
    "(Thirty empty coffee mugs sit stacked like a haphazard tower on the central workbench.)"

    "(Standing atop her wooden step-stool, holding a crystal flask filled with a swirling, perfectly stabilized luminescence, is Tansy. Her hair looks like a thunderstorm passed through it, her protective goggles are upside down on her forehead, and she has a massive smear of glittering purple soot across her nose.)"

    # Source sprite direction:
    # Tansy — Triumphant Gremlin, Wild Eyes, Holding Glowing Flask
    show tansy happy at tansy_size, char_center

    tansy "BEHOLD! THE ALKAHEST OF TRUE FORM! IT IS COMPLETE! EAT YOUR HEART OUT, SANCTUM ARCHMAGI!"

    "(She turns around on her stool so fast she nearly loses her balance, pointing the glowing crystal flask dramatically at your chest.)"

    # Source sprite direction:
    # Tansy — Pointing Flask, Unhinged Grin
    show tansy teasing

    tansy "Ninety-six hours of continuous brewing, four near-fatal explosions, and sixty-two cups of black mana-espresso!"
    tansy "We did it, wizard! Your curse cure is officially synthesized!"


    # ========================================================
    # CHOICE 1 — CELEBRATING THE BREAKTHROUGH
    # ========================================================

    menu:

        "You absolute genius! I knew you could do it!":

            "(You grab her off her step-stool and spin her around in a tight, laughing victory hug.)"

            $ tansy_affection += 20

            "(Tansy squeaks loudly as you lift her off her feet, her arms flailing before she wraps them tightly around your neck, cackling with pure, unfiltered joy.)"

            show tansy surprised

            tansy "Whoa! Unexpected physical trajectory! But I'm too excited to file a safety complaint!"


        "Raise a toast to Tansy.":

            "(You grab two empty beakers, fill them with bubbling mana-soda, and raise a toast.)"

            $ tansy_affection += 15

            # SFX: CLINK OF GLASS BEAKERS!

            "(Tansy clinks her beaker against yours so hard it almost shatters, chugging the fizzy liquid in one go.)"

            show tansy happy

            tansy "To alchemy! To breaking health codes! And to us!"


        "Are you sure this breaks my curse and doesn't turn me into a shiny salamander?":

            "(You inspect the glowing flask with a smirk.)"

            $ tansy_affection += 15

            show tansy teasing

            tansy "(Gasp!) Ninety-four percent sure! The remaining six percent is just minor aesthetic sparkles! You're welcome!"


    "(You drink the shimmering formula. A warm, soothing wave of pure light ripples through your veins, permanently dissolving the dark curse marks on your skin. The main quest burden vanishes entirely, leaving a feeling of profound physical relief.)"

    "(Tansy watches you intently, her breath held until she sees the curse fade completely. But as the magical dust settles, her manic gremlin energy suddenly wavers. She hops off her stool, setting the empty flask down, and fiddles nervously with her leather tool belt.)"


    # ========================================================
    # SCENE 2 — BEYOND THE MAIN QUEST
    # Location: The Sanctum — Alchemy Wing Balcony (Sunrise)
    # ========================================================

    # SFX: Soft morning wind whistling through the open terrace,
    # distant morning bells of Mirthhaven.

    "(Tansy steps out onto the small stone balcony overlooking the glowing city below. The morning sun bathes her disheveled form in warm golden light. For the first time since you met her, the loud, caffeinated alchemist is quiet.)"

    # Source sprite direction:
    # Tansy — Fiddling with Goggles, Uncharacteristically Quiet
    show tansy worried

    tansy "So... the quest item is delivered. The curse is broken. The main story flag is officially cleared."

    "(She looks up at you through her messy, soot-stained bangs, her amber eyes reflecting an unexpected, genuine vulnerability.)"

    # Source sprite direction:
    # Tansy — Chewing Lip, Looking Up
    show tansy worried

    tansy "Normally... this is the part where the quest-giver NPC goes back to standing behind her desk."
    tansy "Repeating the same three lines of background dialogue while the main character moves on..."
    tansy "...to the grand romance finales with the cool Guildmaster or the tough Commander."

    "(She steps right up to you, her calloused, ink-stained fingers reaching out to lightly clutch the front of your scholar's robes.)"

    tansy "Be honest with me, wizard."
    tansy "Did you only stay in my messy lab because you needed a potion..."
    tansy "...or do you actually want a chaotic goblin like me in your life after the credits roll?"


    # ========================================================
    # CHOICE 2 — REASSURING THE GREMLIN
    # ========================================================

    menu:

        "I stayed because I fell completely in love with the girl brewing it.":

            "(You reach down, take her soot-covered face in both your hands, and look right into her eyes.)"

            $ tansy_affection += 30
            $ tansy_ending = "ultimate_formula"

            "(Tansy's wide amber eyes go completely wide. A bright, blazing crimson flush erupts across her cheeks, spreading all the way to the tips of her ears.)"

            show tansy surprised

            tansy "(Short-circuiting) Error 404... Heart rate exceeding maximum parameters... You... you actually mean that?!"

            jump tansy_ending_true


        "Leaving you alone in this lab is a safety hazard. We're an item now.":

            "(You wrap your arm securely around her broad shoulders, grinning.)"

            $ tansy_affection += 20
            $ tansy_ending = "partners_in_perpetual_chaos"

            show tansy happy

            tansy "(Grins wildly, leaning her head against your arm) A safety hazard?! I'll have you know I'm a certified threat to public infrastructure! And I'm keeping you forever!"

            jump tansy_ending_partners


        "You were a great quest-giver, Tansy.":

            "(You pat her head awkwardly.)"

            $ tansy_romance_locked = True
            $ tansy_route_locked = True
            $ tansy_ending = "background_npc"

            "(Tansy blinks, her wild expression instantly flattening into a deadpan glare. She steps back, adjusting her goggles.)"

            show tansy sad

            tansy "Right. Quest-giver status maintained. Standard NPC dialogue unlocked. Thanks for playing the secret route, scholar. Door's on your left."

            jump tansy_ending_fail


# ============================================================
# SCENE 3 — THE ULTIMATE SYNTHESIS
# Location: The Sanctum — Alchemy Wing (Sunrise)
# ============================================================

label tansy_ending_true:

    "(The morning sun floods the ruined laboratory with brilliant gold. The air is still filled with floating, harmless glitter particles, creating an absurdly magical, chaotic atmosphere.)"

    "(You don't let her short-circuit any longer. You slide your hands from her cheeks to the back of her messy hair, pulling the brilliant, chaotic alchemist down into a deep, passionate, and delightfully messy kiss under the rising sun.)"

    # Source sprite direction:
    # Tansy — Eyes Wide -> Melted Happiness, Bright Red Blush
    show tansy surprised

    "(Tansy lets out a muffled, squeaky gasp before throwing both her arms wildly around your neck, kissing you back with every ounce of unhinged, fierce passion in her soul. In her excitement, her foot accidentally kicks a nearby shelf—sending a box of sparkling glitter-bombs popping off into the air behind you like indoor fireworks.)"

    "(When you finally part, Tansy is breathless, resting her forehead against yours, her chest heaving as she lets out a dizzy, euphoric giggle.)"

    # Source sprite direction:
    # Tansy — Radiant, Cheeks Crimson, Devoted Smirk
    show tansy happy

    tansy "Okay... yep! Best secret route ending in visual novel history! Official statement!"

    mc "No more scripts, Tansy. Just you and me."

    show tansy teasing

    tansy "(Smirks triumphantly, lacing her ink-stained fingers tightly with yours) You and me, wizard. Now come on—we have a whole lifetime of illegal alchemy and chaotic experiments to run together!"


    hide tansy

    jump finish_tansy_chapter_4


label tansy_ending_partners:

    "(The morning sun floods the ruined laboratory with brilliant gold. The air is still filled with floating, harmless glitter particles, creating an absurdly magical, chaotic atmosphere.)"

    "(Tansy hops onto the balcony railing, raising her glass beaker to the sky with a triumphant, manic cackle.)"

    # Source sprite direction:
    # Tansy — Wild Laugh, Raising Beaker
    show tansy happy

    tansy "Mirthhaven isn't ready for the two of us! We're going to revolutionize magic, blow up half the council's storage sheds, and rewrite every textbook in the Sanctum!"

    "(She jumps off the railing right into your arms, wrapping her legs around your waist as you both laugh loudly under the sunrise—an unstoppable, chaotic power couple bound by magic, science, and absolute anarchy.)"


    hide tansy

    jump finish_tansy_chapter_4


label tansy_ending_fail:

    "(Tansy stands behind her cluttered desk, picking up a feather duster and sweeping soot off her brass scales. Her playful, chaotic spark is gone, replaced by a polite, distant NPC posture.)"

    # Source sprite direction:
    # Tansy — Polite NPC Smile, Standard Posture
    show tansy sad

    tansy "Thank you for visiting the Sanctum Alchemy Wing, scholar! Health potions are twenty copper pieces each. Have a pleasant day in Mirthhaven!"

    "(You walk out of the quiet laboratory, leaving the secret route behind as Tansy fades back into the background of the Sanctum.)"


    hide tansy

    jump finish_tansy_chapter_4