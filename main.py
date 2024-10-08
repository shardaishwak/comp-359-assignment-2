import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Welcome Page")
root.geometry("600x500")  # Set window size for better layout

def show_image_page():
    welcome_frame.pack_forget()  # Hide the welcome frame
    image_frame.pack(fill="both", expand=True)  # Show the image frame

welcome_frame = tk.Frame(root)
welcome_frame.pack(fill="both", expand=True)

welcome_label = tk.Label(welcome_frame, text="Welcome to the Image Gallery!", font=("Helvetica", 20))
welcome_label.pack(pady=50)

start_button = tk.Button(welcome_frame, text="Start", font=("Helvetica", 14), command=show_image_page)
start_button.pack(pady=20)

image_frame = tk.Frame(root)

image_paths = [
    "image.png", "image.png", "image.png",
    "image.png", "image.png", "image.png"
]

selected = None

def onSelect(option: int) -> None:
    global selected
    selected = option
    print(f"Selected option: {option}")
    root.quit()

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

root.mainloop()
