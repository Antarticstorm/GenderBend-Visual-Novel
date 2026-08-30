label chapter_2:

    call chapter_transition(2, "Muscle, Fire & The Docks")
    # =========================
    # SCENE 1 - Salt-Air & Strained Ropes
    # =========================

    #(Sound Effect: Seagulls squawking, heavy waves crashing against mossy wooden pilings, creaking ship timber)
    
    "(The salty breeze hits your face as you make your way down to the slippery cobblestones of Nautilus Point.)"

    "(The air is thick with the scent of brine, tar, and fish.)"

    "(Following Tansy's checklist, you search the lower piers until you spot a massive, muscular sharkfolk struggling near the water's edge.)"
    
    # (Sound Effect: Heavy splashing, straining wood, deep grunting)
    # [SPRITE: Barek Tidejaw — Strained, Frustrated]

    barek "Hnnrgh... Come on, you waterlogged piece of drift-oak... yield!"

    "(Barek Tidejaw, covered in sea spray and damp leather, has his massive clawed hands wrapped around a thick, iron-weighted leviathan net. The net is wedged tightly beneath a rotting wooden piling, trapping a fresh catch below the rising tide.)"

    mc "Need a hand down there?"

    "(Barek glances up over his shoulder, his gilled neck twitching in surprise as he takes in your         transformed form and sorcerer robes.)"

    # [SPRITE: Barek Tidejaw — Surprised, Gruff]
    
    barek "A Sanctum wizard? Down on the wet docks? Heh... Unless you've got three extra sets of arms under those long sleeves, little lady, magic won't lift three tons of snagged iron and oak!"

    mc "Watch me."

    # CHOICE 1

    menu:

        "(Cast a kinetic lift spell while bracing yourself alongside him on the wet pier)":
            "(You plant your boots on the slick timber, digging in beside the massive sharkfolk as blue kinetic energy coats your arms. With a synchronized grunt, you both heave.)"

            barek "HA! Look at that grit! You're stronger than you look, wizard!"

        "(Channel a precise magic pulse directly into the rotting piling to shatter the obstruction)":
            "(You extend your staff, firing a concentrated magic shockwave into the trapped wood. The rotten piling shatters into splinters, instantly freeing the net ropes.)"

            barek "Bwahaha! Clean shot! Saved me two hours of aching shoulders!"

        "(Use a levitation weave on the iron weights while instructing Barek when to pull)":
            "(You weave a glowing blue harness around the sunken iron weights, lifting their mass as you call out the cadence for Barek to hoist.)"

            barek "Smooth call! Work smart, not hard—I like how your mind operates!"
 
    # (Sound Effect: Heavy net splashing onto the cobblestones, fish flopping)
    
    "(Barek wipes sea foam from his brow with a thick forearm, giving you a booming, appreciative laugh that echoes over the wharves.)"

    # [SPRITE: Barek Tidejaw — Hearty, Grateful]

    barek "Well, I'll be damned! Most soft-handed scholars from the Sanctum wouldn't even step on these wet boards, let alone help haul leviathan mesh! What brings a sharp sorcerer like you down to my docks?"
    
    mc "I'm looking for a catalyst for a... temporary body restoration potion. Tansy sent me for a Luminescent Sea-Gland."
    # [SPRITE: Barek Tidejaw — Grinning, Generous]

    barek "Tansy's student, huh? That explains the sheer nerve! Lucky for you, today's catch brought in a deep-sea angler."

    "(Barek reaches into his belt pouch and pulls out a glowing, pearlescent orb that pulses with a calm, bioluminescent blue light. He presses it warmly into your palm.)"

    # [SPRITE: Barek Tidejaw — Warm, Welcoming]

    barek "Ingredient number two: Luminescent Sea-Gland, fresh from the depths. But you're not walking away just yet! You helped me save my haul—that means you're coming to The Laughing Anchor for a proper tavern toast!"

    # =========================
    # SCENE 2 - Foam & Dragon-Fire
    # =========================

    # Location: The Laughing Anchor — Main Taproom (Dusk)
    # (Sound Effect: Roaring crowd chatter, clinking heavy mugs, lively fiddle music, crackling hearth)
    
    "(The Laughing Anchor is packed to the rafters. Barek leads you to a large oak table near the fireplace where a towering, copper-scaled dragon-kin is currently draining a wooden pitcher of dark ale in one long gulp.)"

    # (Sound Effect: Slamming heavy pitcher on wood)
    # [SPRITE: Bao Zhao — Boisterous, Merry]
    bao "AHA! Outstanding brew! Hey, landlord! Bring another round for the house!"
    
    # [SPRITE: Barek Tidejaw — Laughing, Slapping Shoulder]
    barek "Bao, meet our savior of the day! This little sorcerer helped me pull three hundred pounds of net out of the bay!"
    
    "(Bao turns around, his golden reptilian eyes lighting up with playful curiosity as he looks you up and down.)"

    # [SPRITE: Bao Zhao — Intrigued, Smirking]
    bao "Well, well! A Sanctum scholar with actual muscle! Sit down, sit down! Any friend of Barek's is getting a mug of Mirthhaven's finest dark draught!"

    "(Before you can even take a seat, a familiar, chaotic voice pops up right over your shoulder.)"

    # (Sound Effect: Pop of magic smoke, light laughter)
    # [SPRITE: Tansy — Mischievous, Popping In]

    show tansy happy at tansy_size, char_right
    tansy "Did somebody say free drinks?! Don't mind if I do!"

    mc "Tansy?! What are you doing here?! You said you were stabilizing the lab!"
    # [SPRITE: Tansy — Carefree, Teasing]
    
    show tansy teasing
    tansy "Oh, the lab's fine! Just a few glowing bubbles left. I came to make sure my star apprentice hadn't turned into sea kelp! And look at you—you brought the sea-gland!"
    
    "(Tansy swigs a glass of ale, turning her wicked smirk toward the big dragon-smith.)"
    
    # [SPRITE: Tansy — Challenging, Smirking]
    show tansy teasing
    tansy "So, Bao... my student here needs a spark of your legendary draconic flame to harvest some Draconic Cinder-Ash. But I told them your forge fire's gotten a bit dim in your old age~"

    # [SPRITE: Bao Zhao — Roaring Laugh, Fiery Eyebrows]
    bao "DIM?! MY FLAME?! Ha! Them's fighting words, witch! I could ignite the ocean if I felt like it!"
    
    "(Bao leans across the table toward you, small plumes of warm smoke drifting from his nostrils.)"
    
    #CHOICE 2
    menu:
        "(Raise your mug and join in their rowdy tavern banter)":
            mc "Don't hold back on my account, Bao! Show my mentor what real fire looks like!" 
            bao "BHAHA! I like this kid! You've got real taproom spirit!"

        "(Use a small flame-shaping spell to dance sparks over your knuckles)" :
            mc "Careful, Bao. If your flame slacks, I might just have to ignite the cinder-ash myself." 
            bao "Oho! Showing off little sparks to a dragon? Bold move, wizard! I respect it!"

        "(Keep your cool and gently nudge Tansy back into her seat)" :
            mc "Tansy, stop poking the dragon. Bao, ignore her—we just need a controlled spark for the Alkahest." 
            bao "Ha! Controlled? Fair enough, but where's the fun without a little show?!"

    # [SPRITE: Bao Zhao — Focused, Grinning]

    bao "Alright, apprentice! Hold up your enchanted collection vial! Let's see if you can hold steady when a dragon breathes true heat!"

    "(Bao takes a deep breath, his chest expanding as glowing golden light shines through the copper scales along his throat and jaw.)"
    # (Sound Effect: Deep rumbling heat, roaring flame ignition)

    # =========================
    # SCENE 3 - Cinder & Steel
    # =========================

    # Location: The Laughing Anchor — Hearthside

    "(The air around the table turns scorchingly hot as Bao opens his mouth, exhaling a concentrated, brilliant stream of white-hot draconic flame. The fire swaths directly toward the enchanted brass-lined flask in your hands.)"

    # (Sound Effect: Roaring draconic fire, crackling magic wards)

    # [SPRITE: Tansy — Excited, Watching Close]

    tansy  "Hold it steady! Don't let the thermal shock crack the glass!"

    "(The intense heat radiates against your face, turning your cheeks flushed red. Glowing, crystalline ash begins to settle at the bottom of the flask, burning with embers of pure draconic magic.)"

    # Choice 3
    menu:
        "Hold the collection vial steady without flinching.":

            "(You hold the glass dead steady right next to his jaws without flinching a single inch.)"

            $ chapter_2_ending = "a_heart_of_the_forge"
            jump chapter_2_ending_a

        "Channel the ash with a heat-deflection ward.":

            "(You weave an elegant heat-deflection ward around your fingers to channel the ash cleanly.)"

            $ chapter_2_ending = "masterful_tempering"
            jump chapter_2_ending_b

        "Tease Bao about his dragon flame.":

            "(You laugh through the heat, teasing Bao that his dragon flame feels like a cozy hearth fire.)"

            $ chapter_2_ending = "wild_spark"
            jump chapter_2_ending_c


