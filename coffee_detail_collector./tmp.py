import matplotlib as plt
import numpy as np


#I hold x a line while defining new values for each y
x = np.linspace(0, 20, 2000)
#1*x[1] + 0*x[2] <= 5
#y0*0=5-x  #No initialization with respect to y0 because it is zero.
#0*x[1] + 1*x[2] <= 5
y1=5+x*0
#1*x[1] + 0*x[2] >= 1
#y2*0=1-x  #No inititialization
#0*x[1] + 1*x[2] >= 1
y3=1-x*0
#1*x[1] + 1*x[2] <= 6
y4=6-x

#TODO: HOW TO DRAW THE ABOVE LINEAR EQUATIONS ELEGANTLY in matplotlib?
#Drawing the lines by end points because of the zeroes.
plt.plot(x,y4,label=r'$x[1]+x[2]<=6$')
plt.plot([5,5],[10,-10])       #x  <  5
plt.plot([10,-2],[5,5])        #y2 <  5
plt.plot([1,1],[10,-10], 'r-') #x  >= 1
plt.plot([10,-2],[1,1],'b--')  #y3 >= 1
#TODO: how to fill the upper triangle only?
# http://benalexkeen.com/linear-programming-with-python-and-pulp-part-1/
plt.fill_between(x, y5, y6, where=y5>y6, color='grey', alpha=0.5)
plt.show()