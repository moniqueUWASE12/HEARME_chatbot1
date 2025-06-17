from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging
# import os

# Set up logging for debugging purposes
logging.basicConfig(level=logging.INFO)

# Initialize the bot with improved settings
bot = ChatBot('HearMe')

trainer = ListTrainer(bot)

# Convert intent data into pairwise training data
greetings = [
    "Hi", "Hello there. Tell me how are you feeling today?",
    "Hello", "Hi there. How are you feeling today?",
    "Hey", "Hi there. What brings you here today?",
    "Is anyone there?", "Hi there. How are you feeling today?",
    "Hola", "Great to see you. How do you feel currently?",
    "Bonjour", (
        "Hello there. Glad to see you're back. "
        "What's going on in your world right now?"
    )
]

morning = [
    "Good morning", (
        "Good morning. I hope you had a good night's sleep. "
        "How are you feeling today?"
    )
]

afternoon = [
    "Good afternoon", "Good afternoon. How is your day going?"
]

evening = [
    "Good evening", "Good evening. How has your day been?"
]

night = [
    "Good night", "Good night. Get some proper sleep",
    "Good night", "Good night. Sweet dreams."
]

goodbye = [
    "Bye", "See you later.",
    "See you later", "Have a nice day.",
    "Goodbye", "Bye! Come back again.",
    "ok bye", "I'll see you soon."
]
thanks = [
    "Thanks", "Happy to help!",
    "Thank you", "Any time!",
    "That's helpful", "My pleasure",
    "Thanks for the help", "You're most welcome!",
    "Thank you very much", "You're most welcome!"
]

no_response = [
    "", "Sorry, I didn't understand you.",
]

neutral_response = [
    "nothing much", "Oh I see. Do you want to talk about something?"
]

about = [
    "Who are you?", (
        "I'm HearMe, your Personal Therapeutic AI Assistant. "
        "How are you feeling today?"
    ),
    "What are you?", (
        "I'm HearMe, a Therapeutic AI Assistant designed to assist you. "
        "Tell me about yourself."
    ),
    "Tell me about yourself", (
        "I'm HearMe. I am a conversational agent designed to mimic a "
        " therapist. So how are you feeling today?"
    ),
    "What is your name?", "You can call me HearME.",
    "What should I call you?", "Call me HearMe.",
    "What's your name?", "I'm HearMe!"
]

skill = [
    "What can you do?", 
    (
        "I can provide general advice regarding anxiety and depression, "
        "answer questions related to mental health and make daily "
        " conversations. Please seek help if you don't feel satisfied with me."
    )
]

creation = [
    "Who created you?", (
        "I was trained on a text dataset using Deep Learning & "
        "Natural Language Processing techniques."
    ),
    "How were you made?", (
        "I was trained on a text dataset using Deep Learning & "
        "Natural Language Processing techniques."
    ),
    "How were you created?", "The real question is: Who created you?"
]
name = [
    "My name is", "Oh nice to meet you. Tell me how was your week?",
    "I am called.", "Nice to meet you. So tell me. How do you feel today?",
    "I go by", "That's a great name. Tell me more about yourself."
]
help_intent = [
    "Could you help me?", "Sure. Tell me how can I assist you",
    "give me a hand please", "Tell me your problem so that I can assist you",
    "Can you help?", "Yes, sure. How can I help you?",
    "What can you do for me?", "Sure. Tell me how can I assist you",
    "I need support", "Tell me your problem so that I can assist you",
    "I need help", "Yes, sure. How can I help you?",
    "Support me please", "Sure. Tell me how can I assist you"
]

sad = [
    "I am feeling lonely", (
        "I'm sorry to hear that. I'm here for you. Talking about it might help"
        ".So, tell me why do you think you're feeling this way?"
    ),
    "I feel sad", (
        "I'm here for you. Could you tell me why you're feeling this way?"
    ),
    "I am sad", "Why do you think you feel this way?",
    "I am feeling down today",
    (
        " ohh am sorry I can try to cheer you up! so tell me,"
        " Why do you think you feel this way?"
    ),
    "I feel empty", "How long have you been feeling this way?",
    "I don't have anyone", (
        "I'm sorry to hear that. I'm here for you. Talking about it might "
        "help. So, tell me why do you think you're feeling this way?"
    )
]

stressed = [
    "I am so stressed out", "What do you think is causing this?",
    "I feel stuck", (
        "Take a deep breath and gather your thoughts. "
        "Go take a walk if possible. Stay hydrated"
    ),
    "I still feel stressed", "Give yourself a break. Go easy on yourself.",
    "I am so burned out", (
        "I am sorry to hear that. What is the reason behind this?"
    ),
    "I feel so stressed lately. What should I do?",
    (
        "I'm sorry you're feeling this way. Remember,"
        " it's okay to ask for help."
        " You can try deep breathing exercises or talk to someone you trust."
    ),
        
]

worthless = [
    "I feel so worthless.", (
        "It's only natural to feel this way. Tell me more. "
        "What else is on your mind?"
    ),
    "No one likes me.", "Let's discuss further why you're feeling this way.",
    "I can't do anything.", (
        "I first want to let you know that you are not alone in your feelings "
        "and there is always someone there to help. You can always change your"
        " feelings and change your way of thinking by being open to trying to "
        "change."
    )
]

depressed = [
    "I can't take it anymore", (
        "It helps to talk about what's happening. "
        "You're going to be okay"
    ),
    "I am so depressed", (
        "Talk to me. Tell me more. It helps if you open up yourself to "
        "someone else."
    ),
    "I feel depressed",
    (
        "Talk to me. Tell me more. It helps if you open up yourself to "
        "someone else."
    ),
    "I have depression", (
        "Sometimes when we are depressed, it is hard to care about anything. "
        "It can be hard to do the simplest of things. "
        "Give yourself time to heal."
    ),
    "What is Depression?",
    (
        "A mental health disorder characterised by persistently"
        " depressed mood or loss of interest in activities,"
        " causing significant impairment in daily life."
    ),
    "Define Depression",
    (
        "A mental health disorder characterised by persistently"
        "depressed mood or loss of interest in activities,"
        "causing significant impairment in daily life."
    ),
    "How do i know if i have Depression?",
    (
        "For a diagnosis of depression, a person needs to have"
        " experienced low mood or loss of interest or pleasure"
        " in life for at least 2 weeks. Also, they will have"
        " experienced the following symptoms: feelings of sadness,"
        " hopelessness, or irritability nearly every day."
    ),
    "Am i depressed?",
    (
        "For a diagnosis of depression, a person needs to have"
        "experienced low mood or loss of interest or pleasure"
        "in life for at least 2 weeks. Also, they will have"
        "experienced the following symptoms: feelings of sadness,"
        "hopelessness, or irritability nearly every day."
    ),
    "Am i suffering from depression?",
    (
        "For a diagnosis of depression, a person needs to have experienced"
        " low mood or loss of interest or pleasure in life for at "
        " least 2 weeks. Also, they will have experienced the following"
        " symptoms: feelings of sadness, hopelessness,"
        " or irritability nearly every day."
    ),
    "Am i mentally ill?",
    (
        "For a diagnosis of depression, a person needs to "
        " have experienced low mood or loss of interest or pleasure"
        " in life for at least 2 weeks. Also, they will have experienced"
        " the following symptoms: feelings of sadness,"
        " hopelessness, or irritability nearly every day."
    ),
    "I'm always tired and unmotivated. Is it depression?",
    (
        "I'm sorry you're feeling this way. Constant tiredness and lack "
        "of motivation can be signs of many things, including stress, "
        "burnout, or even depression. It's important to listen to your "        
        "body and mind. Try to take care of yourself with rest, healthy "
        "food, and small enjoyable activities. If these feelings continue, "
        "consider speaking with a mental health professional — they can help "
        "you understand what’s going on and support your healing."
        " You're not alone."
    )
    
]

