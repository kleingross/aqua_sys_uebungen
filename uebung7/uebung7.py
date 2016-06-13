import numpy as np
import matplotlib.pyplot as plt


def LMWL(O):
    return 7.70*O + 5.74

def standardise(O, H):
    return O - 1.336, H - 88

height = -np.array([0.36, 3.26, 4.26, 6.26, 9.26, 11.26, 11.66, 12.06, 12.66])
d18_O = -np.array([0.52, 0.79, 1.33, 1.77, 2.43, 2.83, 3.08, 4.67, 5.04])
d2_H = np.array([68.5, 67.3, 64.1, 61.4, 57.1, 55.9, 53.5, 45.8, 43.8])

d18_O_std, d2_H_std = standardise(d18_O, d2_H)

#f = open('standardised.txt', 'w')
#f.write(d18_O_std)
#f.write(d2_H_std)
#f.close()

np.savetxt('standardised.txt', zip(height, d18_O_std, d2_H_std))

O = np.linspace(-8.5, -1.5, 10)

plt.scatter(d18_O_std, d2_H_std)
plt.plot(O, LMWL(O), 'r', label="LMWL")
#plt.scatter(-8.2, -58.0)
plt.xlabel(r"$\delta ^{18} O$")
plt.ylabel(r"$\delta ^2 H$")


plt.savefig("plot_data_LMWL.png")
