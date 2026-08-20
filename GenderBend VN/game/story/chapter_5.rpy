label chapter_5:

    call chapter_transition(5, "Rebirth & A Master's Pride")
    # =========================
    # SCENE 1 - The Drinking of the Alkahest
    # =========================

    # Location: The Solarium Sanctum — Grand Alchemy Laboratory
    # (Sound Effect: Swirling magical energy, golden liquid bubbling in a crystal goblet, deep thrumming spell resonance)

    "(The crystal goblet rests upon the polished stone altar, filled to the brim with the glowing, honey-gold Alkahest of True Form. The radiant potion emanates a blend of sea-spray cool, draconic heat, solar warmth, and starlight magic.)"

    # [SPRITE: Tansy — Eager, Anticipatory]
    tansy "This is it, my star apprentice! Six catalyst ingredients from all six districts of Mirthhaven, forged into a single elixir. Bottoms up!"

    # [SPRITE: Ellie — Nervous, Hands Clasping]
    ellie "Please be careful... Drink slowly so the reversal magic can flow through your mana channels evenly."

    "(You pick up the heavy crystal goblet. The golden brew sparkles against your reflection, reflecting the female form you've inhabited throughout your arduous quest across Mirthhaven.)"

    mc "Here goes everything..."

    # CHOICE 1
    menu:
        "(Raise the goblet high and drink with calm, steady focus, guiding the spell flow through your core)":
            "(The golden liquid glides smoothly down your throat. A harmonious warmth spreads from your chest, aligning perfectly with your internal magic channels.)"
            tansy "Flawless posture! Look at that spell synchronization!"

        "(Embrace the wild elemental surges with unyielding willpower, downing the potion in one gulped breath)":
            "(You gulp down the brew in one bold motion! A violent rush of draconic fire and sea currents surges through your veins.)"
            tansy "HA! That's how a real wizard drinks! Ride the wave!"

        "(Hesitate nervously before taking a trembling sip)":
            "(You take a small, hesitant sip, but as the magic touches your tongue, the Alkahest automatically ignites, washing over your mouth in a warm cascade.)"
            ellie "Don't be afraid! Let the solar warmth guide you!"

    # (Sound Effect: ROARING EXPANSION OF MAGIC! Divine solar light and draconic flame erupting!)
    "(Blinding golden light bursts from your skin, illuminating the entire laboratory! A swirling aura of dragon-fire, ocean vapor, lotus shadow, and hardened marrow energy lifts you inches off the marble floor. The transfiguration curse burns away like dry leaves in a forge!)"

    # (Sound Effect: Deep sigh of magical release, gentle thud of boots landing on stone)
    "(The blinding light slowly fades into shimmering dust. You look down at your hands—they are broad, familiar, and calloused from years of staff training. Your voice drops back into its natural, resonant male register.)"

    mc "My voice... my hands... I'm back. I'm finally back to myself!"

    # [SPRITE: Tansy — Boisterous, Boasting Laughter]
    tansy "BHAHAHAHA! IT WORKED! BY THE HIGHER MAGES, IT WORKED!"

    "(Tansy leaps forward, slapping your shoulder with enough force to send you stumbling.)"

    # [SPRITE: Tansy — Proud, Beaming]
    tansy "Look at you! Restored, unscathed, and carrying the magic of six districts! I declare this the greatest practical exam the Solarium Sanctum has ever seen—and you passed with flying colors!"

    # [SPRITE: Ellie — Tearful, Gentle Smile]
    ellie "Welcome back, sorcerer. You were truly remarkable through it all."

    # =========================
    # SCENE 2 - The Gathering at The Laughing Anchor
    # =========================

    # Location: The Laughing Anchor — Main Taproom (Nightfall)
    # (Sound Effect: Boisterous tavern crowd, clinking beer mugs, roaring hearth fire, lively acoustic fiddles)

    "(Night has fallen over Mirthhaven. The grand taproom of The Laughing Anchor is decorated with guild banners and flower garlands. Gathered around the main high table is the entire cast: Clara Vane, Tariq Vane, Barek Tidejaw, Bao Zhao, Commander Domitilla Bruni, Ellie Sylvane, and Tansy.)"

    # (Sound Effect: Door opening, tavern noise briefly quieting)
    "(You step through the wooden entrance in your original male body, clad in a fresh, master-tier apprentice cloak.)"

    # [SPRITE: Barek Tidejaw — Booming Voice, Grinning]
    barek "HO! LOOK WHO IT IS! The hero of the docks has returned!"

    # [SPRITE: Bao Zhao — Laughing, Raising Mug]
    bao "BHAHA! So that's what you look like in your true form! Handsome kid! Come sit down and grab a dark draught!"

    # [SPRITE: Clara Vane — Warm, Welcoming]
    clara "Welcome back, young master. You look positively radiant tonight."

    # [SPRITE: Tariq Vane — Sly, Smirking]
    tariq "I must admit... you carry your true face just as sharply as you carried my market deal. Well done, wizard."

    # [SPRITE: Commander Bruni — NDT Nod, Crossed Arms]
    bruni "Hmph! Standing tall! Good to see you recovered from the Iron Ring!"

    "(They clear a central seat for you at the head of the table. Tansy hands you an overflowing horn of spiced honey-mead.)"

    # CHOICE 2
    menu:
        "(Raise your mead horn high, giving a humble and heartfelt tribute to everyone who helped you)":
            mc "To Mirthhaven! To the strength of the Bastion, the wisdom of the Guild, the fire of the Docks, and the healing of the Sanctum!"
            "Everyone raises their glasses together."
            "TO MIRTHHAVEN!"

        "(Playfully tease Tansy while boasting about out-smarting every trial in Mirthhaven)":
            mc "I survived Tansy's potion, Barek's nets, Bao's fire, Tariq's shadow games, and Bruni's giant blade! Nothing in this city can stop me now!"
            tansy "Ha! Don't get cocky, hotshot! I still have fifty untested potions in the vault!"

        "(Gaze warmly at Ellie and the guild masters, expressing your deep gratitude for their trust)":
            mc "I couldn't have gathered a single catalyst without every one of you believing in me. Thank you."
            ellie "It was an honor to stand by your side..."

    "(The tavern celebration reaches its peak. Music fills the air, feast platters are emptied, and stories of your quest echo across the room. As midnight approaches, the guild leaders look toward you with deep expectation.)"

    # [SPRITE: Clara Vane — Smiling]
    clara "You began this day as a flustered apprentice hiding from a botched potion... but you end it as a spell-caster who unified all six districts."

    # [SPRITE: Commander Bruni — Stern, Proud]
    bruni "So state your intent, wizard. Where does your staff lead you next?"

    # =========================
    # SCENE 3 - The Path Ahead
    # =========================

    # Location: The Laughing Anchor — Hearthside (Midnight)
    "(The room falls quiet as everyone listens. The hearth fire casts golden light across your face and your polished sorcerer staff.)"

    # CHOICE 3
    menu:
        "(Formally embrace your path as a true Arch-Mage in training—weaving all six district elements into a breathtaking, harmonious starlight illusion over the tavern)":
            $ chapter_5_ending = "legacy_of_the_arch_mage"
            jump chapter_5_ending_a

        "(Pledge your staff directly to Mirthhaven's people—stepping beyond the Sanctum walls to become the city's official roaming Champion and protector)":
            $ chapter_5_ending = "champion_of_mirthhaven"
            jump chapter_5_ending_b

        "(Arrogantly attempt to show off your restored power by casting an unvetted, maximum-power multi-elemental spell blast inside the enclosed tavern to impress everyone)":
            $ chapter_5_ending = "tavern_reckoning"
            jump chapter_5_ending_c


