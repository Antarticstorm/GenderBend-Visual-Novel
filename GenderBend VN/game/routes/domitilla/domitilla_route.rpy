# ============================================================
# COMMANDER DOMITILLA BRUNI ROUTE
# "Unbending Steel, Tender Hearth"
# ============================================================
# Requires:
#   domitilla_route_unlocked
#   domitilla_route_progress
#   domitilla_affection
#   domitilla_romance_locked
#   domitilla_route_locked
#   domitilla_ending
#   finish_domitilla_event
# ============================================================

label domitilla_chapter_1:

    call route_transition(
    "Domitilla Bruni",
    1,
    "Discipline and Iron"
)


    show domitilla angry at domitilla_size, char_center


    "At the Crestward Bastion's Iron Ring, Commander Domitilla Bruni drives a line of exhausted recruits through relentless drills."

    domitilla "Wider stance! If a harbor drake hits that shield wall, half of you are going into the bay! Again!"

    "Her eyes find you watching from the perimeter."

    "Without warning, she hurls a padded practice buckler directly at your chest."

    show domitilla talking
    domitilla "Hey! Sanctum scholar! Stop gawking from the cheap seats and get in the Ring!"

    menu:
        "Catch the buckler cleanly and strap it to your arm without breaking eye contact.":
            $ domitilla_affection += 20
            domitilla "Decent grip. At least you don't have butterfingers like these recruits."

        "Freeze the buckler in mid-air with kinetic magic and catch it casually.":
            $ domitilla_affection += 20
            domitilla "Fancy tricks. Let's see if that aura holds when eighty pounds of steel comes cracking down."

        "Catch it clumsily, recover immediately, and step into the pit.":
            $ domitilla_affection += 15
            domitilla "Lacks grace, but you didn't run away. Better than most bookworms."

    domitilla "Garrison rules, wizard. No lethal spells. Keep your feet planted, protect your core, and don't cry if you get a bruise."

    "Domitilla closes the distance with frightening speed, bringing her practice blade down in a brutal overhead strike."

    menu:
        "Reinforce the buckler with a kinetic barrier and absorb the blow head-on.":
            $ domitilla_affection += 20
            "The impact sends a shock through your arms, but your stance holds."
            show domitilla happy
            domitilla "Solid! You actually rooted your weight!"

        "Use a flash-light spell and pivot around her flank.":
            $ domitilla_affection += 20
            "Her strike misses as you ring your buckler against her backplate."
            show domitilla surprised
            domitilla "Clever footwork! Using the sun against me!"

        "Counter with kinetic force and lock weapons with her.":
            $ domitilla_affection += 20
            "You stand toe-to-toe in a contest of leverage."
            show domitilla happy
            domitilla "Look at you pushing back! Not bad, kid!"

    "Domitilla finally lowers her weapon, an approving smirk cutting across her scarred face."

    show domitilla happy
    domitilla "You've got actual iron in your spine, sorcerer. Come back when you want real training."

    menu:
        "I'll be back, Commander. Next time, don't hold back.":
            $ domitilla_affection += 20
            domitilla "Ha! I like the fire in your belly, wizard! The Ring is open to you anytime."

        "It's an honor to learn from the best warrior in Mirthhaven.":
            $ domitilla_affection += 15
            domitilla "A weapon is only as good as the hand holding it. You proved your hand is steady today."

        "I wanted to see the famous Commander Bruni in action.":
            $ domitilla_affection += 20
            "A flustered heat flashes briefly in her eyes."
            show domitilla surprised
            domitilla "Is that so? Don't be a stranger. I keep a close eye on people who catch my attention."

    hide domitilla
    jump finish_domitilla_event


