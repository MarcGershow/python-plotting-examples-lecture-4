#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 16:01:27 2018

@author: gershow
"""

import numpy as np
import matplotlib.pyplot as plt

"""
plot sin and cosine over a 2 pi period
add a title and legend
"""
plt.figure(1)
plt.clf()
t = np.linspace(0,2*np.pi,100)
x = np.sin(t)
l1 = plt.plot(t,x, 'b-', label = 'sin')

y = np.cos(t)
l2 = plt.plot(t,y, 'g*-', label = 'cosine')

plt.legend()
plt.title("Sines and Cosines")
plt.xlabel("t")

"""
plot a red circle of radius 1
"""

plt.figure(2)
plt.plot(x,y,'r-')
plt.title ("my circle looks like an ellipse because the axes aren't scaled equally")
plt.show();


"""
plot a red circle of radius 1
that doesn't look like an ellipse
"""

plt.figure(3)
plt.plot(x,y,'r-')
plt.title ('axes equally scaled')
ax = plt.gca() #gca = "get current axes"
ax.axis('equal') #set x-axis and y-axis to be equally scaled
plt.show();

"""
plots adjusted approval polls for donald trump
as collected and adjusted by fivethirtyeight
"""
mydata = np.loadtxt('polls.txt');
day = mydata[:,0]
approve = mydata[:,1]
disapprove = mydata[:,2]
electionday = 43410 #nov 6 2018 in microsoft date code

plt.figure(4)
plt.clf()
plt.plot(electionday-day, approve, 'ro', markersize = 1, label = 'approve')
plt.plot(electionday-day, disapprove, 'bo', markersize = 1, label = 'disapprove')
ax = plt.gca()
ax.invert_xaxis()
plt.xlabel('days until midterm election')
plt.ylabel('approval')
plt.title('fivethirtyeight collected and adjusted approval polls')
plt.legend()

"""
makes a histogram of approval and disapproval polls from above
divides by total number of samples to get a normalized distribution
"""
plt.figure(5)
plt.clf()
binedges = np.arange(25,76)
happ,_binedges = np.histogram(approve,binedges) #_binedges means ignore this output
hdis,_binedges = np.histogram(disapprove,binedges)
bins = np.arange(25,75)
plt.bar(bins, happ/np.sum(happ), width=1, color='r', label='approve')
plt.bar(bins, hdis/np.sum(hdis), width=1, color='b', label='disapprove')
plt.xlabel('adjusted poll value')
plt.ylabel('fraction of polls')
plt.title('all polls since january 2017')
plt.legend()


