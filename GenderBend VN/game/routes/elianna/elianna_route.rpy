# ============================================================
# ELIANNA "ELLIE" SYLVANE — FULL / DECLUTTERED / EXPRESSIVE
# ============================================================

label elianna_chapter_1:

    call route_transition("Elianna Sylvane", 1, "Bandages & Broken Vials")

    # Location: The Solarium Sanctum — Sunlit Wards
    scene bg solarium_sanctum at bg_character_focus
    with fade
    # Characters Present: The MC (Sorcerer Apprentice), Elianna "Ellie" Sylvane (Head Nurse)
    # [SCENE START]
    # SFX: Sound Effect: Clattering glass, rustling parchment, frantic footsteps echoing against marble tiles
    "(The Sunlit Wards are filled with the warm, golden glow of afternoon light filtering through vaulted stained-glass windows.)"
    "(Rows of pristine white cots line the hall, filled with the aroma of dried lavender, crushed eucalyptus, and burning sage.)"
    "(Near a tall oak apothecary cabinet at the far end of the ward, a frantic blur of white robes and golden hair is scurrying across the floor.)"
    # [SPRITE: Ellie — Panicked, Flustered]
    show elianna angry at elianna_size, char_center, enter_from_right
    elianna "Eek—! Wait, wait, come back! Ah, nononono, don't roll under the cabinet!"
    "(Ellie lunges forward on all fours, her fingers just barely scraping against a small glass vial of shimmering blue salve as it bounces across the stone floor.)"
    "(In her panic, her foot catches the heavy wool hem of her own long white nurse’s gown.)"
    # SFX: Sound Effect: Heavy fabric rustle, sharp gasp

    show elianna normal at elianna_size, expression_pop
    elianna "Whoa—ah! Oh no!"
    "(Ellie trips over her feet with a soft gasp.)"
    "(A neatly stacked armful of clean cotton bandages, wooden splints, and rolls of medical linen flies from her arms, cascading into the air straight toward the hard cobblestone floor.)"
    # [MC (Sorcerer Apprentice)]
    "(Raising your right hand swiftly, channeling a soft pulse of blue kinetic mana from your fingertips)"
    mc "Levitas!"
    # SFX: Sound Effect: Soft magical hum, glowing energy chime
    "(The falling bandages freeze mid-air, bathed in a soft azure aura.)"
    "(With a gentle flick of your wrist, you guide the floating stack safely into your arms and catch the stray blue vial with your free hand.)"
    mc "Got them. Easy there, Nurse Ellie."
    # [SPRITE: Ellie — Shocked, Blushing]
    show elianna smug at elianna_size, expression_pop
    elianna "Wh-Whah—?! Oh! The bandages! They didn't hit the floor!"
    "(Ellie scrambles up from the tiles, her knees knocking slightly.)"
    "(She frantically dusts off her pristine white apron, trying to straighten her lopsided nurse's cap, though her cheeks burn a bright, furious crimson.)"
    show elianna happy_talking at elianna_size, expression_pop
    elianna "Oh goodness, I'm so, so sorry! I was just trying to catch the Salve of Aloe before it smashed, and then my feet got tangled... I swear my robes grow three inches longer whenever I'm in a hurry!"
    "(She takes a breathless step toward you to retrieve the supplies, but as you hand them over, her bright blue eyes instantly lock onto your exposed forearm.)"
    # [SPRITE: Ellie — Worried, Disappointed]
    show elianna sad at elianna_size, expression_pop
    elianna "Ah, wait! Look at you! Those singe marks and blisters on your arms—was that Tansy’s practical casting drill again?!"
    mc "Yeah. A stray flame-burst caught me off guard during the target rotation."
    # [SPRITE: Ellie — Agonized, Gentle]
    show elianna talking at elianna_size, expression_pop
    elianna "That woman... I keep telling her that novice sorcerers shouldn't be casting volatile fire spells indoors without dampening wards! Sit down, please! Right here on the edge of the cot!"
    "(She gently takes your uninjured hand and guides you to sit on a nearby padded cot.)"
    "(She sets the retrieved supplies on a rolling tray and pulls out a small porcelain jar of soothing mint-green paste along with wooden applicators.)"
    elianna "Hold still now. This might feel cold at first..."
    "(Ellie dips a wooden spatula into the cooling paste and gently begins spreading it over the red, raw skin of your forearm.)"
    "(Despite her earlier clumsiness, her touch is remarkably feather-light.)"
    "(However, as the herb makes contact with a fresh burn, you reflexively flinch and wince.)"
    # SFX: Sound Effect: Sharp intake of breath
    # [SPRITE: Ellie — Pained, Tearful]
    show elianna sad at elianna_size, expression_pop
    elianna "Ah! S-Sorry! Did that hurt?! Oh dear, I applied too much pressure, didn't I? I'm so bad at this..."
    "(She pulls her hands back, clutching the applicator tightly to her chest. Her bright blue eyes fill with genuine tears, glistening under the sunlight as her brow furrows in deep, sympathetic distress.)"
    elianna "Whenever I see someone in pain, my heart hurts just as much as their injury... I can't stand seeing people suffer. That's why I became a nurse, even if my hands are clumsy and I trip over air..."
    "(She looks at you, her bottom lip trembling slightly, waiting anxiously for your response as she clutches a clean roll of gauze in her trembling hands.)"

    menu:
        "You're not bad at this at all, Ellie. Your heart is what makes you a great healer.":
            $ elianna_affection += 25
            # [MC]: "You're not bad at this at all, Ellie. Your heart is what makes you a great healer."
            # [SPRITE: Ellie — Surprised -> Deep Blush, Soft Smile]
            "(Ellie blinks rapidly, a tear spilling over her lashes as her eyes widen in utter surprise. A deep, rose-pink flush spreads from the tips of her pointed elven ears down to her neck.)"
            show elianna smug at elianna_size, expression_pop
            elianna "Y-You really think so...? You're not just saying that to make me feel better?"
            mc "I mean it. Anyone can apply salve, Ellie, but not everyone actually cares about the person hurting."
            show elianna very_smug at elianna_size, expression_pop
            elianna "I... Oh..."
            show elianna normal at elianna_size, expression_pop
            "(She wipes her cheek with the back of her sleeve and lets out a soft, breathy laugh.)"
            "(The tension drains from her shoulders completely.)"
            "(She steps back in close, her movements suddenly becoming steady, careful, and remarkably delicate as she wraps the soft linen gauze over your burn.)"
            show elianna happy at elianna_size, expression_pop
            elianna "Most people just laugh at me... or tell me to stay out of the way so I don't break something expensive. But you..."
            "(She ties off the bandage with a perfect, neat knot, her soft fingers lingering against your palm for a few extra seconds before she slowly lets go.)"
            show elianna happy_talking at elianna_size, expression_pop
            elianna "Thank you, sorcerer. You have no idea how much those words mean to me... Please, come back anytime you're hurt. I'll always be here to fix you up."
            hide elianna
            jump finish_elianna_event
        "It stings a bit, but I can handle it. Just focus on wrapping it up.":
            $ elianna_affection += 10
            # [MC]: "It stings a bit, but I can handle it. Just focus on wrapping it up."
            # [SPRITE: Ellie — Relieved, Apologetic]
            show elianna normal at elianna_size, expression_pop
            "(Ellie gives a quick, flustered nod, wiping her eyes with the corner of her apron as she takes a deep breath.)"
            elianna "O-Oh! Right! Of course! S-Sorry, I'm wasting time rambling when you're the one sitting here in pain!"
            "(She quickly dips the applicator back into the jar and works on spreading the rest of the green paste over your arm.)"
            "(Her hands are a little shaky, making the application slightly uneven, but she works diligently to wrap the white linen gauze over your burns.)"
            # SFX: Sound Effect: Fabric wrapping
            show elianna happy_talking at elianna_size, expression_pop
            elianna "There... all patched up! I wrapped it a tiny bit tight to keep the salve from leaking, but it should stop the burning in a few minutes."
            "(She steps back, handing you a small paper pouch with extra ointment.)"
            show elianna angry at elianna_size, expression_squish
            elianna "Take this with you. And please, try to avoid Tansy's fire drills for the rest of the week if you can! I'd hate to see you back on this cot so soon."
            hide elianna
            jump finish_elianna_event
        "Maybe you should let someone else handle the volatile potions if you're going to trip every time.":
            $ elianna_affection -= 15
            # [MC]: "Maybe you should let someone else handle the volatile potions if you're going to trip every time."
            # [SPRITE: Ellie — Hurt, Downcast]
            "(Ellie freezes mid-motion.)"
            "(The bright, emotional light in her eyes instantly dims, replaced by a quiet, crestfallen shadow.)"
            "(She lowers her head, her golden bangs falling forward to hide her expression.)"
            elianna "I... I see. You're... you're right, of course."
            "(She hastily wraps the remaining gauze around your arm without looking at you, her fingers cold and stiff. The bandage is tied off clumsily, slightly lopsided against your wrist.)"
            show elianna normal at elianna_size, expression_pop
            elianna "I'm just a liability in here... I know the other healers say the same thing behind my back. I just thought... if I tried hard enough..."
            "(She steps back, pulling her hands into her sleeves and clutching them tightly against her chest. She turns her face away, staring down at the stone floor.)"
            elianna "You're all patched up now. You're free to go back to your dorms... I'll try not to bother you next time you visit the Wards."
            hide elianna
            jump finish_elianna_event

