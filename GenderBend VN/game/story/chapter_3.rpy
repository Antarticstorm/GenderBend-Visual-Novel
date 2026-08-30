# ============================================================
# MAIN CHAPTER 3 — SHADOW MARKETS & THE CRUCIBLE
# Adjusted four-character version.
# ============================================================

label chapter_3:

    call chapter_transition(3, "Shadow Markets & The Crucible")

    show clara normal at char_center, clara_size
    # Scene 1: Shaded Silk & Cursed Trinkets
    # Location: The Sun-Gilded Market — Shade Alleys
    # [SCENE START]
    # SFX: Sound Effect: Distant market shouting, exotic sitar music, rustling silk curtains, scent of burning incense and cloves
    "(Holding Clara’s Guild Seal scroll, you navigate through the dense crowds of the Sun-Gilded Market, pushing past canopy stalls laden with spice mounds and embroidered tapestries.)"
    "(In a quiet alleyway, you spot an oily merchant in opulent silk robes aggressively hawking a dark, pulsing gem to an anxious young couple.)"
    # SFX: Sound Effect: Soft footsteps on cobblestone
    "(Clara Vane steps up beside you under the shade of a velvet canopy, watching the merchant with a sharp, stern glare.)"
    # Source [SPRITE: Clara Vane — Serious, Observant]
    show clara teasing
    clara "There he is."
    clara "He’s selling 'Blessed Sun-Gems' that supposedly cure blood-fever."
    clara "In truth, it’s a cursed leech-stone that drains mana from unsuspecting buyers."
    clara "I don't tolerate scams in our trade districts... show me how a Sanctum sorcerer handles a fraud, little wizard."
    # [MC]
    mc "Watch and learn, Guildmaster."

    menu:
        "Expose the curse with Aura-Sight.":
            "(Cast Aura-Sight to project the hidden dark curse as a visible black smoke above the gem)"
            show clara happy
            clara "Magnificent! A public revelation—nothing exposes a liar faster than visual evidence!"
        "Trick the merchant into exposing his own fraud.":
            "(Publicly challenge the merchant, tricking him into touching the gem's core spell himself)"
            show clara happy
            clara "Ha! Out-witted by his own greed! Brilliant psychology, apprentice!"
        "Disrupt the merchant's containment rune.":
            "(Use a subtle kinetic flick to disrupt his containment rune, causing the gem to flare harmlessly)"
            show clara normal
            clara "Clean, quiet, and decisive. You cut the spell right out from under him!"

    hide clara

    # SFX: Sound Effect: Gasps from the market crowd, scammer fleeing in panic
    "(Clara walks over with a smooth, approving stride. From beneath her cloak, she pulls a velvet box containing a dark purple flower petal that glimmers like a starlit night sky.)"
    # Source [SPRITE: Clara Vane — Respectful, Handing Over Item]
    show clara happy at clara_size, char_center
    clara "A deal’s a deal, sorcerer. Ingredient number four: Midnight Lotus Petal. You’ve earned my deep respect... now go give Commander Bruni at the fortress a run for her money!"

    hide clara
    # Scene 2: The Iron Ring
    # Location: The Crestward Bastion — Training Grounds
    # [SCENE START]
    # SFX: Sound Effect: Heavy iron boots stomping, clashing steel, booming shouts, dust kicking up
    "(You enter the formidable stone fortress of The Crestward Bastion.)"
    "(In the center of the dusty parade grounds stands Commander Domitilla Bruni—draped in black iron plate armor, resting a giant wooden practice greatsword against her shoulder.)"
    # Source [SPRITE: Commander Bruni — Intimidating, Stern]
    show domitilla angry at domitilla_size, char_right
    domitilla "LIFT THOSE SHIELDS, RECRUITS! IF YOUR ARMS ARE BLEEDING, IT MEANS YOU’RE STILL ALIVE!"
    "(Bruni turns her gaze toward you. Her fierce golden eyes lock onto your sorcerer robes.)"
    # Source [SPRITE: Commander Bruni — Unimpressed, Gruff]
    show domitilla angry
    domitilla "Halt right there, scholar! This is a military stronghold, not the academe library. State your business before I put a wooden blade in your hands!"
    # [MC]
    mc "Commander Bruni. I require Steel-Core Marrow from your armory vault to complete an essential reversal brew."
    # Source [SPRITE: Commander Bruni — Booming Laughter]
    show domitilla happy
    domitilla "BWAHAHA! Military-grade Steel-Core Marrow?! That metal is reserved for knight armor, not soft wizard alchemy! I don't give Bastion iron to students who hide behind parchment!"
    "(Bruni slams the tip of her massive wooden greatsword into the dirt, causing a small shockwave to rumble through the ground.)"
    # Source [SPRITE: Commander Bruni — Challenging, Fierce]
    show domitilla angry
    domitilla "If you want that marrow, step into The Iron Ring! Survive three minutes against my blade without running away, and you'll earn your prize. Refuse, and walk home empty-handed!"

    menu:
        "Step directly into the Iron Ring.":
            "(Step directly into the dirt ring, drawing your staff with absolute combat readiness)"
            show domitilla happy
            domitilla "HA! No hesitation! You've got blood in your veins after all, wizard!"
        "Study Domitilla's armor and footwork first.":
            "(Analyze her heavy plate armor and footwork to calculate her attack angles first)"
            show domitilla talking
            domitilla "Studying your opponent? Good! But vision won't save you when three hundred pounds of oak comes swinging!"
        "Try to negotiate a magical duel.":
            "(Try to negotiate a magical duel instead of a martial sparring match)"
            show domitilla talking
            domitilla "Negotiate?! This is a battlefield, scholar! Steel doesn't negotiate!"

    # SFX: Sound Effect: Heavy iron bell ringing, roaring recruits surrounding the ring
    # Source [SPRITE: Commander Bruni — Fierce, Charging]
    show domitilla talking
    domitilla "TIME STARTS NOW! SHOW ME YOUR GRIT!"
    "(Bruni lunges forward with terrifying speed, sweeping her massive wooden sword around in a crushing arc aimed directly at your torso!)"
    # Scene 3: The Crucible of Steel
    # Location: The Crestward Bastion — The Iron Ring Arena
    # [SCENE START]
    # SFX: Sound Effect: Whooshing wind from giant sword swing, crackling mana barriers, dust cloud billowing
    "(You leap backward, barely dodging her first two heavy thrusts.)"
    "(The wooden blade whistles through the air like a catapult projectile.)"
    "(Two minutes tick by as you dodge and deflect her relentless onslaught with defensive wards.)"
    # Source [SPRITE: Commander Bruni — Grinning, Preparing Finisher]
    show domitilla talking
    domitilla "FINAL TEN SECONDS! LET'S SEE IF YOUR MAGIC CAN HOLD UP TO REAL POWER!"
    "(Bruni leaps high into the air, raising her giant greatsword above her head with both hands.)"
    "(She descends like a falling anvil, bringing her full weight down in her signature finisher: the Granite-Breaker Overhead Crush!)"
    # SFX: Sound Effect: Deafening roar, air pressure dropping, sword descending rapidly

    menu:
        "Deflect the strike with an angled kinetic barrier.":
            "(You weave an angled kinetic barrier at a 45-degree slope to deflect her blade momentum into the dirt.)"
            # SFX: Sound Effect: CRASH! Wood sliding off angled magic barrier, heavy thud into earth
            "(Bruni’s massive wooden sword strikes your angled barrier, sliding harmlessly down the sloped magic plane and burying deeply into the dirt floor.)"
            "(Her momentum pulls her forward, leaving her completely open as the timer bell rings.)"
            # SFX: Sound Effect: Loud iron bell ringing thrice
            # Source [SPRITE: Commander Bruni — Stunned -> Booming Approval]
            show domitilla surprised
            domitilla "WHAT?! Deflected my Granite-Breaker with a sloped ward?!"
            "(Bruni pulls her blade from the dirt and throws her head back in a thunderous roar of laughter.)"
            show domitilla happy
            domitilla "OUTSTANDING! Brilliant combat tactics! You didn't just survive—you completely outmaneuvered me!"
            "(Bruni reaches into her armor belt and tosses a heavy, gleaming ingot of black metal to you.)"
            show domitilla happy
            domitilla "Ingredient number five: Steel-Core Marrow! You earned it, sorcerer! Any time you want a real commission in the Vanguard, my doors are open!"
            hide domitilla
            $ story_progress += 1
            $ setup_free_time(3)
            jump free_time
        "Anchor yourself and absorb the strike head-on.":
            "(You anchor your boots with earth magic, reinforcing your shield to absorb the shockwave head-on through grit.)"
            # SFX: Sound Effect: EXPLOSIVE IMPACT! Heavy wooden shockwave reverberating
            "(Your anchored boots dig six inches into the dirt as her giant blade smashes against your reinforced barrier.)"
            "(The ground shatters beneath you, but your posture holds firm.)"
            "(The timer bell rings just as her strike dissipates.)"
            # SFX: Sound Effect: Loud iron bell ringing thrice
            # Source [SPRITE: Commander Bruni — Deeply Impressed, NDT Nod]
            show domitilla surprised
            domitilla "BY THE GODS! You absorbed my full overhead blow and stayed standing?!"
            "(Bruni lowers her sword, wiping sweat from her brow with a grin of genuine military respect.)"
            show domitilla talking
            domitilla "You’ve got raw iron in your core, scholar! Few recruits can take a hit like that without breaking a shoulder. Here is your Steel-Core Marrow—use it well!"
            hide domitilla
            $ story_progress += 1
            $ setup_free_time(3)
            jump free_time
        "Block the full strike with a flat shield.":
            "(You cast a simple flat glass shield directly above your head to block her full downward weight dead-on without angling or dodging.)"
            $ chapter_3_bad_outcome = True
            # SFX: Sound Effect: DEAFENING GLASS SHATTER! BONE-CRUNCHING IMPACT!
            "(The flat, unyielding magic shield shatters instantly under three hundred pounds of descending oak and armor weight.)"
            "(The force of the strike smashes directly into your staff, snapping the polished wood in half and sending you flying backward across the ring!)"
            # SFX: Sound Effect: Heavy crash into stone wall, groaning in pain, coughing
            # [MC]
            mc "Ghhk—! Aaggh!"
            "(You collapse onto the dirt, clutching your bruised ribs and gasping for air. Your staff lies shattered in two pieces beside you, and your mana channels throb with severe magic backlash.)"
            # Source [SPRITE: Commander Bruni — Disappointed, Frowning]
            show domitilla angry
            domitilla "FOOLISH! A flat shield against an overhead crush?! Did they teach you nothing in the academe about force distribution?!"
            "(Bruni walks over, looking down at you with a scowl as recruits whisper in the background.)"
            show domitilla talking
            domitilla "You survived the three minutes only because I pulled my blow at the last fraction of a second. A real monster would have crushed your skull."
            "(She reaches into her belt and carelessly drops a chipped piece of Steel-Core Marrow into the dirt beside your bleeding hand.)"
            show domitilla talking
            domitilla "Take your marrow and get out of my ring."
            domitilla "You have the ingredient, but you leave here with broken gear, bruised ribs, and zero honor."
            domitilla "Learn how to fight properly before you get yourself killed."
            # [SCENE END]
            hide domitilla
            $ story_progress += 1
            $ setup_free_time(3)
            jump free_time