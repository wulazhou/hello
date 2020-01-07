import matplotlib.pyplot as plt

from random import choice
import os
import sys
o_path = os.getcwd()
sys.path.append(o_path)
sys.path.append(o_path+"/matplot")
from matplot.random_walk  import RandomWalk


# while True:
rw = RandomWalk(50000)
rw.fill_walk()
plt.figure(dpi=128, figsize=(10,6))
point_numbers = list(range(rw.num_points))
# plt.scatter(rw.x_values,rw.y_values,c=rw.y_values,
#             cmap=plt.cm.rainbow, edgecolor='none',s=15)
plt.scatter(rw.x_values,rw.y_values,c=point_numbers,
            cmap=plt.cm.rainbow, edgecolor='none',s=5)
plt.scatter(0,0,c='green' ,edgecolor='none',s=100)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none', s=100)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()

    # keep_running = input("Make another walk? (y/n)")
    # if keep_running == 'n':
    #     break