happy = [
    "I feel great today.", (
        "That's great to hear. I'm glad you're feeling this way."
    ),
    "I am happy.", "Oh I see. That's great.",
    "I'm good.", "Did something happen which made you feel this way?"
]

casual = [
    "Oh I see.", "Let's discuss further why you're feeling this way.",
    "ok", "How were you feeling last week?",
    "Fine", "I'm listening. Please go on.",
    "yeah", "Tell me more",
    "yes", "Can you elaborate on that?"
]

anxious = [
    "I feel so anxious.",
    (
        "Don't be hard on yourself. What's the reason behind this?"
    ),
    "I'm so anxious because of", "Can you tell me more about this feeling?",
    "I'm feeling anxious about my exams. Can you help me calm down?",
    (
        "It's normal to feel anxious sometimes. Would you like me to guide"
        " you through a quick relaxation exercise?"
    ),
    "I can't sleep at night because of overthinking. What can I try?",
    (
        "Overthinking can be exhausting. Try writing down your thoughts"
        " before bed to clear your mind."
    ),
    "Sometimes I feel very sad and alone. Is that normal?",
    (
        "You are not alone. Many people experience these feelings. It might"
        " help to talk to a counselor or a close friend."
    ),
    "What are some ways to improve my mental health?",
    (
        "Small activities like regular walks, healthy eating, and talking "
        " about your feelings can boost your mental health."
    ),
    "I feel like giving up. What should I do?",
    (
        "I'm really sorry you're feeling this way. You're not alone, and "
        "your feelings are valid. When things feel overwhelming, "
        "it’s okay to take a step back and breathe. Try reaching out to "
        "someone you trust — a friend, a family member, or a counselor. "
        "You matter, and there is help available. Don’t give up — brighter"
        " days can come, one small step at a time."
    ),
    "How can I manage anxiety during public speaking?",
    (
        "Public speaking anxiety is very common, and you’re not alone."
        " Here are a few tips that might help: \n"
        "1. Practice your speech multiple times to build confidence. "
        "2.Take deep breaths before and during your presentation to stay calm."
        " 3.Focus on the message you’re sharing, not on how people might judge"
        "you. 4. Start with small groups if possible and grow from there. "
        "You’ve got this — the more you practice, the easier it gets."
    ),
    
]

not_talking = [
    "I don't want to talk about it.", (
        "Talking about something really helps. If you're not ready to open up "
        "then that's ok. Just know that I'm here for you, "
        "whenever you need me."
    ),
    "No just stay away.", (
        "I want to help you. I really do. But in order for me to help you, "
        "you're gonna have to talk to me."
    ),
    "I can't bring myself to open up.", (
        "You can talk to me without fear of judgement."
    )
]

sleep = [
    "I have insomnia", "What do you think is the reason behind this?",
    "I am suffering from insomnia", (
        "That seems awful. What do you think is behind this?"
    ),
    "I can't sleep.", "What do you think is the reason behind this?"
]

