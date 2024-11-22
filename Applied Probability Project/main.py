import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class ProbabilitySimulatorApp:
    """
    A GUI application to simulate flipping a coin, rolling a die, and drawing a card from a standard deck.
    """
    def __init__(self, master):
        """
        Initialize the application with the main window and its widgets.
        """
        self.master = master
        master.title("Probability Simulator")
        master.configure(bg='white')

        # Create the main title
        self.title_label = tk.Label(master, text="Probability Simulator", font=("Arial", 24, "bold"), bg='white')
        self.title_label.pack(pady=10)

        # Instructions
        instructions = ("Welcome to the Probability Simulator!\n"
                        "Click the buttons below to flip a coin, roll a die, or draw a card.\n"
                        "Results and probabilities will be displayed below.")
        self.instructions_label = tk.Label(master, text=instructions, font=("Arial", 12), bg='white')
        self.instructions_label.pack(pady=10)

        # Create a main frame to hold the three scenarios horizontally
        self.main_frame = tk.Frame(master, bg='white')
        self.main_frame.pack()

        # Create frames for each scenario
        self.create_coin_flip_frame()
        self.create_die_roll_frame()
        self.create_card_draw_frame()

        # Reset button
        self.reset_button = tk.Button(master, text="Reset", command=self.reset, font=("Arial", 12), bg='lightgray')
        self.reset_button.pack(pady=10)

    def create_coin_flip_frame(self):
        """
        Create the coin flip frame with its widgets.
        """
        self.coin_frame = tk.Frame(self.main_frame, bg='white', padx=10, pady=10, relief=tk.RIDGE, borderwidth=2)
        self.coin_frame.pack(side='left', fill='both', expand=True)

        # Coin Flip Section Title
        self.coin_title = tk.Label(self.coin_frame, text="Coin Flip", font=("Arial", 18, "bold"), bg='white')
        self.coin_title.pack()

        # Probability Label
        self.coin_prob_label = tk.Label(self.coin_frame, text="Probability: 50% for Heads or Tails", font=("Arial", 12), bg='white')
        self.coin_prob_label.pack()

        # Sample Space Label
        self.coin_sample_space_label = tk.Label(self.coin_frame, text="Sample Space: {Heads, Tails}", font=("Arial", 12), bg='white')
        self.coin_sample_space_label.pack()

        # Flip Button
        self.flip_button = tk.Button(self.coin_frame, text="Flip Coin", command=self.flip_coin, font=("Arial", 12), bg='lightblue')
        self.flip_button.pack(pady=5)

        # Result Label
        self.coin_result_label = tk.Label(self.coin_frame, text="", font=("Arial", 14), bg='white')
        self.coin_result_label.pack()

        # Event Space Label (will display the result)
        self.coin_event_space_label = tk.Label(self.coin_frame, text="", font=("Arial", 12), bg='white')
        self.coin_event_space_label.pack()

        # Coin Image Label
        self.coin_image_label = tk.Label(self.coin_frame, bg='white')
        self.coin_image_label.pack()

    def create_die_roll_frame(self):
        """
        Create the die roll frame with its widgets.
        """
        self.die_frame = tk.Frame(self.main_frame, bg='white', padx=10, pady=10, relief=tk.RIDGE, borderwidth=2)
        self.die_frame.pack(side='left', fill='both', expand=True)

        # Die Roll Section Title
        self.die_title = tk.Label(self.die_frame, text="Die Roll", font=("Arial", 18, "bold"), bg='white')
        self.die_title.pack()

        # Probability Label
        self.die_prob_label = tk.Label(self.die_frame, text="Probability: 1/6 for each face", font=("Arial", 12), bg='white')
        self.die_prob_label.pack()

        # Sample Space Label
        self.die_sample_space_label = tk.Label(self.die_frame, text="Sample Space: {1, 2, 3, 4, 5, 6}", font=("Arial", 12), bg='white')
        self.die_sample_space_label.pack()

        # Roll Button
        self.roll_button = tk.Button(self.die_frame, text="Roll Die", command=self.roll_die, font=("Arial", 12), bg='lightgreen')
        self.roll_button.pack(pady=5)

        # Result Label
        self.die_result_label = tk.Label(self.die_frame, text="", font=("Arial", 14), bg='white')
        self.die_result_label.pack()

        # Event Space Label (Even or Odd)
        self.die_event_space_label = tk.Label(self.die_frame, text="", font=("Arial", 12), bg='white')
        self.die_event_space_label.pack()

        # Die Image Label
        self.die_image_label = tk.Label(self.die_frame, bg='white')
        self.die_image_label.pack()

    def create_card_draw_frame(self):
        """
        Create the card draw frame with its widgets.
        """
        self.card_frame = tk.Frame(self.main_frame, bg='white', padx=10, pady=10, relief=tk.RIDGE, borderwidth=2)
        self.card_frame.pack(side='left', fill='both', expand=True)

        # Card Draw Section Title
        self.card_title = tk.Label(self.card_frame, text="Card Draw", font=("Arial", 18, "bold"), bg='white')
        self.card_title.pack()

        # Probability Label
        self.card_prob_label = tk.Label(self.card_frame, text="Probability: 1/52 for each card", font=("Arial", 12), bg='white')
        self.card_prob_label.pack()

        # Sample Space Label
        self.card_sample_space_label = tk.Label(self.card_frame, text="Sample Space: 52 Cards", font=("Arial", 12), bg='white')
        self.card_sample_space_label.pack()

        # Draw Button
        self.draw_button = tk.Button(self.card_frame, text="Draw Card", command=self.draw_card, font=("Arial", 12), bg='lightyellow')
        self.draw_button.pack(pady=5)

        # Result Label
        self.card_result_label = tk.Label(self.card_frame, text="", font=("Arial", 14), bg='white')
        self.card_result_label.pack()

        # Event Space Label (Suit)
        self.card_event_space_label = tk.Label(self.card_frame, text="", font=("Arial", 12), bg='white')
        self.card_event_space_label.pack()

        # Card Image Label
        self.card_image_label = tk.Label(self.card_frame, bg='white')
        self.card_image_label.pack()

    def flip_coin(self):
        """
        Simulate flipping a coin with an animation and display the result.
        """
        self.coin_animation_frames = 10  # Number of frames in the animation
        self.coin_animation_counter = 0
        self.animate_coin_flip()

    def animate_coin_flip(self):
        """
        Animate the coin flip by alternating images before displaying the final result.
        """
        if self.coin_animation_counter < self.coin_animation_frames:
            result = random.choice(['Heads', 'Tails'])
            self.coin_result_label.config(text=f"Flipping...")
            try:
                image = Image.open(f"images/coin_{result.lower()}.png")
                image = image.resize((100, 100), Image.LANCZOS)
                self.coin_image = ImageTk.PhotoImage(image)
                self.coin_image_label.config(image=self.coin_image)
            except Exception as e:
                messagebox.showerror("Image Error", f"Could not load coin image: {e}")
                return
            self.coin_animation_counter += 1
            # Call this method again after a short delay
            self.master.after(100, self.animate_coin_flip)
        else:
            # Final result
            result = random.choice(['Heads', 'Tails'])
            self.coin_result_label.config(text=f"Result: {result}")
            self.coin_event_space_label.config(text=f"Event Space: {result}")
            try:
                image = Image.open(f"images/coin_{result.lower()}.png")
                image = image.resize((100, 100), Image.LANCZOS)
                self.coin_image = ImageTk.PhotoImage(image)
                self.coin_image_label.config(image=self.coin_image)
            except Exception as e:
                messagebox.showerror("Image Error", f"Could not load coin image: {e}")

    def roll_die(self):
        """
        Simulate rolling a die with an animation and display the result.
        """
        self.die_animation_frames = 10
        self.die_animation_counter = 0
        self.animate_die_roll()

    def animate_die_roll(self):
        """
        Animate the die roll by cycling through die faces before displaying the final result.
        """
        if self.die_animation_counter < self.die_animation_frames:
            result = random.randint(1, 6)
            self.die_result_label.config(text=f"Rolling...")
            try:
                image = Image.open(f"images/die_{result}.png")
                image = image.resize((100, 100), Image.LANCZOS)
                self.die_image = ImageTk.PhotoImage(image)
                self.die_image_label.config(image=self.die_image)
            except Exception as e:
                messagebox.showerror("Image Error", f"Could not load die image: {e}")
                return
            self.die_animation_counter += 1
            # Call this method again after a short delay
            self.master.after(100, self.animate_die_roll)
        else:
            # Final result
            result = random.randint(1, 6)
            self.die_result_label.config(text=f"Result: {result}")
            event_space = 'Even' if result % 2 == 0 else 'Odd'
            self.die_event_space_label.config(text=f"Event Space: {event_space}")
            try:
                image = Image.open(f"images/die_{result}.png")
                image = image.resize((100, 100), Image.LANCZOS)
                self.die_image = ImageTk.PhotoImage(image)
                self.die_image_label.config(image=self.die_image)
            except Exception as e:
                messagebox.showerror("Image Error", f"Could not load die image: {e}")

    def draw_card(self):
        """
        Simulate drawing a card from a deck and display the result.
        """
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Ace'] + [str(n) for n in range(2, 11)] + ['Jack', 'Queen', 'King']
        suit = random.choice(suits)
        rank = random.choice(ranks)
        result = f"{rank} of {suit}"
        self.card_result_label.config(text=f"Result: {result}")
        self.card_event_space_label.config(text=f"Event Space: {suit}")

        # Load the corresponding image
        try:
            # For image filenames, we assume they are named like 'ace_of_hearts.png', etc.
            image_name = f"{rank.lower()}_of_{suit.lower()}.png"
            image = Image.open(f"images/cards/{image_name}")
            image = image.resize((100, 150), Image.LANCZOS)
            self.card_image = ImageTk.PhotoImage(image)
            self.card_image_label.config(image=self.card_image)
        except Exception as e:
            messagebox.showerror("Image Error", f"Could not load card image: {e}")

    def reset(self):
        """
        Reset the results and images.
        """
        self.coin_result_label.config(text="")
        self.coin_image_label.config(image='')
        self.coin_event_space_label.config(text="")
        self.die_result_label.config(text="")
        self.die_image_label.config(image='')
        self.die_event_space_label.config(text="")
        self.card_result_label.config(text="")
        self.card_image_label.config(image='')
        self.card_event_space_label.config(text="")

def main():
    root = tk.Tk()
    app = ProbabilitySimulatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()