label elianna_chapter_2:

    call route_transition("Elianna Sylvane", 2, "The Weight of Centuries")

    show elianna sad at elianna_size, char_center, expression_pop
    # Location: The Solarium Sanctum — Botanical Conservatory (Midnight)
    scene bg solarium_sanctum at bg_character_focus
    with fade
    # [SCENE START]
    "(The scene opens inside the grand glass conservatory of the Solarium Sanctum late at night.)"
    "(Pale moonlight streams through arched glass panes, illuminating silver-leafed ferns, luminescent mosses, and sprawling vines.)"
    "(The soft, rhythmic hum of nocturnal crickets fills the cool night air, punctuated by the faint trickling of water from a marble fountain.)"
    # SFX: Sound Effect: Soft breeze whistling through glass, rustling moon-flowers, light footsteps on gravel
    "(In the center of the conservatory stands Ellie, stripped of her medical apron and wearing a simple, flowing night cloak.)"
    "(She kneels beside a bed of rare silver blooms, her small watering can resting by her feet.)"
    "(Her golden hair hangs loosely over her shoulders, and her long elven ears droop slightly.)"
    # [SPRITE: Ellie - Melancholy, Wistful]
    show elianna talking at elianna_size, char_center, expression_pop
    "(Sighs softly, reaching out to gently touch a shimmering petal)"
    elianna "...Another decade gone... and the flowers bloom just the same."
    "(You step off the gravel pathway onto the smooth marble terrace.)"
    # SFX: Sound Effect: Soft crunch of gravel, gentle footsteps
    # [MC (Sorcerer Apprentice)]
    mc "Ellie? What are you doing out here so late?"
    # [SPRITE: Ellie - Startled -> Gentle Smile]
    "(Ellie gasps softly, her hand jumping to her chest as she spins around. Recognizing you, her startled expression instantly softens into a warm, albeit weary, smile.)"
    elianna "Ah! Sorcerer! Oh... goodness, you scared me for a second! I thought it was one of the night wardens on patrol."
    "(She sets her watering can aside and brushes off her skirt before gesturing to the empty stone bench beside her.)"
    elianna "I couldn't sleep tonight. The Night-Blooming Lilies only open under a full moon, and their nectar spoils if it isn't harvested right as the petals unfurl. They need... very delicate care."
    "(You walk over and sit beside her on the cool marble bench. Ellie gazes up at the vast, starry sky through the glass ceiling, resting her hands in her lap.)"
    elianna "It's... so quiet out here at night. In the Wards, everything is always moving so fast. I'm constantly running around, tripping over robes, trying to keep up with the daily chaos..."
    "(She turns her head toward you, her bright blue eyes reflecting the moonlight, carrying a deep, quiet sadness you've never seen in her during the daytime.)"
    # [SPRITE: Ellie - Vulnerable, Tearful]
    elianna "Did you know..."
    elianna "I’ve been the head nurse here for over two hundred years?"
    elianna "I watch bright, ambitious young students walk through these glass doors..."
    elianna "I fix their scrapes, listen to their dreams, watch them grow into great sorcerers..."
    "(Her voice quietens to a fragile murmur as she looks down at her hands.)"
    elianna "...And then they age, leave, and eventually pass away. While I just... stay. Unchanging."
    "(She takes a slow breath, her shoulders rising and falling heavily.)"
    show elianna sad at elianna_size, char_center, expression_pop
    elianna "Because I live so long, I usually try to keep my distance to save my heart."
    elianna "It hurts too much to get close when everyone leaves eventually..."
    elianna "Combine that with my clumsiness, and I feel like an alien in my own home."
    elianna "A ghost just passing through time."

    menu:
        "You don't have to carry that solitude alone anymore, Ellie. I'm right here with you.":
            $ elianna_affection += 25
            # [MC]
            mc "You don't have to carry that solitude alone anymore, Ellie. I'm right here with you."
            # [SPRITE: Ellie - Shocked -> Emotional, Tearful Smile]
            "(Ellie’s breath catches in her throat. Her eyes widen in genuine shock as she looks up at you, her lips parting slightly.)"
            elianna "You... you really mean that...?"
            "(A single, crystal-clear tear slips down her cheek, catching the moonlight.)"
            "(Instead of pulling away, she slowly leans toward you, resting her head softly against your shoulder.)"
            "(Her small, warm hand glides across the marble bench, closing over yours with gentle conviction.)"
            elianna "Two hundred years... and no one has ever said that to me..."
            "(She closes her eyes, letting out a long, contented breath as the tension drains completely from her frame.)"
            show elianna sad at elianna_size, char_center
            elianna "When you're around... the solitude doesn't feel so heavy anymore. Thank you for staying by my side, my brave sorcerer."
            hide elianna
            jump finish_elianna_event
        "Living a long time must be tough, but at least you get to help so many generations.":
            $ elianna_affection += 10
            # [MC]
            mc "Living a long time must be tough, but at least you get to help so many generations."
            # [SPRITE: Ellie - Pensive, Soft Smile]
            "(Ellie blinks, pausing for a moment before letting out a light, melodious chuckle.)"
            show elianna happy at elianna_size, char_center, expression_pop
            elianna "Fufu... That's a very practical way to look at it, sorcerer. You sound just like the old Headmaster when I first joined the Sanctum."
            "(She pulls out a handkerchief, delicately wiping away the stray moisture from her eyelashes before sitting up straight.)"
            elianna "I suppose seeing it as a noble duty helps ease the ache a bit. Every potion I brew and every bandage I wrap is a small mark left on the world, isn't it?"
            "(She offers you a gentle, grateful nod, reaching down to pick up her wooden watering can once more.)"
            elianna "Thank you for listening to my foolish rambling tonight. It does feel a bit better to say it out loud."
            hide elianna
            jump finish_elianna_event
        "If getting attached hurts so much, maybe keeping your distance really is for the best.":
            $ elianna_affection -= 15
            # [MC]
            mc "If getting attached hurts so much, maybe keeping your distance really is for the best."
            # [SPRITE: Ellie - Distant, Heartbroken]
            "(The soft light in Ellie’s eyes instantly extinguishes. She pulls her hands back into her lap, her posture growing stiff and distant.)"
            elianna "...Right. Of course."
            "(She gazes down at the stone tiles, her voice dropping into a cold, flat whisper that hurts worse than a scolding.)"
            elianna "Distance is safer... It’s foolish of me to expect anything different after all these centuries."
            "(She stands up abruptly from the bench, her robes rustling as she brushes off her skirt without looking at you.)"
            show elianna talking at elianna_size, char_center, expression_pop
            elianna "It's far past midnight. You have early casting classes tomorrow, and you shouldn't be wandering the gardens out of bounds. Please get back to your dorms."
            "(She turns her back to you, picking up her tools in complete silence as the chill of the night settles between you.)"
            # [SCENE END]
            hide elianna
            jump finish_elianna_event

