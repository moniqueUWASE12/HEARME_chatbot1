from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Initialize the bot
bot = ChatBot(
    'chatbot',
    read_only=False,
    logic_adapters=['chatterbot.logic.BestMatch']
)

# Training data
list_to_train = [
    "Hello",
    "Hi, I'm HearMe. How are you feeling today?",
    "I'm feeling sad",
    "I'm really sorry you're feeling this way. Sometimes talking about your feelings can help. What's on your mind?",
    "I'm anxious",
    "It sounds like you're experiencing anxiety. Would you like some tips on how to relax or talk about what's causing it?",
    "I feel alone",
    "It can be hard feeling isolated. Remember, I'm here to listen. Do you want to share more?",
    "I don't know what to do",
    "When things seem overwhelming, taking small steps can help. Tell me what is troubling you?",
    "Can you recommend a therapist?",
    "I can help with that. Let me check for some available therapist recommendations for you.",
    "Can you show me a video?",
    "Let me find a helpful video for you.",
    "Goodbye",
    "Take care of yourself. I'm always here when you need to talk.",
    "Thank you",
    "You're welcome. I'm glad I could help."
]

# Train the bot
trainer = ListTrainer(bot)
trainer.train(list_to_train)

print("✅ HearMe Chatbot training completed!")
