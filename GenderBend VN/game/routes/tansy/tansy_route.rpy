# Tansy Secret Route - The Gremlin's Formula
# Chapter 1 trigger is set by Clara's route.

label tansy_route_offer:
    $ tansy_route_offer_seen = True
    "A muffled boom rattles the Sanctum hallway. Violet ether-smoke leaks from beneath the Alchemy Wing door."
    "A special opportunity involving Tansy has become available."
    menu:
        "Kick the lab door open. \"Tansy! What did you blow up this time?!\"":
            $ tansy_route_unlocked = True
            $ tansy_route_progress = 3
            jump tansy_chapter_3
        "Ignore the explosion and continue with your free time.":
            $ tansy_route_locked = True
            jump free_time

label tansy_chapter_3:
    "You burst into the laboratory. Violet ether-smoke fills the room."
    tansy "HOLD YOUR BREATH, WIZARD! Unless you want your lungs to taste like bubblegum and wild magic for three business days!"
    tansy "Wait... why are you here?! Isn't it late Chapter 3 right now?"

    menu:
        "I saw purple smoke and smelled an OSHA violation. How could I resist?":
            $ tansy_affection += 20
            tansy "OSHA?! In the Sanctum?! We don't have health codes here, scholar!"
        "The game UI gave me a glowing secret option. I picked you, Tansy.":
            $ tansy_affection += 20
            tansy "The UI gave you a glowing choice?! Do you know what kind of route-flags we just broke?!"
        "You've had too much caffeine. I came to check on my favorite chaotic alchemist.":
            $ tansy_affection += 15
            tansy "Hey! That potion is forty percent caffeine and sixty percent pure magic!"

    tansy "If you're staying, you're helping me. The thermal density keeps spiking!"
    tansy "Quick! The blue jar! Not the green one unless you want to turn us both into frogs!"

    menu:
        "Use the blue salt and a cooling spell.":
            $ tansy_affection += 20
            "The mixture settles into a serene crystalline blue."
            tansy "Perfect thermal stabilization! You actually know what you're doing!"
        "Lift Tansy out of the splash zone and cover the crucible.":
            $ tansy_affection += 20
            tansy "O-Oh. Physical intervention! That's surprisingly effective!"
        "Use the green jar on purpose.":
            $ tansy_affection += 15
            "Tiny harmless mushrooms sprout from both of your robes."
            tansy "You did that on purpose. You're an absolute goblin. I love it."

    tansy "I was supposed to be a background alchemist NPC. But you brought me Clara's lunch and kicked open my door tonight."
    tansy "You ruined my entire character script, wizard."
    mc "Are you complaining, Tansy?"
    tansy "Complaining?! I'm ecstatic!"

    menu:
        "Then let's break the rest of the script together, you adorable chaos-goblin.":
            $ tansy_affection += 30
            tansy "Deal! If the narrative crashes because we fell in love before Chapter 4, I'm blaming you!"
            "She grabs your collar and pulls you into a wild, messy kiss."
            jump finish_tansy_chapter_3
        "You're a complete mess, Tansy... but you're my favorite mess in Mirthhaven.":
            $ tansy_affection += 20
            tansy "Your favorite mess?! I'm framing that quote on the wall!"
            jump finish_tansy_chapter_3
        "Honestly, this lab is a safety hazard. I think I made a mistake coming here.":
            $ tansy_route_locked = True
            $ tansy_romance_locked = True
            $ tansy_ending = "route_crash"

            tansy "Boring! Absolute buzzkill! The door's behind you, scholar!"

            jump finish_tansy_failed_event

label tansy_chapter_4:
    "Dawn reveals an Alchemy Wing covered in glitter, floating bubbles, and empty coffee mugs."
    tansy "BEHOLD! THE ALKAHEST OF TRUE FORM! IT IS COMPLETE!"
    tansy "We did it, wizard!"

    menu:
        "Grab her and spin her around in a victory hug.":
            $ tansy_affection += 20
            tansy "Unexpected physical trajectory! But I'm too excited to file a safety complaint!"
        "Raise a beaker in a toast.":
            $ tansy_affection += 15
            mc "To Mirthhaven's most brilliant, dangerous, and completely unhinged alchemist!"
            tansy "To alchemy! To breaking health codes! And to us!"
        "Are you sure this won't turn me into a shiny salamander?":
            $ tansy_affection += 15
            tansy "Ninety-four percent sure! The remaining six percent is minor aesthetic sparkles!"

    "You drink the shimmering formula. A warm wave of magic ripples through you."
    "Tansy steps onto the balcony overlooking Mirthhaven."
    tansy "So... the quest item is delivered. The main story flag is cleared."
    tansy "Did you only stay because you needed a potion... or do you actually want a chaotic goblin like me after the credits roll?"

    menu:
        "I stayed because I fell completely in love with the girl brewing it.":
            $ tansy_affection += 30
            $ tansy_ending = "ultimate_formula"
            tansy "Error 404... Heart rate exceeding maximum parameters... You actually mean that?!"
            jump tansy_ending_true
        "Leaving you alone is a safety hazard. We're an item now.":
            $ tansy_affection += 20
            $ tansy_ending = "partners_in_perpetual_chaos"
            tansy "I'm a certified threat to public infrastructure! And I'm keeping you forever!"
            jump tansy_ending_partners
        "You were a great quest-giver. I'll stop by whenever I need health potions.":
            $ tansy_romance_locked = True
            $ tansy_route_locked = True
            $ tansy_ending = "background_npc"
            tansy "Right. Quest-giver status maintained. Door's on your left."
            jump tansy_ending_fail

label tansy_ending_true:
    "You pull Tansy into a deep, chaotic kiss beneath the rising sun as glitter-bombs accidentally burst behind you."
    tansy "Best secret route ending in visual novel history! Official statement!"
    mc "No more scripts, Tansy. Just you and me."
    tansy "You and me, wizard."
    jump finish_tansy_chapter_4

label tansy_ending_partners:
    tansy "Mirthhaven isn't ready for the two of us!"
    tansy "We're going to revolutionize magic and rewrite every textbook in the Sanctum!"
    "She jumps into your arms as you both laugh beneath the sunrise."
    jump finish_tansy_chapter_4

label tansy_ending_fail:
    "Tansy's playful spark is replaced by a polite, distant posture."
    tansy "Thank you for visiting the Sanctum Alchemy Wing, scholar! Health potions are twenty copper pieces each."
    "You leave with Tansy's secret route permanently closed."
    jump finish_tansy_chapter_4
