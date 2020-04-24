# Problem stament one:Identity the countries as HIGH RISK TRAVEL destination countries for Internship or Project work for next two years.
import xlrd
import os
import matplotlib.pyplot as plt 
def risk(country_cases,country_death):
    print("Current Covid19 case :",country_cases[-1])
    print("Total death till now :",country_death[-1])
    death_ratio=(country_death[-1]/country_cases[-1])*100
    print("death per case :",death_ratio)
    if(death_ratio >=2):
        print("The Country is in High risk")
    else:
        print("Country is till now safe")
def deathgraph(date,country_death,country):
    country_death.pop(0)
    plt.figure(figsize=(80,20))
    plt.plot(date, country_death) 
    plt.xlabel('Dates')
    plt.ylabel('Deaths')
    plt.title(country)
    plt.show()
print("   Hello Everyone  ")
os.chdir("C:\\Users\\91787\\OneDrive\\Desktop\\my programs\\python\\Hackathon_Cornavirus")
book1 = xlrd.open_workbook("C:\\Users\\91787\\OneDrive\\Desktop\\my programs\\python\\Hackathon_Cornavirus\\covidcase.xlsx")
Totalcase=book1.sheet_by_index(0)
book2 = xlrd.open_workbook("C:\\Users\\91787\\OneDrive\\Desktop\\my programs\\python\\Hackathon_Cornavirus\\coviddeath.xlsx")
Totaldeath=book2.sheet_by_index(0)
date= list(Totalcase.row_values(0))
date.pop(0)
print("Enter the country which you are inrested for internship :")
country=input()
countries=list(Totalcase.col_values(0))
i=0
for a in countries:
    if(a==country):
        break
    i=i+1
country_cases=list(Totalcase.row_values(i))
country_death=list(Totaldeath.row_values(i))
risk(country_cases,country_death)
print("Graph showing death rate :")
deathgraph(date,country_death,country)
print("------Stay Home And Stay Safe------")