label chapter_2_ending_a:

    "Bao cuts off the flame, wiping a speck of ember from his lip as he looks at your steady, unyielding hands with absolute awe."

    bao "BY THE ANCIENTS! Not a flinch! Not a single shake!"

    "(Bao slaps his massive hand onto the wooden table, making the ale mugs jump.)"

    bao "You've got the heart of a master smith, apprentice!"

    bao "Most wizards back away the second my scales glow!"

    bao "That Draconic Cinder-Ash in your flask is as pure as it gets!"

    barek "To the bravest wizard in Mirthhaven! To the apprentice who doesn't back down!"

    "The whole table cheers as you cork the glowing flask, holding two completed ingredients while Barek and Bao toast to your fearlessness."

    hide tansy

    $ setup_free_time(2)
    jump free_time

label chapter_2_ending_b:

    "Tansy watches as your blue magic ward flawlessly weaves around Bao's intense fire, cooling the air just enough to trap every grain of cinder-ash without losing a drop."

    show tansy happy
    tansy "Flawless heat distribution! See that, boys? That's Sanctum precision right there!"

    bao "Heh... slick work, kid. You handled my fire like a seasoned spell-smith tempering rare steel. Clean, sharp, and smart."

    bao "Take that Draconic Cinder-Ash with pride. You earned it with real skill."

    "With your magic control praised by both your mentor and Mirthhaven's greatest smith, you secure your third ingredient with complete composure."

    hide tansy

    $ setup_free_time(2)
    jump free_time


label chapter_2_ending_c:

    "Bao stops breathing fire, blinking in utter shock before letting out a laugh so loud it shakes the tavern rafters."

    bao "A HEARTH CANDLE?! BHAHAHA!"

    bao "Did you hear that, Barek?! This little wizard just called my dragon breath a candle!"

    barek "You've met your match, Bao! You can't intimidate this one!"

    bao "You've got some nerve, kid! I love it! Here—take your Draconic Cinder-Ash before you make fun of my forge tools next!"

    "The taproom bursts into laughter as you cap the glowing vial, enjoying the wild, jovial energy of the docks as you prepare for the next leg of your quest."

    hide tansy

    $ setup_free_time(2)
    jump free_time