label chapter_5_ending_a:

    # (Sound Effect: Melodious starlight chime, gentle glowing aura expanding, soft murmurs of awe)
    "(You close your eyes and raise your staff. Instead of destruction, a breathtaking canopy of soft golden starlight, bioluminescent sea-waves, and glowing lotus petals sweeps across the ceiling of The Laughing Anchor. The six elements dance in perfect, serene harmony above the crowd.)"

    # [SPRITE: Tansy — Wiping a Tear, Radiant Smile]
    tansy "Look at that weave... Absolute elemental equilibrium."

    "(Tansy steps forward, untying her own master arch-mage crest from her lapel and pinning it securely onto your chest.)"

    tansy "You're no longer just my apprentice. As of tonight, you are a recognized Master Sorcerer of Mirthhaven."

    # [SPRITE: Ellie & Clara — Clapping, Joyful]
    clara "A magnificent achievement!"
    ellie "I knew you were capable of greatness..."

    "(The whole tavern erupts into deafening applause. Surrounded by your mentor, your loved ones, and the leaders of Mirthhaven, you stand as a true master of the arcane—ready to lead the city into a golden age of magic.)"

    $ story_progress += 1
    $ chapter = 5

    return


label chapter_5_ending_b:

    # (Sound Effect: Resonant brass horn chime, firm stomp of boots)
    mc "My place isn't tucked away in a library or restricted to Sanctum walls. I belong out there—protecting the docks, the markets, the bastion, and every citizen in need!"

    # [SPRITE: Commander Bruni & Barek — Roaring Approval]
    bruni "HA! SPOKEN LIKE A TRUE WARRIOR!"
    barek "The docks will always have an open berth for you, Champion!"

    # [SPRITE: Tariq Vane — Smirking, Nodding]
    tariq "And the shadow markets will always keep an ear open for our favorite protector."

    "(Bruni hands you an iron-embossed Vanguard badge, while Barek gifts you a sea-blessed amulet. You step into your future not as a reclusive scholar, but as Mirthhaven's legendary Champion—a hero beloved across every district.)"

    $ story_progress += 1
    $ chapter = 5

    return