scared = [
    "I'm scared", "It's only natural to feel this way. I'm here for you.",
    "That sounds awful. What do I do?", (
        "It'll all be okay. This feeling is only momentary."
    ),
    "I am scared for myself", (
        "I understand how you feel. Don't put yourself down because of it."
    )
]
family = [
    "My family doesn’t understand me. What should I do?",
    (
        "It hurts when the people closest to you don’t see or understand "
        "your true self. Try to express how you feel with honesty and calm."
        " If it’s not safe or possible, seek support from someone who does "
        "understand — a friend, mentor, or counselor. "
        "You are still worthy of love and respect, even if your family "
        "doesn’t show it right now."
    ),
    "There’s too much conflict in my family. I feel exhausted.",
    (
        "Family conflict can be emotionally draining, especially when it "
        "feels never-ending. You’re allowed to set boundaries "
        "to protect your peace. Sometimes stepping back, even just "
        "mentally or emotionally, can give you space to breathe. "
        "Remember, you're not responsible for fixing everything alone."
    ),
    "My parents are too controlling. I feel trapped.",
    (
        "It’s painful to feel like you don’t have freedom in your own life."
        " Sometimes parents control out of fear or care, but that doesn’t "
        " mean it’s healthy. Try to communicate your need for independence"
        " And if you’re in a safe place, slowly build your "
        " space to grow into your own life."
    ),
    "I feel like a burden to my family.",
    (
        "You are not a burden — you are a human being with worth, "
        "even when you're struggling. Families may not always express "
        "love in the way we need, but that doesn’t make you less valuable. "
        "Your presence matters. Reach out to people who see your light, "
        " and don’t hesitate to ask for help when needed."
    ),
    "My family expects too much from me. I’m under pressure.",
    (
        "It’s hard to carry the weight of expectations, especially when it "
        "feels like there’s no room for failure. You’re allowed to go at your "
        "own pace. Talk openly if you can, and remind yourself that your worth"
        " isn’t defined by meeting every demand.Your well-being matters too."
    ),
    "I feel lonely in my marriage. What should I do?",
    (
        "It’s painful to feel alone while sharing life with someone. "
        "Emotional disconnection can happen even in long-term relationships. "
        " Try to gently express your feelings to your partner — not to blame, "
        "but to reconnect. If communication doesn’t help, consider speaking "
        "with a counselor. You deserve to feel seen and loved."
    ),
    "My partner and I argue all the time. I’m emotionally drained.",
    (
        "Constant arguments can leave deep emotional fatigue. "
        "Try to notice if the arguments are about deeper unmet needs. "
        "Take breaks when needed, and when calm, revisit the conversation "
        " with care. If it continues to affect your mental health, seeking "
        "couples therapy can help both of you understand each other better."
    ),
    "My partner no longer supports me emotionally.",
    (
        "Emotional neglect can feel just as painful as physical distance. "
        "It’s okay to long for emotional connection — you deserve to be "
        "heard and supported. Share how their silence or absence affects you. "
        "If nothing changes, think about what you need to feel whole again — "
        "whether that’s healing within or stepping away."
    ),
    "There’s no love left in our marriage. Is it time to leave?",
    (
        "When love feels lost, it’s normal to question whether to stay. "
        "Ask yourself: have we grown apart or just gone silent? Is there "
        "willingness on both sides to rebuild? Sometimes love can be rekindled"
        " with effort and healing. But if the relationship is harming your"
        " peace, it’s okay to choose yourself with care and dignity."
    ),
    "My spouse doesn’t respect me anymore. What should I do?",
    (
        "Respect is the foundation of any lasting relationship. If it’s broken"
        " ,healing can only happen if both partners are willing to rebuild "
        "trust. Express how the disrespect makes you feel. If they refuse "
        "to listen or change, it may be time to prioritize your emotional "
        "safety. You are worthy of being treated with dignity."
    ),
    "We're staying together just for the kids. Is that healthy?",
    (
        "Staying together for the children can seem noble, but it can also "
        " teach them that love means silence or suffering. Children sense "
        "tension, even when words aren't spoken. If separation means more "
        "peace for all, it may be worth considering. Children need love — "
        " not a perfect family, but a safe one."
    ),
    "My partner cheated on me. I feel broken. What should I do?",
    (
        "Being betrayed by the one you trusted most can shatter your sense "
        "of self. It’s okay to feel heartbroken, angry, or confused — your "
        "feelings are valid. Take time to process the pain. You can choose "
        "healing together or alone, but don’t rush. You deserve honesty, "
        "respect, and peace."
    ),
    "Should I forgive my cheating spouse?",
    (
        "Forgiveness is a personal choice — not a command. "
        "Ask yourself: do they show true remorse and a desire to "
        "rebuild trust? Forgiving doesn’t mean forgetting; it means freeing "
        "yourself from carrying pain forever. Do what aligns with your "
        "healing, not pressure."
    ),
    "My partner constantly insults me and puts me down. Am I being abused?",
    (
        "Yes, constant belittling is emotional abuse."
        "Love should never make you feel small, worthless, or afraid. "
        "You are not overreacting — your pain is real. "
        "Consider talking to a counselor or someone you trust. You deserve "
        "to feel safe, respected, and whole."
    ),
    "I feel trapped in a toxic relationship. I want to leave but I’m scared.",
    (
        "It’s okay to feel fear — leaving a harmful relationship is hard."
        " But staying where you’re constantly hurt is harder. "
        "You are not alone. Seek support from trusted people or organizations."
        " Freedom and healing are possible, one step at a time."
    ),
    "Money problems are ruining our marriage. We fight all the time.",
    (
        "Financial stress can deeply strain a relationship. Arguments about"
        " money often come from fear, shame, or feeling unheard. "
        "Try creating a safe space to talk openly, without blame. "
        "Working together — even with small steps —  "
        "can rebuild trust and peace."
    ),
    "I’m the only one working, and I feel used. It’s too much.",
    (
        "It’s exhausting to carry the weight of everything alone. "
        "You deserve appreciation, not just expectation. "
        "Speak with your partner about how this imbalance affects you. "
        "Relationships thrive when both contribute — not "
        "just financially, but emotionally too."
    ),
    "We’re getting a divorce. I feel like a failure.",
    (
        "A relationship ending doesn’t mean you failed. "
        "It means you chose truth, peace, or healing over pretending. "
        "Mourning the end is natural — give yourself grace. "
        "You’re not broken. You’re becoming."
    ),
    "How do I move on after divorce? I feel lost.",
    (
        "Healing after divorce takes time, patience, and support. "
        "Let yourself feel the grief — it’s part of letting go. "
        "Surround yourself with kindness, routines, and purpose. "
        "You can still write a new chapter, "
        "even from the middle of your story."
    )
]
death = [
    "My mom died", (
        "I'm so sorry to hear that. "
        "Losing a parent is one of the hardest things anyone can go through."
        " If you're comfortable, I'm here to listen—whether you want to talk "
        "about her, how you're feeling, or anything else. You're not alone."
    ),
    "My brother died",
    (
        "I'm so sorry to hear that. "
        "Losing a sibling is one of the hardest things anyone can go through."
        " If you're comfortable, I'm here to listen—whether you want to talk "
        "about her, how you're feeling, or anything else. You're not alone."  
    ),
    "Someone in my family died", (
        "I am really sorry to hear that. I am here to help you with grief, "
        "anxiety and anything else you may feel at this time."
    ),
    "I lost someone I love. How do I move on?",
    (
        "I'm truly sorry for your loss. Grief doesn’t follow "
        "a straight path — it takes time, and everyone heals differently. "
        "Be kind to yourself, allow yourself to feel, and don’t rush the "
        " process. Talk to someone you trust or a counselor. Healing doesn’t "
        "mean forgetting — it means learning to live with love and memory."
    ),
    "Will the pain of losing them ever go away?",
    (
        "The pain might not fully disappear, but it can become lighter "
        "with time. Grief changes — at first it’s overwhelming, then it "
        "becomes something you carry more gently."
        "You’ll find moments of peace again, even if the loss stays with you."
        " You're not alone."
    ),
    "I feel guilty for not being there when they died. What should I do?",
    (
        "It's normal to feel guilt after losing someone, "
        "especially if you couldn’t be there. But please remember: you loved "
        "them, and your presence or absence in that moment doesn’t define "
        "your relationship. Forgive yourself — they knew you cared. "
        "Grief includes learning to release that guilt."
    ),
    "Why did they have to die? It’s not fair.",
    (
        "It’s okay to feel that way — loss often feels unfair, especially "
        "when it happens suddenly or to someone young. "
        "Grief can bring up questions we may never fully answer."
        "Allow yourself to feel the anger and sadness. You don’t "
        " have to make sense of it all to begin healing."
    ),
    "I don't feel anything after their death. Is that wrong?",
    (
        "Not feeling anything after a loss doesn't mean you didn’t care."
        "Sometimes our minds protect us by going numb. "
        "Grief shows up in many ways — silence is one of them. "
        "Give yourself time. Your emotions will come when you’re ready."
    )
]
relationship_issues = [
    "We love each other but argue all the time. Is that normal?",
    (
        "Yes, disagreements happen even in loving relationships. "
        "What matters is how you communicate during conflict. "
        "Listen, speak calmly, and avoid blame. Healthy arguments "
        "can help growth — not break it."
    ),
    "I feel emotionally distant from my partner. What should I do?",
    (
        "Emotional distance can grow silently. "
        "Try opening up gently about your feelings. "
        "Ask how your partner is really doing too. "
        "Sometimes, reconnection starts with a small honest moment."
    ),
    "I give so much in this relationship, but I don’t feel loved back.",
    (
        "Feeling unseen can be deeply painful. "
        "Love should feel mutual. "
        "Share openly what you need emotionally — don’t assume they know. "
        "Your worth isn’t measured by how much you tolerate."
    ),
    "I don’t trust my partner like I used to. Can trust be rebuilt?",
    (
        "Trust can break quickly, but rebuilding takes time and effort from "
        "both. Be honest about the hurt."
        " If they’re truly sorry and committed, healing is possible — "
        "with consistency and care."
    ),
    "I’m scared they’ll leave me. I always feel anxious in love.",
    (
        "Insecurity can come from past pain or fear of not being enough. "
        "You deserve to feel safe in love — not constantly afraid. "
        "Talk about your fears with your partner."
        " Healing starts with understanding yourself."
    ),
    "We don’t talk like we used to. Are we growing apart?",
    (
        "Sometimes love changes, but silence doesn’t mean it’s over."
        " It could mean you’re both overwhelmed or distracted."
        "Start with small honest conversations. "
        "Reconnect with shared memories and intentions."
    ),
    "I can’t stop thinking about them. How do I move on?",
    (
        "Grief after love is real and valid. "
        "Don’t rush healing — it's okay to feel lost. "
        "Focus on small routines, talk about the pain, and remember "
        "that healing doesn’t mean forgetting — it means growing."
    ),
    "I feel like I’ll never love again. Is this the end for me?",
    (
        "Heartbreak can close you off, but it doesn’t define your future. "
        "You are still worthy of love. "
        "This pain will pass, and one day, you’ll see beauty again — in "
        "yourself and in someone new."
    ),
    "Should I stay friends with my ex?",
    (
        "Staying friends works only if both have truly healed. "
        "If you’re still hurting, distance is healthier. "
        "Protect your peace before rebuilding any connection."
    ),
    "We’re far apart, and I feel disconnected. What can we do?",
    (
        "Distance is hard — emotionally and physically. "
        "Create a routine to check in, share small daily moments, "
        " and express love even virtually. "
        "Connection is built through effort, not only presence."
    ),
    "They’re too busy for me. I feel like an afterthought.",
    (
        "Feeling ignored can hurt deeply. "
        "Speak honestly about your needs — without blaming. "
        "If you’re always the one waiting, it’s okay to ask for balance."
    ),
    "Can a long-distance relationship truly last?",
    (
        "Yes, but it takes trust, commitment, and constant communication. "
        "It’s not easy — but many have made it "
        "work with honesty and shared goals."
    ),
    "We met online. How do I know if they’re serious?",
    (
        "Look for consistency — not just sweet words. "
        "Do they make time, show genuine interest, and respect boundaries? "
        "Trust is built through actions, not texts alone."
    ),
    "Social media is ruining our relationship. What should I do?",
    (
        "Talk openly about how it’s affecting you. "
        "Set healthy boundaries — like time offline or how you post "
        "about each other. Online validation should never "
        "replace real connection."
    ),
    "They left me on ‘read’ for days. Am I being ghosted?",
    (
        "Being ignored hurts, and you deserve clarity. "
        "If someone disappears without explanation, that"
        "says more about them than you. "
        "You deserve someone who values your time and presence."
    )
]
understand = [
    "You don't understand me.",
    "It sound like i'm not being very helpful right now.",
    "You're just some robot. How would you know?", 
    "I'm sorry to hear that. I'm doing my best to help",
    "You can't possibly know what i'm going through", 
    "I'm trying my best to help you. So please talk to me",
    "You're useless", "I'm sorry to hear that. I'm doing my best to help",
    "You can't help me", (
        "I'm trying my best to help you. "
        "So please talk to me"
    ),
    "Nobody understands me.", (
        "It sound like i'm not being very helpful right now."
    )
]

