# ============================================================
# CLARA VANE ROUTE — THE HEARTH BEYOND THE LEDGER
# FULL RESTORATION FROM CANONICAL WRITER DOCUMENT
# ============================================================
# All unique narrative, dialogue, choices, and outcomes are preserved.
# The duplicated Chapter 3 block in the source document is implemented once.

label clara_chapter_1:

    call route_transition("Clara Vane", 1, "The Hearth, the Ledger, and the Parcel") from _call_route_transition

    show clara sad at clara_size, enter_from_right
    # Scene 1: Ledgers and Earl Grey
    # Location: The Merchant Guildhall — Clara's Private Office (Midday)
    scene bg laughing_anchor at bg_character_focus
    with fade
    # [SCENE START]
    # SFX: Sound Effect: Muffled shouting of angry harbor merchants outside, rapid scratching of a quill on parchment, heavy clatter of wooden ledger boxes being stacked
    "(The Guildmaster’s office at the top of the Merchant Guildhall is usually an oasis of order, smelling of polished oak, warm wax, and dried lavender. Today, however, it resembles a war room.)" 
    "(Mountains of shipping manifests, tax disputes, and Sanctum reagent permits cover every inch of Clara Vane's desk.)"
    "(Clara sits behind the mahogany desk, her copper-brown hair pinned up in an elegant yet slightly unraveling braid.)" 
    "(Dressed in a dark green velvet coat with silver embroidery, she rubs her temples with a tired sigh, letting out a soft groan as she reviews a disputed cargo tariff.)"
    # Source [SPRITE: Clara Vane — Weary, Overwhelmed, Rubbing Temples]
    show clara sad at clara_size, char_center
    clara "If one more spice merchant threatens to throw his shipment into the bay over a two-copper import tax... I might just throw him in after it." 

    show clara surprised at clara_size, expression_squish
    "(She looks up as you enter, her exhausted expression immediately giving way to a warm, genuine smile that reaches her sharp, amber-hazel eyes.)"
    # Source [SPRITE: Clara Vane — Warm, Welcoming Smile]
    show clara happy at clara_size, expression_pop
    clara "Ah, little sorcerer. Come in, come in! Please tell me you brought quiet news from the Sanctum and not another official complaint about toxic alchemy runoff."

    menu:
        "Actually, I came to sign off on our reagent permits... and solve this tariff issue for you.":

            "(You step up to her desk, taking the disputed permit and cross-referencing it with Sanctum trade codes.)"

            "(You step up to her desk, taking the disputed permit and cross-referencing it with Sanctum trade codes.)"

            $ clara_affection += 20
            show clara surprised at clara_size, expression_squish
            "(You quickly point out an obscure Sanctum trade exemption clause in section four. Clara blinks in surprise, a relieved, brilliant smile breaking across her face.)"
        "Take a breath, Clara. Hand me half those ledgers—let me take some weight off your desk.":

            "(You pull up a comfortable leather chair and sit across from her with a calm, grounding presence.)"
            $ clara_affection += 20
            show clara happy at clara_size, expression_pop
            "(You pull four heavy manifests off her desk and begin quietly organizing them by guild seal. Clara watches you, her shoulders dropping two inches as her posture relaxes.)"
        "I hear the Guildmaster is working herself to the bone again.":

            "(You offer Clara a sleek, reassuring smile.)"
            $ clara_affection += 15
            show clara flirty at clara_size, expression_pop
            mc "Someone needs to look out for Mirthhaven's busiest woman."

    "(A faint, amused flush colors her cheeks)"
    show clara flirty at clara_size, expression_pop
    clara "Flattery from a handsome young scholar? Careful... I might start keeping you here on retainer."
    # [SCENE CONTINUES]
    "(Clara reaches for a silver teapot resting on a small stove in the corner, pouring two cups of dark, fragrant Earl Grey tea. She slides one porcelain cup across the mahogany desk to you, leaning back against her leather chair with a deep, contented sigh.)"
    # Source [SPRITE: Clara Vane — Relaxed, Sipping Tea]
    show clara happy at clara_size, expression_pop
    clara "You have a remarkably steady head on your shoulders for a young sorcerer. Most boys your age are busy picking fights at the docks or spending their coin at the gambling dens with Tariq."
    "(She smiles fondly over the rim of her teacup, her eyes lingering on your calm posture with quiet appreciation.)"
    # Scene 2: The Caretaker's Parcel
    # Location: The Merchant Guildhall — Clara's Private Office
    # [SCENE START]
    "(As you finish signing the reagent permits, Clara stands up and walks over to a side table. Resting beside her official guild seal is a neatly wrapped wooden lunch box, tied with a clean linen napkin and smelling of fresh crusty bread, roasted chicken, and sweet apples.)"
    "(Clara picks up the wooden parcel, looking at it with a blend of exasperated affection and maternal worry.)"
    # Source [SPRITE: Clara Vane — Exasperated, Fond Smile]
    show clara talking at char_center, expression_pop
    clara "Before you head back up the hill to your quarters... I have a small personal favor to ask."
    # [MC]
    mc "Anything, Clara. What is it?"
    # Source [SPRITE: Clara Vane — Holding Parcel, Shaking Head]
    show clara sad at char_center, expression_pop
    clara "That wild-haired lead alchemist up at the Sanctum—Tansy. She came down to the market two days ago to buy glass retorts, looking like she hadn't slept or eaten since Sunday. I know for a fact she hasn't left her laboratory since."
    "(She steps around her desk, holding out the warm wooden lunch parcel toward you.)"
    clara "She's going to starve herself into an alchemical explosion if someone doesn't force food down her neck. Would you be a dear and drop this off at her lab on your way through the Sanctum?"

    menu:
        "I'd be happy to, Clara. Someone needs to make sure our brilliant alchemist stays alive.":

            "(You take the warm wooden box gently from Clara.)"
            $ clara_affection += 15
            $ tansy_route_triggered = True
            show clara happy at char_center, expression_pop
            "(Clara's face brightens with immense gratitude. She squeezes your forearm gently.)"
            show clara happy at clara_size
            clara "Thank you, sweet boy. Tell her if she doesn't finish the apples, I'm coming up there to drag her out by her ears myself."
            hide clara
            jump clara_chapter_1_tansy_scene
        "You really can't stop taking care of everyone in Mirthhaven, can you?":

            "(You take the box, teasing Clara with a warm grin.)"
            $ clara_affection += 15
            $ tansy_route_triggered = True
            show clara happy at char_center, expression_pop
            "(Clara's face brightens with immense gratitude. She squeezes your forearm gently.)"
            show clara happy at  char_center, expression_pop
            clara "Thank you, sweet boy. Tell her if she doesn't finish the apples, I'm coming up there to drag her out by her ears myself."
            hide clara
            jump clara_chapter_1_tansy_scene
        "I'm running a bit tight on time today, Clara.":

            "(You politely decline the parcel.)"
            $ clara_affection += 15
            show clara sad at clara_size, char_center
            "(Sighs softly, setting the parcel back down)"
            show clara sad at clara_size, char_center 
            clara "Fair enough. I'll have a guild courier run it up later. Stay and finish your tea with me instead."
            # [TANSY ROUTE SKIPPED — CLARA ONLY PATH CONTINUES]
            jump clara_chapter_1_clara_only

