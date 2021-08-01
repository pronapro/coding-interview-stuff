# importing all necessary libraries
from itertools import count
import random
import matplotlib
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
#import numpy as np
import re
import os
import datetime
#import seaborn as sns
#%matplotlib qt

# add random points for each line
bugolobi = pd.read_csv('bugolobi_hourly_average_pm25.csv') 
bunamwaya = pd.read_csv('bunamwaya_hourly_average_pm25.csv') 
kiwafu = pd.read_csv('kiwafu_hourly_average_pm25.csv') 
makerere = pd.read_csv('makerere_hourly_average_pm25.csv')

myvar = count(0, 3)

# subplots() function you can draw
# multiple plots in one figure
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))

# set limit for x and y axis
axes.set_ylim(0, 100)
axes.set_xlim(0, 24)

# style for plotting line
plt.style.use("ggplot")

# create 5 list to get store element
# after every iteration
x1, y1, y2, y3, y4 = [], [], [], [], []
myvar = count(0, 3)

def animate(i):
	x1.append(next(myvar))
	y1.append((bugolobi[i]))
	y2.append((bunamwaya[i]))
	y3.append((kiwafu[i]))
	y4.append((makerere[i]))

	axes.plot(x1, y1, color="red")
	axes.plot(x1, y2, color="gray")
	axes.plot(x1, y3, color="blue")
	axes.plot(x1, y4, color="green")


# set ani variable to call the
# function recursively
anim = FuncAnimation(fig, animate, interval=30)
anim.save('bugo.gif',writer='imagemagick')