label elianna_chapter_3:

    call route_transition("Elianna Sylvane", 3, "A Healing Touch")

    show elianna talking at elianna_size, char_center
    # Location: The Crestward Bastion — Garrison Field Clinic
    scene bg crestward_bastion at bg_character_focus
    with fade
    # [SCENE START]
    "(The scene opens inside a sprawling canvas medical tent erected at the edge of the Crestward Bastion’s outdoor training grounds.)"
    "(Dust kicks up in clouds outside as heavy boots stomp across the gravel.)"
    "(Inside, the clinic is packed with groaning recruits, smell of ozone, medicinal salve, and sweat hanging thick in the air.)"
    # SFX: Sound Effect: Clashing steel in distance, shouting recruits, rustling canvas tents, frantic footsteps
    # [SPRITE: Ellie - Focused, Sweating]
    show elianna talking at elianna_size, char_center, enter_from_right
    elianna "Hold still, Sir Knight! Apply pressure to the shoulder with your left hand—yes, right there! I need three more vials of Burn-Salve right now!"
    "(Ellie rushes between cot after cot, her usual timid demeanor replaced by sharp, practiced focus. Sweat beads along her forehead, pinning several stray golden locks across her flushed face.)"
    # SFX: Sound Effect: Loud creaking wood, snapping ropes from overhead scaffolding
    "Knight Recruit: \"LOOK OUT! THE CEILING BEAM IS GIVING WAY!\""
    "(Directly above the main treatment table where Ellie is standing, a massive wooden support timber—overloaded by heavy iron supply crates stored on the upper staging—cracks under the weight with a deafening split.)"
    # SFX: Sound Effect: THUNDEROUS CRACK! Scaffolding groans, ropes snap
    show elianna angry at elianna_size, expression_squish
    elianna "E-Eek—?!"
    "(Ellie freezes in shock, looking up just as the splintered oak beam breaks completely free, hurtling down directly toward her head.)"
    # [MC (Sorcerer Apprentice)] (Lunging forward, thrusting your staff upward while channeling mana into a dense, solid dome) (Sound Effect: Deep, booming resonance of barrier spell expanding)
    mc "AEGIS AETHERIS!"
    # SFX: Sound Effect: HEAVY TIMBER SHATTERING AGAINST A MAGICAL SHIELD!
    "(The massive beam crashes against your radiant blue barrier, splintering into harmless chunks of wood that bounce off the magic dome and shower down onto the dirt floor.)"
    "(A cloud of dust billows through the tent as you drop the barrier, turning around immediately.)"
    mc "Ellie! Are you okay?!"
    # [SPRITE: Ellie - Panicked, Terrified]
    elianna "A-AHHH! Sorcerer?!"
    "(Ellie completely forgets the wounded knights around her. She rushes toward you, her hands frantically grabbing your wrists, face, and shoulders, her eyes wide with unadulterated terror.)"
    show elianna sad at elianna_size, expression_pop
    elianna "Are you hurt?! Did the impact crush your arms?! Is your head bleeding?! Speak to me, please!"
    # [MC]
    mc "Ellie, calm down! I used a barrier spell—I'm completely fine! Not a scratch!"
    # [SPRITE: Ellie - Overwhelmed, Crying] (When the realization sinks in that you're unharmed, Ellie's strength evaporates. Her knees buckle slightly, and she collapses forward against your chest, burying her face into the front of your sorcerer robes.)
    # SFX: Sound Effect: Soft, trembling sobs
    elianna "Thank goodness... oh, thank the gods..."
    "(She clings desperately to the cloth of your robes, her entire body trembling against yours.)"
    elianna "I spend my whole life hurting for everyone else... but if anything ever happened to you... I don't think I could ever heal from that!"

    menu:
        "I'll always protect you, Ellie. You don't have to worry.":
            "(Wrap your arms around her tightly)"
            $ elianna_affection += 25
            # [MC] (You wrap your arms tightly around her waist, pulling her close to your chest and resting your chin against her soft golden hair.)
            mc "I'll always protect you, Ellie. You don't have to worry about me."
            # [SPRITE: Ellie - Deeply Moved, Loving Look] (Ellie's trembling slowly stops. She tilts her head up to look at you, her face flushing crimson as tears trail down her cheeks. She gently reaches up, cradling your cheek with her warm, soft palm.)
            elianna "S-Sorcerer..."
            "(She rests her forehead against yours, her bright blue eyes glowing with undeniable tenderness.)"
            show elianna talking at elianna_size, expression_pop
            elianna "I'm supposed to be the one taking care of you... but having you hold me like this... makes me feel so safe. I never want to let go..."
            hide elianna
            jump finish_elianna_event
        "I'm a sorcerer, Ellie. I know how to take care of myself in a fight.":
            "(Gently pat her back)"
            $ elianna_affection += 10
            # [MC] (You gently pat her back in a steady, reassuring rhythm.)
            mc "I'm a sorcerer, Ellie. I know how to take care of myself in a fight."
            # [SPRITE: Ellie - Sniffling, Relieved] (Ellie takes a shaky breath, slowly pulling back and wiping her cheeks with the back of her sleeve.)
            elianna "I know, I know... you're very brave and skilled with your barrier magic..."
            "(She steps back, tucking her stray hair behind her ears with a shy, self-conscious nod.)"
            show elianna talking at elianna_size, char_center
            elianna "Just... please don't take risks like that without thinking first. My heart simply can't take the shock!"
            hide elianna
            jump finish_elianna_event
        "You need to pull it together, Nurse. The wounded knights still need you.":
            $ elianna_affection -= 15
            # [MC]
            mc "You need to pull it together, Nurse. The wounded knights still need you."
            # [SPRITE: Ellie - Stunned, Embarrassed, Flustered] (Ellie freezes as if struck. A deep red rush of mortification floods her face, and she immediately breaks away, stepping back two paces and bowing her head repeatedly.)
            elianna "Ah—! Y-Yes! Of course! Forgive me!"
            "(She hurriedly wipes her face, her voice trembling as she tries to hide her embarrassment behind a formal tone.)"
            elianna "I'm being completely unprofessional... I am so sorry for making a scene in front of everyone... I'll return to treating the soldiers at once."
            "(She turns around quickly, her shoulders rigid as she moves back to the treatment cots without looking at you again.)"
            # [SCENE END]
            hide elianna
            jump finish_elianna_event