label clara_chapter_1_tansy_scene:

    hide clara
    # Scene 3: The Smoke-Filled Lab (Secret Tansy Scene)
    # Location: The Sanctum — Alchemy Wing (Afternoon)
    scene bg solarium_sanctum at bg_character_focus
    with fade

    # [SCENE START]
    # SFX: Sound Effect: Distant bubbling cauldrons, quiet glass clinking, sudden harsh PFFFT-CLANK of an alchemical burner sputtering!
    "(The Sanctum's main alchemy laboratory is a chaotic labyrinth of towering brass pipes, glowing glass retorts, and floating parchment notes. The air smells strongly of dried lavender, sulfur, and copper.)"
    "(Standing on a small wooden step-stool over a towering glass crucible is Tansy." 
    "Her oversized scholar's robe is tucked messily into a leather tool belt, her wild amber-brown hair pinned up haphazardly with copper glass rods. A smudge of dark soot decorates her right cheek.)"
    # Source [SPRITE: Tansy — Disheveled, Obsessive, Muttering]
    tansy "No, no, no! If the Lotus petal's thermal density drops below four-hundred degrees, the catalyst crystallizes into sludge! Mirthhaven's stupid market spice-traders sold me sub-par lotus!"
    "(She turns around frantically to grab a measuring scale—and nearly trips off her step-stool!)"
    # SFX: Sound Effect: Sudden wooden rattle!
    show tansy worried at tansy_size, char_center, enter_from_right

    menu:
        "Catch Tansy before she falls.":

            "(You catch her arm gently before she falls, holding out the wooden lunch box.)"
            show tansy surprised at tansy_size, char_center, expression_squish
            "(Your steady hand catches her sleeve. Tansy blinks, her wide amber eyes focusing on you for the first time.)"
            "(Gasping, slightly flustered)"
            tansy "W-Wizard! What are you doing in my safety radius? Wait... is that roast chicken?"
        "Stage an official guild intervention.":

            "(You playfully snatch her glass stirring rod away and set the food box directly over her open alchemy ledger.)"
            show tansy confused at tansy_size, char_center, expression_pop
            tansy "Hey! Give back my catalyst rod! I am seven minutes away from a breakthrough on your curse cure—"
            "(Her stomach loudly betrays her with a long, rumbling growl.)"
            "(Blushes crimson)"
            tansy "...Okay, fine. Maybe nine minutes."
        "Relay Clara's threat.":

            "(You set the box down firmly.)"
            show tansy worried at tansy_size, char_center, expression_squish
            "(Shudders dramatically)"
            tansy "Clara said that? Gods, that woman is scarier than an unstable ether-bomb..."
            # [SCENE CONTINUES]

    "(Tansy climbs down from her step-stool, sitting unceremoniously on a brass tool crate. She opens Clara's wooden parcel, the scent of warm roasted chicken and fresh bread filling the cluttered lab.)"
    "(She pulls out a piece of crusty bread, taking a massive, undignified bite, her cheeks puffing out like a squirrel as she chews greedily.)"
    # Source [SPRITE: Tansy — Chewing Greedily, Soot on Cheek]
    "(Talking with her mouth half-full)"
    tansy "Mmmph! Okay... I admit it. Food was a solid tactical decision."
    "(She wipes her mouth with the back of her sleeve, leaving another streak of soot across her forehead. She looks up at you through her messy bangs, her eyes sparkling with chaotic, workaholic brilliance.)"
    # Source [SPRITE: Tansy — Curious, Smirking through Soot]
    tansy "You know... most scholars just drop reagent orders on my desk and run away before something explodes. You actually brought me lunch."
    # [MC]
    mc "Someone has to keep our lead alchemist alive. We can't cure my condition if you pass out from starvation."
    "(Giggles softly, a rare, genuine blush touching her nose)"
    tansy "Fair point, wizard. Tell Clara her chicken saved my life... and tell yourself that you just earned priority status in my laboratory."
    "(She takes another enthusiastic bite of roasted apple, flashing you a bright, messy smile before turning back to her glowing calculations.)"
    show tansy happy at tansy_size, char_center, expression_pop

    "(You leave the alchemy lab as Tansy happily devours her meal, returning to the Sanctum hallways with the warm satisfaction of a job well done. You have earned Clara's deep gratitude while setting up a secret bond with Mirthhaven's most brilliant alchemist.)"
    # [EVENT 1 COMPLETE — BRANCH A: The Caretaker's Reward (Clara Relationship Tier 1 Unlocked — Secret Flag [TANSY_FED] Active! Tansy Route Unlocks in Chapter 3!)]
    hide tansy
    jump finish_clara_event

