# ============================================================
# ELIANNA "ELLIE" SYLVANE ROUTE
# "Petals in the Solarium"
# ============================================================
# Requires:
#   elianna_route_unlocked
#   elianna_route_progress
#   elianna_affection
#   elianna_bad_mood
#   elianna_romance_locked
#   elianna_route_locked
#   elianna_ending
#   finish_elianna_event
# ============================================================

label elianna_chapter_1:

    "After a rough training session leaves your arms singed and bruised, you visit the Sunlit Wards of the Solarium Sanctum."

    "A frantic blur of white robes and golden hair chases a rolling vial across the floor."

    elianna "Eek—! Wait, wait, come back! Ah, nononono, don't roll under the cabinet!"

    "Ellie trips over her robes. A stack of clean bandages flies from her arms."

    "With a quick kinetic spell, you freeze the falling supplies in mid-air and guide them safely into your hands."

    mc "Got them. Easy there, Nurse Ellie."

    elianna "Wh-Whah—?! Oh! The bandages! They didn't hit the floor!"

    "As she takes the supplies, her eyes immediately notice the burns on your forearm."

    elianna "Ah, wait! Look at you! Was that Tansy's practical casting drill again?!"

    mc "Yeah. A stray flame-burst caught me off guard."

    elianna "Sit down, please! Right here on the cot!"

    "Despite her earlier clumsiness, Ellie's touch is remarkably gentle as she applies cooling salve."

    "You flinch slightly."

    elianna "Ah! S-Sorry! Did that hurt?! I'm so bad at this..."

    "Her eyes fill with genuine tears."

    elianna "Whenever I see someone in pain, my heart hurts just as much as their injury."

    elianna "That's why I became a nurse, even if my hands are clumsy and I trip over air..."

    menu:
        "You're not bad at this at all, Ellie. Your heart is what makes you a great healer.":
            $ elianna_affection += 30

            mc "Anyone can apply salve, Ellie, but not everyone actually cares about the person hurting."

            elianna "Y-You really think so...?"

            "Her movements become calmer and steadier as she finishes wrapping your arm."

            elianna "Thank you, sorcerer. You have no idea how much those words mean to me."


        "It stings a bit, but I can handle it. Just focus on wrapping it up.":
            $ elianna_affection += 15

            elianna "O-Oh! Right! Sorry, I'll stop rambling and focus!"

            "She carefully finishes the bandage and gives you extra ointment."

            elianna "Please try to avoid Tansy's fire drills for the rest of the week!"


        "Maybe you should let someone else handle volatile potions if you're going to trip every time.":
            $ elianna_bad_mood += 1

            "The bright emotional light in Ellie's eyes dims."

            elianna "I... I see. You're right, of course."

            elianna "I'm just a liability in here..."

            elianna "You're all patched up now. I'll try not to bother you next time."

    jump finish_elianna_event


label elianna_chapter_2:

    "Late at night, you enter the Solarium Sanctum's glass conservatory."

    "Under the moonlight, Ellie tends a bed of rare silver flowers."

    elianna "...Another decade gone... and the flowers bloom just the same."

    mc "Ellie? What are you doing out here so late?"

    elianna "Ah! Sorcerer! I couldn't sleep. The Night-Blooming Lilies need very delicate care."

    "You sit beside her on a cool marble bench."

    elianna "Did you know I've been the head nurse here for over two hundred years?"

    elianna "I watch bright young students walk through these halls... fix their scrapes, listen to their dreams, watch them become great sorcerers..."

    elianna "...And then they age, leave, and eventually pass away. While I just stay."

    elianna "Because I live so long, I usually keep my distance to save my heart."

    elianna "It hurts too much to get close when everyone leaves eventually."

    menu:
        "You don't have to carry that solitude alone anymore, Ellie. I'm right here with you.":
            $ elianna_affection += 30

            "Ellie's breath catches."

            elianna "You... you really mean that?"

            "She rests her head softly against your shoulder and closes her hand over yours."

            elianna "When you're around... the solitude doesn't feel so heavy anymore."


        "Living a long time must be tough, but at least you get to help so many generations.":
            $ elianna_affection += 15

            elianna "Fufu... That's a very practical way to look at it, sorcerer."

            elianna "Every potion I brew and every bandage I wrap is a small mark left on the world, isn't it?"

            elianna "Thank you for listening."


        "If getting attached hurts so much, maybe keeping your distance really is for the best.":
            $ elianna_bad_mood += 1

            "The soft light in Ellie's eyes extinguishes."

            elianna "...Right. Of course. Distance is safer..."

            elianna "It's late. You should get back to your dorms."

    jump finish_elianna_event


