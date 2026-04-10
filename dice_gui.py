import tkinter as tk
import random

# Dice faces (Unicode)
dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

# Function to animate dice rolling
def roll_dice():
    animate(0)

def animate(count):
    if count < 15:  # number of animation frames
        face = random.choice(dice_faces)
        label.config(text=face, font=("Arial", 100))
        
        # Slight size change for 3D-like effect
        label.config(font=("Arial", 80 + (count % 5) * 5))
        
        root.after(80, animate, count + 1)
    else:
        result = random.randint(1, 6)
        label.config(text=dice_faces[result - 1], font=("Arial", 100))

# Create window
root = tk.Tk()
root.title("🎲 Dice Roller")
root.geometry("300x300")
root.resizable(False, False)

# Dice display label
label = tk.Label(root, text="🎲", font=("Arial", 100))
label.pack(pady=20)

# Roll button
roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 14), command=roll_dice)
roll_button.pack()

# Run app
root.mainloop()
