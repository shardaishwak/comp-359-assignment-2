from enum import Enum
from PIL import ImageTk, Image


class CountryEnum(Enum):
    GERMANY = "Germany"
    FRANCE = "France"
    RWANDA = "Rwanda"


# Factory/builder?? Either way, makes it easier to add countries
class CountryFactory:
    def build(self, country: CountryEnum):
        build_country = Country()

        build_country.name = country.value
        build_country.states = countries[country]["states"]
        build_country.neighbors = countries[country]["neighbors"]
        build_country.image = self.__init_image(countries[country]["image_path"])

        return build_country

    def __init_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((150, 150))
        photo = ImageTk.PhotoImage(img)
        return photo


# Need to create a new object everytime
class Country:
    def __init__(self) -> None:
        self.name = ""
        self.states = {}
        self.neighbors = {}
        self.image = None


# TODO: ADD IMAGE PATHS TO COUNTRIES

countries = {
    CountryEnum.GERMANY: {
        "image_path": "./image.png",
        "states": {
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
            "Sachsen-Anhalt": None,
        },  # German states dictionary
        "neighbors": {
            "Schleswig-Holstein": [
                "Hamburg",
                "Mecklenburg-Vorpommern",
                "Niedersachsen",
            ],
            "Hamburg": ["Schleswig-Holstein", "Niedersachsen"],
            "Mecklenburg-Vorpommern": [
                "Brandenburg",
                "Sachsen-Anhalt",
                "Niedersachsen",
            ],
            "Bremen": ["Niedersachsen"],
            "Nordrhein-Westfalen": ["Niedersachsen", "Hessen", "Rheinland-Pfalz"],
            "Brandenburg": [
                "Berlin",
                "Mecklenburg-Vorpommern",
                "Sachsen-Anhalt",
                "Sachsen",
                "Niedersachsen",
            ],
            "Hessen": [
                "Nordrhein-Westfalen",
                "Rheinland-Pfalz",
                "Baden-Württemberg",
                "Bayern",
                "Thüringen",
                "Niedersachsen",
            ],
            "Rheinland-Pfalz": [
                "Saarland",
                "Hessen",
                "Nordrhein-Westfalen",
                "Baden-Württemberg",
            ],
            "Bayern": ["Baden-Württemberg", "Hessen", "Thüringen", "Sachsen"],
            "Saarland": ["Rheinland-Pfalz"],
            "Thüringen": [
                "Hessen",
                "Bayern",
                "Sachsen",
                "Sachsen-Anhalt",
                "Niedersachsen",
            ],
            "Sachsen": ["Brandenburg", "Sachsen-Anhalt", "Thüringen", "Bayern"],
            "Niedersachsen": [
                "Bremen",
                "Hamburg",
                "Schleswig-Holstein",
                "Sachsen-Anhalt",
                "Thüringen",
                "Hessen",
                "Nordrhein-Westfalen",
                "Mecklenburg-Vorpommern",
                "Brandenburg",
            ],
            "Baden-Württemberg": ["Bayern", "Hessen", "Rheinland-Pfalz"],
            "Berlin": ["Brandenburg"],
        },  # German neighbors dictionary
    },
    CountryEnum.FRANCE: {
        "image_path": "./image.png",
        "states": {
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
            "Corse": None,
        },
        "neighbors": {
            "Hauts-de-France": ["Normandie", "Île-de-France", "Grand Est"],
            "Normandie": [
                "Hauts-de-France",
                "Île-de-France",
                "Centre-Val de Loire",
                "Bretagne",
                "Pays de la Loire",
            ],
            "Île-de-France": [
                "Hauts-de-France",
                "Normandie",
                "Centre-Val de Loire",
                "Bourgogne-Franche-Comté",
                "Grand Est",
            ],
            "Grand Est": [
                "Hauts-de-France",
                "Île-de-France",
                "Bourgogne-Franche-Comté",
            ],
            "Bretagne": ["Normandie", "Pays de la Loire"],
            "Pays de la Loire": [
                "Bretagne",
                "Normandie",
                "Centre-Val de Loire",
                "Nouvelle-Aquitaine",
            ],
            "Centre-Val de Loire": [
                "Normandie",
                "Île-de-France",
                "Bourgogne-Franche-Comté",
                "Auvergne-Rhône-Alpes",
                "Nouvelle-Aquitaine",
                "Pays de la Loire",
            ],
            "Bourgogne-Franche-Comté": [
                "Île-de-France",
                "Centre-Val de Loire",
                "Auvergne-Rhône-Alpes",
                "Grand Est",
            ],
            "Auvergne-Rhône-Alpes": [
                "Centre-Val de Loire",
                "Bourgogne-Franche-Comté",
                "Provence-Alpes-Côte d'Azur",
                "Occitanie",
                "Nouvelle-Aquitaine",
            ],
            "Nouvelle-Aquitaine": [
                "Pays de la Loire",
                "Centre-Val de Loire",
                "Auvergne-Rhône-Alpes",
                "Occitanie",
            ],
            "Occitanie": [
                "Nouvelle-Aquitaine",
                "Auvergne-Rhône-Alpes",
                "Provence-Alpes-Côte d'Azur",
            ],
            "Provence-Alpes-Côte d'Azur": ["Auvergne-Rhône-Alpes", "Occitanie"],
            "Corse": [],  # Corse is an island and does not border any other regions
        },
    },
    CountryEnum.RWANDA: {
        "image_path": "./image.png",
        "neighbors": {
            "Kigali City": [
                "Northern Province, Rwanda",
                "Southern Province, Rwanda",
                "East Province",
            ],
            "East Province": [
                "Kigali City",
                "Northern Province, Rwanda",
                "Southern Province, Rwanda",
            ],
            "Western Province, Rwanda": [
                "Southern Province, Rwanda",
                "Northern Province, Rwanda",
            ],
            "Southern Province, Rwanda": [
                "Western Province, Rwanda",
                "Northern Province, Rwanda",
                "Kigali City",
                "East Province",
            ],
            "Northern Province, Rwanda": [
                "Kigali City",
                "East Province",
                "Southern Province, Rwanda",
                "Western Province, Rwanda",
            ],
        },  # Rwandan neighbors dictionary
        "states": {
            "Kigali City": None,
            "East Province": None,
            "Western Province, Rwanda": None,
            "Southern Province, Rwanda": None,
            "Northern Province, Rwanda": None,
        },  # Rwandan states dictionary
    },
}
