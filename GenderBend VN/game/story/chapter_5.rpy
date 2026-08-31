# ============================================================
# FOUR CHARACTER POSITION PRESETS
# Keep these in your shared character asset/transform file if preferred.
# ============================================================

transform char_far_left:
    xanchor 0.5
    xpos 0.12
    yalign 1.0

transform char_mid_left:
    xanchor 0.5
    xpos 0.37
    yalign 1.0

transform char_mid_right:
    xanchor 0.5
    xpos 0.63
    yalign 1.0

transform char_far_right:
    xanchor 0.5
    xpos 0.88
    yalign 1.0


# ============================================================
# MAIN CHAPTER 5 — REBIRTH, CHAOS & THE CORE FOUR VICTORY
# Adjusted four-character finale.
# ============================================================

label chapter_5:

    call chapter_transition(5, "Rebirth, Chaos & The Core Four Victory")

    # Core Four staging.
    show tansy worried at tansy_size, char_far_left
    show clara normal at clara_size, char_mid_left
    show domitilla normal at domitilla_size, char_mid_right
    show elianna happy at elianna_size, char_far_right
    # Scene 1: The Gilded Transformation
    # Location: The Solarium Sanctum — Grand Alchemy Laboratory
    # [SCENE START]
    # SFX: Sound Effect: Radiant choir-like hum, swirling golden wind, magical chiming bell, loud cork popping
    "(You lift the crystal goblet containing the golden Alkahest of True Form to your lips.)"
    "(Tansy, Ellie, Clara, and Domitilla—who just burst through the lab doors carrying a keg of armory mead—all stand in a hushed circle, holding their breath.)"
    # Source [SPRITE: Tansy — Nervous, Holding Breath]
    show tansy happy at tansy_size, char_far_left
    tansy "Bottoms up, kiddo! Don't spill a single drop!"
    "(You swallow the warm, golden brew in one big gulp.)"
    "(Instantly, a wave of intense heat washes from your stomach to your toes.)"
    "(Bright golden light erupts from your body, lifting you two feet off the floor as your magic channels flare!)"
    # SFX: Sound Effect: WHOOSH! Bone snaps re-aligning, deep pitch drop in chest
    "(Your hair shortens back to its familiar cut.)"
    "(Your shoulders broaden, snapping your sorcerer robes tight across your chest.)"
    "(Your height stretches back up, and when you let out a gasp, your deep, natural male voice returns!)"
    # [MC]
    mc "HAH! MY VOICE! MY SHOULDERS! I'M BACK!"
    # SFX: Sound Effect: MAGICAL POP! Sparkles bursting
    "(However, because of the wild mix of six legendary catalysts, a side effect triggers: every time you blink or speak with passion, a tiny burst of harmless, radiant golden glitter pops out of your hair and hovers in the air like a walking party spell.)"
    # Source [SPRITE: Commander Bruni — Stunned -> Booming Laughter]
    show domitilla happy at domitilla_size, char_mid_right
    domitilla "BWAHAHAHA! Look at him! You're built like a vanguard commander, but you're shedding fairy dust like a festival float!"
    # Source [SPRITE: Ellie — Beaming, Clapping]
    show elianna happy at elianna_size, char_far_right
    elianna "Oh, it's wonderful! You look so handsome, and the sparkles are surprisingly flattering!"
    # Source [SPRITE: Clara Vane — Smirking, Adjusting Glasses]
    show clara happy at clara_size, char_mid_left
    clara "I can already see the fashion trend. 'Sanctum Glitter-Bourbon'. We'll make a fortune."

    menu:
        "Strike an absurdly heroic pose.":
            "(Strike an absurdly heroic pose, striking a pose that sends glitter flying across the lab)"
            mc "Behold! The Arch-Mage of Glamour has returned!\" Bruni: \"HA! That’s the spirit! A true warrior owns their glitter!"
        "Sweep Tansy and Ellie into a massive bear hug.":
            "(Laugh hysterically and sweep Tansy and Ellie into a massive bear hug)"
            show elianna normal at elianna_size, char_far_right
            elianna "Eek! Oh! You're so warm and strong again!\" Tansy: \"Aww! See? I told you my tea would make you unforgettable!"
        "Try to brush the sparkles out of your hair.":
            "(Try to brush the sparkles out of your hair, growing completely flustered)"
            show clara happy at clara_size, char_mid_left
            clara "Don't bother fighting it, dear. You look magnificent. Own the spotlight!"

    # Re-establish the Core Four for the tavern group shot.
    show tansy happy at tansy_size, char_far_left
    show clara happy at clara_size, char_mid_left
    show domitilla happy at domitilla_size, char_mid_right
    show elianna happy at elianna_size, char_far_right

    # Scene 2: Revelry at The Laughing Anchor
    # Location: The Laughing Anchor Tavern — Private Guild Suite (Night)
    # [SCENE START]
    # SFX: Sound Effect: Lute playing, tavern patrons cheering, heavy wooden mugs clanking, roaring fireplace
    "(The entire central table of The Laughing Anchor is covered in roasted meats, glowing botanical pastries made by Ellie, and heavy iron flagons brought by Domitilla.)"
    "(Clara has rented out the entire upper deck for the core four heroines and you.)"
    # Source [SPRITE: Clara Vane — Raising Crystal Glass]
    show clara happy at clara_size, char_mid_left
    clara "A toast! To our favorite apprentice—who survived transfiguration, market fraud, military hazing, and double-witch chaos!"
    # [ALL HEROINES]
    tansy "TO THE SPARKLE WIZARD!"
    elianna "TO THE SPARKLE WIZARD!"
    domitilla "TO THE SPARKLE WIZARD!"
    clara "TO THE SPARKLE WIZARD!"
    # SFX: Sound Effect: Mugs clanking together violently
    "(Domitilla slams her flagon onto the table, challenging you to an arm-wrestling match right on top of Clara’s expensive silk tablecloth.)"
    "(Ellie is feeding you sweet-berry tarts, while Tansy uses your magical glitter aura to summon little glowing fireworks that dance over the tavern rafters.)"
    # Source [SPRITE: Commander Bruni — Grinning, Gripping Your Hand]
    show domitilla talking at domitilla_size, char_mid_right
    domitilla "Come on, scholar! Let's see if that new male body can push back against three hundred pounds of Garrison power!"

    menu:
        "Challenge Domitilla at arm wrestling.":
            "(Slam Domitilla's hand down onto the table with a surge of kinetic magic and raw muscle)"
            "(The wooden table cracks as you pin Domitilla's arm! The entire tavern erupts in deafening cheers!)"
            show domitilla happy at domitilla_size, char_mid_right
            domitilla "BWAHAHA! YES! THAT'S WHAT I'M TALKING ABOUT!"
        "Toast warmly to all four women.":
            "(Toast warmly to all four women, giving a heartwarming speech about how much you trust them)"
            mc "I couldn't have asked for a better master, partner, ally, or commander. To the four women who make Mirthhaven legendary!\" Ellie: (Tearing up) \"Oh goodness... that is the sweetest thing anyone has ever said!"
        "Turn your glitter aura into a tavern-wide light show.":
            "(Channel your glitter aura into a full tavern-wide magical light show)"
            "(Golden sparks cascade over the tavern balcony like shimmering rain. Patrons downstairs break into wild applause!)"
            show tansy happy at tansy_size, char_far_left
            tansy "We're charging admission for this show next time!"

    # Scene 3: A Destiny Forged in Magic & Steel
    # Location: The Laughing Anchor — Balcony Overlooking Mirthhaven
    show tansy normal at tansy_size, char_far_left
    show clara normal at clara_size, char_mid_left
    show domitilla normal at domitilla_size, char_mid_right
    show elianna normal at elianna_size, char_far_right
    # [SCENE START]
    # SFX: Sound Effect: Night breeze blowing softly, distant ocean waves, stars twinkling overhead
    "(You step out onto the tavern balcony overlooking the glowing harbor lights of Mirthhaven. One by one, Tansy, Ellie, Clara, and Domitilla join you at the railing, leaning beside you under the moonlight.)"
    # Source [SPRITE: Tansy — Warm, Proud Smile]
    show tansy talking at tansy_size, char_far_left
    tansy "So... the brew is finished. Your body is restored. The Alkahest worked. What’s your next step, little wizard?"
    # Source [SPRITE: Commander Bruni — Crossing Arms, Grinning]
    show domitilla talking at domitilla_size, char_mid_right
    domitilla "The Vanguard always has a high seat open for a mage who isn't afraid to fight in the dirt."
    # Source [SPRITE: Clara Vane — Gentle Smile, Adjusting Ring]
    show clara talking at clara_size, char_mid_left
    clara "And the Merchant Guild could always use a sharp mind to co-rule the trade lanes."
    # Source [SPRITE: Ellie — Blushing, Soft Tone]
    show elianna talking at elianna_size, char_far_right
    elianna "Or... you could stay right here in the Sanctum with us, researching new magic and tending the wards."
    "(You look at the four extraordinary heroines who helped you reclaim your true self. The future of Mirthhaven stretches out before you.)"

    menu:
        "The Arch-Mage of Mirthhaven — Remain at the Solarium Sanctum.":
            $ main_ending = "sparkle_arch_mage"
            "(Tansy pulls you into a playful headlock while Ellie beams with pure joy!)"
            # Source [SPRITE: Tansy — Ecstatic, Laughing]
            show tansy happy at tansy_size, char_far_left
            tansy "YES! The Solarium Sanctum gets to keep its favorite disaster-apprentice!"
            "(Together with Tansy and Ellie, you step into your new role as Grand Arch-Mage.)"
            "(Over the coming years, your signature spell becomes legendary across the continent: a glorious, unstoppable golden burst of raw magic and sparkly light that strikes terror into monsters and brings endless laughter to Mirthhaven.)"
            hide tansy
            hide elianna
            hide clara
            hide domitilla
            jump chapter_5_end
        "The Vanguard Champion — Join Domitilla at the Crestward Garrison.":
            $ main_ending = "gilded_champion"
            "(Domitilla slams her hand onto your back so hard you almost knock over the balcony railing, roaring with pride!)"
            # Source [SPRITE: Commander Bruni — Thunderous Joy]
            show domitilla happy at domitilla_size, char_mid_right
            domitilla "HA! WELCOME TO THE VANGUARD, CHAMPION!"
            "(Dressed in custom-forged armor crafted by Domitilla that glimmers with eternal golden sparks, you become the most formidable warrior-mage in Mirthhaven’s history.)"
            "(Leading the Garrison, you protect the realm with iron discipline, unstoppable magic, and a flair for theatrical combat that no enemy can breach!)"
            hide tansy
            hide elianna
            hide clara
            hide domitilla
            jump chapter_5_end
        "The Shadow Merchant Lord — Partner with Clara at the Wanderlust Guild.":
            $ main_ending = "glamour_overlord"
            "(Clara hands you a golden signet ring engraved with the Wanderlust Guild crest, winking with a clever smile.)"
            # Source [SPRITE: Clara Vane — Sophisticated, Smirking]
            show clara happy at clara_size, char_mid_left
            clara "A brilliant choice, partner. Together, we'll buy and sell whole kingdoms."
            "(Teaming up with Clara, you revolutionize trade across the realm.)"
            "(Using your magic and her financial genius, you build a prosperous trade syndicate.)"
            "(And yes—your eternal glitter aura becomes the single most sought-after luxury fashion spell in the high courts, making you both obscenely wealthy!)"
            hide tansy
            hide elianna
            hide clara
            hide domitilla
            jump chapter_5_end

label chapter_5_end:

    scene black
    with fade

    centered "{size=52}THE END{/size}"

    return