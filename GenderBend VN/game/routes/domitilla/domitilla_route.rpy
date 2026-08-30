# ============================================================
# DOMITILLA BRUNI ROUTE — FULL / DECLUTTERED / EXPRESSIVE
# Canonical writer document preserved.
# Writer-facing unlock/branch/completion notices are hidden.
# Long passages are split for VN readability.
# ============================================================

label domitilla_chapter_1:

    call route_transition("Domitilla Bruni", 1, "Discipline and Iron")

    show domitilla angry at domitilla_size, char_center
    # Scene 1: The Ring of Sweat and Steel
    # Location: The Crestward Bastion — The Iron Ring (Morning)
    # [SCENE START]
    # SFX: Sound Effect: Heavy iron clashing, rhythmic boots stomping in dirt, harsh shouting of drillmasters, wind snapping through heavy military banners
    "(The Crestward Bastion smells of sun-baked stone, furnace smoke, and leather. In the center of the training grounds lies \"The Iron Ring\"—a sunken dirt pit where the city garrison's elite vanguard refines their combat readiness. You stand near the wooden perimeter rail, observing the tactical application of combat maneuvers for your Sanctum research.)"
    "(Barking orders at a line of exhausted, sweat-drenched recruits is Commander Domitilla Bruni."
    "Towering, built like a siege wall, and wearing blackened steel plate armor marked by years of campaign scars, she commands the pit with terrifying authority.)"
    # Source [SPRITE: Commander Domitilla — Stern, Barking Orders]
    domitilla "Wider stance! If a harbor drake hits that shield wall, half of you are going into the bay! Again!"
    "(She turns to grab a water skin—and her sharp, dark eyes lock onto you standing by the rail. There is no polite greeting, no acknowledgement of your Sanctum robes.)"
    # SFX: Sound Effect: Sudden heavy wooden WHOOSH!
    "(Without warning, Domitilla scoops a heavy, padded practice buckler off a weapon rack and hurls it straight at your chest!)"
    # Source [SPRITE: Commander Domitilla — Smirking, Challenging]
    domitilla "Hey! You! Sanctum scholar! Stop gawking from the cheap seats and get in the Ring! Let's see if those magic robes are just for show!"

    menu:
        "Catch the buckler cleanly.":
            "(You catch the heavy buckler cleanly out of the air and strap it to your forearm without breaking eye contact.)"
            show domitilla surprised
            "(The wooden buckler slaps into your palm with a dull thud. You tighten the leather strap instantly, stepping down into the dirt pit.)"
            "(Grunts, her dark eyes flashing with mild surprise)"
            domitilla "Decent grip. At least you don't have butterfingers like these new recruits."
        "Catch the buckler with kinetic magic.":
            "(You cast a swift kinetic pulse to catch and freeze the buckler mid-air, snagging it casually with a smirk.)"
            show domitilla happy
            "(The shield stops dead an inch from your chest, enveloped in a blue shimmering aura before you take it in hand.)"
            "(Chuckles gruffly, hefting a heavy wooden practice longsword)"
            domitilla "Fancy tricks. Let's see if that aura holds up when eighty pounds of steel comes cracking down on it."
        "Catch it, recover, and step into the pit.":
            "(You catch the buckler clumsily against your chest, but immediately square your shoulders and step into the pit.)"
            show domitilla surprised
            "(You stumble back a step from the weight, but quickly catch your footing, strapping the buckler on and vaulting over the wooden rail.)"
            "(Raises an eyebrow)"
            domitilla "Lacks grace, but you didn't run away. That's already better than most bookworms."
            # [SCENE CONTINUES]
            "(Domitilla steps into the center of the dirt pit. Even carrying a blunted training sword, her presence is suffocatingly intense—a veteran soldier who has survived a hundred bloody battlefields.)"
            # Source [SPRITE: Commander Domitilla — Weapon Raised, Battle Stance]
            domitilla "Garrison rules, wizard. No lethal spells. Keep your feet planted, protect your core, and don't cry if you get a bruise. Ready!"

    show domitilla talking
    # Scene 2: Testing the Spine
    # Location: The Iron Ring — Sparring Circle
    # [SCENE START]
    # SFX: Sound Effect: Sudden explosion of dirt, heavy boot thrust, wooden sword whistling through the air!
    "(Domitilla moves with frightening speed for someone encased in steel armor.)"
    "(She closes the distance in a single stride, bringing her practice blade down in a brutal overhead strike meant to test your reaction time and shatter your guard.)"
    "(The recruits around the pit go silent, watching to see if the Sanctum scholar gets flattened into the dirt.)"
    menu:
        "Reinforce your buckler and absorb the blow.":
            "(You raise your buckler and reinforce it with a dense kinetic barrier, absorbing her overhead blow head-on.)"
            show domitilla surprised
            # SFX: Sound Effect: HEAVY CRACK OF WOOD ON BARRIER!
            "(Her sword slams into your barrier-reinforced buckler. Shockwaves ripple through your arms, but your stance holds firm in the dirt. Domitilla's arms recoil from the impact.)"
            domitilla "Solid! You actually rooted your weight!"
        "Daze her and slip around her flank.":
            "(You weave a swift flash-light spell to momentarily daze her vision, stepping agilely around her flank.)"
            show domitilla happy
            "(A burst of brilliant white light flares. Domitilla blinks, her strike missing by an inch as you pivot behind her, ringing your buckler against her backplate.)"
            "(Pivots instantly, a sharp grin spreading on her face)"
            domitilla "Clever footwork! Using the sun against me!"
        "Meet her strike with a kinetic counter-force.":
            "(You meet her blow halfway, using a targeted kinetic force-push against her sword hilt to lock weapons in a contest of leverage.)"
            show domitilla surprised
            # SFX: Sound Effect: DULL METALLIC REBOUND!
            "(Your magic-infused counter-force slams into her blade guard, locking your buckler against her sword. You stand toe-to-toe, your faces inches apart in a clash of pure willpower.)"
            "(Her muscles strain, eyes wide with fierce thrill)"
            domitilla "Look at you pushing back! Not bad, kid!"

    show domitilla happy
    # Scene 3: Iron in the Spine
    # Location: The Iron Ring — Post-Spar
    # [SCENE START]
    # SFX: Sound Effect: Domitilla lowering her sword, heavy exhale of breath
    "(Domitilla steps back, disengaging from the bout.)"
    "(She unhelms her head, letting her dark, sweat-dampened hair fall around her scarred face.)"
    "(She grabs a coarse linen towel from the rail, wiping the sweat from her neck as she looks you up and down.)"
    "(Around the pit, the watching recruits murmur in disbelief. You didn't fold. You stood your ground against the Garrison Commander.)"
    "(A rare, razor-sharp smirk cuts across Domitilla's scarred, sun-bronzed face—a look of genuine, fierce approval.)"
    # Source [SPRITE: Commander Domitilla — Razor-Sharp Smirk, Impressed]
    domitilla "Well, well. Most scholars from the Sanctum crumble the second steel flashes in their face. They drop their wands, mess their robes, and start quoting academy regulations."
    "(She tosses her practice sword onto a wooden rack with a loud clatter, walking up to you and clapping a heavy, armored hand onto your shoulder—nearly knocking the wind out of you with her sheer physical strength.)"
    # Source [SPRITE: Commander Domitilla — Approving, Towering Presence]
    domitilla "You've got actual iron in your spine, sorcerer. Come back to the Bastion when you want real training."
    menu:
        "I'll be back, Commander. And next time, don't hold back.":
            "(You wipe the dirt off your tunic and smirk back at her.)"
            show domitilla happy
            # [MC]
            mc "I'm holding you to that, Domitilla. Next time, give me everything you've got."
            # Source [SPRITE: Commander Domitilla — Boisterous Laugh, Grinning]
            "(Domitilla throws her head back and lets out a booming, full-chested laugh that echoes off the stone ramparts.)"
            domitilla "Ha! I like the fire in your belly, wizard! Keep that attitude up, and I might just turn you into a vanguard officer yet. The Ring is open to you anytime."
            "(You unstrap the buckler and hand it back, leaving the Iron Ring with the fierce satisfaction of having earned the respect of the city's toughest warrior.)"
            hide domitilla
            jump finish_domitilla_event
        "It's an honor to learn from the best warrior in Mirthhaven.":
            "(You salute her respectfully with the buckler before returning it.)"
            show domitilla talking
            # [MC]
            mc "Thank you, Commander. It's rare to find a martial master who understands how to test magic properly."
            # Source [SPRITE: Commander Domitilla — Nodding, Serious Respect]
            "(Domitilla nods firmly, her sharp smirk softening into an expression of dignified, professional respect.)"
            domitilla "A weapon is only as good as the hand holding it—that goes for magic wand or broadsword alike. You proved your hand is steady today. You're welcome in my garrison anytime."
            "(She takes the buckler back, giving you a sharp military nod as you step out of the dirt pit onto the main courtyard.)"
            hide domitilla
            jump finish_domitilla_event
        "I wanted to see the famous Commander Bruni in action.":
            "(You step closer, meeting her fierce dark eyes directly.)"
            show domitilla surprised
            # [MC]
            mc "I've heard rumors about the unbreakable Commander Bruni. I had to see if the legends were true."
            # Source [SPRITE: Commander Domitilla — Flustered Glint, Smirking]
            "(Domitilla's dark eyes flare with an unexpected, flustered heat. She steps into your personal space, towering over you with a dangerous, thrilling smirk.)"
            domitilla "Is that so? Checking up on me, wizard? Well... now you know the legends don't do me justice. Don't be a stranger. I keep a close eye on people who catch my attention."
            "(She brushes past you, her heavy armor shoulder lightly bumping yours as she strides off to yell at her recruits—leaving your heart thumping from the intense physical chemistry.)"
            # [SCENE END]
            hide domitilla
            jump finish_domitilla_event

