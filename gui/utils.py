import tkinter as tk

def show_frame(frame, hide=False):
    """Show or hide a frame."""
    if hide:
        frame.pack_forget()
    else:
        frame.pack(fill="both", expand=True)

def create_welcome_frame(root):
    """Create and return a welcome frame with a title and description."""
    welcome_frame = tk.Frame(root)
    welcome_frame.pack(expand=True, fill='both')

    title_label = tk.Label(
        welcome_frame,
        text="Welcome to the Color Matching Application!",
        font=("Helvetica", 24, "bold")
    )
    title_label.pack(pady=(50, 20))

    description_text = (
        "Our application takes the colors and the map you select "
        "and creates a color matching where each state has a different "
        "color than its neighbors."
    )
    description_label = tk.Label(
        welcome_frame,
        text=description_text,
        font=("Helvetica", 14),
        wraplength=600,
        justify='center'
    )
    description_label.pack(pady=(0, 50))

    return welcome_frame