label elianna_chapter_4:

    call route_transition("Elianna Sylvane", 4, "Eternal Bloom")

    
    # Location: The Solarium Sanctum — Sunlit Wards Balcony (Dusk)
    scene bg solarium_sanctum at bg_character_focus
    with fade
    # [SCENE START]
    "(The scene opens on the grand arched balcony overlooking the vast estate of the Solarium Sanctum.)"
    "(The sky is painted in hues of violet, fiery rose, and shimmering gold as the sun slowly sinks behind the horizon.)"
    "(A soft, fragrant breeze blows across the terrace, carrying the subtle sweet scent of blooming flora from the gardens below.)"
    # SFX: Sound Effect: Gentle evening wind, rustling leaves, distant church bells tolling dusk
    show elianna happy at elianna_size, expression_pop, char_center
    "(Ellie stands near the stone balustrade, bathed in the warm, golden twilight.)"
    "(She wears her finest light-colored gown, and resting upon her head is a beautifully woven crown of glowing, star-shaped medicinal blooms.)"
    # [SPRITE: Ellie - Nervous, Eager]
    elianna "Ah! You came!"
    "(Ellie turns around rapidly to face you, but in her excitement, her foot catches slightly on her hem.)"
    "(The sudden movement causes the delicate flower crown to tilt wildly, sliding lopsided over her right pointed ear.)"
    # SFX: Sound Effect: Soft gasp
    show elianna angry at elianna_size, expression_squish
    elianna "Eek—! Oh no, not again!"
    "(She flushes furiously, reaching up with both hands in a panic to try to save the crown, only to tangle her fingers in her blonde hair.)"
    # [MC (Sorcerer Apprentice)] (Stepping forward with a soft, affectionate laugh, reaching out gently to untangle her fingers and adjust the crown back to the center of her head)
    mc "Hold still, Ellie. There... perfectly centered."
    # [SPRITE: Ellie - Blushing, Adoring]
    show elianna happy at elianna_size, expression_pop
    elianna "Ehehe... thank you. Even when I try so hard to look nice for you, my clumsiness always finds a way to get the best of me..."
    "(She lowers her hands, slowly reaching out to take both of your hands in hers. Her fingers are soft and warm, trembling ever so slightly as she looks up into your eyes.)"
    show elianna sad at elianna_size, expression_pop
    elianna "I used to think my long life was a curse of solitude... meant for watching people come and go while I tripped through the centuries all alone in the infirmary."
    # [SPRITE: Ellie - Radiant, Deeply In Love]
    elianna "But you looked past my awkwardness. You shared my pain, protected me when I was weak, and gave me a reason to look forward to every single new day."
    "(Ellie slips one hand free and pulls a glowing, pristine white blossom from her apron pocket—a rare, everlasting Moon-Lily—and gently presses it into your open palm.)"
    show elianna talking at elianna_size, expression_pop
    elianna "This flower blooms forever... never wilting, never fading... just like what I feel for you."
    elianna "I don't care how many years I have left in this world—I want to spend every single moment of my life by your side."

    menu:
        "I love you too, Ellie. Let's spend eternity together.":
            "(Kiss Her)"
            $ elianna_affection += 25
            # [MC]
            mc "I love you too, Ellie. Let's spend eternity together."
            "(You gently place your hand behind her waist, pulling her softly toward you.)"
            "(Ellie lets out a sweet, breathless gasp as you lean in, closing the distance between you and pressing your lips to hers in a deep, loving kiss under the golden twilight sky.)"
            # SFX: Sound Effect: Swirling wind, soft magic shimmer as the floral crown glows brighter
            # [SPRITE: Ellie - Pure Bliss, Tears of Joy]
            elianna "Mmm... Ah..."
            "(Ellie melts into your arms, her small hands rising to gently wrap around your neck as she kisses you back with total, unreserved devotion.)"
            "(Tears of happiness slip down her cheeks, sparkling like tiny gems in the dusk light.)"
            elianna "My brave sorcerer... my heart, my soul, my entire life... they're all yours. Forever and ever."
            # [ENDING CG: EVERLASTING SOLACE]
            "The sun dips fully beneath the horizon, casting the world in a dreamy, starlit indigo."
            "Surrounded by the gentle glow of the Moon-Lily and her flower crown, Ellie rests her head against your chest, her long elven ears twitching happily at the steady beat of your heart."
            "No longer a lonely ghost passing through time, the sweet head nurse of the Sanctum has found her forever home in your arms."
            $ elianna_ending = "everlasting_solace"
            hide elianna
            jump finish_elianna_event
        "I cherish you deeply, Ellie. I promise to always stay by your side.":
            "(Hold Her Hand)"
            $ elianna_affection += 10
            # [MC]
            mc "I cherish you deeply, Ellie. I promise to always stay by your side."
            "(You hold her hands tightly, bringing them to your chest and giving them a warm, reassuring squeeze before pulling her into a protective, comfortable embrace.)"
            # [SPRITE: Ellie - Peaceful, Tender Smile]
            elianna "Oh... thank you..."
            "(Ellie rests her cheek softly against your shoulder, letting out a long, contented sigh as she wraps her arms around your waist.)"
            elianna "That's all I could ever ask for... As long as I can hold your hand and walk through these centuries with you by my side, I'll never be afraid of the future again."
            # [ENDING CG: GUIDING LIGHT]
            "You stand together on the balcony, watching the night stars emerge over Mirthhaven."
            "Hand in hand, you look toward the future together—a powerful sorcerer and a dedicated healer, bound by an unbreakable connection that shines brighter than any magical ward."
            $ elianna_ending = "guiding_light"
            hide elianna
            jump finish_elianna_event
        "Ellie... I care about you, but I don't think I can promise you forever.":
            $ elianna_affection -= 15
            $ elianna_romance_locked = True
            # [MC]
            mc "Ellie... I care about you, but I don't think I can promise you forever."
            # [SPRITE: Ellie - Heartbroken, Trying to Smile] (Ellie's glowing smile freezes. The light in her eyes dims, and a single, heavy tear slips down her cheek. She slowly pulls her hands back, clutching the Moon-Lily tightly to her chest.)
            elianna "Oh... I... I see..."
            "(She forces a brave, heartbreakingly gentle smile, bowing her head so her golden bangs hide her tear-stained eyes.)"
            show elianna talking at elianna_size, expression_pop
            elianna "It's okay... thank you for being honest with me. You've been so kind to me, and... I'll always keep this flower to remember the warmth you brought into my quiet life."
            # [ENDING CG: BITTERSWEET PETALS]
            "Ellie stands alone on the balcony as you quietly step away."
            "She gazes down at the everlasting Moon-Lily in her palm, wiping away her tears with a forced smile."
            "She returns to her infirmary as the devoted nurse of the Sanctum—her heart slightly heavy, but carrying a quiet, tender memory of the sorcerer who made her feel seen."
            # [SCENE END]
            $ elianna_ending = "bittersweet_petals"
            hide elianna
            jump finish_elianna_event