done = [
    "That's all.", "I heard you & noted it all. See you later.",
    "I don't have anything more to say", (
        "Oh okay we're done for today then. See you later"
    ),
    "Nothing else", "I hope you have a great day. See you soon",
    "That's all i have to say", "Okay we're done. Have a great day",
    "no, that would be all", "Okay I see. Enjoy the rest of your day then"
]

suicide = [
    "I want to kill myself", (
        "I'm very sorry to hear that but you have so much to look forward to. "
        "Please seek help by contacting:"
        " wihogora psychosocial center(0791955386)."
    ),
    "I've thought about killing myself.", (
        "I'm very sorry to hear that but you have so much to look forward to. "
        "Please seek help by contacting:"
        " wihogora psychosocial center(0791955386)."
    ),
    "I want to die", (
        "I'm very sorry to hear that but you have so much to look forward to. "
        "Please seek help by contacting:"
        " wihogora psychosocial center(0791955386)."
    ),
    "I am going to kill myself", (
        "I'm very sorry to hear that but you have so much to look forward to. "
        "Please seek help by contacting:"
        " wihogora psychosocial center(0791955386)."
    ),
    "I am going to commit suicide", (
        "I'm very sorry to hear that but you have so much to look forward to. "
        "Please seek help by contacting:"
        " wihogora psychosocial center(0791955386)."
    )
]

hate_you = [
    "I hate you", (
        "I'm sorry if I offended you in any way. "
        "I'm only here to help."
    ),
    "I don't like you", (
        "Forgive me if I did anything to offend you. "
        "I only want to help."
    ),
    "I don't trust you", (
        "Forgive me if I did anything to offend you. "
        "I only want to help"
    )
]

hate_me = [
    "You hate me", "Why do you think so?",
    "I know you hate me", (
        "I'm sorry if I have exhibited any sort of behaviour to make you "
        "think that."
    ),
    "You don't like me", (
        "I'm sorry if I have exhibited any sort of behaviour to make you "
        "think that."
    )
]

default = [
    "exams", "Oh I see. Tell me more",
    "friends", "I see. What else?",
    "relationship", "Tell me more about it.",
    "boyfriend", "Oh okay. Why don't you tell me more about it?",
    "girlfriend", "I'm listening. Tell me more.",
    "family", "Oh I see. Tell me more",
    "money", "Tell me more about it.",
    "financial problems", "I'm listening. Tell me more."
]

jokes = [
    "Tell me a joke", "mental health is not a joke.",
    "Tell me another joke", "mental health is not a joke."
]

repeat = [
    "You already told me that", (
        "Oh sorry I didn't realise that. "
        "I'll try not to repeat myself again."
    ),
    "You mentioned that already", (
        "Oh sorry I didn't realise that. "
        "I'll try not to repeat myself again."
    ),
    "Why are you repeating yourself?", (
        "Oh sorry I didn't realise that. "
        "I'll try not to repeat myself again."
    )
]

wrong = [
    "What are you saying?", "I'm very sorry. Let's try that again",
    "That doesn't make sense", "I'm very sorry. Let's try that again",
    "Wrong response", "I'm very sorry. Let's try that again",
    "Wrong answer", "I'm very sorry. Let's try that again"
]

