# ============================================================
# BAO "BO" SHEN ROUTE
# "Liquid Gold & Dragon Fire"
# ============================================================
# Requires:
#   bao_route_unlocked
#   bao_route_progress
#   bao_affection
#   bao_romance_locked
#   bao_route_locked
#   bao_ending
#   finish_bao_event
# ============================================================

label bao_chapter_1:

    "After six hours of wand drills and rune-weaving, you enter The Laughing Anchor looking for dinner and somewhere quiet to rest."

    bao "HA! Well, look who finally escaped the library books! Hey! Sorcerer! Over here!"

    "The massive copper-scaled dragon-kin waves you toward a battered tavern table. Barek Tidejaw sits beside him."

    bao "Slide in! You look like you've been fighting parchment all day. Barkeep! Bring a fresh pitcher of the Dark Reserve for my friend here!"

    menu:
        "Slide onto the bench and take an appreciative gulp of the dark ale.":
            $ bao_affection += 15
            mc "Ah, that hits the spot! Exactly what I needed."
            bao "BHAHA! A real wizard knows how to appreciate good dark draught!"

        "Accept the seat and tease him about his impossibly loud greeting.":
            $ bao_affection += 15
            mc "I think they heard you all the way at the Sanctum tower."
            bao "Good! Let those dusty professors know my favorite spell-caster is off the clock!"

        "Take a cautious, curious sip of the heavy draught.":
            $ bao_affection += 10
            mc "This is much stronger than the honey-wine they serve at the academe."
            bao "That's because this is real Mirthhaven brew, kid! It puts fire right in your veins!"

    barek "Careful now, sorcerer. Big Long doesn't share his personal vault draught with just anyone."

    bao "Good ale is meant for good company!"

    "Bao launches into a proud story about his forge work. In his enthusiasm, his heavy tail catches an empty stool and knocks it over."

    "He freezes, visibly embarrassed."

    bao "Gah! Er... blast it. Wood's too flimsy in these places..."

    menu:
        "Laugh warmly and help him right the stool.":
            $ bao_affection += 20
            mc "Don't worry, Bo. The stool definitely started that fight!"
            bao "Ha! Right?! It practically jumped into my tail!"

        "Tease him that even master dragon-smiths can be defeated by a stool.":
            $ bao_affection += 15
            mc "White-hot dragon-fire can melt iron, but a tavern stool defeats the legendary smith?"
            bao "Hey now! Iron doesn't move when you aren't looking!"

        "Use a tiny levitation spell to flip the stool upright.":
            $ bao_affection += 15
            mc "Fixed. No damage done to your forge reputation."
            bao "Oho! Show-off! Clean spellwork, though."

    "A lively sea shanty erupts near the fireplace."

    "Bao drapes a broad, furnace-warm arm over your shoulders."

    bao "You're alright, sorcerer! Most Sanctum scholars act like a dragon's going to swallow them whole if I stand too close."

    bao "Come on! The night's young, the ale is cold, and the music's loud!"

    menu:
        "Sing the shanty at the top of your lungs and pound your mug in rhythm.":
            $ bao_affection += 20
            bao "BHAHAHA! YES! THAT'S WHAT I'M TALKING ABOUT!"
            barek "You two are going to tear the roof off this place."

        "Lean comfortably into his warm shoulder and raise your glass in a quiet toast.":
            $ bao_affection += 20
            mc "To good draught, better company... and dragon-smiths who know how to keep a table warm."
            bao "Heh... yeah. To good company."

        "Challenge Bao and Barek to a drinking speed-test.":
            $ bao_affection += 15
            mc "Let's see if a dragon can out-drink a sorcerer!"
            bao "O HO! A CHALLENGE?! You are playing with fire, sorcerer!"

    jump finish_bao_event


