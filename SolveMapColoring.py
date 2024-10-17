import tkinter as tk
from gui.image_selector import show_image_page
from gui.utils import create_welcome_frame, show_frame


country_choice = "Germany" #Replace with coutnry chosen
#Adjacency list
if country_choice == "Germany":
    neighbors = {
        "Schleswig-Holstein": ["Hamburg", "Mecklenburg-Vorpommern", "Niedersachsen"],
        "Hamburg": ["Schleswig-Holstein", "Niedersachsen"],
        "Mecklenburg-Vorpommern": ["Brandenburg", "Sachsen-Anhalt", "Niedersachsen"],
        "Bremen": ["Niedersachsen"],
        "Nordrhein-Westfalen": ["Niedersachsen", "Hessen", "Rheinland-Pfalz"],
        "Brandenburg": ["Berlin", "Mecklenburg-Vorpommern", "Sachsen-Anhalt", "Sachsen", "Niedersachsen"],
        "Hessen": ["Nordrhein-Westfalen", "Rheinland-Pfalz", "Baden-Württemberg", "Bayern", "Thüringen", "Niedersachsen"],
        "Rheinland-Pfalz": ["Saarland", "Hessen", "Nordrhein-Westfalen", "Baden-Württemberg"],
        "Bayern": ["Baden-Württemberg", "Hessen", "Thüringen", "Sachsen"],
        "Saarland": ["Rheinland-Pfalz"],
        "Thüringen": ["Hessen", "Bayern", "Sachsen", "Sachsen-Anhalt", "Niedersachsen"],
        "Sachsen": ["Brandenburg", "Sachsen-Anhalt", "Thüringen", "Bayern"],
        "Niedersachsen": ["Bremen", "Hamburg", "Schleswig-Holstein", "Sachsen-Anhalt", "Thüringen",
                          "Hessen", "Nordrhein-Westfalen", "Mecklenburg-Vorpommern", "Brandenburg"],
        "Baden-Württemberg": ["Bayern", "Hessen", "Rheinland-Pfalz"],
        "Berlin": ["Brandenburg"]
    }  # German neighbors dictionary
    states = {
        "Schleswig-Holstein": None,
        "Hamburg": None,
        "Mecklenburg-Vorpommern": None,
        "Bremen": None,
        "Nordrhein-Westfalen": None,
        "Brandenburg": None,
        "Hessen": None,
        "Rheinland-Pfalz": None,
        "Bayern": None,
        "Saarland": None,
        "Thüringen": None,
        "Sachsen": None,
        "Niedersachsen": None,
        "Baden-Württemberg": None,
        "Berlin": None,
        "Sachsen-Anhalt": None
    }  # German states dictionary
elif country_choice == "France":
    neighbors = {
        "Hauts-de-France": ["Normandie", "Île-de-France", "Grand Est"],
        "Normandie": ["Hauts-de-France", "Île-de-France", "Centre-Val de Loire", "Bretagne","Pays de la Loire"],
        "Île-de-France": ["Hauts-de-France", "Normandie", "Centre-Val de Loire", "Bourgogne-Franche-Comté", "Grand Est"],
        "Grand Est": ["Hauts-de-France", "Île-de-France", "Bourgogne-Franche-Comté"],
        "Bretagne": ["Normandie", "Pays de la Loire"],
        "Pays de la Loire": ["Bretagne", "Normandie", "Centre-Val de Loire", "Nouvelle-Aquitaine"],
        "Centre-Val de Loire": ["Normandie", "Île-de-France", "Bourgogne-Franche-Comté", "Auvergne-Rhône-Alpes",
                                "Nouvelle-Aquitaine", "Pays de la Loire"],
        "Bourgogne-Franche-Comté": ["Île-de-France", "Centre-Val de Loire", "Auvergne-Rhône-Alpes", "Grand Est"],
        "Auvergne-Rhône-Alpes": ["Centre-Val de Loire", "Bourgogne-Franche-Comté",
                                 "Provence-Alpes-Côte d'Azur", "Occitanie", "Nouvelle-Aquitaine"],
        "Nouvelle-Aquitaine": ["Pays de la Loire", "Centre-Val de Loire", "Auvergne-Rhône-Alpes", "Occitanie"],
        "Occitanie": ["Nouvelle-Aquitaine", "Auvergne-Rhône-Alpes", "Provence-Alpes-Côte d'Azur"],
        "Provence-Alpes-Côte d'Azur": ["Auvergne-Rhône-Alpes", "Occitanie"],
        "Corse": []  # Corse is an island and does not border any other regions
    }

    states = {
        "Hauts-de-France": None,
        "Normandie": None,
        "Île-de-France": None,
        "Grand Est": None,
        "Bretagne": None,
        "Pays de la Loire": None,
        "Centre-Val de Loire": None,
        "Bourgogne-Franche-Comté": None,
        "Auvergne-Rhône-Alpes": None,
        "Nouvelle-Aquitaine": None,
        "Occitanie": None,
        "Provence-Alpes-Côte d'Azur": None,
        "Corse": None
    }

elif country_choice == "Rwanda":
    neighbors = {
        "Kigali City": ["Northern Province, Rwanda", "Southern Province, Rwanda", "East Province"],
        "East Province": ["Kigali City", "Northern Province, Rwanda", "Southern Province, Rwanda"],
        "Western Province, Rwanda": ["Southern Province, Rwanda", "Northern Province, Rwanda"],
        "Southern Province, Rwanda": ["Western Province, Rwanda", "Northern Province, Rwanda", "Kigali City",
                                      "East Province"],
        "Northern Province, Rwanda": ["Kigali City", "East Province", "Southern Province, Rwanda",
                                      "Western Province, Rwanda"]
    }  # Rwandan neighbors dictionary
    states = {
        "Kigali City": None,
        "East Province": None,
        "Western Province, Rwanda": None,
        "Southern Province, Rwanda": None,
        "Northern Province, Rwanda": None
    }  # Rwandan states dictionary
else:
    neighbors = {}
    states = {}

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