label elianna_chapter_3:

    "At the Crestward Bastion field clinic, Ellie rushes between wounded knights after a heavy training exercise."

    elianna "Hold still, Sir Knight! I need three more vials of Burn-Salve right now!"

    "A massive wooden support beam suddenly cracks overhead."

    "It falls directly toward Ellie."

    mc "AEGIS AETHERIS!"

    "Your radiant barrier catches the beam, splintering it harmlessly against the shield."

    elianna "A-AHHH! Sorcerer?!"

    "Ellie rushes toward you, frantically checking your hands, face, and shoulders."

    elianna "Are you hurt?! Is your head bleeding?! Speak to me, please!"

    mc "Ellie, calm down! I'm completely fine!"

    "Her knees weaken and she collapses against your chest."

    elianna "Thank goodness... oh, thank the gods..."

    elianna "I spend my whole life hurting for everyone else... but if anything ever happened to you, I don't think I could ever heal from that!"

    menu:
        "Wrap your arms around her. \"I'll always protect you, Ellie.\"":
            $ elianna_affection += 35

            "You hold her tightly until her trembling stops."

            elianna "S-Sorcerer..."

            elianna "I'm supposed to be the one taking care of you... but having you hold me like this makes me feel so safe."

            elianna "I never want to let go..."


        "Gently reassure her that you know how to take care of yourself.":
            $ elianna_affection += 15

            mc "I'm a sorcerer, Ellie. I know how to take care of myself in a fight."

            elianna "I know... you're very brave and skilled."

            elianna "Just please don't take risks like that without thinking. My heart can't take it!"


        "You need to pull it together, Nurse. The wounded knights still need you.":
            $ elianna_bad_mood += 1

            "Ellie immediately steps away, deeply embarrassed."

            elianna "Ah—! Y-Yes! Of course! Forgive me!"

            elianna "I'm being completely unprofessional. I'll return to my duties at once."

    # Repeatedly rejecting Ellie's vulnerability locks the romantic ending.
    if elianna_bad_mood >= 2:
        $ elianna_romance_locked = True

    jump finish_elianna_event


label elianna_chapter_4:

    "At dusk, Ellie waits for you on the balcony outside the Sunlit Wards."

    "A hand-woven crown of glowing medicinal flowers rests on her golden hair."

    elianna "Ah! You came!"

    "She turns too quickly and the crown slips lopsided over one pointed ear."

    elianna "Eek—! Oh no, not again!"

    "You step close and gently straighten it."

    mc "Hold still, Ellie. There... perfectly centered."

    elianna "Ehehe... thank you."

    "Ellie takes both of your hands."

    elianna "I used to think my long life was a curse of solitude... meant for watching people come and go while I tripped through the centuries alone."

    elianna "But you looked past my awkwardness. You shared my pain, protected me, and gave me a reason to look forward to every single day."

    "She presses a rare, glowing Moon-Lily into your palm."

    elianna "This flower blooms forever... just like what I feel for you."

    elianna "I don't care how many years I have left—I want to spend every single moment of my life by your side."

    # If too many earlier bad choices were made, the full romance option is unavailable.
    if elianna_romance_locked:

        menu:
            "I cherish you deeply, Ellie. I promise to always stay by your side.":
                $ elianna_ending = "guiding_light"
                jump elianna_ending_companion

            "Ellie... I care about you, but I don't think I can promise you forever.":
                $ elianna_ending = "bittersweet_petals"
                jump elianna_ending_bittersweet

    else:

        menu:
            "I love you too, Ellie. Let's spend eternity together.":
                $ elianna_affection += 30
                $ elianna_ending = "everlasting_solace"
                jump elianna_ending_true

            "I cherish you deeply, Ellie. I promise to always stay by your side.":
                $ elianna_affection += 15
                $ elianna_ending = "guiding_light"
                jump elianna_ending_companion

            "Ellie... I care about you, but I don't think I can promise you forever.":
                $ elianna_ending = "bittersweet_petals"
                jump elianna_ending_bittersweet


label elianna_ending_true:

    mc "I love you too, Ellie. Let's spend eternity together."

    "You pull her gently into a loving kiss beneath the golden twilight."

    "The flowers around you glow brighter as Ellie wraps her arms around your neck."

    elianna "My brave sorcerer... my heart, my soul, my entire life... they're all yours. Forever and ever."

    "No longer a lonely ghost passing through time, Ellie has found a home in your arms."

    jump finish_elianna_event


label elianna_ending_companion:

    mc "I cherish you deeply, Ellie. I promise to always stay by your side."

    "You hold her hands tightly before pulling her into a warm embrace."

    elianna "That's all I could ever ask for..."

    elianna "As long as I can hold your hand and walk through these centuries with you by my side, I'll never be afraid of the future again."

    jump finish_elianna_event


label elianna_ending_bittersweet:

    mc "Ellie... I care about you, but I don't think I can promise you forever."

    "Ellie's glowing smile freezes. A tear slips down her cheek as she clutches the Moon-Lily."

    elianna "Oh... I see..."

    elianna "It's okay. Thank you for being honest with me."

    elianna "I'll always keep this flower to remember the warmth you brought into my quiet life."

    jump finish_elianna_event