label clara_chapter_1_clara_only:

    show clara happy at char_center, expression_pop

    "(You remain in Clara's quiet, oak-paneled office, sharing hot tea and quiet conversation until the afternoon shadows lengthen over the Merchant Guildhall. Clara looks at you with deep, tranquil comfort, grateful for a rare hour of peace.)"
    # [EVENT 1 COMPLETE — BRANCH B: The Guildmaster's Tea (Clara Relationship Tier 1 Unlocked — Deep Professional & Emotional Rapport)]
    # [SCENE END]
    hide clara
    jump finish_clara_event

label clara_chapter_2:

    call route_transition("Clara Vane", 2, "Caretaker's Burden") from _call_route_transition_1

    # Scene 1: Lanterns in the Quiet Market
    # Location: The Market District — Guild Supply Stall (Late Evening)
    scene bg market at bg_character_focus
    with fade
    # [SCENE START]
    # SFX: Sound Effect: Distant lap of harbor waves, soft creaking of hanging iron lanterns, cold evening wind whistling through empty wooden stalls
    "(The bustling Market District, usually deafening with shouting fishmongers and haggling spice merchants, is eerily quiet under the late-night sky. Most vendor stalls are shuttered, bathed in the long, flickering shadows of amber streetlamps.)"
    "(Near the central harbor warehouse, a single Guild lantern burns brightly. Clara Vane stands beside a stack of heavy wooden crates, clad in a dark travel cloak over her velvet tunic. She is alone, holding a heavy leather ledger in one hand while trying to adjust a displaced iron cargo strap with the other.)"
    # SFX: Sound Effect: Heavy iron strap slipping, muffled exhale of frustration
    "(Her copper-brown hair has slipped entirely from its formal braid, falling around her neck in soft, wavy strands. She looks exhausted—her shoulders drooping, her breath visible in the cool harbor air.)"
    # Source [SPRITE: Clara Vane — Alone, Weary, Struggling with Cargo]
    show clara sad at clara_size, char_center, expression_pop, enter_from_bottom
    clara "Come on, stay locked... If this silk cargo sits in the sea damp overnight, the entire harbor shipment is ruined..."

    menu:
        "Lock the heavy cargo strap into place.":

            "(You step in without a word, reaching over Clara's shoulder to lift the heavy iron cargo strap and lock it firmly into place.)"
            $ clara_affection += 15
            show clara surprised at char_center, expression_squish
            # SFX: Sound Effect: HEAVY METALLIC LATCH CLICK!
            "(Your hands cover hers on the cold iron, easily snapping the lever shut. Clara gasps softly, turning her head to find you standing close beside her.)"
            "(Exhales a long breath, her eyes softening)"
            show clara surprised at clara_size, char_center
            clara "You... you always show up right when my strength gives out, don't you?"
        "Working past midnight again, Clara?":

            "(You walk up with a calm, grounding presence.)"
            $ clara_affection += 15
            show clara talking at clara_size, char_center, expression_pop
            mc "You know, normal people go home when the sun sets."
            "(Lets out a small, self-deprecating laugh, rubbing her sore wrist)"
            show clara talking at clara_size, char_center
            clara "Normal people don't have forty merchant vessels docking at dawn, little wizard."
        "That's enough. You're stepping away from these crates.":

            "(You take the heavy ledger out of Clara's hand and set it on a nearby crate with a firm, protective smile.)"
            $ clara_affection += 20
            show clara teasing at clara_size, char_center, expression_pop
            mc "I'm relieving you of duty for the night, Clara."
            "(Blinks in surprise, a tired yet deeply touched smile breaking across her lips)"
            show clara teasing at clara_size, char_center
            clara "Relieving me? Careful... taking authority over the Guildmaster is a serious offense."
            # [SCENE CONTINUES]
            "(Clara attempts to take another step toward the next crate, but her knee buckles slightly from pure fatigue. She catches herself against the wooden bench of an empty spice stall, letting out a soft, defeated sigh.)"

    # Source [SPRITE: Clara Vane — Resting against Bench, Hand over Heart]
    clara "I just... needed to finish the manifest audits for the morning crew. Tariq was supposed to handle the harbor manifests, but he got dragged into a gambling match at the docks, and if I don't double-check the ledger seals—"
    # [MC]
    mc "Clara. Stop."
    "(You gently take her by her hands, guiding her down onto the wooden bench beneath the warm, amber glow of the hanging market lantern.)"
    # Scene 2: Taking Care of the Caretaker
    # Location: The Market District — Empty Spice Stall Bench
    # [SCENE START]
    # SFX: Sound Effect: Warm crackle of the iron lamp, gentle rustle of evening wind
    "(Clara sits on the wooden bench, her hands resting in her lap. For the first time since you met her, her rigid, dignified posture is gone. She looks smaller under the vast night sky, her amber-hazel eyes reflecting the flickering lantern light.)"
    "(Her fingers are cold from the harbor air, stiffness evident in her joints from hours of writing and hauling ledgers.)"

    menu:
        "Drape your warm cloak over Clara's shoulders.":

            "(You unclamp your warm outer cloak and drape it over her shoulders, tucking it gently around her neck.)"
            $ clara_affection += 15
            show clara happy at char_center, expression_pop
            "(The heavy, warm fabric settles over her shoulders. Clara buries her chin slightly into the collar, looking at you with breathless warmth.)"
            clara "It smells like crushed herbs and mountain wind... Thank you. I didn't realize how cold I was."
        "Warm Clara's hands with kinetic magic.":

            "(You sit beside her, taking her cold, quill-calloused hands between both of yours to warm them with gentle kinetic heat.)"
            $ clara_affection += 20
            show clara flirty at char_center, expression_pop
            # SFX: Sound Effect: Soft, magical hum of kinetic warmth
            "(A subtle wave of gentle thermal magic ripples from your palms into her fingers. Clara lets out a shuddering, contented sigh, her hands relaxing entirely in your grip.)"
        "Offer Clara the warm spiced mulled wine.":

            "(You pull out a small, sealed clay flask of warm spiced mulled wine you picked up from the tavern and hand it to her.)"
            $ clara_affection += 15
            show clara surprised at char_center, expression_squish
            "(Whispers)"
            clara "Your hands are so warm... That magic feels divine, wizard."
            "(She takes the warm flask, taking a small, slow sip. The spices bring a healthy, rosy color back to her pale cheeks.)"
            clara "Spiced pear wine... You really thought of everything, didn't you?"
    # Scene 3: Cracks in the Armor
    # Location: The Market District — Bench under the Lantern
    # [SCENE START]
    "(The silence between you is peaceful and deep. The empty market feels miles away from the noise of Mirthhaven. Clara leans back against the wooden support pillar, looking at you with a mix of wonder and quiet emotion.)"
    # Source [SPRITE: Clara Vane — Soft, Vulnerable, Looking at You]
    show clara sad at char_center, expression_pop
    clara "My whole life... ever since our parents passed and I took over the family debt... I've been the one holding the umbrella over everyone else's head."
    "(She looks down at her hands, a wistful, tender smile touching her lips.)"
    # Source [SPRITE: Clara Vane — Tender, Sincere Whispers]
    clara "I raised Tariq. I built the Guildhall network. I make sure two hundred merchants get paid every week, and that the town council doesn't starve the dockworkers."
    "(She turns her face toward you, her sharp eyes glistening with unreserved vulnerability.)"
    clara "In thirty years... almost no one has ever stopped to ask if I needed someone to hold the umbrella for me. No one... except a young sorcerer with a heart too big for his robes."

    menu:
        "Then let me hold it, Clara.":

            "(You reach out and gently tuck a stray lock of hair behind her ear, holding her gaze.)"
            $ clara_affection += 20
            show clara surprised at char_center, expression_squish

            "(Your fingers lightly brush against her cheek as you tuck her hair back. Clara's breath hitches softly. She doesn't pull away—instead, she leans her face slightly into your palm, closing her eyes as a tear of relief slips down her cheek.)"
            # Source [SPRITE: Clara Vane — Deeply Moved, Restings Against Your Hand]
            show clara surprised at char_center, expression_squish
            clara "I... I think I've waited my whole life to hear someone say that to me."
            "(She reaches up, covering your hand on her cheek with her own, holding you close in the quiet amber light of the market lantern.)"
            # [EVENT 2 COMPLETE — BRANCH A: The Caretaker's Sanctuary (Relationship Tier 2 Unlocked — Deep Emotional Sanctuary & Mutual Trust)]
            hide clara
            jump finish_clara_event
        "Mirthhaven can survive without its Guildmaster for one night.":

            "(You take her hand firmly, looking into her eyes with mature, unwavering devotion.)"
            $ clara_affection += 20
            show clara happy at char_center, expression_pop

            "(You squeeze her hand firmly, offering her a steady, grounded anchor that bridges any age gap between you.)"
            # [MC]
            mc "You're a human being before you're a Guildmaster, Clara. Let me look out for you."
            # Source [SPRITE: Clara Vane — Radiant, Sincere Emotion]
            "(Clara looks at you with profound, affectionate awe. She leans her shoulder against yours, resting her head softly against your shoulder under the cool night sky.)"
            show clara happy at char_center
            clara "You carry yourself with more strength and grace than men twice your age, wizard. I'm... so glad you came into my life."
            # [EVENT 2 COMPLETE — BRANCH B: Unmasked Devotion (Relationship Tier 2 Unlocked — Unshakeable Maturity & Emotional Bonding)]
            hide clara
            jump finish_clara_event
        "You take care of the entire city... it's about time someone took care of you.":

            "(You offer a warm, reassuring smile, leaning in slightly.)"
            $ clara_affection += 15
            show clara flirty at char_center, expression_pop

            "(You offer a bright, gentle smile that breaks through years of her built-up stress.)"
            # [MC]
            mc "It's my official duty as your favorite scholar."
            # Source [SPRITE: Clara Vane — Flustered Flush, Soft Chuckle]
            "(A soft, beautiful crimson flush colors Clara's cheeks. She lets out a warm, musical laugh, shaking her head affectionately as she wraps her arm through yours.)"
            show clara flirty at clara_size, char_center
            clara "Favorite scholar, hmm? You're playing a dangerous game, little sorcerer... my heart isn't as tough as my ledgers."
            "(The physical closeness and sweet romance linger long after the market lanterns fade, cementing a deep, mutual romantic attraction.)"
            # [EVENT 2 COMPLETE — BRANCH C: Warmth Beneath the Ledgers (Relationship Tier 2 Unlocked — Sweet Romantic Chemistry)]
            hide clara
            jump finish_clara_event

