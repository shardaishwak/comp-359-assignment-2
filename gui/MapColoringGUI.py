import geopandas as gpd
import matplotlib.pyplot as plt

from Country import CountryEnum


def ColorCountry(country_choice, states_colors):
    if country_choice == CountryEnum.GERMANY.value:
        country_states = gpd.read_file("path_to_german_states_geojson.json")
    elif country_choice == CountryEnum.FRANCE.value:
        country_states = gpd.read_file("path_to_france_states_geojson.json")
    elif country_choice == CountryEnum.RWANDA.value:
        country_states = gpd.read_file("path_to_rwanda_states_geojson.json")

    # Prepare the figure and axis
    fig, ax = plt.subplots(1, 1, figsize=(10, 12))

    # Plot each state with its corresponding color
    for state, color in states_colors.items():
        # print(len(country_states[country_states['name'].str.upper() == state.upper()]))
        country_states[country_states["name"].str.upper() == state.upper()].plot(
            ax=ax, color=color, edgecolor="black"
        )
    # Remove axis off
    ax.set_axis_off()
    plt.title(f"Map of {country_choice} with States")
    plt.show()
