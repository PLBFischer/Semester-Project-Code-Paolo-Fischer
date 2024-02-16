import numpy as np
import matplotlib.pyplot as plt


y = 27.2*np.array([-0.013,-0.0163,-0.047,-0.09])
x = np.array([10,20,30,40])


print(0.001*52.9*np.array([10,100,1000]))
print(y)
plt.figure(dpi = 1000)
plt.xlabel("n")
plt.ylabel("-log(-$E_0$)")
plt.hlines(-np.log(27.2),100,1600,color="red")
plt.plot(x**2,-np.log(-y),"o--",color="darkgreen")
#plt.scatter(x**2,y,marker="x",color="b",s=90)

plt.show()