label clara_chapter_3:

    call route_transition("Clara Vane", 3, "Unmasked Warmth") from _call_route_transition_2

   
    # Scene 1: Wine at The Laughing Anchor
    # Location: The Laughing Anchor — Private Upper Booth (Night)
    scene bg laughing_anchor at bg_character_focus
    with fade
    # [SCENE START]
    # SFX: Sound Effect: Muffled lute music and low chatter from the tavern taproom below, gentle night breeze rustling the velvet curtains of the upper balcony booth
    "(Tucked away in the quietest, shadow-draped corner of the tavern's upper terrace, Clara Vane sits in a high-backed booth overlooking the illuminated harbor." 
    "Dressed down out of her formal guild coat, she wears a simple, soft linen shirt unbuttoned slightly at the collar. Her copper-brown hair falls freely over her shoulders in rich waves.)"
    "(A half-empty bottle of deep red Valen wine rests on the table alongside a single glass. Clara swirly the dark liquid, staring out at the sea with a weary, distant gaze.)"
    # Source [SPRITE: Clara Vane — Unarmored, Exhausted, Sipping Wine]
    show clara sad at clara_size, char_center, expression_pop
    clara "Three hours... Three whole hours of listening to the Town Council argue about salt tariffs while the city's storehouses rot. Sometimes I wonder why I bother."
    "(She notices you standing at the curtained entryway, her posture instantly softening as she gestures toward the cushion across from her.)"
    # Source [SPRITE: Clara Vane — Soft, Weary Smile]
    show clara happy at clara_size, char_center, expression_pop
    clara "Ah, sorcerer. Thank gods. Sit down before my mind completely numbs itself."

    menu:
        "Sounds like a brutal session. Let's leave the council outside.":

            "(You quietly slide into the booth across from her, pouring yourself a glass from the bottle.)"
            $ clara_affection += 20
            show clara happy at clara_size, char_center
            "(Clara lets out a long, grateful sigh, setting her chin in her hand as she watches you handle the wine with calm composure.)"
            show clara happy at clara_size, char_center
            clara "Always so composed. You have no idea how refreshing that is after dealing with loud old men all day."
        "The council doesn't deserve you, Clara. I'm here to steal you away for the night.":

            "(You sit beside her on the bench, offering a warm, grounding shoulder.)"
            $ clara_affection += 15
            show clara flirty at clara_size, char_center, expression_pop
            "(Clara's breath catches slightly as you sit close beside her. A faint, lovely color touches her cheeks.)"
            show clara flirty at clara_size, char_center
            clara "Steal me away, hmm? Careful... people might talk if the Guildmaster vanishes into the shadows with a sharp scholar."
        "Name the council members who annoyed you.":

            "(You slam your fist on the wooden table, scowling.)"
            $ clara_kid_warning = True
            show clara teasing at clara_size, char_center, expression_pop
            "(Clara blinks, her soft expression suddenly flattening into an amused, slightly patronizing chuckle. She reaches out and taps your nose lightly with her finger.)"
            "(Chuckles softly)"
            clara "Easy there, tiger. Save the hotheaded temper for the training yards. You sound just like Tariq when someone steals his dice."
            # [KID_WARNING_FLAG] ACCUMULATED!
    # Scene 2: The Age Gap & Hesitation
    # Location: The Laughing Anchor — Upper Booth
    # [SCENE START]
    "(The ambient noise of the tavern fades into the background. Clara sets her glass down, her amber-hazel eyes searching your face with a mix of deep fondness and sudden, nervous hesitation.)"
    # Source [SPRITE: Clara Vane — Flustered, Hesitant, Looking Down]
    show clara talking at char_center, expression_pop
    clara "I need to be honest with you about something... something that's been keeping me up at night."
    # [MC]
    mc "You can tell me anything, Clara."
    # Source [SPRITE: Clara Vane — Chewing Lip, Vulnerable]
    show clara sad at char_center, expression_pop
    clara "Look at us. You are young—brilliant, young, with your whole life and entire world stretching out ahead of you."
    clara "And me? I'm over thirty. I've spent my entire youth managing merchants, raising my brother, and carrying the weight of Mirthhaven."
    "(She traces the rim of her glass with a trembling finger, her voice dropping to a vulnerable, quiet whisper.)"
    clara "When I'm around you, my heart races like a foolish girl's. But then I stop and think... am I being selfish?"
    clara "Am I taking advantage of a bright young man who just needs someone to guide him?"
    clara "I don't ever want to be just another caretaker in your life... or worse, make a fool of myself."

    menu:
        "I don't need a caretaker, Clara. I need you.":

            "(You reach across the table, taking both her hands in yours with steady, unwavering strength.)"
            $ clara_affection += 25
            show clara happy at char_center, expression_pop
            "(Clara looks up, her eyes wide with emotional impact. Your calm, grounded devotion completely shatters her doubts. She lets out a trembling breath, squeezing your fingers tightly.)"
            show clara surprised at char_center, expression_squish
            clara "You... you say things with such absolute certainty. You make me feel like I can finally stop overthinking."
            jump clara_chapter_3_romance_continue
        "If you're making a fool of yourself, then so am I.":

            "(You lean in with a sincere, tender smile.)"
            $ clara_affection += 20
            show clara happy at  char_center, expression_pop
            "(Clara looks up, her eyes wide with emotional impact. Your calm, grounded devotion completely shatters her doubts. She lets out a trembling breath, squeezing your fingers tightly.)"
            show clara surprised at char_center, expression_squish
            clara "You... you say things with such absolute certainty. You make me feel like I can finally stop overthinking."
            jump clara_chapter_3_romance_continue
        "Why do you keep bringing up my age? I'm not a kid!":

            "(You pull your hands back defensively, frowning.)"
            $ clara_romance_locked = True
            show clara teasing at char_center, expression_pop
            "(The romantic tension in the air instantly dies. Clara's eyes soften, but the romantic spark in them vanishes, replaced by a weary, motherly indulgence. She chuckles softly, reaching over to gently pat your cheek like a protective older sister.)"
            "(Sighs fondly, shaking her head)"
            clara "Oh, sweet boy... see? That right there. That defensive pout is exactly what Tariq does when he wants to prove he's grown up."
            # [SIBLING_LOCKED] FLAG TRIGGERED! Proceeding to Branch Ending C!
            jump clara_chapter_3_family

