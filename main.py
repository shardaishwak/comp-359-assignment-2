import tkinter as tk
from PIL import ImageTk, Image  # Pillow library to handle image formats like PNG/JPEG

# Initialize the main window
root = tk.Tk()
root.title("Image with Button")

# Load the image (Make sure Pillow is installed with `pip install pillow`)
img = Image.open("image.png")  # Replace with your image file path
img = img.resize((300, 300))  # Resize if necessary
photo = ImageTk.PhotoImage(img)

# Create a label to display the image
image_label = tk.Label(root, image=photo)
image_label.pack(pady=10)

# Create a button below the image
button = tk.Button(root, text="Click Me!", command=lambda: print("Button clicked"))
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
