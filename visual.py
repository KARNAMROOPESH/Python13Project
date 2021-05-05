import pandas as pd 
import plotly.figure_factory as pf 
import statistics

data = pd.read_csv('./StudentsPerformance.csv')

# "math score","reading score","writing score"

math = data['math score'].tolist()
mean = statistics.mean(math)
median = statistics.median(math)
mode = statistics.mode(math)
stan = statistics.stdev(math)


# caluculating percentage of data in the first mean range
math1 = []
lowermean1 = mean-stan
uppermean1 = mean+stan
for i in math:
    if(i > lowermean1 and i < uppermean1):
        math1.append(i)
percentage = (len(math1)/len(math))*100 

# caluculating percentage of data in the second mean range
math2 = []
lowermean2 = mean-(2*stan)
uppermean2 = mean+(2*stan)
for i in math:
    if(i > lowermean2 and i < uppermean2):
        math2.append(i)
percentage2 = (len(math2)/len(math))*100 

# caluculating percentage of data in the third mean range
math3 = []
lowermean3 = mean-(3*stan)
uppermean3 = mean+(3*stan)
for i in math:
    if(i > lowermean3 and i < uppermean3):
        math3.append(i)
percentage3 = (len(math3)/len(math))*100 

print(mean)
print(mode)
print(median)
print(stan)
print( percentage)
print( percentage2)
print( percentage3)

fig = pf.create_distplot([math] , ["Math Marks"] , show_hist=False )
fig.show()

