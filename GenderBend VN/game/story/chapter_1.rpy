label chapter_1:

    # =========================
    # SCENE 1 - TANSY'S LAB
    # =========================

    "You open your eyes..."

    mc "Ngh... my head... Wait. What happened to my voice?!"

    # Rest of story...

    tansy "Here's the catch, little wizard..."

    # CHOICE 1
    # Does NOT affect the ending.

    menu:

        "You used me as an accidental guinea pig again! You're brewing this cure with me, mentor or not!":
            tansy "That's the spirit! A little fire in your gut!"

        "Six ingredients?! Tansy, I can barely walk in these robes right now!":
            tansy "Oh, stop whining! You look adorable..."

        "Fine. Hand over the list. The faster I get these ingredients, the faster I get my body back.":
            tansy "Ooh, pragmatic! I knew I picked the right apprentice."

    # All three choices automatically merge here.

    tansy "Your first stop is The Wanderlust Wheel..."



    # =========================
    # SCENE 2 - CLARA
    # =========================

    "You enter the cozy, oak-paneled headquarters..."

    clara "Welcome to The Wanderlust Wheel!"

    # Story continues...

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

    clara "Luckily for you, Sunstone Powder is something I can authorize directly."

    clara "Here you are. Ingredient number one: Sunstone Powder."



    # =========================
    # SCENE 3 - TARIQ
    # =========================

    tariq "Now what do we have here?"

    # Rest of Tariq scene...

    tariq "When you're ready for a real deal, come find me in the backroom stalls."



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

    jump chapter_2


label chapter_1_ending_b:

    tariq "Fair and square? In the Sun-Gilded Market?"

    "Tariq chuckles softly, pocketing his obsidian coin as he looks at you with newfound respect."

    tariq "A principled sorcerer. Rare breed in Mirthhaven. Very well... bring that iron resolve with you when you visit my stalls. You'll need every drop of it."

    clara "You have a strong heart, apprentice. Take care down by the docks—Barek can be gruff, but he's a good soul."

    "Holding the Sunstone Powder tightly, you march out of the guild hall with unwavering determination, ready to take on whatever challenges lie ahead at Nautilus Point."

    $ story_progress += 1

    jump chapter_2


label chapter_1_ending_c:

    tariq "Oh, this is going to be far too much fun."

    "Tariq winks at you, leaning back against the wooden pillar with a low laugh."

    tariq "Getting under your skin is already turning out to be the highlight of my week. See you at the market, little wizard—bring your temper, it makes the bargaining far livelier!"

    clara "Ignore him, dear. Here's a spare cloak brooch to keep your robes tight while you walk down to Nautilus Point. Stay safe!"

    "Flustered but holding ingredient number one—the Sunstone Powder—safely in hand, you hurry out of the office, eager to put distance between yourself and Tariq as you head toward the coastal breeze of Nautilus Point."

    $ story_progress += 1

    jump chapter_2