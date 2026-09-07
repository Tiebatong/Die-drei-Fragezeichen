import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

directory_path = r"C:\Users\Anwender\Documents\Obsidian Vault\Obsidian Vault\Die drei Fragezeichen\Folgen"

def main():

    property_name = "play_time: "
    times = get_property(property_name)
    times = list(map(int, times))
    print(times)
    vector = np.array(times)


    max_minuten = 120
    vector = vector[vector <= max_minuten]


    x = np.arange(len(vector))
    #plt.bar(x,vector)
    plt.scatter(x, vector, s=8)
    

    slope, intercept = np.polyfit(x, vector, 1)
    trend = slope * x + intercept
    plt.plot(x, trend, linewidth=1, color="red")

    ax = plt.gca()

    max_value = max(vector)

    ax.set_yticks(np.arange(0, max_value + 15, 15))
    ax.set_ylim(bottom=0)


    plt.annotate("Durchschnittliche Zunahme pro Folge = " + str(round(slope,2)) + " Minuten", xy=(0,85))

    plt.xlabel("Folgen Nummer")
    plt.ylabel("Folgen Länge in Minuten")
    plt.title("Folgen Dauer Verlauf")


    plt.savefig("plot.png", dpi=300, bbox_inches="tight")
    plt.show


def get_property(property_name):

    playtimes = []
    for f in os.scandir(directory_path):
        if f.is_file():
            with open(f.path, "r") as file:
                if contains_number(file.name):
                    file_contents = file.readlines()
                    for line in file_contents:
                        if line.startswith(property_name):
                            playtimes.append(line.split(property_name)[1].split("\n")[0]) # removes leading and trailing text

    return playtimes

def contains_number(string_to_check):
    return any(char.isdigit() for char in string_to_check)

main()