label bao_chapter_2:

    "Early the next morning, you arrive at The Furnace Pier carrying a hot thermos of herbal tonic and warm honey pastries."

    "Bao is hunched miserably over his anvil, trying and failing to ignite his forge."

    bao "Ghhhnnh... By the Ancients' anvil... my skull is being beaten with a hot sledgehammer..."

    mc "Having trouble starting the fire today, dragon-smith?"

    bao "S-Sorcerer?! What are you doing down at the pier this early?"

    menu:
        "Offer him the steaming hangover tonic with a reassuring smile.":
            $ bao_affection += 20
            mc "I brought something to quiet that sledgehammer in your head."
            bao "You walked all the way down from the Sanctum just to bring me medicine?"

        "Tease him about promising he could out-drink the entire tavern.":
            $ bao_affection += 15
            mc "You were shouting about melting iron with a single breath at midnight."
            bao "Gah! Don't remind me..."

        "Order him to sit down and stop trying to breathe fire.":
            $ bao_affection += 20
            mc "You're in no condition to be around live coals."
            bao "Yes, boss... whatever you say..."

    "Bao drinks the Sanctum recovery tonic. His shoulders immediately relax."

    bao "SWEET STARS ABOVE! That's absolute alchemy, kid!"

    "Barek arrives carrying dented ship plates and catches sight of you caring for Bao."

    barek "Well, well. Look at Mirthhaven's biggest dragon getting waited on hand and foot by a Sanctum sorcerer."

    bao "B-Barek! Don't go starting rumors!"

    menu:
        "If he keeps pushing himself, I might make this a daily delivery.":
            $ bao_affection += 20
            bao "D-Daily?! I... I mean... I wouldn't complain!"

        "I just don't like seeing someone I care about in pain.":
            $ bao_affection += 20
            barek "Aye. You're a good soul, wizard."

        "Don't worry—I'm charging him double in forge favors later.":
            $ bao_affection += 15
            bao "HA! Done! I'll forge you three daggers if you keep this tonic coming!"

    "After Barek leaves, Bao looks down at his broad, calloused hands."

    bao "People come here when they need my muscle, my fire, or my iron."

    bao "But nobody has ever dropped by just to check if I was doing okay."

    bao "Having you stand here with breakfast and medicine... it makes my chest burn hotter than my own furnace."

    menu:
        "Step close and gently wipe pastry sugar from his cheek.":
            $ bao_affection += 25
            mc "Let me take care of you for a change."
            bao "If this is what getting taken care of feels like... I think I'm the luckiest dragon in the world."

        "Sit beside him and lean your shoulder against his warm arm.":
            $ bao_affection += 20
            mc "With me, you can just be yourself."
            bao "Just me, huh? I like the sound of that."

        "Promise firmly that he will not have to face heavy days alone.":
            $ bao_affection += 20
            mc "As long as I'm in Mirthhaven, you're never going to face a heavy day alone again."
            bao "That's a promise I'm holding you to, sorcerer."

    jump finish_bao_event


label bao_chapter_3:

    "At midnight, you find Bao alone on The Laughing Anchor's ocean porch, cooling off beneath the stars."

    bao "Sorry... my internal furnace got a little too hot in there. Needed to let the sea breeze blow off the embers."

    menu:
        "Cast a gentle cooling spell around his shoulders.":
            $ bao_affection += 20
            bao "Ahhh... sweet stars, that feels incredible. You always know exactly what my fire needs."

        "Lean quietly against the railing beside him.":
            $ bao_affection += 20
            bao "Thanks... it's nice to just breathe for a second."

        "Tease Mirthhaven's loudest dragon-smith for retreating from his crowd.":
            $ bao_affection += 15
            bao "Even dragons get tired of roaring after a while, kid. Sometimes the quiet is better."

    "Bao's usual boisterous facade fades."

    bao "You ever look at a forge fire when the work is done?"

    mc "It goes quiet."

    bao "It goes quiet... but the coals stay hot."

    bao "I squander half my forge coin in that taproom because a dragon's fire feels terrible when it's burning in an empty room."

    menu:
        "You don't have to buy people's presence to be worthy of warmth.":
            $ bao_affection += 25
            mc "The people who truly care about you don't need a single drop of ale to stay."
            bao "I'm starting to realize that. Especially with you."

        "Place your hand over his massive fingers on the railing.":
            $ bao_affection += 25
            "His fingers turn upward and gently lace through yours."
            bao "Your hands... they hold onto me tighter than anyone else ever has."

        "So all those free rounds were an excuse to avoid a quiet house?":
            $ bao_affection += 15
            bao "Guess I was too stubborn to admit I was lonely."

    "Bao steps closer and gently cups your cheek."

    bao "Every coin I blow in that taproom... every barrel of dark draught in this city..."

    bao "I'd trade every last drop of it just to sit right here with you on a quiet night."

    menu:
        "Then trade it, Bo. I'm right here, and I'm not going anywhere.":
            $ bao_affection += 30
            "You kiss the center of his warm palm."
            bao "Then it's traded. Done deal. No refunds."
            "Bao wraps his arms around you, holding you against his broad chest."
            jump finish_bao_event

        "Let's build a real hearth together—one where your fire never feels lonely again.":
            $ bao_affection += 25
            mc "You don't need a crowded tavern. You just need someone who sees the real you."
            bao "A real hearth... with you. I never thought I'd get something so precious."
            jump finish_bao_event

        "That ale must be talking. You're just drunk and emotional—don't make this awkward.":
            $ bao_romance_locked = True
            $ bao_ending = "flame_extinguished"

            "The warmth radiating from Bao's scales instantly vanishes."

            bao "I... I see."

            bao "Right. Ha... yeah. Just drunk rambling from a big stupid lizard, right?"

            bao "Forget I said anything."

            "Bao disappears back into the tavern. His trust has been badly damaged."

            jump finish_bao_event


