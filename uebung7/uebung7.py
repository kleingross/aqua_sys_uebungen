import numpy as np
import matplotlib.pyplot as plt

#functions
def LMWL(O):
    return 7.70*O + 5.74

#wrong standardise function
#def standardise(O, H):
#    return O - 1.336, H - 88

def standardise(O, H):
    return (-1.336*O)/1000.0 + O - 1.336, (-88*H)/1000.0 + H - 88

#input data
height = -np.array([0.36, 3.26, 4.26, 6.26, 9.26, 11.26, 11.66, 12.06, 12.66])
d18_O = -np.array([0.52, 0.79, 1.33, 1.77, 2.43, 2.83, 3.08, 4.67, 5.04])
d2_H = np.array([68.5, 67.3, 64.1, 61.4, 57.1, 55.9, 53.5, 45.8, 43.8])

#standardise and save to file
d18_O_std, d2_H_std = standardise(d18_O, d2_H)

table = np.concatenate((height.reshape(-1,1), d18_O_std.reshape(-1,1), d2_H_std.reshape(-1,1)), axis=1)
np.savetxt('standardised.txt', table , delimiter=" & ", fmt="%2.2f", newline=" \\\\" )

#plot data
plt.scatter(d18_O_std, d2_H_std, label="lake data")
#plot LMWL
O = np.linspace(-8.5, -1.5, 2)
plt.plot(O, LMWL(O), 'r', label="LMWL")
#plot groundwater data point
plt.scatter(-8.2, -58.0, color="green", label="local groundwater")

plt.xlabel(r"$\delta ^{18} O$")
plt.ylabel(r"$\delta ^2 H$")
plt.legend(loc=2)
plt.savefig("plot_data_LMWL.png")
