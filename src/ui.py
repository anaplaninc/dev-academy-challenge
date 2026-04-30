import tkinter as tk
from tkinter import ttk

from player import Player


class MainUI:
    def __init__(self, root):
        self.main = root
        self.main.geometry("200x200")
        self.p1 = Player("P1")
        self.p2 = Player("P2")
        self.turn = self.p1
        self.main_menu()

    def main_menu(self):
        """ Inits the main menu"""
        for i in self.main.winfo_children():
            i.destroy()
        frame = tk.Frame(self.main, width=300, height=300)
        frame.pack()
        start_game_btn = ttk.Button(
            frame, text="Start Game", command=self.init_game)
        start_game_btn.pack()

    def init_game(self):
        """ Initialises the game """
        for i in self.main.winfo_children():
            i.destroy()

        frame = tk.Frame(self.main, width=300, height=300)
        frame.pack()

        p1_score = ttk.Label(frame, text=f"P1's Score:{self.p1.held_score}")
        p1_score.pack()

        self.p2_score = ttk.Label(
            frame, text=f"P2's Score:{self.p2.held_score}")
        self.p2_score.pack()

        self.turn_txt = ttk.Label(frame, text=f"{self.turn.name}'s turn.")
        self.turn_txt.pack()

        self.current_held = ttk.Label(
            frame, text=f"Current held value: {self.turn.held_score}")
        self.current_held.pack()

        self.roll_btn = ttk.Button(
            frame, text="Roll", command=self.handle_roll)
        self.roll_btn.pack()

        self.hold_btn = ttk.Button(
            frame, text="Hold", state='disabled', command=self.handle_hold
        )
        self.hold_btn.pack()

    def handle_roll(self):
        """ Uses player class to roll dice"""
        val = self.turn.roll()
        if val == 1:
            self.switch_turn
        self.hold_btn.config(state='active')

    def handle_hold(self):
        """ Hold the dice score """
        self.turn.hold()

        self.switch_turn()

    def switch_turn(self):
        if self.turn == self.p1:
            self.turn = self.p2
        else:
            self.turn = self.p1


if __name__ == "__main__":
    root = tk.Tk()
    ui = MainUI(root)
    root.mainloop()
