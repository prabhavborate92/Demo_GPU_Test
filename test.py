sum = 0
for x in [1,2,3,4,5]:
      sum = sum + x

print(sum)

import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
myarr = np.random.randint(1000, size=100000)
plt.hist(myarr, bins=40)
plt.show()

#cd /home/pgb5080/output

f = open("sum.txt", "w")
f.write(str(sum))
f.close()

f = open("myarr.txt", "w")
f.write(str(myarr))
f.close()