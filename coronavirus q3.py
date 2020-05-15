import pandas as pd
import matplotlib.pyplot as plt


def bar(f):
    plt.figure(figsize = (10,5))
    plt.bar(f['Date'],f['No of Deaths'])
          #set label
    plt.ylabel('No of Deaths')
    plt.xlabel('Date')
    plt.title('Daily covid 19 deaths in '+ k, fontweight = 'bold')
    plt.show()
print("Time data for no of confirmed death cases of different countries") 
print("For India click 1")   
print("For UK click 2")
print("For USA click 3")
print("For Italy click 4")
print("For Germany click 5")
n=int(input("click the desired country"))
if(n==1):
    k="India"
elif(n==2):
    k="UK"
elif(n==3):
    k="USA"
elif(n==4):
    k="Italy"
elif(n==5):
    k="Germany"
df = pd.read_excel ('C:\\Users\\91787\\OneDrive\\Desktop\\my programs\\python\\Hackathon_Cornavirus\\daily deaths in covid 19.xlsx',k)
print (df)    
bar(df)    