label clara_chapter_3_romance_continue:

    # Scene 3: Deepening Bonds
    # Location: The Laughing Anchor — Upper Terrace Balcony

    # [SCENE START]
    "(Clara stands up from the table, stepping out onto the small, secluded balcony overlooking the starry harbor. The cool night sea air gently stirs her hair. You step up right behind her.)"
    "(Without hesitation, Clara turns around and closes the distance between you. She rests her hands gently against your chest, leaning her forehead against yours in the quiet darkness.)"
    # Source [SPRITE: Clara Vane — Eyes Closed, Leaning Against You, Intimate]
    "(Whispers softly)"
    clara "No one has looked at me the way you do in... I don't even know how long. Not as Guildmaster Vane. Not as Tariq's big sister. Just... Clara."
    "(Her breath is warm against your lips, her fingers clutching the front of your scholar's robes as she surrenders her guarded heart to you.)"
    show clara flirty at char_center, expression_pop
    clara "If you'll have me... age, ledgers, and all... I'm yours, sorcerer."
    show clara flirty at  char_center

    if clara_affection >= 100 and not clara_kid_warning:

        "(You wrap your arms firmly around Clara's waist, pulling her close against you. She lets out a contented, soft sigh, lifting her face to press a slow, deep, passionate kiss to your lips under the starlight—sealing her route for Chapter 4.)"
        # [EVENT 3 COMPLETE — BRANCH A: The Hearth's Embrace (Clara Relationship Tier 3 Unlocked — Full Romantic Lock! Ready for Chapter 4 Finale!)]
    else:

        "(You hold her hand firmly against your heart, letting her feel how rapidly it beats for her. Clara smiles radiantly, kissing your cheek softly before resting her head against your shoulder as you watch the harbor lights together.)"
        # [EVENT 3 COMPLETE — BRANCH B: Unmasked Devotion (Clara Relationship Tier 3 Unlocked — Deep Mutual Attraction! Ready for Chapter 4 Finale!)]

    hide clara
    jump finish_clara_event

