import pandas as pd #importing library
import matplotlib.pyplot as plt #importing library
import numpy as np #importing library

dffullnames = pd.read_csv('DATA.csv') #importing csv file

ws=dffullnames.loc[:100,('Name','Nationality','Reactions','Aggression','Contract_Expiry','Rating', 'Finishing','Long_Shots','Club_Position','Freekick_Accuracy','Penalties','Stamina','Crossing','Shot_Power','Finishing','Index','Average')] #filtering csv file
wsx=ws[ws.Club_Position != 'GK']

#Displaying Index with the corresponding Player name
df1= dffullnames.loc[:100,('Name','Index')]
print(df1)

#best Goal Scorer
print("ANALYTICS ON BEST GOAL SCORER :")
x1= wsx['Average'].tolist()
for index, item in enumerate(x1):
    x1[index] = int(item)
a=wsx['Name'].tolist()
y=max(x1)
z=x1.index(y)
print ("The best Goal Scorer is"+" "+a[z])

#Analysis on field behaviour of players 
print("ANALYTICS ON ON-FIELD BEHAVIOUR OF PLAYERS :")
plt.scatter(x='Index', y='Average', data=ws) #index=player 
plt.xlabel('Players')
plt.ylabel('Average')
plt.title('Player vs On field Behaviour')
plt.show()
#Analysis on Aggression of Players
x=ws['Index'].tolist()
y=ws['Aggression'].tolist()
plt.plot(x,y) 
plt.xlabel('Players')
plt.ylabel('Aggerssion')
plt.title('Player vs Aggression')
plt.show()
#Analysis on Reactions of Players
x=ws['Index'].tolist()
y=ws['Reactions'].tolist()
plt.plot(x,y) 
plt.xlabel('Players')
plt.ylabel('Reactions')
plt.title('Player vs Reaction')
plt.show()

#Analysis on what attributes Real Madrid Prefers
print("ANALYTICS ON THE ATTRIBUTES PREFFERED BY REAL MADRID : ")
ws1=dffullnames[dffullnames['Club'] == 'Real Madrid']
a=ws1['Speed'].tolist()
b=ws1['Stamina'].tolist()
c=ws1['Agility'].tolist()
d=ws1['Balance'].tolist()
e=ws1['Strength'].tolist()
tot_mean=[np.mean(a),np.mean(b),np.mean(c),np.mean(d),np.mean(e)]
for index, item in enumerate(tot_mean):
    tot_mean[index] = int(item)
t=['Speed','Stamina','Agility','Balance','Strength']
max_mean=max(tot_mean)
z=tot_mean.index(max_mean)
plt.scatter(t,tot_mean)
plt.show()
print ("Real Madrid Prefers"+" "+t[z])

#Analysis on what attributes FC Barcelona Prefers
print("ANALYTICS ON THE ATTRIBUTES PREFFERED BY FC BARCELONA :")
ws1=dffullnames[dffullnames['Club'] == 'FC Barcelona']
a=ws1['Speed'].tolist()
b=ws1['Stamina'].tolist()
c=ws1['Agility'].tolist()
d=ws1['Balance'].tolist()
e=ws1['Strength'].tolist()
tot_mean=[np.mean(a),np.mean(b),np.mean(c),np.mean(d),np.mean(e)]
for index, item in enumerate(tot_mean):
    tot_mean[index] = int(item)
t=['Speed','Stamina','Agility','Balance','Strength']
max_mean=max(tot_mean)
z=tot_mean.index(max_mean)
plt.scatter(t,tot_mean)
plt.show()
print ("FC Barcelona Prefers"+" "+t[z])

#Analysis on Contract Period
print("ANALYTICS ON CONTRACT PERIOD :")
plt.scatter(x='Contract_Expiry', y='Index', data=ws)
plt.xlabel('Contract Period')
plt.ylabel('Players')
plt.title('Contract vs Players')
plt.show()

#Analytics of the best attribute of the players of a particular continent
print("ANALYTICS OF THE BEST ATTRIBUTE OF THE PLAYER OF A PARTICULAR CONTINENT :")
a=dffullnames.loc[:4500,('Nationality','Crossing','Attacking_Position','Vision','Marking','Dribbling')]
a['Nationality']=a['Nationality'].replace(['Spain','Germany','England','Croatia','Slovakia','Serbia','Bosnia Herzegovina','Wales','Ireland','France','Portugal','Belgium','Italy','Romania','Poland','Netherland','Turkey','Denmark','Switzerland','Austria','Sweden','Greece','Czech Republic','Scotland','Norway','Hungary','Northern Ireland','Finland','Bulgaria'],'Europe')
a['Nationality']=a['Nationality'].replace(['Brazil','Argentina','Uruguay','Chile','Colombia','Paraguay','Ecuador','Venezuela','Peru','Bolivia'],'South America')
a['Nationality']=a['Nationality'].replace(['Mexico','United States','Canada',],'North America')
a['Nationality']=a['Nationality'].replace(['India','China','Russia'],'Asia')
a['Nationality']=a['Nationality'].replace(['Egypt','South Africa','Algeria','Cameroon'],'Africa')
#for europe
ws1=a[a['Nationality'] == 'Europe']
x=ws1['Dribbling'].tolist()
b=ws1['Crossing'].tolist()
c=ws1['Attacking_Position'].tolist()
d=ws1['Vision'].tolist()
e=ws1['Marking'].tolist()
tot_mean=[np.mean(x),np.mean(b),np.mean(c),np.mean(d),np.mean(e)]
for index, item in enumerate(tot_mean):
    tot_mean[index] = int(item)
