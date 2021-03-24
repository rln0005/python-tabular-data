#!/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def get_unique_species():
    """ Get a non-duplicated list of the species in the dataframe.
    Dataframe (csv file) is scanned for the column labeled "species" and the function returns a list of the species contained in that column.

    Returns
    -------
    array : An array containing the full name of each species present in that column listed only once
    """
    species_array = dataframe.species.unique()
    return species_array

def get_regression_plots():
    """ Creates an individual scatterplot of petal length (cm) vs sepal length (cm) with fitted regression line for each species from get_unique_species.

    Returns
    -------
    png files labeled according to species name.png and "Generating a regression plot for {species}".
    """
    i = 0
    for i in range(0, len(get_unique_species())):
        df = dataframe[dataframe.species == species_list[i]]
        x = df.petal_length_cm
        y = df.sepal_length_cm
        regression = stats.linregress(x,y)
        slope = regression.slope
        intercept = regression.intercept
        plt.scatter(x, y, label=species_list[i])
        plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
        plt.xlabel("Petal length(cm)")
        plt.ylabel("Sepal length(cm)")
        plt.legend()
        plt.savefig(species_list[i] + ".png")
        plt.close()
        i += 1

if __name__ == '__main__':
    dataframe = pd.read_csv("iris.csv")
    species_list = get_unique_species()
    print("Generating a Regression plot for " + species_list)
    get_regression_plots()

