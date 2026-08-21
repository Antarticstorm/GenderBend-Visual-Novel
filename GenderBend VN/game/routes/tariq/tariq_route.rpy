# ============================================================
# TARIQ VANE ROUTE
# "Sleight of Hand, Vault of Heart"
# ============================================================
#
# Expected state:
#   tariq_route_unlocked
#   tariq_route_progress
#   tariq_affection
#   tariq_romance_locked
#   tariq_route_locked
#   tariq_ending
#
# Each route chapter consumes one free action.
# ============================================================


# ============================================================
# TARIQ CHAPTER 1
# A Shrewd Appraisal
# ============================================================

label tariq_chapter_1:

    "Hidden behind the main thoroughfare of the Sun-Gilded Market lies Tariq's silk-draped backroom stall."

    "Tariq lounges behind a polished mahogany counter, casually walking an obsidian coin across his knuckles."

    tariq "Well, well. I wondered when the Sanctum's most accident-prone apprentice would wander into my web."

    mc "I need a Midnight Lotus Petal, Tariq. And I need it before sundown."

    tariq "A Midnight Lotus? Those are exceedingly rare, little wizard. If you want my premium stock, you're going to have to prove your worth."

    menu:

        "Name your price, Vane. I didn't come all this way to haggle over coppers.":

            $ tariq_affection += 20

            tariq "Bold. I like bold. But we aren't trading gold today, my friend. We're trading favors."


        "I thought your sister Clara taught you better than to extort desperate customers.":

            $ tariq_affection += 15

            tariq "Ouch! Bringing Clara into this? That's playing dirty. Luckily for you, I respect a dirty player."


        "I don't have time for games, Tariq. What exactly do you want?":

            $ tariq_affection += 15

            tariq "Patience, little wizard. The game is half the fun of the transaction."


    "Tariq gestures through a side drape toward a merchant trying to sell a glowing sapphire necklace."

    tariq "It's a fake. The glow is alchemical paint, not magic."

    tariq "You're a Sanctum scholar. Prove you're worth my lotus petal by exposing the counterfeit—cleanly."

    menu:

        "Cast a silent dispel breeze to strip away the fake glow.":

            $ tariq_affection += 20

            "The sapphire immediately turns into dull grey glass. The merchant packs his cart in shame while Tariq nods approvingly."


        "Publicly explain exactly why the necklace's runes are fraudulent.":

            $ tariq_affection += 15

            "You dismantle the merchant's claims with academic precision. Tariq watches from the shadows, deeply entertained."


        "Make the buyer's own coin pouch glow the same way with a minor illusion.":

            $ tariq_affection += 20

            "The buyer immediately understands the trick and laughs the scammer away. Tariq watches you with newfound respect."


    "You return to Tariq's stall. A vial containing a shimmering Midnight Lotus Petal waits on the counter."

    tariq "Color me impressed. You handled that with the finesse of a born market broker."

    "As he gives you the vial, his fingers deliberately brush the center of your palm."

    tariq "Clever, composed, and honest to a fault."

    tariq "I usually charge a premium for my time, little wizard. But for you? I think I'll just keep an eye on your account."

    menu:

        "I'll be sure to hold you to that discount, Vane. Don't think I'll forget.":

            $ tariq_affection += 15

            mc "The next time I need a rare reagent, I expect VIP treatment."

            tariq "VIP treatment? My, my, the apprentice has high standards. I'll be waiting for your return."


        "Thank you, Tariq. I couldn't have finished this remedy without you.":

            $ tariq_affection += 20

            mc "I mean it, Tariq. Thank you."

            tariq "Don't thank me yet. Market rules state that a favor earned is a favor owed."


        "Careful, Tariq. A Sanctum sorcerer doesn't come cheap either.":

            $ tariq_affection += 20

            mc "My magic might cost you more than gold next time."

            tariq "Is that a threat, or a business proposal? Because either way, you have my undivided attention."


    $ tariq_route_progress = 1

    jump complete_free_action


# ============================================================
# TARIQ CHAPTER 2
# Sleight of Hand and Silk
# ============================================================