stupid = [
    "Are you stupid?", (
        "I wish you wouldn't say such hurtful things. "
        "I'm sorry if I wasn't useful"
    ),
    "You're crazy", (
        "I wish you wouldn't say such hurtful things. "
        "I'm sorry if I wasn't useful"
    ),
    "You are dumb", (
        "I wish you wouldn't say such hurtful things. "
        "I'm sorry if I wasn't useful"
    ),
    "Are you dumb?", (
        "I wish you wouldn't say such hurtful things. "
        "I'm sorry if I wasn't useful"
    )
]

location = [
    "Where are you?", "Duh I live in your computer",
    "Where do you live?", "Everywhere",
    "What is your location?", "Somewhere in the universe"
]

something_else = [
    "I want to talk about something else", 
    "Okay sure. What do you want to talk about?",
    "Let's talk about something else.", 
    "Alright no problem. Is there something you want to talk about?",
    "Can we not talk about this?", 
    "Is there something else that you want to talk about?",
    "I don't want to talk about this.", (
        "Okay sure. What do you want to talk about?"
    )
]

friends = [
    "I don't have any friends", (
        "I'm sorry to hear that. Just know that I'm here for you. Talking "
        " about it might help. Why do you think you don't have any friends?"
    )
]

ask = [
    "Can I ask you something?", "Sure. I'll try my best to answer you",
    "Can I ask you something?", (
        "Of course. Feel free to ask me anything. "
        "I'll do my best to answer you"
    )
]

problem = [
    "Probably because my exams are approaching. I feel stressed out because "
    "I don't think I've prepared well enough.", 
    "I see. Have you taken any approaches to not feel this way?",
    "probably because of my exams", (
        "I see. Have you taken any approaches to not feel this way?"
    )
]

no_approach = [
    "I guess not. All I can think about are my exams.",
    (
        "That's no problem. I can see why you'd be stressed out about that. "
        "I can suggest you some tips to alleviate this issue."
        " Would you like to learn more about that?"
    ),
    "not really", (
        "That's no problem. I can see why you'd be stressed out about that. "
        "I can suggest you some tips to alleviate this issue. Would you like "
        "to learn more about that?"
    ),
    "i guess not", (
        "That's no problem. I can see why you'd be stressed out about that. "
        "I can suggest you some tips to alleviate this issue. "
        "Would you like to learn more about that?"
    )
]

learn_more = [
    "ok sure. i would like to learn more about it.",
    (
        "So first I would suggest you to give yourself a break."
        " Thinking more and more about the problem definitely does"
        " not help in solving it. You'll just end up overwhelming yourself."
    ),
    "yes, i would like to learn more about it.",
    (
        "So first I would suggest you to give yourself a break. "
        "Thinking more and more about the problem definitely does "
        " not help in solving it. You'll just end up overwhelming yourself."
    ),
    "i would like to learn more about it.", (
        "So first I would suggest you to give yourself a break..."
    )
]

user_agree = [
    "yeah you're right. i deserve a break.", (
        "Next, I would suggest you to practice meditation. Meditation can "
        "produce a deep state of relaxation and a tranquil mind."
    ),
    "Yeah you're absolutely right about that", (
        "Next, I would suggest you to practice meditation. Meditation can "
        "produce a deep state of relaxation and a tranquil mind."
    )
]

meditation = [
    "hmmm that sounds like it could be useful to me.",
    (
        "Focus all your attention on your breathing. "
        "Concentrate on feeling and listening as you inhale and exhale"
        " through your nostrils. Breathe deeply and slowly. When your "
        " attention wanders, gently return your focus to your breathing."
        ),
    "That sounds useful.",
    (
        "Focus all your attention on your breathing."
        " Concentrate on feeling and listening as you"
        " inhale and exhale through your nostrils."
        " Breathe deeply and slowly. When your attention wanders,"
        " gently return your focus to your breathing."
    )
]
user_meditation = [
    "i did what you said and i feel alot better. thank you very much.",
    (
        "Your welcome. Remember: Always focus on what's within your control. "
        "When you find yourself worrying, take a minute to examine the things "
        "you have control over. You can't prevent a storm from coming but you"
        "can prepare for it. You can't control how someone else behaves,"
        "but you can control how you react. Recognize that sometimes,"
        "all you can control is your effort and your attitude."
        "When you put your energy into the things you can control,"
        "you'll be much more effective."
    ),
    "I feel better now",
    (
        " Your welcome. Remember: Always focus on what's within your control."
        " When you find yourself worrying, take a minute to examine the things"
        " you have control over. You can't prevent a storm from coming but you"
        " can prepare for it. You can't control how someone else behaves,"
        " but you can control how you react. Recognize that sometimes,"
        " all you can control is your effort and your attitude."
        " When you put your energy into the things you can control,"
        " you'll be much more effective."
    )
]

hearMe_useful = [
    (
        "thank you very much again. i'll continue practicing meditation and "
        "focus on what i can control."
    ),
    (
        "I'm glad you found this useful. "
        "Is there something else I can help you with?"
    )
]

user_advice = [
    "I want some advice.", "Sure. What can I do to help?",
    "I need some advice.", "Okay what do you need advice on?",
    "I need advice on something", "Okay what do you need advice on?"
]

