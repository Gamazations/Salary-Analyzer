#Imports libraries to be able to run operations easier.
import pandas as pd
import statistics as stat

#Writes the name of a file into a variable for easier calling if need be for the future
nameFile = 'employee - Sheet1.csv'
#Uses pandas dataframes to read the csv file into this variable
df = pd.read_csv(nameFile)
#Creates a new column called TotalPay by multiplying the values of HoursWorked and HourlyRate
df["TotalPay"] = df["HoursWorked"]*df["HourlyRate"]

#Creates a variable that represents the final version of the file for easier use if need be for future reference
nameFileFinal = 'Final Version - employee.csv'
#Writes the final output in a new final version of the file seperate from the original by referencing the variable, index=False prevents row numbers from being written
df.to_csv("nameFileFinal", index = False)

#Prints the final variable of which is the entire new file
print(df)

#Calculates the mean amount that the employees are paid
#Gets access to all the TotalPay values and puts them in a list
finalTotalPay = df["TotalPay"].tolist()
#Uses the statistics library to use the .mean() function to calculate the mean of the TotalPay values and stores it in a variable
meanOfPay = stat.mean(finalTotalPay)
#Prints this variable in a printed statement.
print("The average pay of the employees is", meanOfPay)