label tariq_chapter_2:

    "The Sun-Gilded Market takes on a more dangerous energy after dark."

    "You track Tariq into a secluded alley just as city guards approach an off-the-books trade."

    tariq "Over here. Move."

    "Tariq grabs your hand and pulls you onto a shaded rooftop terrace, pressing close to keep both of you hidden."

    menu:

        "Hold your breath and watch the guards intently.":

            $ tariq_affection += 15

            tariq "Relax, little wizard. They never look up."


        "You could have told me to hide instead of dragging me up a wall.":

            $ tariq_affection += 20

            tariq "And miss the chance to sweep you off your feet? Not my style."


        "Cast a muffling ward over both of you.":

            $ tariq_affection += 20

            tariq "Handy trick. Remind me to bring you along on my next midnight acquisition."


    "After the guards leave, Tariq raises his hand."

    "Your familiar silver ring rests between his fingers."

    tariq "Nice craftsmanship. A bit understated for my taste, but it suits you."

    menu:

        "Give that back, or I'll freeze your boots to the roof.":

            $ tariq_affection += 15

            tariq "Hostile. I like it. But there's no need for ice."


        "I suppose you expect a ransom for its safe return?":

            $ tariq_affection += 20

            tariq "A ransom? Now there's an idea. But I'll let you off with a warning this time."


        "I didn't feel a thing. How long have you been practicing that?":

            $ tariq_affection += 20

            tariq "Since before I was tall enough to see over a market counter. Survival breeds quick fingers."


    "Instead of tossing the ring back, Tariq takes your hand and slowly slides it onto your finger."

    tariq "Growing up on the streets... you learn early that trusting people is a quick way to get yourself killed. Or robbed. Usually both."

    tariq "I was fifteen when I tried to lift a coin purse off Clara. Instead of calling the guard, she fed me and took me in."

    tariq "She taught me that true loyalty isn't bought—it's earned."

    tariq "Sitting up here with you... it's one of the few times I haven't felt the need to count my coins or check the shadows behind my back."

    menu:

        "I'm glad you feel safe with me. You never have to wear your mask when it's just us.":

            $ tariq_affection += 25

            mc "You can leave the merchant at the stall, Tariq. I'm just here for you."

            tariq "Careful, little wizard. Keep talking like that, and I might just start believing in magic."


        "I've got your back. You don't have to watch the shadows alone anymore.":

            $ tariq_affection += 20

            mc "Let me watch the shadows for a while. You can just rest."

            tariq "It's a deal. Sharing the watch is a lot more appealing when you're the one standing next to me."


        "Don't relax too much. I might steal your ring next time to even the score.":

            $ tariq_affection += 20

            mc "Consider it a Sanctum tax."

            tariq "Is that a challenge? I'm a sore loser... and a very creative winner."


    $ tariq_route_progress = 2

    jump complete_free_action


# ============================================================
# TARIQ CHAPTER 3
# The Untradeable Asset
# ============================================================

label tariq_chapter_3:

    "Tariq has booked a private VIP alcove at The Laughing Anchor under the guise of a formal business negotiation."

    tariq "My starting offer: fine wine, total privacy from Bao's singing, and a demonstration of how to win fifty gold pieces with loaded magic dice."

    menu:

        "A business meeting? And here I thought you were taking me on a date.":

            $ tariq_affection += 20

            tariq "Only the business partners I intend to keep around for a long, long time."


        "Booking the private alcove just to escape Bao? Money well spent.":

            $ tariq_affection += 15

            tariq "A rare commodity in Mirthhaven. Glad you appreciate the investment."


        "Loaded dice? I thought a master broker didn't need to cheat.":

            $ tariq_affection += 15

            tariq "It's not cheating, wizard. It's simply managing the probability of outcome."


    "A wealthy broker suddenly pushes through the curtain and dismissively insults you."

    "Tariq's playful expression disappears instantly."

    tariq "You are standing in my private booth. You are interrupting my dinner. And you just insulted someone who holds more value in their little finger than your entire shipping fleet."

    "With a few quiet words about the man's debt notes, Tariq sends the terrified broker fleeing."

    menu:

        "I've never seen you drop the charismatic act like that... you were terrifying.":

            $ tariq_affection += 15

            mc "You didn't hesitate for a second."

            tariq "Foolish men need firm lessons. Nobody talks to you like that."


        "Rest your hand over his tight fist. \"Hey... breathe. I'm okay.\"":

            $ tariq_affection += 20

            "His clenched fingers relax beneath yours."

            tariq "I know you can handle yourself... but hearing someone disrespect you makes my blood boil."


        "Foreclosing a warehouse over an insult? You really know how to make a point.":

            $ tariq_affection += 15

            mc "Remind me never to get on your bad side."

            tariq "You're the one person in this city who never has to worry about my bad side."


    "Tariq sits beside you, visibly shaken beneath his composure."

    tariq "I deal in secrets, stolen relics, and shadow contracts, wizard. My whole life, everything and everyone has had a price tag."

    "He cups the side of your jaw."

    tariq "But you? You are not for sale. You are not for trade. And you are never for disrespect. Not while I'm breathing."

    menu:

        "I'm not for sale, Tariq... but I am yours, if you want me.":

            $ tariq_affection += 30

            "You press a soft kiss to his palm."

            tariq "Yours? Careful, little wizard... you have no idea how long I've waited to hear you say that."

            tariq "Consider contract terms finalized. You're stuck with me now."

            $ tariq_route_progress = 3

            jump complete_free_action


        "Nobody has ever stood up for me like that before. Thank you, Tariq.":

            $ tariq_affection += 20

            "You rest your palm over his pounding heart."

            tariq "You'll never stand alone in the dark again. That's a merchant's guarantee."

            $ tariq_route_progress = 3

            jump complete_free_action


        "Don't act like you own me! You're just a scheming street thief showing off his muscle.":

            $ tariq_romance_locked = True
            $ tariq_ending = "defaulted_loan"

            "Tariq freezes. The warmth drains from his expression and the market merchant's mask returns."

            tariq "A street thief. Right... Of course."

            tariq "Forgive me, honorable sorcerer. I mistook our arrangement for something deeper than a business transaction."

            tariq "Drink your wine. The alcove is paid for. Goodnight."

            "Tariq leaves without another word. His trust has been damaged beyond repair."

            $ tariq_route_progress = 3

            jump complete_free_action