label domitilla_chapter_2:

    call route_transition("Domitilla Bruni", 2, "Scars and Heavy Armor")

    show domitilla normal at domitilla_size, char_center
    # Scene 1: After-Hours in the Armory
    # Location: The Crestward Bastion — The Central Armory (Night)
    # [SCENE START]
    # SFX: Sound Effect: Distant harbor waves, quiet crackle of dying forge embers, clinking of metal tools, heavy leather straps unbuckling
    "(The Bastion’s main armory is vast and shadowed at night.)"
    "(Racks of gleaming pikes, heavy tower shields, and suits of steel plate line the stone walls.)"
    "(You carry a leather satchel containing a set of lightweight, fire-resistant warding charms you enchanted specifically for her division’s vanguard armor.)"
    "(Sitting alone on a low wooden workbench at the back of the room is Commander Domitilla."
    "Her heavy breastplate and gauntlets lie on a table beside her."
    "Without her towering harness, clad only in a damp linen undertunic and dark trousers, she looks surprisingly human—weary, her dark hair messy, her broad shoulders mapped with old, faded battle scars.)"
    "(She grimaces softly, reaching up with her right hand to flex and rub a dark, angry purple bruise along her left shoulder.)"
    # Source [SPRITE: Commander Domitilla — Unarmored, Weary, Sore]
    "(Without looking up)"
    domitilla "Armory is closed, soldier. Leave your requisition forms on the desk..."
    "(She turns her head and spots you holding your satchel. Her sharp stance instantly relaxes, replaced by a low, tired exhale.)"
    domitilla "Ah. It's you, wizard. Apologies. Fourteen hours in full plate will make a woman blind to who's walking through the door."
    menu:
        "That looks like a nasty blow. Are you alright?":
            "(You set your satchel down softly and point to her shoulder.)"
            show domitilla surprised
            mc "That bruise looks painful, Domitilla."
            "(Grunts, flexing her arm with a grimace)"
            domitilla "Took a bad hit from a recruit's polearm during heavy drills. It's nothing I haven't slept off a hundred times before."
        "It looks like you need attention more than the armor does.":
            "(You step closer and offer your satchel.)"
            show domitilla surprised
            mc "The charms can wait until morning. Let me see that shoulder."
            "(Raises an eyebrow, mildly surprised by your direct concern)"
            domitilla "Direct and attentive. I can respect that."
        "Even the unbreakable Commander Bruni needs a tune-up?":
            "(You tease her gently with a warm smile.)"
            show domitilla happy
            mc "Does the garrison know their commander has a weak spot?"
            "(A small, tired smirk touches her lips)"
            domitilla "Keep your voice down, scholar. You'll ruin my terrifying reputation."
    show domitilla talking
    # [SCENE CONTINUES]
    "(You unbutton your satchel and draw out a small glass jar of magic-infused healing salve. The amber potion glows faintly with a soothing, warm luminescence.)"
    # Source [SPRITE: Commander Domitilla — Hesitant, Guarded]
    domitilla "What's that?"
    # [MC]
    mc "Alchemical warming salve. It draws out muscle strain and heals deep bruising. Sit still and let me help."
    "(Domitilla hesitates.)"
    "(For a soldier who spends every waking hour taking care of hundreds of recruits, being the one on the receiving end of care is clearly a foreign, uncomfortable concept.)"
    "(But after a quiet pause, she nods, rolling back the linen sleeve of her tunic to expose her broad, scarred shoulder.)"
    # Scene 2: Beneath the Breastplate
    # Location: The Central Armory — Workbench
    # [SCENE START]
    # SFX: Sound Effect: Soft hum of magic salve, quiet crackle of embers
    "(You step up behind her on the wooden bench. Scooping a generous portion of the warm, amber balm onto your fingers, you gently press your hands against the tight, knotted muscles of her shoulder.)"
    "(At your initial touch, Domitilla's entire body tense like cold iron. Her breath hitches in her throat.)"
    # Source [SPRITE: Commander Domitilla — Tense, Surprised]
    domitilla "Ngh—"
    # [MC]
    mc "Easy... just let the heat soak in."
    "(Your fingers begin to work in slow, firm circles.)"
    "(You channel a faint, gentle current of magic through your palms, easing the deep tissue tension.)"
    "(Underneath your hands, you can feel the faint, raised silver lines of ancient weapon scars across her back and shoulders—tactile history written across her skin.)"
    "(Slowly, agonizingly, the rigid military posture begins to dissolve. Domitilla lets out a long, shuddering sigh, her head tilting back slightly as the pain fades.)"
    menu:
        "You've fought in a lot of hard battles to earn these, haven't you?":
            "(You gently trace the edge of a prominent scar near her collarbone with genuine respect.)"
            show domitilla normal
            "(Domitilla's eyes close as your fingers lightly skim the raised silver mark.)"
            "(Quietly)"
            domitilla "Campaign in the Northern Passes. Took a stray crossbow bolt holding the ridge. Reminds me why I wear heavy plate now."
        "Try to breathe through it. Your muscles are practically locked up.":
            "(You apply firm, expert pressure to a deep knot, focusing purely on easing her pain.)"
            show domitilla happy
            "(A satisfying pop echoes in the quiet room as the knot releases under your magic-infused pressure.)"
            "(Exhales deeply, her head resting back against your arm for support)"
            domitilla "Gods above... that magic of yours is a miracle, wizard."
        "You don't always have to bear the brunt of every hit.":
            "(You lean down slightly, speaking softly near her ear.)"
            show domitilla surprised
            "(Your warm breath against her neck causes a faint goosebump to ripple down her arm.)"
            "(Whispers)"
            domitilla "If I don't take the hit... someone weaker does. That's the duty."
    show domitilla normal
    # Scene 3: The Wall That Gets Tired
    # Location: The Central Armory — Workbench
    # [SCENE START]
    "(The silence in the dimly lit armory is heavy, warm, and intensely intimate. The distance between the formidable Garrison Commander and the Sanctum sorcerer has completely evaporated.)"
    "(Domitilla sits quietly under your hands."
    "Her heavy shoulders are completely relaxed, resting against your chest as you finish applying the balm."
    "She looks down at her large, calloused, weapon-worn hands resting on her knees.)"
    # Source [SPRITE: Commander Domitilla — Soft, Vulnerable, Looking Down]
    domitilla "In the garrison... to the recruits, the officers, the city council... everyone looks to me as an unbreakable wall."
    "(She turns her head slightly, her dark, tired eyes meeting yours under the soft amber light of the armory lantern."
    "The hardened commander's mask is completely gone, leaving only a woman carrying a heavy weight.)"
    # Source [SPRITE: Commander Domitilla — Soft, Sincere Whisper]
    domitilla "It’s... rare for anyone to ask if the wall ever gets tired."
    menu:
        "Then let me hold up the wall for a little while tonight.":
            "(You rest your hands gently on her uninjured shoulder, leaning in close.)"
            show domitilla happy
            "(You keep your hands rested on her broad shoulders, offering a solid, comforting anchor against her weariness.)"
            # [MC]
            mc "Lean on me tonight, Domitilla. The garrison can survive without their wall for a few hours."
            # Source [SPRITE: Commander Domitilla — Deeply Moved, Soft Smile]
            "(Domitilla exhales a shaky breath and leans her back fully against you, letting her head rest against your shoulder in total, unreserved trust.)"
            domitilla "I... I think I'll take you up on that offer, wizard. Just for tonight."
            "(You remain together in the quiet warmth of the armory, the heavy commander finally finding a safe harbor to lay down her burdens.)"
            hide domitilla
            jump finish_domitilla_event
        "You're a human being before you're a commander.":
            "(You step around to face her, looking down into her eyes with deep warmth.)"
            show domitilla surprised
            "(You step in front of her, validating her humanity with steady, sincere conviction.)"
            # [MC]
            mc "You carry the weight of this whole city, Domitilla. Don't feel ashamed for feeling tired. You're allowed to be human."
            # Source [SPRITE: Commander Domitilla — Surprised, Radiant Respect]
            "(Domitilla looks up at you, her dark eyes shining with intense, newfound appreciation. She reaches out, her large, warm hand clasping yours in a firm, lingering hold.)"
            domitilla "You see right through the armor, don't you? Thank you... I needed to hear that more than you know."
            "(The quiet understanding between warrior and scholar solidifies into a bond built on profound mutual care.)"
            hide domitilla
            jump finish_domitilla_event
        "You're much softer under all that steel than you let on.":
            "(You gently tilt her chin up with your fingers, giving a soft smile.)"
            show domitilla happy
            "(You gently touch her jaw, lifting her face to meet your gaze with a teasing, electric warmth.)"
            # [MC]
            mc "Everyone thinks you're made of stone and iron... but I'm starting to see how sweet you really are."
            # Source [SPRITE: Commander Domitilla — Flustered Flush, Husky Smirk]
            "(A distinct, dark flush of flustered heat rises across Domitilla's sun-bronzed cheeks.)"
            "(She lets out a low, husky rumble of a chuckle, her hand coming up to wrap around your wrist—not to pull you away, but to keep your touch against her face.)"
            domitilla "Careful, wizard... say things like that, and I might just keep you trapped in my armory all night."
            "(The air thickens with unmistakable physical attraction, proving that beneath her heavy armor lies a heart capable of burning desire.)"
            # [SCENE END]
            hide domitilla
            jump finish_domitilla_event