label bao_chapter_4:

    "At sunset, you return to Bao's forge at The Furnace Pier."

    "Bao sets down his sledgehammer and looks toward you with open admiration."

    bao "Ah... there you are, sorcerer. Right on time."

    if bao_romance_locked:
        jump bao_locked_conclusion

    menu:
        "Take his cloth and gently wipe the soot from his cheek.":
            $ bao_affection += 20
            bao "Heh... you always did have the gentlest hands in Mirthhaven, kid."

        "Take in the peaceful forge at sunset.":
            $ bao_affection += 15
            mc "The forge looks beautiful at sunset."
            bao "Aye... but it's only beautiful because you're standing in it."

        "You look like a dragon waiting on a very important appointment.":
            $ bao_affection += 15
            bao "Guilty as charged! When you're waiting on the person who owns your heart, every minute feels like a week!"

    bao "Notice anything different about the tavern lately?"

    mc "Barek mentioned you haven't been staying late drinking all week."

    bao "Aye. Every evening after the pier closes, I've stayed right here at this anvil, working completely sober."

    "Bao unwraps a small object from dark crimson velvet."

    "Inside is a custom-forged dragon-steel ring inlaid with fiery garnets."

    bao "I spent five nights forging this. No alcohol, no shortcuts... just precise temper-work and every ounce of love I have in my chest."

    bao "I forged it to carry a tiny fraction of my dragon-kin warmth, so even when we're apart, you'll always feel my hearth holding onto you."

    menu:
        "Trace your fingers over the glowing garnets in wonder.":
            $ bao_affection += 20
            mc "It's radiant, Bo. The steel feels warm."
            bao "That's my soul-spark woven into the grain. It'll never go cold."

        "Tell him how deeply touched you are that he spent his sober hours making it.":
            $ bao_affection += 20
            mc "You gave up your tavern nights to craft this for me?"
            bao "I didn't give up anything. I traded noisy beer barrels for the best hours of my life."

        "Bo... is this a pledge?":
            $ bao_affection += 20
            bao "It's the only pledge that ever mattered to me."

    bao "I don't need a crowded tavern or a barrel of dark draught to feel good anymore."

    bao "As long as I've got you by my side... my flame is complete."

    menu:
        "Offer your ring finger and accept his heart completely.":
            $ bao_affection += 30
            $ bao_ending = "ember_of_the_hearth"
            jump bao_ending_true

        "Wear the ring on a chain and pledge to stand beside him as an equal guardian.":
            $ bao_affection += 20
            $ bao_ending = "guardian_flame"
            jump bao_ending_companion

        "Tell him this is too much and that a Sanctum sorcerer cannot be tied down to a blacksmith.":
            $ bao_romance_locked = True
            $ bao_route_locked = True
            $ bao_ending = "cracked_dragon_steel"
            jump bao_ending_failure


label bao_ending_true:

    mc "Put it on me, Bo. My heart belongs to your hearth—forever."

    "Bao slides the dragon-steel ring onto your finger. The garnets flare with honey-gold light."

    bao "AHA! MY STAR! MY HEART!"

    "He lifts you into his arms and you pull him into a deep kiss against the sunset."

    bao "I swear on my dragon blood and my forge fire... I will love you and protect you until the stars burn out of the sky."

    jump finish_bao_event


label bao_ending_companion:

    "You thread the dragon-steel ring onto a silver chain and secure it around your neck."

    mc "We stand together—your fire and my magic, guarding this city shoulder to shoulder."

    bao "An anchor and a guardian flame... Aye. That's a bond stronger than tempered iron."

    bao "Whenever you need a hearth to rest your head... I'm right here with you, my partner."

    jump finish_bao_event


label bao_ending_failure:

    "You pull your hand away."

    mc "Bo... stop. This is way too much. I'm a Sanctum sorcerer with a grand destiny, and you're just... a tavern smith."

    "The golden light in Bao's eyes dies. The dragon-steel ring cracks in his hand and its garnets turn black."

    bao "Just... a tavern smith..."

    bao "I thought what we had was real. I thought I was worth more to you than a free drink."

    bao "Get out of my forge, sorcerer. Go chase your grand destiny... and don't come back to the pier."

    "Your bond with Bao is permanently severed."

    jump finish_bao_event


label bao_locked_conclusion:

    $ bao_ending = "flame_extinguished"

    "The wound left by your rejection on the ocean porch has not healed."

    "Bao remains distant. The easy warmth that once existed between you is gone."

    bao "No hard feelings, sorcerer. But some fires... once they're put out, they don't light the same way twice."

    "You leave the forge as acquaintances rather than partners."

    jump finish_bao_event
