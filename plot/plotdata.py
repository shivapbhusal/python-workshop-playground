import matplotlib.pyplot as plt 
plt.plot([100,-99.8],[-99.8,100]) #x1 + 5x2-1=0 Blue

plt.plot([100,-100],[99,-101]) # Orange -x1+x2+1=0 

plt.plot([10,10,10],[0,100,-100]) # Green -x1-10=0 

plt.ylim(-100, 100)
plt.xlim(-100,100)

plt.show()