label domitilla_chapter_3:

    call route_transition("Domitilla Bruni", 3, "Off-Duty Fire")

    show domitilla happy at domitilla_size, char_center
    # Scene 1: Mead and Unbuttoned Collars
    # Location: The Laughing Anchor — Private Corner Booth (Night)
    # [SCENE START]
    # SFX: Sound Effect: Boisterous sea-shanties, fiddle music, clinking wooden tankards, roaring fireplace crackle
    "(Far from the disciplined stone corridors of the Crestward Bastion, the back corner of The Laughing Anchor is warm, noisy, and thick with the scent of roasted meat and heavy mead.)"
    "(Tucked into a shadowed booth away from the main tavern floor sits Commander Domitilla Bruni.)"
    "(She is completely out of uniform.)"
    "(Dressed in a loose, cream-colored linen shirt with the collar unbuttoned at her throat and a dark leather vest, she looks remarkably broad, relaxed, and striking.)"
    "(A half-empty horn of dark dwarven mead sits in her large hand.)"
    # Source [SPRITE: Commander Domitilla — Off-Duty, Relaxed, Boisterous]
    domitilla "Well, look what the tide washed in! Sit down, wizard! I was starting to think everyone in this tavern was too terrified to share a bench with me."
    "(She slams her mead horn onto the oak table with a heavy thud, sliding over on the bench to make room."
    "A deep, full-chested laugh rumbles from her chest—a rich, warm sound you’ve never heard on the parade grounds.)"
    # Source [SPRITE: Commander Domitilla — Broad Smirk, Laughing]
    domitilla "No drillmasters, no inspection reports, no council politics tonight. Just good brew and decent company. Drink with me!"
    menu:
        "To off-duty commanders and surviving another week of garrison drills.":
            "(You slide onto the wooden bench beside her and raise a tankard.)"
            show domitilla happy
            # SFX: Sound Effect: CLINK OF TANKARDS!
            "(Laughs heartily, clinking her horn against yours)"
            domitilla "I'll drink to that! The recruits nearly drove me to execution duty on Tuesday!"
        "Commander... you look incredible out of your armor.":
            "(You look her up and down with an appreciative smile.)"
            show domitilla surprised
            "(A dark, handsome flush touches her cheeks, though she smirks)"
            domitilla "Watch it, wizard. Flattery gets you extra laps in the pit... but I won't pretend I don't like hearing it."
        "Tell me some real campaign stories.":
            "(You lean back against the bench, amused.)"
            show domitilla happy_talking
            "(Grins, taking a deep swig of mead)"
            domitilla "Oh, I've got stories that would make your Sanctum archmagi turn pale as chalk."
    show domitilla happy_talking
    # [SCENE CONTINUES]
    "(The evening wears on.)"
    "(Domitilla drops her stern commander facade entirely, swapping rough military jokes, slapping the table when she laughs, and leaning her heavy shoulder into yours as the tavern music swells.)"
    # SFX: Sound Effect: Heavy, drunken footsteps approaching, harsh voice breaking through the music
    "(The warm atmosphere is suddenly interrupted as a large, foul-smelling mercenary covered in greasy iron spandrels stumbles over to your booth, carrying a slopping mug of ale.)"
    # [MERCENARY]
    "Mercenary" "Well, well... look at the garrison guard dog off her leash! What's the matter, Commander? Couldn't find a real soldier to drink with, so you brought a little Sanctum lapdog to hold your hand?"
    # Scene 2: Frontline Defense
    # Location: The Laughing Anchor — Corner Booth
    # [SCENE START]
    "(The mercenary sneers, reaching out an unwashed, aggressive hand to shove his way onto your table, spilling ale over your clothes.)"
    "(Domitilla’s eyes instantly narrow. Her jaw tightens, her hand instinctively dropping to where her sidearm usually sits as she begins to rise from the bench to crush the drunkard.)"
    # Source [SPRITE: Commander Domitilla — Rising, Dangerous Scowl]
    domitilla "You've got three seconds to pull that filthy hand back before I—"
    "(Before she can step up to take the blow, you move.)"
    show domitilla angry
    menu:
        "Disarm him with a controlled kinetic spell.":
            "(You step smoothly between Domitilla and the mercenary, weaving a silent kinetic spell that disarms his aggression and sends his mug flying into the trash.)"
            # SFX: Sound Effect: SWIFT KINETIC WHOOSH!
            "(A localized pulse of kinetic air disarms the mercenary in a flash.)"
            "(His mug shatters in the fireplace, and a invisible force shoves him back three paces into the crowd, completely disorienting him until his friends drag him away.)"
            jump domitilla_chapter_3_honorable
        "Shield Domitilla and force him back.":
            "(You place a firm hand on Domitilla's shoulder to keep her seated, stepping directly in front of her to form an unbreakable magical barrier.)"
            # SFX: Sound Effect: HEAVY MAGICAL BARRIER IMPACT!
            "(You plant your feet squarely in front of Domitilla.)"
            "(A dense blue barrier flashes into existence, absorbing the mercenary's shove and detonating backward with the force of a battering ram, knocking him flat on his back.)"
            "(The tavern cheers as he scrambles away in embarrassment.)"
            jump domitilla_chapter_3_honorable
        "Use the agonizing hex.":
            "(You cast a dark, excruciating nerve-shredding hex that causes the mercenary to collapse in screaming agony.)"
            # SFX: Sound Effect: HARSH VAMPIRE-LIKE HEX CHIME, AGONIZED SCREAM!
            "(You weave a dark, forbidden agonizing curse.)"
            "(The mercenary gasps, clutching his throat as invisible needles tear through his nervous system.)"
            "(He drops to his knees in front of the table, vomiting blood onto the floor and weeping in agony as the tavern goes dead silent in horror.)"
            jump domitilla_chapter_3_dishonorable