label clara_chapter_3_family:

    $ clara_romance_locked = True
    show clara happy at char_center, expression_pop

    "(The atmosphere becomes completely platonic. Clara smiles warmly, but the romantic boundary is firmly re-erected. She wraps a motherly arm around your shoulders, giving you an affectionate side-hug as if you were her younger brother.)"
    # Source [SPRITE: Clara Vane — Patronizing, Maternal Smile, Arm around Shoulder]
    clara "You're a good kid, sorcerer. Truly. Remind me to give you an extra allowance of reagent permits tomorrow—you and Tariq really are the little brothers I never knew I needed to keep me on my toes."
    "(She pats your back heartily before turning back to her wine, completely blind to any romantic intent. You are permanently locked out of Clara's romance route.)"
    # [EVENT 3 COMPLETE — BRANCH C: The Big Sister's Shield (ROMANCE FAILED — Clara permanently views you as a younger sibling/kid. Route Ended.)]
    # [SCENE END]
    hide clara
    jump finish_clara_event

label clara_chapter_4:

    call route_transition("Clara Vane", 4, "Where the Anchor Rests") from _call_route_transition_3

    # Scene 1: Midnight on the Harbor Docks
    # Location: The Seadocks (Midnight)
    scene bg nautilus_point at bg_character_focus
    with fade
    # [SCENE START]
    # SFX: Sound Effect: Slow, rhythmic lap of ocean waves against dark oak pylons, distant chime of the city harbor bell striking midnight
    "(The harbor is quiet, silver moonlight reflecting off the dark, glass-like water. The major guild trade conflict that had threatened Mirthhaven's docks for months has finally been settled, thanks to your Sanctum diplomacy and Clara's sharp economic maneuvering.)"
    "(Clara stands at the edge of the wooden pier, looking out toward the horizon. She still wears her familiar dark green velvet coat with silver embroidery, though her coat is unbuttoned against the soft night air, and her long copper-brown hair flows loosely over her shoulders in the sea breeze.)"
    "(She turns as she hears your boots on the creaking dock planks. Her sharp, amber-hazel eyes catch the moonlight, softening into a look of profound, breathtaking tenderness.)"
    # Source [SPRITE: Clara Vane — Soft, Reflective, Moonlight on Face]
    show clara happy at clara_size, char_center, enter_from_bottom
    clara "Listen to that... Silence. Real, unbroken silence. I can't remember the last time the docks were this peaceful at midnight."
    "(She steps closer to you, the hem of her dark green velvet coat brushing against your boots. She wraps her arms around herself, letting out a long, quiet breath.)"
    show clara sad at clara_size, char_center, expression_pop
    clara "Before you came into my life, sorcerer... I honestly believed my youth was completely behind me."
    clara "I used to look in the mirror every morning at thirty-two and see an old, tired woman whose whole existence was reduced to ink, tax ledgers, and trade manifests."
    "(She reaches out, her hand trembling slightly as her cold, soft fingers gently touch the side of your neck, feeling the warm pulse beneath your skin.)"
    # Source [SPRITE: Clara Vane — Vulnerable, Sincere, Eyes Glistening]
    show clara sad at clara_size, char_center
    clara "I convinced myself that love was something meant for other people—for the young, the carefree, people who had time for romance."
    clara "My schedule was my cage, and my age was my sentence."
    clara "But then... you looked at me. Not as Guildmaster Vane. Not as a weary bossy woman... but as Clara."

    if clara_romance_locked:
        jump clara_chapter_4_family_path

    menu:
        "You were never old, Clara. You just forgot how to shine.":

            "(You cover her hand on your neck with yours, stepping close until there is no space between you.)"
            $ clara_affection += 20
            show clara happy at clara_size, char_center, expression_pop
            "(Clara lets out a shaky breath, a brilliant crimson blush sweeping across her cheeks. She smiles with a pure, radiant joy that makes her look like a girl half her age.)"
            show clara surprised at clara_size, char_center, expression_squish
            clara "You... you always know exactly how to make my heart feel like it's nineteen again."
        "An old woman? I see a vibrant, stunning woman who steals my breath every day.":

            "(You smile warmly, wrapping your arm gently around her waist.)"
            $ clara_affection += 15
            show clara flirty at clara_size, char_center, expression_pop
            "(She lets out a soft, musical laugh, resting her hands against your chest as she leans into your warm embrace.)"
            show clara flirty at clara_size, char_center
            clara "Flatterer. But gods help me... I love hearing you say it."
        "Hey, you're not old! You've got as much energy as Tariq.":

            "(You offer a friendly, energetic pat on her shoulder.)"
            $ clara_romance_locked = True
            show clara teasing at clara_size, char_center, expression_pop
            "(Clara's warm expression settles into a fond, sisterly smile. She chuckles softly, shaking her head as she gives your shoulder an affectionate squeeze.)"
            "(Sighs fondly)"
            clara "Always comparing me to Tariq... You really are two of a kind, aren't you?"
            # [FAMILY_PATH_CONFIRMED]
            jump clara_chapter_4_family_path
    # Scene 2: Strolling Through the Starlit City
    # Location: The Market District / Cobblestone Streets (Late Night)
    # [SCENE START]
    # SFX: Sound Effect: Quiet echoing footsteps on smooth cobblestones, soft rustle of midnight wind through empty vendor stalls
    "(You walk together back toward the central district. The city is asleep, the warm amber streetlamps casting long, intimate shadows across the stone paths. Clara walks close beside you, her hand entwined tightly with yours, her fingers interlocked with a steady, protective warmth.)"
    # Source [SPRITE: Clara Vane — Radiant, Holding Hands, Looking Up]
    show clara happy at clara_size, char_center, expression_pop
    clara "Look at these streets... I've walked down this exact path ten thousand times. Running to cargo emergency meetings, chasing down late shipments, worrying about gold and guild politics. I never once noticed how pretty the moonlight looks on the cobblestones."
    "(She stops beneath the warm glow of a streetlamp, turning her body to face you fully. Her green coat catches the amber light, her eyes sparkling with a playful, newfound lightness.)"
    # Source [SPRITE: Clara Vane — Playful Flush, Bicker-Flirting]
    show clara teasing at clara_size, char_center, expression_pop
    clara "Do you know what you've done to me, wizard? You've ruined my terrible work ethic. Yesterday, during the harbor council meeting, I spent twenty minutes staring out the window daydreaming about... well, about taking long walks with an eighteen-year-old scholar who turned my whole world upside down."

    menu:
        "Then stop fighting it, Clara. Walk with me through everything that comes next.":

            "(You pull her close by her waist, gazing directly into her eyes.)"
            $ clara_affection += 25
            show clara flirty at clara_size, char_center, expression_pop
            "(Clara's breath catches. She steps into your space, her chest pressing against yours. All her former worries about her age, her position, and her heavy schedule vanish entirely in the warmth of your gaze.)"
            show clara flirty at clara_size, char_center
            clara "I'm done fighting it. I don't care about the age gap, I don't care about the city rumors... I just want you."
            jump clara_final_ending_check
        "I'm not going anywhere, Clara. I'll always be waiting at the end of your day.":

            "(You lift her hand to your lips, pressing a tender, respectful kiss to her knuckles.)"
            $ clara_affection += 20
            show clara flirty at clara_size, char_center
            "(Clara's breath catches. She steps into your space, her chest pressing against yours. All her former worries about her age, her position, and her heavy schedule vanish entirely in the warmth of your gaze.)"
            show clara flirty at clara_size, char_center
            clara "I'm done fighting it. I don't care about the age gap, I don't care about the city rumors... I just want you."
            jump clara_final_ending_check
        "If Tariq heard that, he'd tease you for being a sappy big sister!":

            "(You chuckle awkwardly, scratching the back of your neck.)"
            $ clara_romance_locked = True
            show clara teasing at clara_size, char_center, expression_pop
            "(Clara blinks, her flustered expression cooling into a warm, indulgent, maternal grin. She reaches up and messily ruffles your hair like a loving older sister.)"
            "(Laughs warmly)"
            clara "He certainly would! Which is why you are going to keep your mouth shut about it, little brother."
            # [PERMANENT_FAMILY_LOCK] ACTIVATED! Proceeding to Branch Ending C!
            jump clara_chapter_4_family_path