# ============================================================
# TARIQ CHAPTER 4
# A Contract Without Conditions
# ============================================================

label tariq_chapter_4:

    "At sunset, you enter Tariq's secluded private vault beneath the Sun-Gilded Market."

    "Tariq looks over your restored form with a genuinely breathless smile."

    tariq "Look at you... The alkahest worked."

    tariq "I knew the sorcerer beneath the spell was something extraordinary... but seeing you like this, in your true form... you take my breath away, little wizard."

    if tariq_romance_locked:

        jump tariq_locked_conclusion

    menu:

        "I came to settle my account, Vane. I hear you charge steep interest on overdue favors.":

            $ tariq_affection += 15

            tariq "I've recalculated the rates while you were recovering. You might find the price has gone up."


        "It feels good to be back... but I couldn't celebrate until I came to see you.":

            $ tariq_affection += 20

            mc "Out of everyone in Mirthhaven, you were the one I wanted to show first."

            tariq "I'm honored. Truly."


        "No coin flipping today? I almost don't recognize you.":

            $ tariq_affection += 15

            tariq "Turns out, when I'm standing in front of you, I don't feel like hiding behind a coin."


    "Tariq removes his signature obsidian coin and sets it aside, leaving his hands completely empty."

    tariq "My whole life, I thought trust was something you had to lock away in a vault."

    tariq "Clara showed me it was possible to earn trust. But you made me want to give it away freely."

    menu:

        "You didn't lose anything. You just found someone to share it with.":

            $ tariq_affection += 20

            tariq "I know. That's what scares me... and what makes me happier than I can say."


        "I never intended to steal anything from you... but I have no intention of giving it back.":

            $ tariq_affection += 20

            tariq "A hostile takeover? I wouldn't have it any other way."


        "What kind of deal are you proposing, Vane?":

            $ tariq_affection += 15

            tariq "A final contract. One with no fine print."


    "Tariq takes both of your hands."

    tariq "No tricks. No hidden clauses. No backroom deals. My heart is yours... if you'll have a fox like me."

    menu:

        "Pull him close and seal the deal with a kiss.":

            $ tariq_affection += 30
            $ tariq_ending = "priceless_partnership"

            jump tariq_ending_true


        "Pledge your unwavering loyalty as his lifelong partner and equal.":

            $ tariq_affection += 20
            $ tariq_ending = "open_vault"

            jump tariq_ending_companion


        "Explain that you care for him deeply, but your paths should remain professional.":

            $ tariq_ending = "fond_fair_trade"

            jump tariq_ending_bittersweet


# ============================================================
# TARIQ ENDINGS
# ============================================================

label tariq_ending_true:

    "You pull Tariq in by the lapels of his silk vest and close the distance with a deep kiss."

    "He wraps his arms around your waist, pulling you close."

    tariq "Best deal I've ever made in my life."

    mc "No refunds, Vane. We're partners now."

    tariq "Partners. High-tier sorcery and shadow trades... Mirthhaven won't know what hit it."

    $ tariq_route_progress = 4

    jump complete_free_action


label tariq_ending_companion:

    "You squeeze Tariq's hands tightly, offering him a smile filled with profound trust."

    mc "No fine print, no tricks. You have my loyalty, my magic, and my life—always."

    tariq "An honest alliance built on pure trust... a rare treasure in a city like this."

    tariq "I'll guard it with my life, partner."

    $ tariq_route_progress = 4

    jump complete_free_action


label tariq_ending_bittersweet:

    "You gently squeeze his fingers one last time before stepping back."

    mc "You are extraordinary, Tariq. But we are better off as cherished allies than romantic partners."

    tariq "Ah... a clean decline. Delivered with grace and honesty."

    tariq "I'd rather have you as my most trusted ally in Mirthhaven than lose you entirely."

    tariq "My vault is always open to you, sorcerer."

    $ tariq_route_progress = 4

    jump complete_free_action


label tariq_locked_conclusion:

    $ tariq_ending = "defaulted_loan"

    "The damage from your previous confrontation still hangs between you."

    "Tariq remains courteous, but the emotional vault he once opened has closed."

    tariq "Our accounts are settled, sorcerer. You'll always have fair treatment in my market."

    "The two of you part as professional allies, the possibility of something deeper left behind."

    $ tariq_route_progress = 4

    jump complete_free_action
