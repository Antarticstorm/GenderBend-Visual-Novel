# ============================================================
# MAIN CHAPTER 1 — THE MISHAP & THE MASTER PLAN
# Full restoration from canonical writer document.
# Writer-facing branch/unlock/completion annotations are not shown to players.
# ============================================================

label chapter_1:

    call chapter_transition(1, "The Mishap & The Master Plan")
    # Opening narration / character introductions.
    show tansy happy at tansy_size, char_center
    show clara flirty at clara_size, char_left
    show elianna angry at elianna_size, char_right

    tansy "Record check, one two, three... Alright! Let's talk about my favorite star apprentice—the one currently running around Mirthhaven trying not to trip over their own spell-robe!"

    tansy "Meet our lead sorcerer-in-training: bright, ridiculously persistent, and entirely incapable of staying inside a classroom." 

    hide clara
    hide elianna

    show tansy talking at tansy_size

    tansy "While most Sanctum scholars spend four years glued to dusty spellbooks until they turn as grey as gargoyles, my apprentice learned magic the practical way—by getting dragged across all six districts of Mirthhaven running errands for my 'highly experimental' alchemy trials."

    tansy "Naturally, walking around a bustling port city with glowing magical reagents in your satchel means you tend to bump into... eccentric locals. Before the big potion disaster hit, they were just familiar faces around town:"

    show tansy surprised at tansy_size

    tansy "'Bo' Shen & Barek Tidejaw: Met 'em down at Nautilus Point while hunting for bioluminescent fish-scales." 
    tansy "Bo almost mistook my apprentice for a forge-bellows assistant, and Barek threatened to throw them into the harbor if they didn't stop levitating the dock crates. Standard greeting!"

    tansy "Clara & Tariq Vane: Bumps into them in the trade square. Tariq tried to sell them 'genuine dragon teeth'"
    tansy "(spoiler: painted shark teeth from Barek), while Clara took one look at their ragged apprentice cloak and offered a quick lesson on proper district diplomacy."
    
    show tansy talking at tansy_size

    tansy "Commander Domitilla Bruni: Knows them as 'that loud Sanctum kid who keeps setting off the Vanguard's anti-magic wards near the Iron Ring gate.'" 
    tansy "She threatened three days of guard duty, but secretly respects anyone who doesn't faint when she draws that massive sword."

    show tansy happy
    tansy "Ellianna Sylvane: The absolute saint of the Sanctum. Ellie is the only student with enough patience to help my apprentice mop up exploded potion cauldrons without reporting us to the Headmaster."

    hide tansy

    #Player name
    $ mc_name = renpy.input("What is your name?", default="")

    $ mc_name = mc_name.strip()

    if mc_name == "":
        $ mc_name = "Apprentice"
    # Scene 1 — Waking Up Under the Alchemy Glass
    # Location: The Solarium Sanctum — Tansy's Alchemy Lab
    # SFX: Sound Effect: Bubbling cauldrons, glass vials clinking, distant thunder of a small magical reaction
    "(You open your eyes to find the ceiling spinning. The air smells strongly of burnt cinnamon and ozone.)"
    "(As you sit up on the stone workbench, your hair feels unnaturally long, cascading past your shoulders.)"
    "(When you clear your throat, the sound that escapes your mouth is a high, soft melodic voice.)"
    # [MC]
    mc "Ngh... my head... Wait. What happened to my voice?!"
    "(You scramble to reach for a shiny silver flask on the table, staring at your reflection. The sharp face of a young male apprentice is gone—replaced by a strikingly beautiful young woman with bright, startled eyes.)"
    # [MC]
    mc "WHAT IN THE SANCTUM’S NAME—?!"
    "(A sudden burst of loud, unrestrained cackling echoes from behind a row of glowing green alembics.)"
    show tansy happy at tansy_size, char_center

    tansy "BHAHAHA! Oh, by the stars! Look at you! It took three weeks of trial and error, but the Aura-Shift Catalytic Broth actually worked!"
    "(Tansy strides over, resting her elbows on your bench with an enormous, wicked grin. She pokes your cheek with the feather end of her quill.)"
    # Source [SPRITE: Tansy — Excited, Mischievous]
    show tansy teasing
    tansy "Relax, my dear apprentice! You aren't dead, and your mana channels are completely intact."
    tansy "Sure, I accidentally spilled the catalyst into your morning tea instead of the testing beaker..."
    tansy "...but look at the silver lining! The magic is delightfully stable!"
    # [MC]
    mc "Tansy! You transformed me into a woman! How is this stable?!"
    # Source [SPRITE: Tansy — Dismissive, Laughing]
    show tansy teasing
    tansy "Details, details! An arch-mage never dwells on minor side effects."
    tansy "Besides, I already know the cure: the Alkahest of True Form."
    tansy "One swig of that golden brew, and you’ll be shifted back to your handsome old self in no time."
    "(She pulls a parchment roll from her leather coat and snaps it open with a flourish. A list of six complex ingredients is drawn in gold ink.)"
    # Source [SPRITE: Tansy — Informative, Proud]
    show tansy talking
    tansy "Here’s the catch, little wizard: brewing the Alkahest requires six rare catalyst ingredients scattered across Mirthhaven's districts."
    tansy "And since my hands are tied stabilizing the lab warding..."
    tansy "...you get to go on a city-wide scavenger hunt!"

    menu:
        "You used me as an accidental guinea pig again! You're brewing this cure with me, mentor or not!":
            show tansy happy
            tansy "That's the spirit! A little fire in your gut! Don't worry, I'll guide the final brewing myself. Now get moving before your voice stays octave-high forever~"
        "Six ingredients?! Tansy, I can barely walk in these robes right now!":
            show tansy teasing
            tansy "Oh, stop whining! You look adorable, and besides, consider this a practical test in adaptability. Master wizards don't sweat a wardrobe change!"
        "Fine. Hand over the list. The faster I get these ingredients, the faster I get my body back.":
            show tansy happy
            tansy "Ooh, pragmatic! I knew I picked the right apprentice. Here’s your first destination, hotshot!"
    # [SCENE CONTINUES]
    # Source [SPRITE: Tansy — Direct, Pointing]
    show tansy talking
    tansy "Your first stop is The Wanderlust Wheel in the central merchant district. Go find Clara Vane."
    tansy "She holds the first key to our brew: Sunstone Powder."
    tansy "Tell her Tansy sent you—and try not to trip over your new hemline on the way out!"
    # SFX: Sound Effect: Door slamming, footsteps hurrying out
    hide tansy

    # Scene 2 — Tea & Sympathy at The Wanderlust Wheel
    show clara normal at clara_size, char_center
    # SFX: Sound Effect: Gentle merchant bells ringing, quiet chatter of traders, warm fireplace crackling
    "(You enter the cozy, oak-paneled headquarters of the merchant guild. Maps and velvet cases cover the walls. Clara Vane stands behind a large polished desk, carefully reviewing a ledger.)"
    # Source [SPRITE: Clara Vane — Warm, Welcoming]
    show clara happy
    clara "Welcome to The Wanderlust Wheel! How can the guild help you today, young lady—"
    "(Clara pauses, taking in your frantic expression, your oversized sorcerer robes, and the unmistakable Sanctum apprentice crest pinned to your cloak.)"
    # Source [SPRITE: Clara Vane — Surprised -> Amusement]
    show clara surprised
    clara "Wait... those robes. That magic signature... Is that you, little apprentice?"
    # [MC]
    mc "Clara... please don't laugh. Tansy spiked my tea with an untested catalytic broth."
    # Source [SPRITE: Clara Vane — Laughing Softly, Chuckling]
    show clara happy
    clara "Oh, my poor dear! Tansy strikes again!"
    "(Clara walks around her desk, gently taking your arm and guiding you to a plush velvet armchair by the hearth. She pours a steaming cup of spiced tea and places it in your hands.)"
    # Source [SPRITE: Clara Vane — Gentle, Comforting]
    show clara talking
    clara "Drink this. It will settle your nerves."
    clara "That woman is a absolute force of nature, but she certainly keeps life in Mirthhaven entertaining."
    clara "Now, tell me—what did she send you here for?"
    # [MC]
    mc "She needs Sunstone Powder from your guild vault to stabilize the Alkahest of True Form."

    menu:
        "I'm mortified... Walking across the district in this body was an utter nightmare.":
            show clara sad
            clara "There’s no need to feel embarrassed here, dear. You look lovely, but more importantly, your dignity is intact. We’ll get you fixed up in no time."
        "Tansy’s lucky I respect her as a master, or I’d turn her lab into a frog pond.":
            show clara happy
            "(Laughs heartily)"
            clara "Oh, I’d pay good guild gold to see Tansy as a frog! But hold off on the transfiguration until after she brews your cure."
        "How do you deal with people like Tansy without losing your mind, Clara?":
            show clara teasing
            clara "Patience, tea, and keeping a firm lock on my trade vaults! Mirthhaven is full of wild talents; you learn to roll with their tide."
    # [SCENE CONTINUES]
    # Source [SPRITE: Clara Vane — Helpful, Smiling]
    show clara talking
    clara "Luckily for you, Sunstone Powder is something I can authorize directly. Consider it a gift from the guild to set right Tansy's chaos."
    "(Clara pulls a small iron key from her apron, unlocks a decorative wall safe, and retrieves a velvet pouch filled with shimmering, golden dust. She places it securely into your hands.)"
    # Source [SPRITE: Clara Vane — Reassuring]
    show clara happy
    clara "Here you are. Ingredient number one: Sunstone Powder. One step closer to your true form."
    # SFX: Sound Effect: Door creaking open softly, light footsteps strolling in

    # Scene 3 — A Sly Shadow Steps In
    # Tariq has no sprite asset yet; Clara remains visible.
    "(A smooth, fox-like voice cuts through the quiet room as a tall, sharp-dressed man leans lazily against the doorframe, flipping an obsidian coin between his fingers.)"
    # Source [SPRITE: Tariq Vane — Sly, Mischievous, Smirking]
    tariq "Now what do we have here? Dear sister, since when did we start giving away vault catalysts to mysterious, pretty sorceresses?"
    # Source [SPRITE: Clara Vane — Sighing, Fond]
    show clara teasing
    clara "Tariq... do behave. This is Tansy's apprentice. There was an... accidental potion mishap this morning."
    "(Tariq pushes off the doorframe, strolling closer with a slow, deliberate stride. His dark eyes sparkle with sharp amusement as he inspects you from head to toe.)"
    # Source [SPRITE: Tariq Vane — Teasing, Intrigued]
    tariq "An accident? Well, well... I'd call it an upgrade, little wizard. You carry the look surprisingly well."
    # [MC]
    mc "I’m not looking for compliments, Tariq. I’m looking for cure ingredients."
    # Source [SPRITE: Tariq Vane — Cryptic, Smirking]
    tariq "Oh, I know. I saw the parchment in your cloak pocket."
    tariq "But if you think Sunstone Powder is hard to get, wait until you try finding the Midnight Lotus Petal in the Sun-Gilded Market."
    tariq "The contraband merchants don't hand those out for tea and smiles."
    "(Tariq leans in slightly, his voice dropping to an intriguing whisper as his coin catches the firelight.)"
    # Source [SPRITE: Tariq Vane — Playful, Challenging]
    tariq "When you're ready for a real deal, come find me in the backroom stalls. That is... if you've got the wits to bargain with a fox."

    menu:
        "Careful, Tariq. You might find out this 'pretty sorceress' can out-think your best shadow deal.":

            "(You match his smirk.)"
            # Source [SPRITE: Tariq Vane — Deeply Impressed, Sharp Smile]
            tariq "Ha! Fire and sharp wit... Now that is my favorite combination."
            "(Tariq steps back, executing a smooth, theatrical bow, catching his obsidian coin effortlessly.)"
            tariq "I do love a customer with backbone. Don't keep me waiting too long in the market, little wizard. I'll make sure to reserve a front-row stall just for you."
            # Source [SPRITE: Clara Vane — Warm Smile]
            show clara happy
            clara "Good luck on your search, apprentice. Keep your chin up—and don't let my brother overcharge you!"
            "(With the Sunstone Powder secured in your pouch and Tariq’s curiosity piqued, you step out of The Wanderlust Wheel with newfound confidence, ready to brave the docks of Nautilus Point.)"

            hide clara
            $ story_progress += 1
            $ chapter = 1
            $ setup_free_time(1)
            jump free_time
        "I'm here for business, not games. I'll earn that lotus petal fair and square when the time comes.":

            "(You stand firm and serious.)"
            # Source [SPRITE: Tariq Vane — Surprised -> Respectful Smirk]
            tariq "Fair and square? In the Sun-Gilded Market?"
            "(Tariq chuckles softly, pocketing his obsidian coin as he looks at you with newfound respect.)"
            tariq "A principled sorcerer. Rare breed in Mirthhaven. Very well... bring that iron resolve with you when you visit my stalls. You'll need every drop of it."
            # Source [SPRITE: Clara Vane — Proud Nod]
            show clara happy
            clara "You have a strong heart, apprentice. Take care down by the docks—Barek can be gruff, but he's a good soul."
            "(Holding the Sunstone Powder tightly, you march out of the guild hall with unwavering determination, ready to take on whatever challenges lie ahead at Nautilus Point.)"

            hide clara
            $ story_progress += 1
            $ chapter = 1
            $ setup_free_time(1)
            jump free_time
        "Just keep your coin tricks to yourself until I actually need your market stalls!":

            "(You grow flustered and huff.)"
            # Source [SPRITE: Tariq Vane — Highly Entertained, Wide Smirk]
            tariq "Oh, this is going to be far too much fun."
            "(Tariq winks at you, leaning back against the wooden pillar with a low laugh.)"
            tariq "Getting under your skin is already turning out to be the highlight of my week. See you at the market, little wizard—bring your temper, it makes the bargaining far livelier!"
            # Source [SPRITE: Clara Vane — Sympathetic Smile]
            show clara teasing
            clara "Ignore him, dear. Here's a spare cloak brooch to keep your robes tight while you walk down to Nautilus Point. Stay safe!"
            "(Flustered but holding ingredient number one—the Sunstone Powder—safely in hand, you hurry out of the office, eager to put distance between yourself and Tariq as you head toward the coastal breeze of Nautilus Point.)"

            hide clara
            $ story_progress += 1
            $ chapter = 1
            $ setup_free_time(1)
            jump free_time