label clara_final_ending_check:

    if clara_romance_locked:
        jump clara_chapter_4_family_path
    elif clara_affection >= 100:
        jump clara_ending_true
    else:
        jump clara_ending_good

label clara_ending_true:

    $ clara_ending = "hearth_of_the_heart"
    # Scene 3: Where the Anchor Rests
    # Location: The Merchant Guildhall — Clara's Private Office (Late Night)
    scene bg laughing_anchor at bg_character_focus
    with fade
    # [SCENE START]
    # SFX: Sound Effect: Soft click of a heavy brass door locking shut, quiet crackle of a warm hearth fire burning in the corner
    "(You return to where it all began: Clara's private office at the top of the Merchant Guildhall." 
    "(The room smells of polished oak, warm wax, and familiar dried lavender. The heavy stacks of chaotic ledgers that once overwhelmed her desk have been neatly put away.)"
    "(Clara stands beside her mahogany desk, bathed in the soft, flickering orange light of the fireplace." 
    "She unclasps the silver chain at her throat, letting out a long, peaceful sigh as she looks around her domain—a room that used to feel like her personal prison, but now feels like home.)"
    show clara flirty at clara_size, char_center, expression_pop

    "(Clara walks around her desk toward you. From her coat pocket, she pulls out a heavy, ornate brass key stamped with her personal Guildmaster seal. She takes your hand, pressing the cold key directly into your palm, before closing her warm fingers over yours.)"
    # Source [SPRITE: Clara Vane — Deeply In Love, Soft Tear of Happiness]
    show clara flirty at clara_size, char_center
    clara "This is the master key to my private residence... and to my heart."
    clara "For fifteen years, I gave every second of my life to Mirthhaven, believing I was destined to end up alone, buried under work and age."
    "(She reaches up, resting both her hands on your cheeks, her thumb softly tracing your cheekbone as a quiet, breathless tear of pure joy slips down her cheek.)"
    clara "You gave me back my youth, sorcerer. You made me feel wild, beautiful, and desperately in love for the very first time in my life."
    clara "I don't care how busy my days get—my nights will always belong to you."
    "(Clara pulls you down into a deep, slow, passionate kiss under the warm glow of the Guildhall hearth. Her arms wrap tightly around your neck, holding you close as the harbor bells chime softly in the distance, sealing a lifelong partnership of love, passion, and shared sanctuary.)"
    # [STORY COMPLETE — TRUE ROMANCE ENDING: "The Hearth of the Heart" — Clara Vane's Route Completed! You gave her back her youth, earning a loving, devoted life partner in Mirthhaven's formidable Guildmaster!]
    hide clara
    jump finish_clara_event

