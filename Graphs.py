import matplotlib.pyplot as plt
import numpy as np



#plot 1
#xpoints = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ypoints = np.array([1, 2, 4, 6, 9, 12, 14, 15, 16, 0, 0, 1, 2, 3, 5, 1, 0])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.subplot(2,2,1)
plt.plot(ypoints, marker = 'D', linestyle = 'dashed')

plt.title("Groepsdynamica", fontdict = font1, loc = "left")
plt.xlabel("Tijd in dit project", fontdict = font2)
plt.ylabel("Onze Motivatie", fontdict = font2)

#plot 2
xpoints = np.array([10, 20, 30, 45, 60, 12, 45, 62, 97, 12, 53, 1, 5, 90, 6, 12, 67])
ypoints = np.array([12, 96, 34, 65, 23, 64, 76, 76, 83, 54, 9, 8, 2, 67, 110, 100, 34])
sizes = np.array([20, 50, 100, 200, 500, 10, 60, 90, 10, 300, 600, 800, 75, 50, 125, 125, 90])

font1 = {'family':'serif','color':'grey','size':18}
font2 = {'family':'serif','color':'black','size':25}

plt.subplot(2,2,2)
plt.scatter(xpoints, ypoints, s=sizes)

plt.title("Iets", fontdict = font1, loc = "left")
plt.xlabel("Geld of tijd, IDK", fontdict = font2)
plt.ylabel("Een waarde van iets", fontdict = font2)

#plot 3
xpoints = np.array(["Hawai","Salami","Jasmina","Calzone","Mojito","Paparazzi","Canto"])
ypoints = np.array([1, 3, 6, 7, 1, 13, 8])

font1 = {'family':'serif','color':'red','size':20}
font2 = {'family':'serif','color':'purple','size':20}


plt.subplot(2,2,3)
plt.bar(xpoints, ypoints)

plt.title("Molah", fontdict = font1, loc = "right")
plt.xlabel("Green papers", fontdict = font2)
plt.ylabel("Waarde per papier", fontdict = font2)

def Plot4():
    #plot 4
    ypoints = np.array([1, 1, 1, 1, 1, 1, 1, 1, 50, 1])

    font1 = {'family':'serif','color':'green','size':20}
    font2 = {'family':'serif','color':'blue','size':15}


    plt.subplot(2,2,4)
    plt.pie(ypoints)

    plt.title("Moet hier iets neerzetten", fontdict = font1, loc = "left")
    plt.xlabel("Laten zien hoe je iedere grafiek hun eigen titels and labels geeft", fontdict = font2)
    plt.ylabel("Dit is voor presentatie waarde", fontdict = font2)

Plot4()

plt.show()