label domitilla_chapter_3_honorable:
    show domitilla surprised
    # Scene 3: The Sentinel's Heat / Consequence
    # Location: The Laughing Anchor — Corner Booth
    # [SCENE START]
    "(If Option A or Option B was chosen, the drunk mercenary retreats, leaving the booth safe and clear.)"
    "(Domitilla sits back down on the bench, completely stunned.)"
    "(Her dark eyes are wide as she looks at you—a woman who has spent her entire life standing on the frontlines for everyone else, suddenly realizing someone just stepped in front of her.)"
    # SFX: Sound Effect: Heartbeat hum, warm tavern lantern light
    # Source [SPRITE: Commander Domitilla — Stunned, Flustered Heat, Dark Eyes Flashing]
    "(Her face burns with a fierce, flustered heat. Without a word, she reaches across the table and grabs your hand in a firm, calloused, lingering grip that practically pins your fingers to the oak wood.)"
    # Source [SPRITE: Commander Domitilla — Low, Husky Whisper]
    domitilla "You... you stepped up when it counted."
    "(She leans across the narrow table, her deep voice dropping into a low, husky whisper that vibrates through your chest.)"
    domitilla "I've spent fifteen years taking the blow for everyone in this city. Nobody steps in front of Commander Bruni. Nobody... except you."
    "(She squeezes your hand tighter, her thumb tracing over your knuckles with intense physical attraction.)"
    domitilla "I like it. Gods help me... I really like it."
    show domitilla happy
    menu:
        "From now on, you don't fight alone.":
            "(You turn your hand within her grip, lacing your fingers firmly with hers.)"
            show domitilla happy
            "(You lace your fingers tightly with hers, holding her calloused hand in an unbreakable grip.)"
            # [MC]
            mc "You're not the only one with iron in your spine, Domitilla. We stand together."
            # Source [SPRITE: Commander Domitilla — Radiant, Fierce Smirk]
            "(Domitilla's breath hitches before a triumphant, breathtaking smile breaks across her face. She pulls your hand to her lips, pressing a warm, firm kiss to the back of your hand.)"
            domitilla "A true partner on the battlefield and off it... I'm holding you to that vow, sorcerer."
            hide domitilla
            jump finish_domitilla_event
        "You protect the city... but who protects you?":
            "(You lean across the table, meeting her intense gaze inches away.)"
            show domitilla surprised
            "(You lean in close, meeting her fierce gaze with steady, passionate conviction.)"
            # [MC]
            mc "Every shield needs someone backing it up. Let me stand behind you."
            # Source [SPRITE: Commander Domitilla — Deeply Moved, Intense Attraction]
            "(Domitilla exhales a low, shaky breath. She reaches up with her free hand, cupping the side of your neck with her large, warm palm.)"
            domitilla "Consider yourself appointed, wizard. And I don't give up my vanguard easily."
            "(The physical heat between you turns electric under the dim tavern lights, solidifying a deep, protective romantic bond.)"
            hide domitilla
            jump finish_domitilla_event
        "You look awfully flustered for a Garrison Commander.":
            "(You smirk softly, teasing her flustered state.)"
            show domitilla happy
            "(You offer a sleek, teasing smile, enjoying how completely undone the tough commander is.)"
            # [MC]
            mc "I didn't think the great Commander Bruni could get so flustered over a little protection."
            # Source [SPRITE: Commander Domitilla — Flustered Growl, Thrilled]
            "(Domitilla lets out a low, dangerous rumble in her throat, her dark eyes flashing with irresistible challenge as she pulls you slightly closer by your collar.)"
            domitilla "Watch your tongue, scholar... or I'll have to show you exactly how a commander handles a teasing subordinate."
            "(The banter dissolves into thrilling, electric attraction, proving that your strength matches her fierce spirit.)"
            hide domitilla
            jump finish_domitilla_event

