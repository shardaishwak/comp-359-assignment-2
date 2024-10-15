import tkinter as tk
from PIL import ImageTk, Image
from gui.color_picker import show_color_picker
from gui.utils import show_frame


def on_select_image(root, image_frame, option: int):
    """Handle the selection of an image."""
    print(f"Selected option: {option}")
    show_frame(image_frame, hide=True)
    show_color_picker(root)


def show_image_page(root, welcome_frame):
    """Show the image page."""
    show_frame(welcome_frame, hide=True)

    image_frame = tk.Frame(root)
    image_frame.pack(fill="both", expand=True)

    image_paths = [
        "image.png",
        "image.png",
        "image.png",
        "image.png",
        "image.png",
        "image.png",
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

        button = tk.Button(
            image_frame,
            text=f"Button {i+1}",
            command=lambda i=i: on_select_image(root, image_frame, i + 1),
        )
        button.grid(row=row + 1, column=col, pady=5)
