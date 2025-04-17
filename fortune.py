
print("🔮 Welcome to Ayush Agrawal's Fortune Teller (21JE0204) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Ayush! Keep smiling. ✨")
elif mood == "sad":
    print("🌧 Your fortune: Tough times don't last, but tough people do.")
elif mood == "neutral":
    print("😐 Your fortune: A surprise is waiting for you just around the corner.")
else:
    print("Please enter a valid mood (happy/sad/neutral).")
