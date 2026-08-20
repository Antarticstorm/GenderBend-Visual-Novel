label chapter_1:

    call chapter_transition(1, "The Mishap & The Master Plan")
    # =========================
    # SCENE 1 - TANSY'S LAB
    # =========================

    $ mc_name = renpy.input("What is your name?", default="")

    $ mc_name = mc_name.strip()

    if mc_name == "":
        $ mc_name = "Apprentice"

    "(You open your eyes to find the ceiling spinning. The air smells strongly of burnt cinnamon and ozone.)"
    "(As you sit up on the stone workbench, your hair feels unnaturally long, cascading past your shoulders.)" 
    "(When you clear your throat, the sound that escapes your mouth is a high, soft melodic voice.)"

    mc "Ngh... my head... {w} Wait. What happened to my voice?!"

    "(You scramble to reach for a shiny silver flask on the table, staring at your reflection.)" 
    "(The sharp face of a young male apprentice is gone—replaced by a strikingly beautiful young woman with bright, startled eyes.)"
    
    mc "WHAT IN THE SANCTUM’S NAME—?!"

    "(A sudden burst of loud, unrestrained cackling echoes from behind a row of glowing green alembics.)"

    show tansy normal at tansy_size


    tansy "BHAHAHA! Oh, by the stars! Look at you! {w} It took three weeks of trial and error, but the Aura-Shift Catalytic Broth actually worked!"

    hide tansy

    "(Tansy strides over, resting her elbows on your bench with an enormous, wicked grin. She pokes your cheek with the feather end of her quill.)"

    tansy "Relax, my dear apprentice! You aren't dead, and your mana channels are completely intact. Sure, I accidentally spilled the catalyst into your morning tea instead of the testing beaker... but look at the silver lining! The magic is delightfully stable!"

    mc "Tansy! You transformed me into a woman! How is this stable?!"

    tansy "Details, details! An arch-mage never dwells on minor side effects. Besides, I already know the cure: the Alkahest of True Form. One swig of that golden brew, and you’ll be shifted back to your handsome old self in no time."

    "(She pulls a parchment roll from her leather coat and snaps it open with a flourish. A list of six complex ingredients is drawn in gold ink.)"


    tansy "Here’s the catch, little wizard: brewing the Alkahest requires six rare catalyst ingredients scattered across Mirthhaven's districts." 
    tansy "And since my hands are tied stabilizing the lab warding... {w} you get to go on a city-wide scavenger hunt!"

    # CHOICE 1
    # Does NOT affect the ending.

    menu:

        "You used me as an accidental guinea pig again! You're brewing this cure with me, mentor or not!":
            tansy "That's the spirit! A little fire in your gut!"

        "Six ingredients?! Tansy, I can barely walk in these robes right now!":
            tansy "Oh, stop whining! You look adorable..."

        "Fine. Hand over the list. The faster I get these ingredients, the faster I get my body back.":
            tansy "Ooh, pragmatic! I knew I picked the right apprentice."


    tansy "Your first stop is The Wanderlust Wheel in the central merchant district." 
    tansy "Go find Clara Vane. She holds the first key to our brew: Sunstone Powder."
    tansy "Tell her Tansy sent you—and try not to trip over your new hemline on the way out!"


    # =========================
    # SCENE 2 - CLARA
    # =========================

    "(You enter the cozy, oak-paneled headquarters of the merchant guild.)" 
    "(Maps and velvet cases cover the walls. Clara Vane stands behind a large polished desk, carefully reviewing a ledger.)"

    clara "Welcome to The Wanderlust Wheel! {w} How can the guild help you today, young lady—"

    "(Clara pauses, taking in your frantic expression, your oversized sorcerer robes, and the unmistakable Sanctum apprentice crest pinned to your cloak.)"

    clara "Wait... those robes. That magic signature... Is that you, little apprentice?"

    mc "Clara... please don't laugh. Tansy spiked my tea with an untested catalytic broth."

    clara "Oh, my poor dear! Tansy strikes again!"

    "(Clara walks around her desk, gently taking your arm and guiding you to a plush velvet armchair by the hearth. She pours a steaming cup of spiced tea and places it in your hands.)"

    clara "Drink this. It will settle your nerves. That woman is an absolute force of nature, but she certainly keeps life in Mirthhaven entertaining. Now, tell me—what did she send you here for?"

    mc "She needs Sunstone Powder from your guild vault to stabilize the Alkahest of True Form."

    # CHOICE 2
    # Also does NOT affect the ending.

    menu:

        "I'm mortified... Walking across the district in this body was an utter nightmare.":
            clara "There's no need to feel embarrassed here, dear."

        "Tansy's lucky I respect her as a master, or I'd turn her lab into a frog pond.":
            clara "Oh, I'd pay good guild gold to see Tansy as a frog!"

        "How do you deal with people like Tansy without losing your mind, Clara?":
            clara "Patience, tea, and keeping a firm lock on my trade vaults!"

    # All three merge again.

    clara "Luckily for you, Sunstone Powder is something I can authorize directly. Consider it a gift from the guild to set right Tansy's chaos."

    "(Clara pulls a small iron key from her apron, unlocks a decorative wall safe, and retrieves a velvet pouch filled with shimmering, golden dust. She places it securely into your hands.)"

    clara "Here you are. Ingredient number one: Sunstone Powder. One step closer to your true form."

    #SFX

    # =========================
    # SCENE 3 - TARIQ
    # =========================

    "(A smooth, fox-like voice cuts through the quiet room as a tall, sharp-dressed man leans lazily against the doorframe, flipping an obsidian coin between his fingers.)"

    tariq "Now what do we have here? Dear sister, since when did we start giving away vault catalysts to mysterious, pretty sorceresses?"

    clara "Tariq... do behave. This is Tansy's apprentice. There was an... accidental potion mishap this morning."

    "(Tariq pushes off the doorframe, strolling closer with a slow, deliberate stride. His dark eyes sparkle with sharp amusement as he inspects you from head to toe.)"

    tariq "An accident? Well, well... I'd call it an upgrade, little wizard. You carry the look surprisingly well."

    mc "I’m not looking for compliments, Tariq. I’m looking for cure ingredients."

    tariq "Oh, I know. I saw the parchment in your cloak pocket. But if you think Sunstone Powder is hard to get, wait until you try finding the Midnight Lotus Petal in the Sun-Gilded Market. The contraband merchants don't hand those out for tea and smiles."

    "(Tariq leans in slightly, his voice dropping to an intriguing whisper as his coin catches the firelight.)"

    tariq "When you're ready for a real deal, come find me in the backroom stalls. That is... if you've got the wits to bargain with a fox."

    # =========================
    # CHOICE 3 - IMPORTANT
    # =========================

    menu:

        "Careful, Tariq. You might find out this 'pretty sorceress' can out-think your best shadow deal.":
            $ chapter_1_ending = "promising_gambit"
            jump chapter_1_ending_a

        "I'm here for business, not games. I'll earn that lotus petal fair and square when the time comes.":
            $ chapter_1_ending = "unshakable_purpose"
            jump chapter_1_ending_b

        "Just keep your coin tricks to yourself until I actually need your market stalls!":
            $ chapter_1_ending = "easy_target"
            jump chapter_1_ending_c

