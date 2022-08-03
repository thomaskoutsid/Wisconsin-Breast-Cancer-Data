'''
Thomas Koutsidis
7/29/22
Final Project, phase 3
This program analyzes the quality of the clustering from phase 2.
'''
import pandas as pd

def main():
    
    # uses the dataframe from phase 2
    df = pd.read_csv("/Users/thomaskoutsidis/Desktop/PYTHON/Final/phase2.csv")
    
    # these are three columns needed
    df = df[["Scn", "Class", "Predicted Class"]]
    
    # creating a variable for all points that are class 2 and 4
    class2 = df[df["Class"] == 2]
    class4 = df[df["Class"] == 4]
    
    # number of data points predicted as class 2, while the correct class is 4
    error_24 = class4[class4["Predicted Class"] == 2]
    # number of data pointed predicted as class 4, while the correct class is 2
    error_42 = class2[class2["Predicted Class"] == 4]
    # number of data points with predicted class not equal to correct class
    error_all = len(error_24) + len(error_42)
    # number of data points with predicted class equal to 2
    pclass_2 = len(df[df["Predicted Class"] == 2])
    # number of data points with predicted class equal to 4
    pclass_4 = len(df[df["Predicted Class"] == 4])
    # number of data points
    class_all = len(df)
    # error rate of the benign cells
    error_B = (len(error_24) / pclass_2) * 100
    # error rate of the malign cells
    error_M = (len(error_42) / pclass_4) * 100
    # total error rate
    error_T = (error_all / class_all) * 100
    error_T = round(error_T, 1)
    
    print("\nTotal errors:", error_T, "%")
    
    # if the total error is less than 50
    if error_T < 50:
        print("\nData points in Predicted Class 2:", pclass_2)
        print("\nData points in Predicted Class 4:", pclass_4)
        print("\nError data points, Predicted Class 2:\n", error_24)
        print("\nError data points, Predicted Class 4:\n", error_42)
        print("\nNumber of all data points:", class_all)
        print("\nNumber of error points:", error_all)
        print("\nError rate for class 2:", round(error_B, 1), "%")
        print("Error rate for class 4:", round(error_M, 1), "%")
        print("Total error rate:", round(error_T, 1), "%")
   
    # if the total error is more than 50
    else:
    # re-defining variables based on else statement
        df["Predicted Class"] = df["Predicted Class"].replace([2,4], [4,2])
        error_24 = class4[class4["Predicted Class"] == 2]
        error_42 = class2[class2["Predicted Class"] == 4]
        error_all = len(error_24) + len(error_42)
        pclass_2 = len(df[df["Predicted Class"] == 2])
        pclass_4 = len(df[df["Predicted Class"] == 4])
        class_all = len(df)
        error_B = (len(error_24) / pclass_2) * 100
        error_M = (len(error_42) / pclass_4) * 100
        error_T = (error_all / class_all) * 100
        error_T = round(error_T, 1)
        
        print("Clusters are swapped!")
        print("Swapping Predicted Class")
        print("\nData points in Predicted Class 2:", pclass_2)
        print("\nData points in Predicted Class 4:", pclass_4)
        print("\nError data points, Predicted Class 2:\n", error_24)
        print("\nError data points, Predicted Class 4:\n", error_42)
        print("\nNumber of all data points:", class_all)
        print("\nNumber of error points:", error_all)
        print("\nError rate for class 2:", round(error_B, 1), "%")
        print("Error rate for class 4:", round(error_M, 1), "%")
        print("Total error rate:", round(error_T, 1), "%")
    
    
main()
    
    
    
