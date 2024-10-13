import tkinter as tk
from tkinter import colorchooser, messagebox
from PIL import ImageTk, Image

MAX_COLORS = 5
selected_colors = []

def choose_color():
    if len(selected_colors) >= MAX_COLORS:
        messagebox.showinfo("Limit Reached", f"You can only select up to {MAX_COLORS} colors.")
        return

    color = colorchooser.askcolor(title="Choose a color")[1]
    if color:
        if color not in selected_colors:
            selected_colors.append(color)
            display_selected_colors()
        else:
            messagebox.showwarning("Duplicate Color", "You've already selected this color.")
    else:
        messagebox.showinfo("Info", "No color was selected.")

    if selected_colors:
        next_button.config(state="normal")

def display_selected_colors():
    for widget in color_display_frame.winfo_children():
        widget.destroy() 

    for i, color in enumerate(selected_colors):
        color_label = tk.Label(color_display_frame, text=color, bg=color, font=("Helvetica", 14), width=10)
        color_label.grid(row=i // 3, column=i % 3, padx=10, pady=10)

def onSelect(option: int) -> None:
    global selected
    selected = option
    print(f"Selected option: {option}")
    image_frame.pack_forget() 
    show_color_picker() 

def show_color_picker():
    color_frame.pack(fill="both", expand=True)
    choose_color_button = tk.Button(color_frame, text="Pick a Color", command=choose_color)
    choose_color_button.pack(pady=20)

def on_next():
    color_frame.pack_forget() 
    result_frame.pack(fill="both", expand=True) 

    result_label = tk.Label(result_frame, text="[render the algorithm here]", font=("Helvetica", 20))
    result_label.pack(pady=50)

root = tk.Tk()
root.title("Image and Color Picker")
root.geometry("600x600") 

welcome_frame = tk.Frame(root)
welcome_frame.pack(fill="both", expand=True)

welcome_label = tk.Label(welcome_frame, text="Welcome to the Image Gallery!", font=("Helvetica", 20))
welcome_label.pack(pady=50)

start_button = tk.Button(welcome_frame, text="Start", font=("Helvetica", 14), command=lambda: show_image_page())
start_button.pack(pady=20)

def show_image_page():
    welcome_frame.pack_forget() 
    image_frame.pack(fill="both", expand=True) 

image_frame = tk.Frame(root)
image_paths = [
    "image.png", "image.png", "image.png",
    "image.png", "image.png", "image.png"
]

image_objects = []
for path in image_paths:
    img = Image.open(path)
    img = img.resize((150, 150))
    photo = ImageTk.PhotoImage(img)
    image_objects.append(photo)

for i, image in enumerate(image_objects):
    row = i // 3 * 2
    col = i % 3 
    
    image_label = tk.Label(image_frame, image=image)
    image_label.grid(row=row, column=col, padx=10, pady=5)

    button = tk.Button(image_frame, text=f"Button {i+1}", command=lambda i=i: onSelect(i+1))
    button.grid(row=row+1, column=col, pady=5)

color_frame = tk.Frame(root)

color_display_frame = tk.Frame(color_frame)
color_display_frame.pack(pady=20)

next_button = tk.Button(color_frame, text="Next", command=on_next, state="disabled")
next_button.pack(pady=20)

result_frame = tk.Frame(root)

root.mainloop()