label clara_ending_good:

    $ clara_ending = "anchored_in_devotion"
    scene bg laughing_anchor at bg_character_focus
    # Scene 3: Where the Anchor Rests
    # Location: The Merchant Guildhall — Clara's Private Office (Late Night)
    # [SCENE START]
    # SFX: Sound Effect: Soft click of a heavy brass door locking shut, quiet crackle of a warm hearth fire burning in the corner
    "(You return to where it all began: Clara's private office at the top of the Merchant Guildhall." 
    "The room smells of polished oak, warm wax, and familiar dried lavender. The heavy stacks of chaotic ledgers that once overwhelmed her desk have been neatly put away.)"
    "(Clara stands beside her mahogany desk, bathed in the soft, flickering orange light of the fireplace." 
    "She unclasps the silver chain at her throat, letting out a long, peaceful sigh as she looks around her domain—a room that used to feel like her personal prison, but now feels like home.)"
    show clara happy at clara_size, char_center, expression_pop

    "(Clara sits beside you on the edge of her mahogany desk, resting her head against your shoulder as the fire crackles softly.)"
    # Source [SPRITE: Clara Vane — Content, Peaceful Smile]
    show clara happy at clara_size, char_center
    clara "I spent so long worrying about the years between us... but when I'm in your arms, time doesn't mean a thing. You are my anchor, wizard."
    "(She turns her face, pressing a tender, sweet kiss to your lips, holding your hand tightly as you spend the rest of the night sharing quiet wine and warm laughter in her office.)"
    # [STORY COMPLETE — SWEET ROMANCE ENDING: "Anchored in Devotion" — Clara Vane's Route Completed! A sweet, grounded romance built on mutual respect and everlasting warmth!]
    hide clara
    jump finish_clara_event

label clara_chapter_4_family_path:

    $ clara_romance_locked = True
    $ clara_ending = "guildmasters_family"
    scene bg laughing_anchor at bg_character_focus
    # Scene 3: Where the Anchor Rests
    # Location: The Merchant Guildhall — Clara's Private Office (Late Night)
    # [SCENE START]
    # SFX: Sound Effect: Soft click of a heavy brass door locking shut, quiet crackle of a warm hearth fire burning in the corner
    "(You return to where it all began: Clara's private office at the top of the Merchant Guildhall." 
    "The room smells of polished oak, warm wax, and familiar dried lavender. The heavy stacks of chaotic ledgers that once overwhelmed her desk have been neatly put away.)"
    "(Clara stands beside her mahogany desk, bathed in the soft, flickering orange light of the fireplace." 
    "She unclasps the silver chain at her throat, letting out a long, peaceful sigh as she looks around her domain—a room that used to feel like her personal prison, but now feels like home.)"
    show clara happy at clara_size, char_center

    "(Clara steps up to her desk and pulls out a polished wooden box. Inside rests a silver signet ring carrying the Merchant Guild seal. She hands it to you with a proud, deeply affectionate smile.)"
    # Source [SPRITE: Clara Vane — Proud, Sisterly / Maternal Smile]
    clara "I raised Tariq to be a man, but I never thought I'd find another younger brother to care about as much as him. You've brought so much life, energy, and trouble into this boring old Guildhall."
    "(She wraps her arms around you in a big, warm, motherly hug, patting your back heartily like a loving older sister.)"
    # Source [SPRITE: Clara Vane — Hearty Laugh, Patting Your Back]
    show clara happy at clara_size, char_center
    clara "You're family now, sorcerer. Official Guild family. If anyone in Mirthhaven ever gives you trouble, you come tell your big sister, and I'll handle them myself!"
    "(Though romantic love was not found, you earned an unshakeable, lifelong spot as a cherished younger brother in Clara and Tariq's family, gaining the absolute protection and fierce loyalty of Mirthhaven's Guildmaster forever.)"
    # [STORY COMPLETE — PLATONIC ENDING: "The Guildmaster's Family" — Clara Vane permanently sees you as a beloved younger brother/family member. Deep loyalty and lifelong family bond established!]
    # [SCENE END]
    hide clara
    jump finish_clara_event
