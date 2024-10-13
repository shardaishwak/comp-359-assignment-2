import tkinter as tk

def show_frame(frame, hide=False):
    """Show or hide a frame."""
    if hide:
        frame.pack_forget()
    else:
        frame.pack(fill="both", expand=True)

def create_welcome_frame(root):
    """Create a welcome frame."""
    welcome_frame = tk.Frame(root)
    
    welcome_label = tk.Label(welcome_frame, text="Welcome to the Image Gallery!", font=("Helvetica", 20))
    welcome_label.pack(pady=50)
    
    return welcome_frame
