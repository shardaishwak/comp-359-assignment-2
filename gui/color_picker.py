import tkinter as tk
from tkinter import colorchooser, messagebox
from gui.utils import show_frame

MAX_COLORS = 5
selected_colors = []


def choose_color(color_display_frame, next_button):
    """Choose a color."""
    if len(selected_colors) >= MAX_COLORS:
        messagebox.showinfo(
            "Limit Reached", f"You can only select up to {MAX_COLORS} colors."
        )
        return

    color = colorchooser.askcolor(title="Choose a color")[1]
    if color:
        if color not in selected_colors:
            selected_colors.append(color)
            display_selected_colors(color_display_frame)
        else:
            messagebox.showwarning(
                "Duplicate Color", "You've already selected this color."
            )
    else:
        messagebox.showinfo("Info", "No color was selected.")

    if selected_colors:
        next_button.config(state="normal")


def display_selected_colors(color_display_frame):
    """Display the selected colors."""
    for widget in color_display_frame.winfo_children():
        widget.destroy()

    for i, color in enumerate(selected_colors):
        color_label = tk.Label(
            color_display_frame, text=color, bg=color, font=("Helvetica", 14), width=10
        )
        color_label.grid(row=i // 3, column=i % 3, padx=10, pady=10)


def show_color_picker(root):
    """Show the color picker."""
    color_frame = tk.Frame(root)
    color_frame.pack(fill="both", expand=True)

    color_display_frame = tk.Frame(color_frame)
    color_display_frame.pack(pady=20)

    choose_color_button = tk.Button(
        color_frame,
        text="Pick a Color",
        command=lambda: choose_color(color_display_frame, next_button),
    )
    choose_color_button.pack(pady=20)

    next_button = tk.Button(
        color_frame,
        text="Next",
        state="disabled",
        command=lambda: show_next_step(root, color_frame),
    )
    next_button.pack(pady=20)


def show_next_step(root, color_frame):
    """Show the next step."""
    show_frame(color_frame, hide=True)
    result_frame = tk.Frame(root)
    result_frame.pack(fill="both", expand=True)

    ## TODO: Continue for here in rendering the AC3 algorithm
    result_label = tk.Label(
        result_frame, text="[render the algorithm here]", font=("Helvetica", 20)
    )
    result_label.pack(pady=50)
