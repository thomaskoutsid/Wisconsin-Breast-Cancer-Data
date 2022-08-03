'''
Thomas Koutsidis
7/13/22
Final Project, phase 1
This program finds the attributes of breast cancer data and creates histograms.
'''


import matplotlib.pyplot as plt
import pandas as pd


def main():
    # download data and insert names of columns
    col = ["Scn", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "Class"]
    df = pd.read_csv('breast-cancer-wisconsin.data',
                     na_values = '?', names = col)      
    
    # mean imputation
    col_means = df["A7"].mean()
    df["A7"] = df["A7"].fillna(col_means)
  
    # printed results of attributes A2 to A10, rounded to 1 decimal place
    print("Attribute A2")
    print("------------")
    print("Mean:", "{:.1f}".format(df["A2"].mean()))
    print("Median:", "{:.1f}".format(df["A2"].median()))
    print("Variance:", "{:.1f}".format(df["A2"].var()))
    print("Standard Deviation:", "{:.1f}".format(df["A2"].std()))
    
    print("\nAttribute A3")
    print("------------")
    print("Mean:", "{:.1f}".format(df["A3"].mean()))
    print("Median:", "{:.1f}".format(df["A3"].median()))
    print("Variance:", "{:.1f}".format(df["A3"].var()))
    print("Standard Deviation:", "{:.1f}".format(df["A3"].std()))
    
    print("\nAttribute A4")
    print("------------")
    print("Mean:", "{:.1f}".format(df["A4"].mean()))
    print("Median:", "{:.1f}".format(df["A4"].median()))
    print("Variance:", "{:.1f}".format(df["A4"].var()))
    print("Standard Deviation:", "{:.1f}".format(df["A4"].std()))
    
    print("\nAttribute A5")
    print("------------")
    print("Mean:", "{:.1f}".format(df["A5"].mean()))
    print("Median:", "{:.1f}".format(df["A5"].median()))
    print("Variance:", "{:.1f}".format(df["A5"].var()))
    print("Standard Deviation:", "{:.1f}".format(df["A5"].std()))
    
    print("\nAttribute A6")
    print("------------")
    print("Mean:", "{:.1f}".format(df["A6"].mean()))
    print("Median:", "{:.1f}".format(df["A6"].median()))
    print("Variance:", "{:.1f}".format(df["A6"].var()))
    print("Standard Deviation:", "{:.1f}".format(df["A6"].std()))
    
    print("\nAttribute A7")
    print("------------")
    print("Mean:", "{:.1f}".format(df["A7"].mean()))
    print("Median:", "{:.1f}".format(df["A7"].median()))
    print("Variance:", "{:.1f}".format(df["A7"].var()))
    print("Standard Deviation:", "{:.1f}".format(df["A7"].std()))
    
    print("\nAttribute A8")
    print("------------")
    print("Mean:", "{:.1f}".format(df["A8"].mean()))
    print("Median:", "{:.1f}".format(df["A8"].median()))
    print("Variance:", "{:.1f}".format(df["A8"].var()))
    print("Standard Deviation:", "{:.1f}".format(df["A8"].std()))
    
    print("\nAttribute A9")
    print("------------")
    print("Mean:", "{:.1f}".format(df["A9"].mean()))
    print("Median:", "{:.1f}".format(df["A9"].median()))
    print("Variance:", "{:.1f}".format(df["A9"].var()))
    print("Standard Deviation:", "{:.1f}".format(df["A9"].std()))
    
    print("\nAttribute A10")
    print("-------------")
    print("Mean:", "{:.1f}".format(df["A10"].mean()))
    print("Median:", "{:.1f}".format(df["A10"].median()))
    print("Variance:", "{:.1f}".format(df["A10"].var()))
    print("Standard Deviation:", "{:.1f}".format(df["A10"].std()))
    
    # plotted histograms with 10 bins for attributes A2 to A10
    fig1 = plt.figure()
    a2plot = fig1.add_subplot(1, 1, 1)
    a2plot.hist(df["A2"], bins = 10, color = "blue", alpha = 0.5, edgecolor = "black")
    a2plot.set_xticks(range(11))
    a2plot.set_title("Histogram of attribute A2")
    a2plot.set_xlabel("Value of the attribute")
    a2plot.set_ylabel("Number of the data points")
    
    fig2 = plt.figure()
    a3plot = fig2.add_subplot(1, 1, 1)
    a3plot.hist(df["A3"], bins = 10, color = "blue", alpha = 0.5, edgecolor = "black")
    a3plot.set_xticks(range(11))
    a3plot.set_title("Histogram of attribute A3")
    a3plot.set_xlabel("Value of the attribute")
    a3plot.set_ylabel("Number of the data points")
    
    fig3 = plt.figure()
    a4plot = fig3.add_subplot(1, 1, 1)
    a4plot.hist(df["A4"], bins = 10, color = "blue", alpha = 0.5, edgecolor = "black")
    a4plot.set_xticks(range(11))
    a4plot.set_title("Histogram of attribute A4")
    a4plot.set_xlabel("Value of the attribute")
    a4plot.set_ylabel("Number of the data points")
    
    fig4 = plt.figure()
    a5plot = fig4.add_subplot(1, 1, 1)
    a5plot.hist(df["A5"], bins = 10, color = "blue", alpha = 0.5, edgecolor = "black")
    a5plot.set_xticks(range(11))
    a5plot.set_title("Histogram of attribute A5")
    a5plot.set_xlabel("Value of the attribute")
    a5plot.set_ylabel("Number of the data points")
    
    fig5 = plt.figure()
    a6plot = fig5.add_subplot(1, 1, 1)
    a6plot.hist(df["A6"], bins = 10, color = "blue", alpha = 0.5, edgecolor = "black")
    a6plot.set_xticks(range(11))
    a6plot.set_title("Histogram of attribute A6")
    a6plot.set_xlabel("Value of the attribute")
    a6plot.set_ylabel("Number of the data points")
    
    fig6 = plt.figure()
    a7plot = fig6.add_subplot(1, 1, 1)
    a7plot.hist(df["A7"], bins = 10, color = "blue", alpha = 0.5, edgecolor = "black")
    a7plot.set_xticks(range(11))
    a7plot.set_title("Histogram of attribute A7")
    a7plot.set_xlabel("Value of the attribute")
    a7plot.set_ylabel("Number of the data points")
    
    fig7 = plt.figure()
    a8plot = fig7.add_subplot(1, 1, 1)
    a8plot.hist(df["A8"], bins = 10, color = "blue", alpha = 0.5, edgecolor = "black")
    a8plot.set_xticks(range(11))
    a8plot.set_title("Histogram of attribute A8")
    a8plot.set_xlabel("Value of the attribute")
    a8plot.set_ylabel("Number of the data points")
    
    fig8 = plt.figure()
    a9plot = fig8.add_subplot(1, 1, 1)
    a9plot.hist(df["A9"], bins = 10, color = "blue", alpha = 0.5, edgecolor = "black")
    a9plot.set_xticks(range(11))
    a9plot.set_title("Histogram of attribute A9")
    a9plot.set_xlabel("Value of the attribute")
    a9plot.set_ylabel("Number of the data points")
    
    fig9 = plt.figure()
    a10plot = fig9.add_subplot(1, 1, 1)
    a10plot.hist(df["A10"], bins = 10, color = "blue", alpha = 0.5, edgecolor = "black")
    a10plot.set_xticks(range(11))
    a10plot.set_title("Histogram of attribute A10")
    a10plot.set_xlabel("Value of the attribute")
    a10plot.set_ylabel("Number of the data points")
    
    
   
main()