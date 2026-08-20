label chapter_3:

    call chapter_transition(3, "Shadow Bargains & The Crucible")
    # =========================
    # SCENE 1 - Shaded Silk & Cursed Trinkets
    # =========================

    # Location: The Sun-Gilded Market - Tariq's Backroom Stall
    # (Sound Effect: Distant market shouting, exotic sitar music, rustling silk curtains, scent of burning incense and cloves)

    "(You navigate through the dense crowds of the Sun-Gilded Market, pushing past canopy stalls laden with spice mounds and embroidered tapestries. In a quiet, shaded alley behind a jeweler's tent, Tariq Vane sits lazily atop a pile of velvet cushions, spinning a dark glass vial between his fingers.)"

    # [SPRITE: Tariq Vane - Sly, Smirking]
    tariq "Right on time, little wizard. I must say, news travels fast—word on the cobblestones says you helped haul a leviathan net and stood down a dragon's breath at the docks."

    mc "I don't have time for gossip, Tariq. I need the Midnight Lotus Petal."

    # [SPRITE: Tariq Vane - Playful, Amused]
    tariq "Direct. I like that. But in this market, nothing of true value is simply handed over. A real trade requires a demonstration of good judgment."

    "(Tariq gestures toward a nearby stall where an oily merchant in opulent silk robes is aggressively hawking a dark, pulsing gem to an anxious young couple.)"

    # [SPRITE: Tariq Vane - Serious, Observant]
    tariq "See that merchant? He's selling 'Blessed Sun-Gems' that supposedly cure blood-fever. In truth, it's a cursed leech-stone that drains mana from unsuspecting buyers. I don't tolerate poisonous scammers in my market district... but revealing him myself ruins my shadow business."

    mc "You want me to expose him?"

    # [SPRITE: Tariq Vane - Smirking]
    tariq "I want you to use your sorcery to unmask his scam fairly and cleanly. Do that, and the Midnight Lotus Petal is yours."

    # CHOICE 1
    menu:

        "(Cast Aura-Sight to project the hidden dark curse as a visible black smoke above the gem)":
            "(You channel mana into your eyes, casting a bright revelation ward. A dark, oily shadow erupts from the gem, hovering in the air for all the market buyers to see.)"

            tariq "Magnificent! A public illusion burst—nothing exposes a liar faster than visual evidence!"

        "(Publicly challenge the merchant, tricking him into touching the gem's core spell himself)":
            "(You step up and loudly compliment the gem, asking the merchant to demonstrate its curing power on his own palm. Panicked, the merchant backs away, dropping the gem in terror.)"

            tariq "Ha! Out-witted by his own greed! Brilliant psychology, apprentice!"

        "(Use a subtle kinetic flick to disrupt his containment rune, causing the gem to flare harmlessly)":
            "(A tiny pulse of kinetic mana shoots from your fingers, snapping the merchant's hidden illusion spell. The 'blessed gem' instantly dulls into a worthless lump of lead.)"

            tariq "Clean, quiet, and decisive. You cut the magic right out from under him!"

    # (Sound Effect: Gasps from the market crowd, scammer fleeing in panic)

    "(Tariq slides down from his cushions, walking over with a smooth, approving stride. From beneath his cloak, he pulls a velvet box containing a dark purple flower petal that glimmers like a starlit night sky.)"

    # [SPRITE: Tariq Vane - Respectful, Handing Over Item]
    tariq "A deal's a deal, sorcerer. Ingredient number four: Midnight Lotus Petal. You've earned my respect... now go give the military mages at the fortress a run for their money."

    # =========================
    # SCENE 2 - The Iron Ring
    # =========================

    # Location: The Crestward Bastion - Training Grounds
    # (Sound Effect: Heavy iron boots stomping, clashing steel, booming shouts, dust kicking up)

    "(You enter the formidable stone fortress of The Crestward Bastion. In the center of the dusty parade grounds stands Commander Domitilla Bruni—a towering, seven-foot-tall knight draped in black iron plate armor, resting a giant wooden practice greatsword against her shoulder.)"

    # [SPRITE: Commander Bruni - Intimidating, Stern]
    bruni "LIFT THOSE SHIELDS, RECRUITS! IF YOUR ARMS ARE BLEEDING, IT MEANS YOU'RE STILL ALIVE!"

    "(Bruni turns her gaze toward you. Her fierce golden eyes lock onto your sorcerer robes with heavy disdain.)"

    # [SPRITE: Commander Bruni - Unimpressed, Gruff]
    bruni "Halt right there, scholar! This is a military stronghold, not the academe library. State your business before I put a wooden blade in your hands!"

    mc "Commander Bruni. I require Steel-Core Marrow from your armory vault to complete an essential reversal brew."

    # [SPRITE: Commander Bruni - Booming Laughter]
    bruni "BWAHAHA! Military-grade Steel-Core Marrow?! That metal is reserved for knight armor, not soft wizard alchemy! I don't give Bastion iron to students who hide behind parchment!"

    "(Bruni slams the tip of her massive wooden greatsword into the dirt, causing a small shockwave to rumble through the ground.)"

    # [SPRITE: Commander Bruni - Challenging, Fierce]
    bruni "If you want that marrow, step into The Iron Ring! Survive three minutes against my blade without running away, and you'll earn your prize. Refuse, and walk home empty-handed!"

    # CHOICE 2
    menu:

        "(Step directly into the dirt ring, drawing your staff with absolute combat readiness)":
            bruni "HA! No hesitation! You've got blood in your veins after all, wizard!"

        "(Analyze her heavy plate armor and footwork to calculate her attack angles first)":
            bruni "Studying your opponent? Good! But vision won't save you when three hundred pounds of oak comes swinging!"

        "(Try to negotiate a magical duel instead of a martial sparring match)":
            bruni "Negotiate?! This is a battlefield, scholar! Steel doesn't negotiate!"

    # (Sound Effect: Heavy iron bell ringing, roaring recruits surrounding the ring)
    # [SPRITE: Commander Bruni - Fierce, Charging]

    bruni "TIME STARTS NOW! SHOW ME YOUR GRIT!"

    "(Bruni lunges forward with terrifying speed for her size, sweeping her massive wooden sword around in a crushing arc aimed directly at your torso!)"

    # =========================
    # SCENE 3 - The Crucible of Steel
    # =========================

    # Location: The Crestward Bastion - The Iron Ring Arena
    # (Sound Effect: Whooshing wind from giant sword swing, crackling mana barriers, dust cloud billowing)

    "(You leap backward, barely dodging her first two heavy thrusts. The wooden blade whistles through the air like a catapult projectile. Two minutes tick by as you dodge and deflect her relentless onslaught with defensive wards.)"

    # [SPRITE: Commander Bruni - Grinning, Preparing Finisher]
    bruni "FINAL TEN SECONDS! LET'S SEE IF YOUR MAGIC CAN HOLD UP TO REAL POWER!"

    "(Bruni leaps high into the air, raising her giant greatsword above her head with both hands. She descends like a falling anvil, bringing her full seven-foot mass down in her signature finisher: the Granite-Breaker Overhead Crush!)"

    # (Sound Effect: Deafening roar, air pressure dropping, sword descending rapidly)

    # CHOICE 3 - CRITICAL CHOICE
    menu:

        "(Weave an angled kinetic barrier at a 45-degree slope to deflect her blade momentum into the dirt)":
            $ chapter_3_ending = "victory_of_mind_and_shield"
            jump chapter_3_ending_a

        "(Anchor your boots with earth magic, reinforcing your shield to absorb the shockwave head-on through grit)":
            $ chapter_3_ending = "tested_in_fire"
            jump chapter_3_ending_b

        "(Cast a simple flat glass shield directly above your head to block her full downward weight dead-on without angling or dodging)":
            $ chapter_3_ending = "broken_shield"
            jump chapter_3_ending_c