label domitilla_chapter_2:

    call route_transition(
    "Domitilla Bruni",
    1,
    "Scars and Heavy Armor"
)

    show domitilla normal at domitilla_size, char_center


    "Late at night, you enter the Bastion's shadowed central armory carrying fire-resistant warding charms."

    "Domitilla sits alone on a workbench without her heavy plate armor, rubbing a dark bruise along her shoulder."

    domitilla "Armory is closed, soldier. Leave your requisition forms on the desk..."

    "She notices you."

    show domitilla surprised
    domitilla "Ah. It's you, wizard. Fourteen hours in full plate will make a woman blind to who's walking through the door."

    menu:
        "That looks like a nasty blow. Are you alright?":
            $ domitilla_affection += 20
            mc "That bruise looks painful, Domitilla."
            domitilla "Took a bad hit during drills. It's nothing I haven't slept off before."

        "The armor charms can wait. It looks like you need attention more.":
            $ domitilla_affection += 20
            mc "Let me see that shoulder."
            domitilla "Direct and attentive. I can respect that."

        "Even the unbreakable Commander Bruni needs a tune-up after shift?":
            $ domitilla_affection += 15
            show domitilla happy
            domitilla "Keep your voice down, scholar. You'll ruin my terrifying reputation."

    "You produce a jar of magic-infused warming salve."

    mc "Sit still and let me help."

    "After a hesitant pause, Domitilla rolls back her sleeve and lets you work the balm into her bruised shoulder."

    "Her rigid military posture slowly begins to dissolve."

    menu:
        "Trace the edge of one of her scars with genuine respect.":
            $ domitilla_affection += 20
            mc "You've fought in a lot of hard battles to earn these."
            domitilla "Northern Passes. Took a crossbow bolt holding the ridge."

        "Focus on easing the deep knots in her muscles.":
            $ domitilla_affection += 20
            mc "Breathe through it. Your muscles are practically locked up."
            show domitilla happy
            domitilla "Gods above... that magic of yours is a miracle, wizard."

        "Tell her she doesn't always have to bear the brunt of every hit.":
            $ domitilla_affection += 25
            domitilla "If I don't take the hit... someone weaker does. That's the duty."

    "Domitilla looks down at her calloused hands."

    show domitilla normal
    domitilla "In the garrison, everyone looks to me as an unbreakable wall."

    domitilla "It's... rare for anyone to ask if the wall ever gets tired."

    menu:
        "Then let me hold up the wall tonight. You can just rest.":
            $ domitilla_affection += 25
            mc "The garrison can survive without their wall for a few hours."
            domitilla "I... think I'll take you up on that offer, wizard. Just for tonight."

        "You're a human being before you're a commander. You deserve care too.":
            $ domitilla_affection += 25
            mc "You're allowed to be human."
            show domitilla happy
            domitilla "You see right through the armor, don't you? Thank you."

        "You're much softer under all that steel than you let on.":
            $ domitilla_affection += 20
            "A dark flush rises across her cheeks."
            show domitilla happy
            domitilla "Careful, wizard... say things like that, and I might keep you trapped in my armory all night."

    hide domitilla
    jump finish_domitilla_event


label domitilla_chapter_3:

    call route_transition(
    "Domitilla Bruni",
    3,
    "Off-Duty Fire"
)

    show domitilla happy at domitilla_size, char_center


    "At The Laughing Anchor, you find Domitilla completely out of uniform in a secluded corner booth."

    domitilla "Well, look what the tide washed in! Sit down, wizard!"

    domitilla "No drillmasters, no inspection reports, no council politics tonight. Just good brew and decent company."

    menu:
        "Raise a tankard to off-duty commanders and surviving another week.":
            $ domitilla_affection += 20
            domitilla "I'll drink to that! The recruits nearly drove me to execution duty on Tuesday!"

        "You look incredible out of your armor.":
            $ domitilla_affection += 25
            "A dark flush touches her cheeks."
            domitilla "Watch it, wizard. Flattery gets you extra laps... but I won't pretend I don't like hearing it."

        "Tell me some real campaign stories now that your recruits aren't listening.":
            $ domitilla_affection += 15
            domitilla "I've got stories that would make your Sanctum archmagi turn pale as chalk."

    "A drunken mercenary approaches the booth and insults both of you before aggressively reaching across the table."

    show domitilla angry
    domitilla "You've got three seconds to pull that filthy hand back before I—"

    menu:
        "Disarm him cleanly with a controlled kinetic spell.":
            $ domitilla_affection += 25
            "A precise pulse sends his mug into the trash and shoves him harmlessly away."
            jump domitilla_chapter_3_honorable

        "Step in front of Domitilla and repel him with a defensive barrier.":
            $ domitilla_affection += 25
            "Your barrier absorbs his shove and knocks him backward."
            jump domitilla_chapter_3_honorable

        "Use a cruel nerve-shredding hex to make an example of him.":
            $ domitilla_romance_locked = True
            $ domitilla_ending = "dishonorable_steel"

            "The mercenary collapses in agony. The tavern falls silent."

            show domitilla angry
            domitilla "Enough!"

            "Domitilla breaks your spell focus with a sharp strike to your wrist."

            domitilla "We use force to defend the innocent and enforce order—not to torture an unarmed drunkard for petty spite!"

            mc "I was defending you, Domitilla!"

            domitilla "That wasn't defense, sorcerer! That was sadism!"

            domitilla "I thought you had iron in your spine. Torture and cruel magic are the tools of cowards."

            "She leaves the tavern in bitter disappointment."

            hide domitilla
    jump finish_domitilla_event


label domitilla_chapter_3_honorable:

    "Domitilla sits back down, stunned that someone stepped in front of her for once."

    "She grabs your hand in a firm, lingering grip."

    show domitilla surprised
    domitilla "You... you stepped up when it counted."

    domitilla "I've spent fifteen years taking the blow for everyone in this city. Nobody steps in front of Commander Bruni. Nobody... except you."

    show domitilla happy
    domitilla "I like it. Gods help me... I really like it."

    menu:
        "Get used to it. From now on, you don't fight alone.":
            $ domitilla_affection += 30
            "You lace your fingers tightly with hers."
            domitilla "A true partner on the battlefield and off it... I'm holding you to that vow."

        "You protect the city—but who protects you? Let me be your vanguard.":
            $ domitilla_affection += 30
            domitilla "Consider yourself appointed, wizard. And I don't give up my vanguard easily."

        "You look awfully flustered for a Garrison Commander.":
            $ domitilla_affection += 20
            "Domitilla pulls you slightly closer by your collar."
            domitilla "Watch your tongue, scholar... or I'll show you exactly how a commander handles a teasing subordinate."

    hide domitilla
    jump finish_domitilla_event


