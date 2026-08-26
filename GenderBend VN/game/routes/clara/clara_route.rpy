# Clara Vane Route — The Hearth Beyond the Ledger
# Requires the Clara/Tansy state variables and finish_clara_event backend.

label clara_chapter_1:
    "The Guildmaster's office is usually an oasis of order. Today, mountains of manifests, tax disputes, and Sanctum reagent permits cover Clara's desk."
    clara "If one more spice merchant threatens to throw his shipment into the bay over a two-copper import tax... I might just throw him in after it."
    clara "Ah, little sorcerer. Come in! Please tell me you brought quiet news from the Sanctum."

    menu:
        "Actually, I came to sign off on our reagent permits... and solve this tariff issue for you.":
            $ clara_affection += 20
            "You point out an obscure Sanctum trade exemption clause."
            clara "A tax exemption clause? Gods above... you just saved me three hours of screaming at the docks."
        "Take a breath, Clara. Hand me half those ledgers—let me take some weight off your desk.":
            $ clara_affection += 20
            "You organize several heavy manifests by guild seal."
            clara "Look at you... sensible, quiet, and reliable. You're a blessing, wizard."
        "Mind if I stick around to make sure you don't collapse?":
            $ clara_affection += 15
            mc "Someone needs to look out for Mirthhaven's busiest woman."
            clara "Flattery from a handsome young scholar? Careful... I might start keeping you here on retainer."

    "Clara pours two cups of Earl Grey tea."
    clara "You have a remarkably steady head on your shoulders for a young sorcerer."

    "As you finish the reagent permits, Clara picks up a neatly wrapped lunch parcel."
    clara "Before you head back up the hill... I have a small personal favor to ask."
    clara "Tansy hasn't left her laboratory in days. Would you be a dear and drop this off at her lab?"

    menu:
        "I'd be happy to. Someone needs to make sure our brilliant alchemist stays alive.":
            $ clara_affection += 15
            $ tansy_route_triggered = True
            clara "Thank you, sweet boy. Tell her if she doesn't finish the apples, I'm coming up there to drag her out by her ears myself."
            jump clara_chapter_1_tansy_scene
        "You really can't stop taking care of everyone in Mirthhaven, can you?":
            $ clara_affection += 15
            $ tansy_route_triggered = True
            clara "Thank you, sweet boy. Tell her if she doesn't finish the apples, I'm coming up there to drag her out by her ears myself."
            jump clara_chapter_1_tansy_scene
        "I'm running a bit tight on time today. Tansy will remember to eat eventually.":
            $ clara_affection += 15
            clara "Fair enough. I'll have a guild courier run it up later. Stay and finish your tea with me instead."
            jump clara_chapter_1_clara_only

label clara_chapter_1_tansy_scene:
    "You find Tansy absorbed in a towering glass crucible in the Sanctum's chaotic alchemy laboratory."
    tansy "No, no, no! If the Lotus petal's thermal density drops below four-hundred degrees, the catalyst crystallizes into sludge!"
    "She turns for a measuring scale and nearly trips from her step-stool."

    menu:
        "Catch her arm and hold out the lunch box.":
            mc "Careful, Tansy! I brought a delivery from Guildmaster Clara."
            tansy "W-Wizard! Wait... is that roast chicken?"
        "Set the food box over her open ledger.":
            mc "Step away from the crucible, alchemist. Official guild intervention."
            tansy "Hey! I am seven minutes away from a breakthrough—"
            "Her stomach growls loudly."
            tansy "...Okay, fine. Maybe nine minutes."
        "Relay Clara's threat.":
            mc "Clara threatened to drag you out by your ears if you don't eat."
            tansy "Gods, that woman is scarier than an unstable ether-bomb..."

    "Tansy finally sits down and begins eating."
    tansy "Okay... I admit it. Food was a solid tactical decision."
    tansy "You actually brought me lunch."
    mc "Someone has to keep our lead alchemist alive."
    tansy "Tell Clara her chicken saved my life... and tell yourself that you just earned priority status in my laboratory."

    jump finish_clara_event

label clara_chapter_1_clara_only:
    "You remain in Clara's quiet office, sharing hot tea and conversation until the afternoon shadows lengthen."
    
    jump finish_clara_event


label clara_chapter_2:
    "Late in the quiet Market District, you find Clara alone beside a stack of cargo crates, visibly exhausted."
    clara "Come on, stay locked... If this silk cargo sits in the sea damp overnight, the entire harbor shipment is ruined..."

    menu:
        "Step in and lock the heavy cargo strap into place.":
            $ clara_affection += 15
            clara "You... you always show up right when my strength gives out, don't you?"
        "Working past midnight again, Clara?":
            $ clara_affection += 15
            mc "Normal people go home when the sun sets."
            clara "Normal people don't have forty merchant vessels docking at dawn, little wizard."
        "Take the ledger from her and order her to rest.":
            $ clara_affection += 20
            mc "I'm relieving you of duty for the night, Clara."
            clara "Careful... taking authority over the Guildmaster is a serious offense."

    "Her knee buckles slightly from exhaustion."
    mc "Clara. Stop."
    "You guide her onto a bench beneath a warm market lantern."

    menu:
        "Drape your warm cloak over her shoulders.":
            $ clara_affection += 15
            clara "Thank you. I didn't realize how cold I was."
        "Warm her cold hands with gentle kinetic magic.":
            $ clara_affection += 20
            clara "Your hands are so warm... That magic feels divine, wizard."
        "Offer her warm spiced mulled wine.":
            $ clara_affection += 15
            clara "Spiced pear wine... You really thought of everything, didn't you?"

    clara "My whole life... I've been the one holding the umbrella over everyone else's head."
    clara "Almost no one has ever stopped to ask if I needed someone to hold the umbrella for me."

    menu:
        "Then let me hold it, Clara. You don't ever have to stand in the storm alone again.":
            $ clara_affection += 20
            clara "I... I think I've waited my whole life to hear someone say that to me."
        "Right now, my only concern is Clara.":
            $ clara_affection += 20
            mc "You're a human being before you're a Guildmaster. Let me look out for you."
            clara "I'm... so glad you came into my life."
        "It's about time someone took care of you.":
            $ clara_affection += 15
            mc "It's my official duty as your favorite scholar."
            clara "Favorite scholar, hmm? You're playing a dangerous game, little sorcerer..."

    jump finish_clara_event