t=['Dribbling','Crossing','Attacking_Position','Vision','Marking']
max_mean=max(tot_mean)
z=tot_mean.index(max_mean)
plt.scatter(t,tot_mean)
plt.show()
print ("European Players are Better at"+" "+t[z])
#for South America
ws1=a[a['Nationality'] == 'South America']
x=ws1['Dribbling'].tolist()
b=ws1['Crossing'].tolist()
c=ws1['Attacking_Position'].tolist()
d=ws1['Vision'].tolist()
e=ws1['Marking'].tolist()
tot_mean=[np.mean(x),np.mean(b),np.mean(c),np.mean(d),np.mean(e)]
for index, item in enumerate(tot_mean):
    tot_mean[index] = int(item)
t=['Dribbling','Crossing','Attacking_Position','Vision','Marking']
max_mean=max(tot_mean)
z=tot_mean.index(max_mean)
plt.scatter(t,tot_mean)
plt.show()
print ("South American Players are Better at"+" "+t[z])
#for Aisa
ws1=a[a['Nationality'] == 'Asia']
#print(ws1)
x=ws1['Dribbling'].tolist()
b=ws1['Crossing'].tolist()
c=ws1['Attacking_Position'].tolist()
d=ws1['Vision'].tolist()
e=ws1['Marking'].tolist()
tot_mean=[np.mean(x),np.mean(b),np.mean(c),np.mean(d),np.mean(e)]
for index, item in enumerate(tot_mean):
    tot_mean[index] = int(item)
t=['Dribbling','Crossing','Attacking_Position','Vision','Marking']
max_mean=max(tot_mean)
z=tot_mean.index(max_mean)
plt.scatter(t,tot_mean)
plt.show()
print ("Asian Players are Better at"+" "+t[z])
#For Africa
ws1=a[a['Nationality'] == 'Africa']
x=ws1['Dribbling'].tolist()
b=ws1['Crossing'].tolist()
c=ws1['Attacking_Position'].tolist()
d=ws1['Vision'].tolist()
e=ws1['Marking'].tolist()
tot_mean=[np.mean(x),np.mean(b),np.mean(c),np.mean(d),np.mean(e)]
for index, item in enumerate(tot_mean):
    tot_mean[index] = int(item)
t=['Dribbling','Crossing','Attacking_Position','Vision','Marking']
max_mean=max(tot_mean)
z=tot_mean.index(max_mean)
plt.scatter(t,tot_mean)
plt.show()
print ("African Players are Better at"+" "+t[z])
# for North America
ws1=a[a['Nationality'] == 'North America']
x=ws1['Dribbling'].tolist()
b=ws1['Crossing'].tolist()
c=ws1['Attacking_Position'].tolist()
d=ws1['Vision'].tolist()
e=ws1['Marking'].tolist()
tot_mean=[np.mean(x),np.mean(b),np.mean(c),np.mean(d),np.mean(e)]
for index, item in enumerate(tot_mean):
    tot_mean[index] = int(item)
t=['Dribbling','Crossing','Attacking_Position','Vision','Marking']
max_mean=max(tot_mean)
z=tot_mean.index(max_mean)
plt.scatter(t,tot_mean)
plt.show()
print ("North American Players are Better at"+" "+t[z])

#Analysis on Rating Vs Player
print("ANALYTICS ON RATING VS PLAYER :")
x=ws['Rating'].tolist()
y=ws['Index'].tolist()
plt.plot(x,y)
plt.xlabel('Rating')
plt.ylabel('Players')
plt.title('Rating vs players')
plt.show()

#Analysis on Count of Players whose Contract Expiry is less than 2019
print("ANALYTICS ON COUNT OF PLAYERS WHOSE CONTRACT EXPIRY IS LESS THAN 2019 :")
x=dffullnames[dffullnames['Contract_Expiry']<=2019].Contract_Expiry.count()
print ("Count of Players whose Contract Expiry is less than 2019")
print (x)


