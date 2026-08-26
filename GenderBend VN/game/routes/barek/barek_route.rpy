# ============================================================
# BAREK TIDEJAW ROUTE
# ============================================================
# Requires:
# barek_route_unlocked, barek_route_progress, barek_affection,
# barek_romance_locked, barek_route_locked, barek_ending
# and finish_barek_event.
# ============================================================

label barek_chapter_1:
    "At Nautilus Point, you find Barek waist-deep in the tide wrestling an iron-weighted leviathan net from a rotting pier pile."
    barek "Ghh... stubborn iron-skin rope..."

    menu:
        "Jump down and haul the rope alongside him.":
            $ barek_affection += 20
            barek "Watch your footing—! Heh, alright... on my count!"
        "Use kinetic magic to lighten the iron sinkers while pulling the line.":
            $ barek_affection += 20
            barek "Clever spellwork! Took the weight right off the timber!"
        "Brace against a pillar and coordinate your pulls with the waves.":
            $ barek_affection += 15
            barek "Good eye! Together now—HEAVE!"

    "The net finally crashes safely onto the planks."
    barek "Appreciate the hand. Most folk see a guy my size and assume I've got it... or they get skittish around the teeth. You didn't hesitate."

    menu:
        "A heavy net is a heavy net. It takes two to haul something that stubborn.":
            $ barek_affection += 20
            barek "Aye. That's dock truth right there."
        "Your teeth don't intimidate me. I deal with Tansy's exploding cauldrons.":
            $ barek_affection += 15
            barek "Fair enough, sorcerer."
        "I'm actually looking for a Luminescent Sea-Gland for the Sanctum.":
            $ barek_affection += 15
            barek "Then you came to the right pile of kelp."

    "Barek retrieves the sea-gland, then finds a smooth piece of blue sea-glass tangled in the net."
    barek "Here's your gland. And... take this too."
    barek "Docks can be a cold place. It's rare finding someone who looks past the sharp edges."

    menu:
        "Hold the sea-glass up to the light with a bright smile.":
            $ barek_affection += 20
            mc "It's beautiful, Barek. I'll keep it on my desk while I study."
            barek "Glad you like it."
        "Slip it safely into the pocket beside your heart.":
            $ barek_affection += 20
            mc "Thank you, Barek. I'll make sure it stays safe."
            barek "Take care going back to the Sanctum."
        "Take it while gently brushing your fingertips against his palm.":
            $ barek_affection += 25
            mc "Quiet respect goes both ways, Barek."
            barek "Aye... it does."

    jump finish_barek_event


label barek_chapter_2:
    "Overwhelmed by the noise of The Laughing Anchor, you slip onto its cold seaside porch."
    "Barek quietly follows and blocks some of the sharp ocean wind with his broad frame."
    barek "Too loud in there for you too, sorcerer?"

    menu:
        "A little quiet is exactly what I needed.":
            $ barek_affection += 20
            barek "Aye. Loud places have a way of draining the battery fast."
        "I didn't think a hardened dock worker like you would mind the noise.":
            $ barek_affection += 15
            barek "I like my drinks quiet. Bo's the one who needs an audience."
        "Between Tansy's chaos and the crowd, my head is spinning.":
            $ barek_affection += 20
            barek "You've been carrying a lot on your shoulders lately."

    "Seeing you shiver, Barek drapes his heavy leather coat around you."
    barek "Keep it on. The sea wind down here bites harder than it looks."
    barek "Tell me true. How are you really holding up with this potion mess?"

    menu:
        "It's terrifying sometimes... wondering if we'll actually find a cure.":
            $ barek_affection += 25
            mc "I just want my true body back."
            barek "You don't have to fake being strong around me."
        "It's hard, but having people like you looking out for me makes it easier.":
            $ barek_affection += 25
            barek "Glad I can be useful for something besides hauling nets."
        "I'm fine! A little magical transformation builds character, right?":
            $ barek_affection += 15
            barek "Stubborn. You don't always have to joke your way through the pain."

    "Barek holds one broad, webbed hand open on the railing."
    barek "If you ever need a break from the noise... my dock is always quiet."

    menu:
        "Rest your hand in his palm and intertwine your fingers.":
            $ barek_affection += 25
            mc "I might just hold you to that offer."
            barek "Door's always open to you, sorcerer. Day or night."
        "Cover his hand with both of yours.":
            $ barek_affection += 20
            mc "Your quiet strength means more than you know."
            barek "I'll stand by you as long as you need me."
        "Lean into his side and rest your hand over his knuckles.":
            $ barek_affection += 20
            mc "Promise me you won't let the noise get too close."
            barek "Nothing gets through me to hurt you. That's a dock promise."

    jump finish_barek_event