label chapter_1_ending_a:

    tariq "Ha! Fire and sharp wit... Now that's my favorite combination."

    "Tariq steps back, executing a smooth, theatrical bow, catching his obsidian coin effortlessly."

    tariq "I do love a customer with backbone. Don't keep me waiting too long in the market, little wizard. I'll make sure to reserve a front-row stall just for you."

    clara "Good luck on your search, apprentice. Keep your chin up—and don't let my brother overcharge you!"

    "With the Sunstone Powder secured in your pouch and Tariq's curiosity piqued, you step out of The Wanderlust Wheel with newfound confidence, ready to brave the docks of Nautilus Point."

    $ story_progress += 1
    $ chapter = 1

    $ day = 1
    $ main_story_day = 3

    jump free_time


label chapter_1_ending_b:

    tariq "Fair and square? In the Sun-Gilded Market?"

    "Tariq chuckles softly, pocketing his obsidian coin as he looks at you with newfound respect."

    tariq "A principled sorcerer. Rare breed in Mirthhaven. Very well... bring that iron resolve with you when you visit my stalls. You'll need every drop of it."

    clara "You have a strong heart, apprentice. Take care down by the docks—Barek can be gruff, but he's a good soul."

    "Holding the Sunstone Powder tightly, you march out of the guild hall with unwavering determination, ready to take on whatever challenges lie ahead at Nautilus Point."

    $ story_progress += 1
    $ chapter = 1

    $ day = 1
    $ main_story_day = 3

    jump free_time


label chapter_1_ending_c:

    tariq "Oh, this is going to be far too much fun."

    "Tariq winks at you, leaning back against the wooden pillar with a low laugh."

    tariq "Getting under your skin is already turning out to be the highlight of my week. See you at the market, little wizard—bring your temper, it makes the bargaining far livelier!"

    clara "Ignore him, dear. Here's a spare cloak brooch to keep your robes tight while you walk down to Nautilus Point. Stay safe!"

    "Flustered but holding ingredient number one—the Sunstone Powder—safely in hand, you hurry out of the office, eager to put distance between yourself and Tariq as you head toward the coastal breeze of Nautilus Point."

    $ story_progress += 1
    $ chapter = 1

    $ day = 1
    $ main_story_day = 3

    jump free_time