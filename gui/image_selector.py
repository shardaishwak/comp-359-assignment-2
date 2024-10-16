import tkinter as tk
from gui.color_picker import show_color_picker
from gui.utils import show_frame
from Country import CountryEnum, Country


# selected_country is passed down 3 functions, might be better to make it global?
def on_select_image(root, image_frame, selected_country: Country):
    """Handle the selection of an image."""
    print(f"Selected option: {selected_country.name}")
    show_frame(image_frame, hide=True)
    show_color_picker(root, selected_country)


def show_image_page(root, welcome_frame):
    """Show the image page."""
    show_frame(welcome_frame, hide=True)

    image_frame = tk.Frame(root)
    image_frame.pack(fill="both", expand=True)

    countryFactory = Country()

    for i, countryEnum in enumerate(CountryEnum):
        country: Country = countryFactory.build(countryEnum)
        row = i // 3 * 2
        col = i % 3

        image_label = tk.Label(image_frame, image=country.image)
        image_label.grid(row=row, column=col, padx=10, pady=5)
        button = tk.Button(
            image_frame,
            text=country.name,
            command=lambda i=i: on_select_image(root, image_frame, country),
        )
        button.grid(row=row + 1, column=col, pady=5)