label chapter_5_ending_c:

    # (Sound Effect: VIOLENT ARCANA CRACKLE! UNCONTROLLED EXPLOSION! SHATTERING WOOD AND BEAMS!)
    "(Overconfident in your restored form, you channel all six raw elemental forces into your staff at once without warding! The unstable magic instantly detonates in a blinding shockwave of fire, water, and shattered stone!)"

    # (Sound Effect: Screams of horror, kegs exploding, roof beams collapsing, sizzle of fire)
    "(When the smoke clears, half of The Laughing Anchor's wooden roof has been blasted into the sky. Bao's dark draught kegs have ruptured, soaking the floor in foam, and the grand feast table lies splintered in ruin. The entire cast is covered in soot, dark ale, and burnt fish.)"

    # [SPRITE: Tansy — Furious, Coughing Smoke]
    tansy "YOU ABSOLUTE IDIOT! RECKLESS MULTI-ELEMENTAL OVERCASTING IN A WOODEN BUILDING?!"

    # [SPRITE: Commander Bruni — Veins Bulging, Furious]
    bruni "MY ARMOR IS COATED IN FOAM! ARE YOU TRYING TO KILL US ALL, APPRENTICE?!"

    # [SPRITE: Bao & Barek — Shaking Heads, Disappointed]
    bao "My kegs... my beautiful dark draught..."

    "(Tansy strides over, yanking your sorcerer staff directly out of your hands and snapping it over her knee with a deafening CRACK.)"

    # [SPRITE: Tansy — Stern, Pointing Finger]
    tansy "You have learned NOTHING about responsibility! Your master privileges are REVOKED. You are demoted back to Novice First-Year status!"

    # [SPRITE: Clara Vane — Cold, Hands on Hips]
    clara "And the guild will be garnishing your Sanctum allowance for the next five years to pay for rebuilding The Laughing Anchor."

    "(You stand alone amidst the smoking ruins of the tavern—humiliated, demoted, stripped of your staff, and heavily in debt to every guild leader in Mirthhaven. Your arrogance transformed a night of triumph into a complete catastrophe.)"

    $ story_progress += 1
    $ chapter = 5

    return