label chapter_3_ending_a:

    # (Sound Effect: CRASH! Wood sliding off angled magic barrier, heavy thud into earth)

    "(Bruni's massive wooden sword strikes your angled barrier, sliding harmlessly down the sloped magic plane and burying deeply into the dirt floor. Her momentum pulls her forward, leaving her completely open as the timer bell rings.)"

    # (Sound Effect: Loud iron bell ringing thrice)
    # [SPRITE: Commander Bruni - Stunned -> Booming Approval]

    bruni "WHAT?! Deflected my Granite-Breaker with a sloped ward?!"

    "(Bruni pulls her blade from the dirt and throws her head back in a thunderous roar of laughter.)"

    bruni "OUTSTANDING! Brilliant combat tactics! You didn't just survive—you completely outmaneuvered me!"

    "(Bruni reaches into her armor belt and tosses a heavy, gleaming ingot of black metal to you.)"

    bruni "Ingredient number five: Steel-Core Marrow! You earned it, sorcerer! Any time you want a real commission in the Vanguard, my doors are open!"

    $ story_progress += 1
    $ chapter = 4

    jump chapter_4


label chapter_3_ending_b:

    # (Sound Effect: EXPLOSIVE IMPACT! Heavy wooden shockwave reverberating)

    "(Your anchored boots dig six inches into the dirt as her giant blade smashes against your reinforced barrier. The ground shatters beneath you, but your posture holds firm. The timer bell rings just as her strike dissipates.)"

    # (Sound Effect: Loud iron bell ringing thrice)
    # [SPRITE: Commander Bruni - Deeply Impressed, NDT Nod]

    bruni "BY THE GODS! You absorbed my full overhead blow and stayed standing?!"

    "(Bruni lowers her sword, wiping sweat from her brow with a grin of genuine military respect.)"

    bruni "You've got raw iron in your core, scholar! Few recruits can take a hit like that without breaking a shoulder. Here is your Steel-Core Marrow—use it well!"

    $ story_progress += 1
    $ chapter = 4

    jump chapter_4


label chapter_3_ending_c:

    # (Sound Effect: DEAFENING GLASS SHATTER! BONE-CRUNCHING IMPACT!)

    "(The flat, unyielding magic shield shatters instantly under three hundred pounds of descending oak and armor weight. The force of the strike smashes directly into your staff, snapping the polished wood in half and sending you flying backward across the ring!)"

    # (Sound Effect: Heavy crash into stone wall, groaning in pain, coughing)

    mc "Ghhk—! Aaggh!"

    "(You collapse onto the dirt, clutching your bruised ribs and gasping for air. Your staff lies shattered in two pieces beside you, and your mana channels throb with severe magic backlash.)"

    # [SPRITE: Commander Bruni - Disappointed, Frowning]
    bruni "FOOLISH! A flat shield against an overhead crush?! Did they teach you nothing in the academe about force distribution?!"

    "(Bruni walks over, looking down at you with a scowl as recruits whisper in the background.)"

    bruni "You survived the three minutes only because I pulled my blow at the last fraction of a second. A real monster would have crushed your skull."

    "(She reaches into her belt and carelessly drops a chipped piece of Steel-Core Marrow into the dirt beside your bleeding hand.)"

    bruni "Take your marrow and get out of my ring. You have the ingredient, but you leave here with broken gear, bruised ribs, and zero honor. Learn how to fight properly before you get yourself killed."

    $ story_progress += 1
    $ chapter = 4

    jump chapter_4