label domitilla_chapter_4:

    call route_transition(
    "Domitilla Bruni",
    3,
    "The Sentinel's Vow"
)
    
    show domitilla normal at domitilla_size, char_center


    "At dusk, you join Domitilla on the rooftop ramparts of the Crestward Bastion overlooking Mirthhaven."

    domitilla "I was wondering when you'd arrive, wizard."

    if domitilla_romance_locked:
        jump domitilla_locked_conclusion

    menu:
        "Stand shoulder to shoulder with her and compliment the company.":
            $ domitilla_affection += 20
            mc "There's nowhere else in Mirthhaven I'd rather be right now."
            domitilla "Nor I."

        "Adjust the clasp of her cloak against the sea chill.":
            $ domitilla_affection += 20
            domitilla "Always looking out for me... I'm still not used to it."

        "Give her a playful salute and report for high-watch duty.":
            $ domitilla_affection += 15
            domitilla "At ease, scholar. Tonight, there are no commanders. Just us."

    "Domitilla unclasps the ancient bronze commander's crest from her cloak."

    show domitilla talking
    domitilla "When I took command fifteen years ago, they gave me this crest. It represents my blood, my oath, and my life."

    "She presses the warm bronze insignium into your palm."

    domitilla "A commander only passes this crest to one person in their lifetime—the person they trust with their absolute life."

    menu:
        "This is the highest honor you could ever give me.":
            $ domitilla_affection += 20
            mc "I won't ever take it for granted."
            domitilla "I know you won't. That's why it belongs in your hands."

        "I will guard fifteen years of your sacrifice with my life.":
            $ domitilla_affection += 20
            mc "I'll wear it as a reminder that I always have your back."
            domitilla "A true vanguard. I couldn't have chosen a better partner."

        "Are you sure? You've carried this shield alone for so long.":
            $ domitilla_affection += 20
            domitilla "I'm not giving up a burden, wizard. I'm choosing who I share my life with."

    domitilla "I spent my whole life training to be an unbreakable shield for Mirthhaven."

    show domitilla happy
    domitilla "I never thought I'd find someone who made me want to lay that heavy shield down... and just be a woman."

    domitilla "You fought your way through my armor, sorcerer... into my heart. And I am never letting you go."

    menu:
        "Pull her down into a deep kiss beneath the twilight sky.":
            $ domitilla_affection += 30
            $ domitilla_ending = "vanguard_of_the_heart"
            jump domitilla_ending_true

        "Accept the crest and pledge yourself as her lifelong vanguard partner.":
            $ domitilla_affection += 20
            $ domitilla_ending = "shield_bound_oath"
            jump domitilla_ending_companion

        "Return the crest and tell her your bond must remain one of noble allies.":
            $ domitilla_ending = "unyielding_watch"
            jump domitilla_ending_bittersweet


label domitilla_ending_true:

    show domitilla happy

    "You grab the lapels of Domitilla's cloak and pull the towering commander down into a fierce, breathless kiss."

    "Her arms wrap around your waist and lift you slightly from your feet."

    domitilla "By the gods... you really know how to take a commander's breath away."

    mc "You laid down your shield, Domitilla. Let me protect you now."

    domitilla "Not alone, wizard. We stand shoulder to shoulder. In the garrison, in the Sanctum, and in every night to come."

    hide domitilla
    jump finish_domitilla_event


label domitilla_ending_companion:

    show domitilla happy

    "You press the bronze crest firmly over your heart."

    mc "Wherever you ride, whatever wall you hold... my magic and my life are bound to yours."

    domitilla "A shield-bound oath... the strongest contract a vanguard can make."

    domitilla "You are my equal, my partner, and my closest companion."

    hide domitilla
    jump finish_domitilla_event


label domitilla_ending_bittersweet:

    show domitilla normal

    "You gently close Domitilla's fingers back over the bronze crest."

    mc "You are the finest warrior I have ever known, but my path lies with the Sanctum. I cannot be the lover you deserve."

    "Her military dignity settles over her features, tempered by quiet sadness."

    domitilla "I see... A clear, honest refusal. Spoken like a true soldier."

    "She presses a firm, respectful kiss to your forehead."

    domitilla "The garrison will always consider you one of our own."

    hide domitilla
    jump finish_domitilla_event


label domitilla_locked_conclusion:

    show domitilla angry

    $ domitilla_ending = "dishonorable_steel"

    "Domitilla meets you on the ramparts, but the warmth that once existed between you is gone."

    "Your use of cruel magic at The Laughing Anchor shattered the martial respect on which your relationship was built."

    domitilla "I can forgive mistakes made in battle. What I cannot ignore is cruelty chosen when restraint was possible."

    domitilla "You'll have the garrison's lawful cooperation, sorcerer. But my personal trust is no longer yours."

    "You part as distant professional allies."

    hide domitilla
    jump finish_domitilla_event