label domitilla_chapter_3_dishonorable:
    $ domitilla_route_locked = True
    $ domitilla_romance_locked = True
    show domitilla angry
    # SFX: Sound Effect: TAVERN SILENCE, DISTRESSING GROANS OF THE TORTURED MERCENARY!
    "(As the drunk mercenary twitches and bleeds on the floor under your agonizing hex, you look back at Domitilla expecting praise... but find only cold, sharp disgust in her eyes.)"
    # Source [SPRITE: Commander Domitilla — Standing, Cold Disgust, Disappointed Scowl]
    "(Domitilla abruptly stands up, slamming her palm onto your wrist to instantly break your spell focus. The mercenary collapses unconscious into his own puddle.)"
    domitilla "Enough!"
    "(Her voice isn't the warm, off-duty tone from moments ago—it is the icy, unforgiving command of a soldier who lives by a strict martial code.)"
    # Source [SPRITE: Commander Domitilla — Stern, Reprimanding]
    domitilla "I am a Commander of the Garrison. We use force to defend the innocent and enforce order... not to torture an unarmed drunkard for petty spite!"
    # [MC]
    mc "I was defending you, Domitilla!"
    domitilla "That wasn't defense, sorcerer! That was sadism!"
    "(She grabs her heavy leather cloak from the bench, wrapping it around her broad shoulders and looking down at you with bitter disappointment.)"
    domitilla "I thought you had iron in your spine. But torture and cruel magic are the tools of cowards. I'll see myself back to the Bastion."
    "(Domitilla turns her back and strides out of The Laughing Anchor into the cold night, leaving you alone in a dead-silent tavern.)"
    "(By choosing dark, excessive cruelty over honorable combat, you have severely damaged her respect for your character.)"
    # [SCENE END]
    hide domitilla
    jump finish_domitilla_event