label barek_chapter_3:
    "At sunset in the Sun-Gilded Market, you encounter Barek carrying a mountain of heavy ship fittings."
    barek "Sorcerer. Didn't expect to see you up in the market."

    menu:
        "Lighten his iron load with a weight-reduction charm.":
            $ barek_affection += 20
            barek "Magic certainly comes in handy. Appreciate it."
        "Are you hauling ship fittings or the entire lower pier?":
            $ barek_affection += 15
            barek "Just another Tuesday errand for the docks."
        "Heading toward Nautilus Point? Mind if I walk with you?":
            $ barek_affection += 20
            barek "Gladly. Lane's better with company."

    "A heavily loaded cart suddenly tears loose and hurtles toward you."
    "Before you can cast, Barek catches the cart with one arm and pulls you tightly against his chest with the other."
    barek "Ghh... gotcha!"

    menu:
        "Rest both hands against his chest and look up at him.":
            $ barek_affection += 25
            mc "You stopped that whole cart... with one arm."
            barek "I wasn't going to let it touch you."
        "Bury your face comfortably into his shoulder.":
            $ barek_affection += 25
            barek "Hold onto me... you're safe."
        "That... was incredible, Barek.":
            $ barek_affection += 20
            barek "When you work the docks, you learn to react before you think."

    "When the danger passes, Barek realizes he is still holding you. A vivid sea-blue flush spreads across his gills."
    barek "S-Sorry. Moved without thinking... you're not hurt, are you?"

    menu:
        "Touch the blue flush on his cheek. \"I'm fine... but my heart is racing.\"":
            $ barek_affection += 30
            barek "Sorcerer... my heart's doing a fair bit of racing too."
            barek "Every time I look at you, the whole harbor goes quiet."
            jump finish_barek_event
        "Place your hand over his heart. \"Don't ever apologize for protecting me.\"":
            $ barek_affection += 25
            mc "I'll always trust you, Barek."
            barek "As long as I'm breathing... no storm and no potion mess is ever going to hurt you."
            jump finish_barek_event
        "Shove him away and call him an overgrown brute.":
            $ barek_romance_locked = True
            $ barek_ending = "wall_of_coral"
            barek "I... I see."
            barek "Forgive me, sorcerer. I forgot my place."
            barek "You can walk back alone. Wouldn't want a brute like me getting in your way."
            "Barek withdraws behind a cold wall of hurt and isolation."
            jump finish_barek_event


label barek_chapter_4:
    "Late at night, Barek waits for you on Nautilus Point's High Watch-Pier, overlooking the moonlit harbor."
    barek "Look at you. Back in your own skin at last."
    barek "Tansy's alkahest worked like a charm. You look... whole."

    if barek_romance_locked:
        jump barek_locked_conclusion

    menu:
        "It feels incredible to be back... but I'm glad you knew me in every form.":
            $ barek_affection += 20
            barek "Form's just a shell, sorcerer. It was always your spirit I was looking at."
        "Lean comfortably against his warm arm.":
            $ barek_affection += 20
            mc "Your quiet company is better than the party below."
            barek "Docks are meant for quiet nights and honest conversation."
        "Did you bring me up here just to inspect Tansy's handiwork?":
            $ barek_affection += 15
            barek "Maybe I wanted an excuse to get my favorite person away from the crowd."

    "Barek draws a leather cord from his pouch."
    "A hand-carved deep-sea whalebone pendant hangs from it, inlaid with the blue sea-glass from the day you first met."

    barek "Down on the docks, we give these to the person who keeps us anchored."

    menu:
        "The sea-glass from our first day at the pier...":
            $ barek_affection += 20
            mc "You kept it all this time?"
            barek "Knew from the second you grabbed that net that it belonged to something special."
        "Barek... you carved this for me?":
            $ barek_affection += 20
            barek "Every scrape of the knife was a thought of you. Time well spent."
        "What does being your anchor mean to you?":
            $ barek_affection += 20
            barek "No matter how wild the ocean gets... I always know where home is."

    barek "My life's mostly iron, salt, and heavy lifting... but you've been the calmest spot in the water for me."
    barek "Doesn't matter what form you take or what magic you cast. I just want to keep you safe when you come back to shore."

    menu:
        "Pull him down into a deep kiss and let him fasten the pendant.":
            $ barek_affection += 30
            $ barek_ending = "safe_harbor"
            jump barek_ending_true
        "Accept the pendant and pledge lifelong devotion as his anchor.":
            $ barek_affection += 20
            $ barek_ending = "grounded_tide"
            jump barek_ending_companion
        "Reject the token and tell him a Sanctum sorcerer has no place with a common dock worker.":
            $ barek_romance_locked = True
            $ barek_route_locked = True
            $ barek_ending = "lost_at_sea"
            jump barek_ending_failure


label barek_ending_true:
    "You step into Barek's chest, cup his jaw, and pull the towering sharkfolk into a tender kiss."
    "His arms wrap around your waist as he fastens the bone-and-glass pendant around your neck."
    barek "You're my safe harbor, sorcerer. Forever."
    mc "And you're mine, Barek. Whenever I come back to shore, I'm coming home to you."
    jump finish_barek_event


label barek_ending_companion:
    "You press the whalebone pendant over your heart and clasp Barek's broad hand."
    mc "No matter where my magic leads me, my heart will always rest down at these docks with you."
    barek "An anchor holds through every storm. You'll never weather a wave alone again, partner."
    jump finish_barek_event


label barek_ending_failure:
    mc "I'm a fully restored Sanctum sorcerer now. My place is among the high archmagi, not tied down to fishnets and dock workers."
    "The leather cord snaps in Barek's claw and the pendant falls into the black water below."
    barek "Forgive me, high sorcerer. I thought you were someone who saw past the surface."
    barek "I won't waste your time again."
    "Your bond with Barek is permanently severed."
    jump finish_barek_event


label barek_locked_conclusion:
    $ barek_ending = "wall_of_coral"
    "The wound left by your rejection in the market has not healed."
    "Barek's old gentleness is buried behind a distant, professional calm."
    barek "I'll make sure the docks cooperate with the Sanctum. That's all I can promise."
    "You part as distant allies, the possibility of a deeper bond lost."
    jump finish_barek_event