label clara_chapter_3:
    "At The Laughing Anchor, Clara sits in a private upper booth overlooking the illuminated harbor."
    clara "Three hours of listening to the Town Council argue about salt tariffs. Sometimes I wonder why I bother."
    clara "Sit down before my mind completely numbs itself."

    menu:
        "Sounds brutal. Let's leave the council outside.":
            $ clara_affection += 20
            clara "Always so composed. You have no idea how refreshing that is."
        "Luckily, I'm here to steal you away for the night.":
            $ clara_affection += 15
            clara "Steal me away, hmm? Careful... people might talk."
        "Name the council members. I'll teach them a lesson with Sanctum magic!":
            $ clara_kid_warning = True
            clara "Easy there, tiger. You sound just like Tariq when someone steals his dice."

    clara "I need to be honest with you about something."
    clara "You are young, brilliant, with your whole life ahead of you. And me? I'm over thirty."
    clara "When I'm around you, my heart races... but am I being selfish?"

    menu:
        "I don't need a caretaker, Clara. I need you.":
            $ clara_affection += 25
            clara "You make me feel like I can finally stop overthinking."
            jump clara_chapter_3_romance_continue
        "If you're making a fool of yourself, then so am I. Just be yourself.":
            $ clara_affection += 20
            clara "You make me feel like I can finally stop overthinking."
            jump clara_chapter_3_romance_continue
        "Why do you keep bringing up my age? I'm not a kid!":
            $ clara_romance_locked = True
            "The romantic tension dies immediately."
            clara "Oh, sweet boy... that defensive pout is exactly what Tariq does when he wants to prove he's grown up."
            jump clara_chapter_3_family

label clara_chapter_3_romance_continue:
    "Clara steps onto the secluded balcony and rests her hands gently against your chest."
    clara "No one has looked at me the way you do. Not as Guildmaster Vane. Not as Tariq's big sister. Just... Clara."
    clara "If you'll have me... age, ledgers, and all... I'm yours, sorcerer."
    if clara_affection >= 100 and not clara_kid_warning:
        "You pull Clara close and share a passionate kiss beneath the starlight."
    else:
        "You hold her hand against your heart. Clara kisses your cheek and rests her head against your shoulder."
    jump finish_clara_event

label clara_chapter_3_family:
    "Clara wraps a motherly arm around your shoulders in an affectionate side-hug."
    clara "You're a good kid, sorcerer. You and Tariq really are the little brothers I never knew I needed."
    jump finish_clara_event


label clara_chapter_4:
    "At midnight, Clara stands at the edge of the quiet harbor beneath silver moonlight."
    clara "Before you came into my life, I believed my youth was behind me."
    clara "I convinced myself that love was meant for other people. But then... you looked at me as Clara."

    if clara_romance_locked:
        jump clara_chapter_4_family_path

    menu:
        "You were never old, Clara. You just forgot how to shine.":
            $ clara_affection += 20
            clara "You always know exactly how to make my heart feel young again."
        "I see a vibrant, stunning woman who steals my breath every day.":
            $ clara_affection += 15
            clara "Flatterer. But gods help me... I love hearing you say it."
        "You've got as much energy as Tariq when he wins a dice match!":
            $ clara_romance_locked = True
            clara "You really are two of a kind, aren't you?"
            jump clara_chapter_4_family_path

    "You walk together through the sleeping Market District."
    clara "You've ruined my terrible work ethic. I spent twenty minutes in council daydreaming about taking long walks with you."

    menu:
        "Walk with me through everything that comes next.":
            $ clara_affection += 25
            clara "I'm done fighting it. I just want you."
            jump clara_final_ending_check
        "I'll always be waiting at the end of your day.":
            $ clara_affection += 20
            clara "I'm done fighting it. I just want you."
            jump clara_final_ending_check
        "If Tariq heard that, he'd tease you for being a sappy big sister!":
            $ clara_romance_locked = True
            clara "Which is why you're going to keep your mouth shut about it, little brother."
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
    "Back in her private office, Clara presses an ornate Guildmaster key into your palm."
    clara "This is the master key to my private residence... and to my heart."
    clara "You made me feel wild, beautiful, and desperately in love."
    clara "I don't care how busy my days get—my nights will always belong to you."
    "Clara pulls you into a deep kiss beneath the warm glow of the Guildhall hearth."
    
    jump finish_clara_event

label clara_ending_good:
    $ clara_ending = "anchored_in_devotion"
    "Clara rests her head against your shoulder beside the warm Guildhall hearth."
    clara "When I'm in your arms, time doesn't mean a thing. You are my anchor, wizard."
    "She presses a tender kiss to your lips."
    jump finish_clara_event

label clara_chapter_4_family_path:
    $ clara_romance_locked = True
    $ clara_ending = "guildmasters_family"
    "Clara opens a polished box containing a silver Merchant Guild signet ring and hands it to you."
    clara "You're family now, sorcerer. Official Guild family."
    clara "If anyone in Mirthhaven ever gives you trouble, you come tell your big sister."
    "Though romantic love was not found, you earn an unshakeable place in Clara and Tariq's family."
    jump finish_clara_event