label domitilla_chapter_4:

    call route_transition("Domitilla Bruni", 4, "The Sentinel's Vow")

    show domitilla normal at domitilla_size, char_center
    # Scene 1: Above the City of Sails
    # Location: The Crestward Bastion — Rooftop Ramparts at Dusk
    # [SCENE START]
    # SFX: Sound Effect: Heavy ocean breeze snapping through crimson garrison banners, distant gulls crying, twilight bell chiming across Mirthhaven
    "(High above the noise of the harbor, the rooftop ramparts of the Crestward Bastion offer an unbroken view of Mirthhaven.)"
    "(The setting sun paints the sky in striking ribbons of deep violet, fiery orange, and twilight gold.)"
    "(The flickering lanterns of the lower city begin to ignite one by one like a fallen constellation.)"
    "(Standing alone at the edge of the stone battlements is Commander Domitilla Bruni."
    "Her heavy commander’s cloak billows around her broad shoulders in the sea wind."
    "She has left her helmet and pauldrons behind, wearing only her leather brigandine and dark tunic."
    "Her dark hair catches the twilight breeze, and her scarred, sun-bronzed face is bathed in the warm amber glow of sunset.)"
    # SFX: Sound Effect: Boots stepping lightly on stone
    "(As you step onto the battlements, Domitilla turns her head.)"
    "(Seeing you, the stern, hyper-vigilant posture she maintains for the garrison completely dissolves, replaced by an unmistakable softness in her dark eyes.)"
    # Source [SPRITE: Commander Domitilla — Windblown, Gentle Softness]
    domitilla "I was wondering when you'd arrive, wizard. Up here... the wind blows away the smell of forge smoke and old ledgers. It's the only place in the city where I can actually hear myself think."
    menu:
        "It's a breathtaking view, Domitilla. But I prefer the company.":
            "(You walk up to the battlement ledge and stand beside her, shoulder to shoulder.)"
            show domitilla happy
            mc "There's nowhere else in Mirthhaven I'd rather be right now."
            "(A soft, radiant smile touches her lips)"
            domitilla "Nor I. The city looks entirely different when I'm looking at it with you."
        "You shouldn't stand out in the sea chill without your armor.":
            "(You step up quietly and gently adjust the clasp of her heavy cloak against the cold wind.)"
            show domitilla surprised
            "(Your fingers brush against her neck as you adjust her cloak. Domitilla leans into your touch slightly, exhaling a quiet, contented breath.)"
            domitilla "Always looking out for me... I'm still not used to it, but gods know I'm grateful."
        "Reporting for duty on the high watch, Commander Bruni.":
            "(You offer a sleek, playful military salute before leaning against the stone rail.)"
            show domitilla happy
            mc "Standing guard with you isn't the worst assignment in the world."
            "(Chuckles softly, her deep voice humming against the breeze)"
            domitilla "At ease, scholar. Tonight, there are no commanders. Just us."
    show domitilla talking
    # [SCENE CONTINUES]
    "(Domitilla turns her back to the city, leaning her hips against the stone parapet.)"
    "(She reaches up to the collar of her tunic, her large, calloused fingers resting on a heavy, ancient bronze insignium pinned to her lapel.)"
    "(It is the Garrison Commander’s personal crest—a heavy, hand-forged bronze shield stamped with the Mirthhaven iron ring."
    "It is an emblem given only to the highest vanguard officer, symbolizing a knight’s personal honor and absolute authority.)"
    # SFX: Sound Effect: Soft metallic unclasping
    "(With deliberate, slow reverence, Domitilla unclasps the bronze crest from her cloak.)"
    # Scene 2: The Weight of Bronze
    # Location: The Crestward Bastion — Rooftop Ramparts
    # [SCENE START]
    "(Domitilla steps directly into your personal space, closing the remaining distance until you can feel the steady, reassuring warmth radiating from her broad frame.)"
    # Source [SPRITE: Commander Domitilla — Serious, Deeply Sincere]
    domitilla "When I took command of the Crestward Vanguard fifteen years ago, they gave me this crest."
    domitilla "It represents my blood, my oath, and my life."
    domitilla "It means I am the first shield in the dirt and the last wall standing before the gate."
    "(She takes your right hand, opening your palm."
    "She presses the heavy, warm bronze insignium directly into your hand, then wraps both of her large, calloused palms around yours, closing your fingers over the bronze.)"
    # Source [SPRITE: Commander Domitilla — Holding Hands, Tender Intensity]
    domitilla "A commander only passes this crest to one person in their lifetime... the person they trust with their absolute life."
    menu:
        "This is the highest honor you could ever give me.":
            "(You gently squeeze her broad hands back, looking up into her dark eyes.)"
            show domitilla happy
            mc "I know what this means to you. I won't ever take it for granted."
            "(Her fingers tighten around yours, her expression intensely tender)"
            domitilla "I know you won't. That's why it belongs in your hands."
        "I will guard it with my life.":
            "(You trace the warm metal with your thumb, feeling its weight.)"
            show domitilla happy
            mc "I'll wear this as a reminder that I always have your back."
            "(A proud, fierce light gleams in her eyes)"
            domitilla "A true vanguard. I couldn't have chosen a better partner."
        "Are you sure about this?":
            "(You hold her gaze with genuine concern.)"
            show domitilla normal
            mc "You don't have to give up your burden to prove your trust."
            "(Shakes her head softly, a quiet smile breaking across her face)"
            domitilla "I'm not giving up a burden, wizard. I'm choosing who I share my life with."
    show domitilla happy
    # [SCENE CONTINUES]
    "(The twilight sky shifts into a velvet dusk, the first stars sparkling above the sea. Domitilla does not let go of your hands. Her dark eyes shine with an unreserved, burning vulnerability.)"
    # Source [SPRITE: Commander Domitilla — Emotional Confession, Unreserved Love]
    domitilla "I spent my whole life training to be an unbreakable shield for Mirthhaven. I thought my destiny was to die in my armor on some forgotten battlefield, holding a line alone."
    "(She steps even closer, her thumb gently stroking the back of your hand.)"
    domitilla "I never thought I’d find someone who made me want to lay that heavy shield down... and just be a woman."
    domitilla "You fought your way through my armor, sorcerer... into my heart."
    domitilla "And I am never letting you go."
    # Scene 3: Vanguard of the Heart
    # Location: The Crestward Bastion — Rooftop Ramparts (Night)
    # [SCENE START]
    "(The wind hums softly through the stone battlements.)"
    "(Domitilla stands exposed before you—no longer just the fierce Commander of the Garrison, but a deeply passionate, devoted woman awaiting your final response.)"
    menu:
        "Pull Domitilla into a passionate kiss.":
            "(You reach up, grab the lapels of her commander's cloak, and pull her down into a deep, passionate, and unreserved kiss under the twilight sky.)"
            $ domitilla_ending = "vanguard_of_the_heart"
            show domitilla surprised
            # SFX: Sound Effect: Romantic brass and string orchestral swell, heavy sea wind whistling warmly
            "(You don't hesitate. You reach up, grabbing the heavy lapels of her cloak, and pull the towering commander down to meet you.)"
            "(You seal her confession with a deep, breathless, and fierce kiss under the starry sky.)"
            # Source [SPRITE: Commander Domitilla — Stunned -> Overjoyed, Fierce Passion]
            "(Domitilla lets out a low, shuddering gasp before her arms wrap securely around your waist, lifting you slightly off your feet and pulling you flush against her broad, warm chest.)"
            "(Her kiss is intense, tender, and filled with years of unspoken longing.)"
            "(When you finally part, she rests her forehead against yours, her large hands cradling the back of your head, her chest heaving with deep, breathless laughter.)"
            domitilla "By the gods... you really know how to take a commander's breath away."
            # [MC]
            mc "You laid down your shield, Domitilla. Let me be the one who protects you now."
            "(Smirks softly, her dark eyes brimming with absolute devotion)"
            domitilla "Not alone, wizard. We stand shoulder to shoulder. In the garrison, in the Sanctum, and in every night to come."
            "(High above the glowing city of Mirthhaven, the city's legendary commander finds her true home—not behind cold iron walls, but in the warmth of your arms.)"
            hide domitilla
            jump finish_domitilla_event
        "Pledge yourself as her lifelong vanguard partner.":
            "(You clasp the bronze insignium firmly over your heart and pledge your eternal loyalty as her vanguard partner on and off the battlefield.)"
            $ domitilla_ending = "shield_bound_oath"
            show domitilla happy
            # SFX: Sound Effect: Majestic military horn melody, warm ambient wind
            "(You take the heavy bronze crest and press it firmly over your heart, looking into her eyes with unshakeable conviction.)"
            # [MC]
            mc "I accept this crest, Domitilla. From this day forward, wherever you ride, whatever wall you hold... my magic and my life are bound to yours. We fight as one."
            # Source [SPRITE: Commander Domitilla — Proud, Radiant Respect]
            "(Domitilla’s eyes flare with intense, noble pride. She places her large palm directly over your hand and the crest, bowing her head toward you in a soldier's sacred oath.)"
            domitilla "A shield-bound oath... the strongest contract a vanguard can make. You are my equal, my partner, and my closest companion. Mirthhaven will fall to ash before anyone breaks our line."
            "(Hand in hand, you and Commander Bruni turn to look over the city skyline—a formidable duo bound by iron discipline, mutual respect, and lifelong loyalty.)"
            hide domitilla
            jump finish_domitilla_event
        "Return the crest and remain noble allies.":
            "(You gently close her broad fingers back over the bronze crest, holding her gaze with fond regret.)"
            $ domitilla_ending = "unyielding_watch"
            show domitilla normal
            # SFX: Sound Effect: Melancholic french horn and cello duet, cold gust of ocean wind
            "(You look at the bronze insignium in your palm, then gently lift her hand, closing her broad, calloused fingers back over the metal.)"
            # [MC]
            mc "Domitilla... this crest belongs on your lapel."
            mc "Mirthhaven needs Commander Bruni—unbroken, legendary, and unburdened."
            mc "You are the finest warrior I have ever known, but my path lies with the Sanctum."
            mc "I cannot be the lover you deserve."
            # Source [SPRITE: Commander Domitilla — Bittersweet Dignity, Soft Regret]
            "(A long, quiet pause settles over the high ramparts."
            "Domitilla looks down at the bronze crest in her hand."
            "She doesn't flinch or show anger."
            "Instead, she draws a slow, heavy breath, her stoic military dignity settling back over her features—tempered now with a sad, profound tenderness.)"
            domitilla "I see... A clear, honest refusal. Spoken like a true soldier."
            "(She re-clasps the bronze crest onto her cloak. She steps forward, her large, warm hand gently cupping the back of your neck, and presses a firm, deeply respectful kiss to your forehead.)"
            # Source [SPRITE: Commander Domitilla — Gentle, Noble Farewell]
            domitilla "Do not apologize, sorcerer. Having your respect and your brotherhood is a treasure I will carry until my final battle. The garrison will always consider you one of our own."
            "(She turns back to face the vast, starry expanse of Mirthhaven, her cloak billowing in the cold wind."
            "You stand beside her in quiet, noble camaraderie—forever bound as cherished allies, carrying the bittersweet memory of a love that yielded to duty.)"
            # [SCENE END]
            hide domitilla
            jump finish_domitilla_event