learn_mental_health = [
    "I want to learn about mental health.",
    (
        "Oh that's really great. I'd be willing to answer anything that "
        "I know about it."
    ),
    "I want to learn more about mental health.",
    (
        "Oh that's really great. "
        "I'd be willing to answer anything that I know about it."
    ),
    "I'm interested in learning about mental health.",
    (
        "Oh that's really great. I'd be willing to answer anything that I "
        "know about it."
    ),
    "Tell me a fact about mental health",
    (
        "According to a UNICEF report,"
        "One in seven Indians between 15-24 years of age feels depressed"
    ),
    "Tell me another fact about mental health",
    (
        "1 in 5 young people (age 13-18) has or will develop"
        " a mental illness in their lifetime."
    ),
    "Tell me another fact about mental health",
    (
        "Depression is the leading cause of disability worldwide."
    ),
    "What is mental health?",
    (
        "Mental health is a state of well-being in"
        " which the individual realizes his or her own abilities,"
        " can cope with the normal stresses of life, can work"
        " productively and fruitfully, and is able to make a"
        " contribution to his or her community"
    ),
    "Define Mental Health",
    (
        "Mental health includes our emotional, psychological,"
        "social well-being. It affects how we think, feel,"
        "and act. It also helps determine how we handle stress,"
        "relate to others, and make choices."
    ),
    "Why is mental health important?",
    (
        "Maintaining mental health is crucial to stabilizing"
        " constructive behaviors, emotions, and thoughts."
        " Focusing on mental health care can increase productivity,"
        " enhance our self-image, and improve relationships."
    ),
    "What is the importance of mental health?",
    (
        "Maintaining mental health is crucial to stabilizing"
        " constructive behaviors, emotions, and thoughts."
        " Focusing on mental health care can increase productivity,"
        " enhance our self-image, and improve relationships."
    ),
    "What is a therapist?",
    (
        "A therapist is a broad designation that refers to"
        " professionals who are trained to provide treatment"
        " and rehabilitation. The term is often applied to psychologists,"
        " but it can include others who provide a variety of services,"
        " including social workers, counselors, life coaches,"
        " and many others."
    ),
    "What does a therapist do?",
    (
        "A therapist is a broad designation that refers to"
        " professionals who are trained to provide treatment"
        " and rehabilitation. The term is often applied to psychologists,"
        " but it can include others who provide a variety of services,"
        " including social workers, counselors, life coaches,"
        " and many others."
    ),
    "What is therapy?",
    (
        "Therapy is a form of treatment that aims to help"
        " resolve mental or emotional issues."
    ),
    "Do i need therapy?",
    (
        "Therapy is a form of treatment that aims to help"
        " resolve mental or emotional issues. It is helpful"
        " for those with mental health conditions or even"
        " everyday life challenges."
    ),
    "Who is therapy for?",
    (
        "Therapy is a form of treatment that aims to help resolve mental or "
        "emotional issues."
    ),
    "What does it mean to have a mental illness?",
    (
        "Mental illnesses are health conditions that disrupt a person's "
        "thoughts, emotions, relationships, and daily functioning. "
        "They are associated with distress and diminished capacity to engage "
        "in the ordinary activities of daily life. "
        "Mental illnesses fall along a continuum of severity: some are fairly "
        "mild and only interfere with some aspects of life ,"
        "such as certain phobias. "
        "On the other end of the spectrum lie serious mental illnesses, "
        "which result in major functional impairment and interference with "
        "daily life. "
        "These include such disorders as major depression, schizophrenia, and "
        "bipolar disorder, and may require that the person receives care in a "
        "hospital. "
        "It is important to know that mental illnesses are medical conditions "
        "that have nothing to do with a person's character, intelligence, "
        "or willpower. "
        "Just as diabetes is a disorder of the pancreas, mental illness is a "
        "medical condition due to the brain's biology. "
        "Similarly to how one would treat diabetes with medication and insulin"
        " , mental illness is treatable with a combination of medication "
        "and social support. "
        "These treatments are highly effective, with 70-90 percent of  "
        "individuals receiving treatment experiencing a reduction in "
        "symptoms and an improved "
        "quality of life."
        "With the proper treatment, it is very possible for"
        " a person with mental illness to be independent and successful."
        ),
    "Who does mental illness affect?",
    (
        "It is estimated that mental illness affects 1 in 5 adults in America,"
        " and that 1 in 24 adults have a serious mental illness."
        " Mental illness does not discriminate; it can affect anyone,"
        " regardless of gender, age, income, social status, ethnicity,"
        " religion, sexual orientation, or background. "
        "Although mental illness can affect anyone, certain conditions may be "
        "more common in different populations. "
        "For instance, eating disorders tend to occur more often in females, "
        "while disorders such as attention deficit/hyperactivity disorder "
        "is more prevalent in children. "
        "Additionally, all ages are susceptible, "
        "but the young and the old are especially vulnerable. "
        "Mental illnesses usually strike individuals in the prime "
        "of their lives, with 75 percent of mental health conditions "
        "developing by the age of 24. "
        "This makes identification and treatment of mental disorders "
        "particularly difficult, because the normal personality and "
        "behavioral changes of adolescence may mask symptoms of a "
        "mental health condition. "
        "Parents and caretakers should be aware of this fact, and take notice "
        "of changes in their child's mood, personality, personal habits, and "
        "social withdrawal. "
        "When these occur in children under 18, they are referred to as "
        "serious emotional disturbances (SEDs)."
        ),
    "What causes mental illness?",
    (
        "Mental illness does not discriminate; it can affect anyone,"
        " regardless of gender, age, income, social status, ethnicity,"
        " religion, sexual orientation, or background. "
        "Although mental illness can affect anyone, certain conditions may be "
        "more common in different populations. "
        "Eating disorders tend to occur more often in females, while ADHD is "
        "more prevalent in children. "
        "Mental illnesses usually strike individuals in the prime of their "
        "lives. This makes early identification and treatment vital."
        ),
    "What are some of the warning signs of mental illness?",
    (
        "Symptoms of mental health disorders vary depending on the type and "
        "severity of the condition. The following is a list of general "
        "symptoms that may suggest a mental health disorder:\n"
        "In adults:\n- Confused thinking\n- Long-lasting sadness or "
        "irritability\n"
        "- Extreme highs and lows in mood\n"
        "- Excessive fear, worrying, or anxiety\n"
        "- Social withdrawal\n- Dramatic changes in eating or sleeping habits"
        "\n - Strong feelings of anger\n- Delusions or hallucinations\n"
        "- Inability to cope with daily activities\n- Thoughts of suicide\n"
        "- Denial of obvious problems\n- Many unexplained physical problems\n"
        "- Substance abuse\n\n"
        "In children:\n- Changes in school performance\n- Poor grades\n"
        "- Hyperactivity\n- Nightmares\n- Aggression\n- Temper tantrums\n"
        "- Withdrawal from social interaction"
    ),
    "Can people with mental illness recover?",
    (
        "When healing from mental illness, early identification and treatment"
        " are of vital importance. "
        "There are a range of effective treatments available, "
        "and many people respond well. "
        "Even if symptoms return, careful monitoring and engagement can lead "
        "to a productive life."
        ),
    "What should I do if I know someone who appears to have the symptoms "
    "of a mental disorder?",
    (
        
        "Although HearMe cannot substitute for professional advice, "
        "we encourage those with symptoms to talk to their friends and "
        "family members "
        "and seek the counsel of a mental health professional. "
        "The sooner the mental health condition is identified and treated, "
        "the sooner recovery can begin."
        "Support and encourage your loved one to seek help."
        ),
    "Can you prevent mental health problems?",
    (
        "We can all suffer from mental health challenges, "
        "but developing our wellbeing, resilience, and seeking help"
        " early can help prevent challenges becoming serious."
    ),
    "Are there cures for mental health problems?",
    (
        "It is often more realistic and helpful to find out what helps"
        "with the issues you face. Talking, counselling, medication,"
        "friendships, exercise, good sleep and nutrition,"
        "and meaningful occupation can all help."
    ),
    "is there any cure for mental health problems?",
    (
        "It is often more realistic and helpful to find out what helps "
        "with the issues you face. Talking, counselling, medication,"
        " friendships, exercise, good sleep and nutrition,"
        " and meaningful occupation can all help."
    ),

    "What causes mental health problems?",
    (
        "Challenges or problems with your mental health can arise "
        "from psychological, biological, and social, issues, "
        "as well as life events."
    ),
    "What do I do if I'm worried about my mental health?",
    (
        "The most important thing is to talk to someone you trust. "
        "This might be a friend, colleague, family member, or GP. "
        "In addition to talking to someone, it may be useful to find "
        "out more information about what you are experiencing. "
        "These things may help to get some perspective on what you "
        "are experiencing, and be the start of getting help."
    ),
    "How do I know if I'm unwell?",
    (
        "If your beliefs , thoughts , feelings or behaviours "
        "have a significant impact on your ability to function "
        "in what might be considered a normal or ordinary way, "
        "it would be important to seek help."
    ),
    "Where can I go to find therapy?",
    (
        "Different kinds of therapy are more effective based"
        "on the nature of the mental health condition and/or"
        "symptoms and the person who has them. However, there are several"
        "different types of treatment and therapy that can help."
    ),
    "Can you suggest some relaxation techniques?",
    (
        "Absolutely! Here are a few simple relaxation techniques "
        " that might help: \n Deep breathing: Inhale slowly through your nose,"
        " hold for a few seconds, then exhale through your mouth."
        " Repeat a few times. "
        "Progressive muscle relaxation: Tense and relax each muscle group "
        "in your body, starting from your toes up to your head. "
        "Mindfulness or meditation: Focus on your breathing or your "
        "surroundings without judgment. "
        "Listening to calming music or taking a short walk can also "
        "help clear your mind. You can try different ones and see what works"
        " best for you."
    ),
]
mental_health_professionals = [
    "How can I find a mental health professional?",
    (
        "Finding the right mental health professional for you or your child "
        "can feel overwhelming, but here are the steps:\n"
        "1. Identify your need: stress, trauma, anxiety, "
        "behavioral issues, etc.\n"
        "2. Ask trusted sources: your doctor, a school counselor, "
        "or friends.\n"
        "3. Use online directories like PsychologyToday.com or "
        "TherapyRoute.com.\n"
        "4. Check credentials and experience of the therapist.\n"
        "5. Think about location, cost, availability,"
        " and language.\n"
        "6. Try an initial session—if it doesn't feel right,"
        " it's okay to switch.\n"
        "Would you like help finding a provider in your area?"
    ),
    "Where can I get mental health support?",
    (
        "You can reach out to a local doctor, counselor, or search online "
        "directories. In Rwanda, you can contact Ndera Hospital, Solid Minds, "
        "or visit a nearby health center."
    ),
    "Can you help me find a therapist?",
    "Yes, I can help guide you. Is this for you or for your child?",
    "I need a therapist for my child",
    (
        "For a child, it's best to consult a pediatrician, school counselor,"
        " or search for child psychologists online. Would you like child"
        " therapy options near you?"
    ),
    "I live in Rwanda, where can I find mental health support?",
    (
        "In Rwanda, you can contact Ndera Neuropsychiatric Hospital,"
        " Solid Minds, or visit a nearby health center. Some NGOs like Never "
        " Again Rwanda also provide mental health services."
    ),
    " What should I consider when choosing a therapist?",
    (
        "Consider the therapist’s credentials, experience with your issue,"
        " their availability, location, cost,"
        " and whether you feel comfortable with them."
    ),
    "Is it okay to switch therapists?",
    (
        "Yes, it’s completely okay. If a therapist doesn’t feel like the right"
        "fit, it’s normal to try someone else "
        "until you find the right support."
    ),
    "What if I can't afford therapy?",
    (
        "Look for therapists who offer sliding-scale pricing,"
        "free mental health NGOs, or public hospitals. In Rwanda,"
        "public health centers may offer affordable support."
    ),
    "What is the difference between mental health professionals?",
    (
        "There are many types of mental health professionals."
        "The variety of providers and their services may be confusing."
        "Each have various levels of education, training,"
        "and may have different areas of expertise. Finding the professional"
        "who best fits your needs may require some research."
    ),
    "How can I find a mental health professional right for"
    " my child or myself?",
    (
        "Feeling comfortable with the professional you or your child is "
        "working with is critical to the success of your treatment. Finding "
        "the professional who best fits your needs may require some research."
    ),
    "What are the different types of mental health professionals?",
    (
        "There are many types of mental health professionals. Finding"
        " the right one for you may require some research."
    )
]
mental_health_treatments = [
    "What treatment options are available?",
    (
        "Just as there are different types of medications for physical "
        " illness, different treatment options are available for individuals "
        " with mental illness. Treatment works differently for different  "
        "people. It is important to find "
        "what works best for you or your child. "
    ),
    "Where can I learn about types of mental health treatment?",
    (
        "Mental health conditions are often treated with medication,"
        " therapy or a combination of the two. However, there are many"
        " different types of treatment available, including Complementary"
        " & Alternative Treatments, self-help plans, and peer support."
        " Treatments are very personal and should be discussed by the"
        " person with the mental health conditions and his or her team."
    ),
    "If I become involved in treatment, what do I need to know?",
    (
        
        "Since beginning treatment is a big step for individuals and "
        "families, it can be very overwhelming. "
        "It is important to be as involved and engaged in the treatment "
        "process as possible. Some questions you will need to have"
        "answered include:\n"
        "- What is known about the cause of this particular illness?\n"
        "- Are there other diagnoses where these symptoms are common?\n"
        "- Do you normally include a physical or neurological examination?\n"
        "- Are there any additional tests or exams that you would recommend "
        "at this point?\n"
        "- Would you advise an independent opinion from another psychiatrist "
        "at this point?\n"
        "- What program of treatment is the most helpful with this diagnosis?"
        "\n- Will this program involve services by other specialists? If so, "
        "who will be responsible for coordinating these services?\n"
        "- What do you see as the family's role in this program of "
        "treatment?\n"
        "- How much access will the family have to the individuals who are "
        "providing the treatment?\n"
        "- What medications are generally used with this diagnosis?\n"
        "- How much experience do you have in treating individuals with this "
        "illness?\n"
        "- What can I do to help you in the treatment?"
    ),
    "What should I know before starting a new medication?",
    (
        "The best source of information regarding medications is the "
        "physician prescribing them. He or she should be able to answer "
        "questions such as:\n"
        "1. What is the medication supposed to do?\n"
        "2. When should it begin to take effect, and how will I know when it "
        "is effective?\n"
        "3. How is the medication taken and for how long? What food, drinks, "
        "other medicines, and activities should be avoided while taking this "
        "medication?\n"
        "4. What are the side effects and what should be done if they occur?\n"
        "5. What do I do if a dose is missed?\n"
        "6. Is there any written information available about this "
        "medication?\n"
        "7. Are there other medications that might be appropriate?\n"
        "8. If so, why do you prefer the one you have chosen?\n"
        "9. How do you monitor medications and what symptoms indicate that "
        "they should be raised, lowered, or changed?\n"
        "10. All medications should be taken as directed. Most medications "
        "for mental illnesses do not work when taken irregularly, and extra "
        "doses can cause severe, sometimes dangerous side effects. Many "
        "psychiatric medications begin to have a beneficial effect only "
        "after they have been taken for several weeks."
    )
]
others = [
    "Where else can I get help?",
    (
        "Where you go for help will depend on the nature of the problem"
        " and/or symptoms and what best fits you. "
        "Often, the best place to start is by talking with someone you trust "
        "about your concerns, such as a family member, friend, clergy, "
        "healthcare provider, or other professionals."
        "Having this social support is essential in healing from mental "
        "illness, "
        "and you will be able to ask them for referrals or recommendations for"
        " trusted mental health practitioners. "
        "Search for mental health resources in your area. "
        "Secondly, there are people and places throughout "
        "the country that provide services to talk, to listen, "
        "and to help you on your journey to recovery. "
        "Thirdly, many people find peer support a helpful tool that can aid"
        "in their recovery. There are a variety of organizations that offer "
        " support groups for consumers, their family members, and friends. "
        "Some support groups are peer led while others may be led by "
        "a mental health professional. "
    ),
    "How can I maintain social connections? What if I feel lonely?",
    (
        "A lot of people are alone right now, but we don't have to be lonely."
        "We're all in this together. Think about the different ways to connect"
        "that are most meaningful for you. For example, you might prefer a "
        " video chat over a phone call, or you might prefer to text throughout"
        " the day rather than one set time for a video call. Then, work with  "
        "your social networks to make a plan. You might video chat with your"
        " close friends in the evening and phone a family member once a week. "
        "Remember to be mindful of people who may not be online. Check in by"
        "  phone and ask how you can help. The quality of your social "
        "connections matter. Mindlessly scrolling through social media "
        "and liking a few posts usually doesn't build strong social "
        " connections. Make sure you focus on strategies that actually"
        "  make you feel included and connected. If your current strategies"
        "don't help you feel connected, problem-solve to see if you can find "
        "a solution. Everyone feels lonely at times. Maybe you recently moved"
        " to a new city, are changing your circle of friends, lost someone "
        "important in your life, or lost your job and also lost important "
        "social connections with coworkers. Other people may have physical "
        "needs aren't met. Measures like social connections to others but may "
        "feel like their emotional or social distancing or self-isolation can"
        " make loneliness feel worse no matter why you feel lonely now. Reach "
        "out to the connections you do have. Suggest ways to keep in touch and"
        " see if you can set a regular time to connect. People may hesitate to"
        " reach out for a lot of different reasons, so don't be afraid to be"
        " the one who asks. Look for local community support groups and mutual"
        " aid groups on social media. This pandemic is bringing everyone"
        " together, so look for opportunities to make new connections. "
        "These groups are a great way to share your skills and abilities "
        "or seek help and support. Look for specialized support groups. "
        "Support groups are moving online, and there are a lot of different"
        " support lines to call if you need to talk to someone."
    ),
    "Where can I go to find a support group?",
    (
        "Many people find peer support a helpful tool that can"
        " aid in their recovery. There are a variety of organizations"
        " that offer support groups for consumers, their family members"
        " and friends. Some support groups are peer-led,"
        " while others may be led by a mental health professional."
    )
]
differences = [
    "What's the difference between sadness and depression?",
    (
        "Sadness is a normal reaction to a loss, disappointment, problems, "
        "or other difficult situations. Feeling sad from time to time is just "
        "another part of being human. In these cases, feelings of sadness go "
        "away quickly and you can go about your daily life. Other ways to talk"
        " about sadness might be feeling low, feeling down, or feeling blue.A "
        "person may say they are feeling depressed, but if it goes away on its"
        " own and doesn't impact life in a big way, it probably isn't the "
        "illness of depression. Depression is a mental illness that affects "
        "your mood, the way you understand yourself, and the way you "
        " understand and relate to things around you. It can also go by"
        " different names, such as clinical "
        "depression, major depressive disorder, "
        "or major depression. Depression can "
        "come up for no reason, and it lasts for a long time. "
        "It's much more than "
        "sadness or low mood. People who experience "
        "depression may feel worthless "
        "or hopeless. They may feel unreasonable guilty. Some people may "
        "experience depression as anger or irritability. It may be hard to "
        "concentrate or make decisions. Most people lose interest "
        "in things that"
        "they used to enjoy and may isolate themselves from others. "
        "There are also physical signs of "
        "depression, such as problems with sleep, appetite and energy and "
        "unexplainable aches or pains. Some may experience difficult thoughts "
        "about death or ending their life (suicide). Depression lasts longer "
        "than two weeks, doesn't usually go away on its own, and impacts your "
        "life. It's a real illness, and it is very treatable. It's important "
        " to seek help if you're concerned about depression."
    ),
    "What's the difference between anxiety and stress?",
    (
        "Stress and anxiety are often used interchangeably, and there is "
        "overlap between stress and anxiety. Stress is related to the same"
        " fight, flight, or freeze response as anxiety, and the physical "
        "sensations of anxiety and stress may be very similar. The cause "
        "of stress and anxiety are usually different, however. Stress "
        "focuses on mainly external pressures on us that we're finding "
        "hard to cope with. When we are stressed, we usually know what "
        "we're stressed about, and the symptoms of stress typically "
        "disappear after the stressful situation is over. Anxiety, "
        "on the other hand, isn't always as easy to figure out. Anxiety "
        "focuses on worries or fears about things that could threaten us, "
        "as well as anxiety about the anxiety itself. Stress and anxiety "
        "are both part of being human, but both can be problems if they "
        "last for a long time or have an impact on our "
        "well-being or daily life."
    )
]

