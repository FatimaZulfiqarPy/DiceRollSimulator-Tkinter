import tkinter as tk
from PIL import Image, ImageTk
import random

# Create main window
window = tk.Tk()
window.geometry("600x480")
window.title("🎲 Dice Roll 🎲")

# List of dice images
dice_images = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]

# Starting random dice
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice_images)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice_images)))

# Labels for dice
label1 = tk.Label(window, image=image1)
label1.image = image1
label1.place(x=20, y=140)

label2 = tk.Label(window, image=image2)
label2.image = image2
label2.place(x=320, y=140)

# Player scores
player1_score = 0
player2_score = 0

# Labels to show scores
score_label1 = tk.Label(window, text="Player 1 Score: 0", font="Times 14 bold")
score_label1.place(x=20, y=410)

score_label2 = tk.Label(window, text="Player 2 Score: 0", font="Times 14 bold")
score_label2.place(x=320, y=410)

# Result label
result_label = tk.Label(window, text="", font="Times 16 bold", fg="blue")
result_label.place(x=200, y=400)

# Roll function
def dice_roll():
    global player1_score, player2_score
    
    # Player 1 roll
    dice1 = random.randint(1, 6)
    new_image1 = ImageTk.PhotoImage(Image.open(dice_images[dice1 - 1]))
    label1.configure(image=new_image1)
    label1.image = new_image1
    player1_score += dice1
    
    # Player 2 roll
    dice2 = random.randint(1, 6)
    new_image2 = ImageTk.PhotoImage(Image.open(dice_images[dice2 - 1]))
    label2.configure(image=new_image2)
    label2.image = new_image2
    player2_score += dice2
    
    # Update scores
    score_label1.config(text=f"Player 1 Score: {player1_score}")
    score_label2.config(text=f"Player 2 Score: {player2_score}")


# Function to check winner
def check_winner():
    if player1_score > player2_score:
        result_label.config(text="🏆 Player 1 Wins!")
    elif player2_score > player1_score:
        result_label.config(text="🏆 Player 2 Wins!")
    else:
        result_label.config(text="🤝 It's a Tie!")

# Roll button
button = tk.Button(window, text="Roll 🎲", bg="black", fg="white", font="Times 20 bold", command=dice_roll)
button.place(x=240, y=30)

# Winner button
winner_button = tk.Button(window, text="Check Winner 🏆", bg="darkgreen", fg="white", font="Times 16 bold", command=check_winner)
winner_button.place(x=210, y=90)

result_label = tk.Label(window, text="", font="Times 20 bold",fg="darkgreen")
result_label.place(x=180, y=438)   # fixed position

# Run window
window.mainloop()
