import random

computer = random.choice(["rock", "paper", "scissors"])

player = input("🎮 Choice - rock, paper, scissors: ")

print("🤖 Computer choice:", computer)

if computer == player:
    print("🤝 Draw!!!")

elif player == "rock" and computer == "scissors":
    print("🪨 You Won!! 🏆")

elif player == "rock" and computer == "paper":
    print("🪨 You Lost!! 😢")

elif player == "paper" and computer == "rock":
    print("📄 You Won!! 🏆")

elif player == "paper" and computer == "scissors":
    print("📄 You Lost!! 😢")

elif player == "scissors" and computer == "paper":
    print("✂️ You Won!! 🏆")

elif player == "scissors" and computer == "rock":
    print("✂️ You Lost!! 😢")