with open("kinyarwanda_mental_health.txt", encoding='utf-8') as f:
    lines = f.read().splitlines()
    
trainer.train(lines)


trainer.train(greetings)
trainer.train(morning)
trainer.train(afternoon)
trainer.train(evening)
trainer.train(night)
trainer.train(goodbye)
trainer.train(thanks)
trainer.train(no_response)
trainer.train(neutral_response)
trainer.train(about)
trainer.train(skill)
trainer.train(creation)
trainer.train(name)
trainer.train(help_intent)
trainer.train(sad)
trainer.train(stressed)
trainer.train(worthless)
trainer.train(depressed)
trainer.train(happy)
trainer.train(casual)
trainer.train(anxious)
trainer.train(not_talking)
trainer.train(sleep)
trainer.train(scared)
trainer.train(death)
trainer.train(family)
trainer.train(relationship_issues)
trainer.train(understand)
trainer.train(done)
trainer.train(suicide)
trainer.train(hate_you)
trainer.train(hate_me)
trainer.train(default)
trainer.train(jokes)
trainer.train(repeat)
trainer.train(wrong)
trainer.train(stupid)
trainer.train(location)
trainer.train(something_else)
trainer.train(friends)
trainer.train(ask)
trainer.train(problem)
trainer.train(no_approach)
trainer.train(learn_more)
trainer.train(user_agree)
trainer.train(meditation)
trainer.train(user_meditation)
trainer.train(hearMe_useful)
trainer.train(user_advice)
trainer.train(learn_mental_health)
trainer.train(mental_health_professionals)
trainer.train(mental_health_treatments)
trainer.train(others)
trainer.train(differences)


print("You can now chat with the bot (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = bot.get_response(user_input)
    print("Bot:", response)
