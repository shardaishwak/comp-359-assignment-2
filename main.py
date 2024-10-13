import tkinter as tk
from image_selector import show_image_page
from gui_utils import create_welcome_frame, show_frame

def run():
    """Run the application."""
    root = tk.Tk()
    root.title("Image and Color Picker")
    root.geometry("600x600") 

    welcome_frame = create_welcome_frame(root)
    welcome_frame.pack(fill="both", expand=True)

    start_button = tk.Button(welcome_frame, text="Start", font=("Helvetica", 14), command=lambda: show_image_page(root, welcome_frame))
    start_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    run()
