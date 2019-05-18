import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

n = 100
p = 0.05
k = np.arange(0, n)
binomial = stats.binom.pmf(k, n, p)
plt.plot(k, binomial, 'o-')
plt.title('binomial:n=%i,p=%.2f' % (n, p), fontsize=15)
plt.xlabel('number of sucess', fontproperties='SimHei')
plt.ylabel('probalility of sucess', fontsize=15)
plt.grid(True)
plt.show()
