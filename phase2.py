'''
Thomas Koutsidis
07/24/22
Final Project, phase 2
This program uses the dataset with imputed missing values from phase 1 and uses columns A2 to A10 for k-means computation.
'''
import pandas as pd
import numpy as np
import math
import random

# created a function to measure the distance
def distance(centroid, point):
    
    distance = math.sqrt(sum([(x - y)**2 for x, y in zip(centroid, point)]))
    return distance
    
    
def main():
    # download data and insert names of columns
    col = ["Scn", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "Class"]
    df = pd.read_csv('breast-cancer-wisconsin.data',
                     na_values = '?', names = col)      
    
    # mean imputation
    col_means = df["A7"].mean()
    df["A7"] = df["A7"].fillna(col_means)
    
    #get shape and location
    n = df.iloc[:, 1:10].astype("float64")
    rows = n.shape[0]
    
    # get two random rows for mu_2 and mu_4
    d1 = random.randint(1, 699)
    d2 = random.randint(1, 699)
    mu_2 = df.loc[d1, "A2":"A10"]
    mu_4 = df.loc[d2, "A2":"A10"]
    
    # print initial centroids
    print("\nRandomly selected row", d1, "for centroid mu_2.\n")
    print("Initial centroid mu_2:")
    print(mu_2, "\n")
    print("Randomly selected row", d2, "for centroid mu_4.\n")
    print("Initial centroid mu_4:")
    print(mu_4)
     
    # create new column for predicted clusters
    df["Predicted Class"] = ''
    
    # set iteration to 0
    iterations = 0
    
    # loop for steps b and c
    for i in range(10):
        iterations += 1
        for i in range(rows):
            mu_2_distance = distance(mu_2, n.iloc[i])
            mu_4_distance = distance(mu_4, n.iloc[i])  
            
            if mu_2_distance > mu_4_distance:
                n.at[i, "Predicted Class"] = 4
            else:
                n.at[i, "Predicted Class"] = 2
        
        i2 = n[n["Predicted Class"] == 2].index
        i4 = n[n["Predicted Class"] == 4].index
        
        mean_2 = np.mean(n.iloc[i2, :9])
        mean_4 = np.mean(n.iloc[i4, :9])
        
        if mean_2.equals(mu_2) and mean_4.equals(mu_4):
            break
        
        mu_2 = mean_2
        mu_4 = mean_4
        
    print("\nProgram ended after", iterations, "iterations.")
    
    # print final centroids
    print("\nFinal centroid mu_2:")
    for i in range(len(mu_2)):
        print(col[i + 1], " ", mu_2[i])
    print("\nFinal centroid mu_4:")
    for i in range(len(mu_4)):
        print(col[i + 1], " ", mu_4[i])
        
    # print final cluster assignment
    print("\nFinal Cluster Assignment:")
    df["Predicted Class"] = n["Predicted Class"].astype("int")
    print(df[["Scn", "Class", "Predicted Class"]].head(20))
    
    df.to_csv(r"/Users/thomaskoutsidis/Desktop/PYTHON/Final/phase2.csv", index = False)


main()