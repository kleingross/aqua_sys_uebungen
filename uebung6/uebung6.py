import numpy as np

#define constants
R = 8.3145 #J / mol / K
M = 18.015e-3 #kg / mol
R_m = R / M #J / kg / K

#L in J/kg
def L(T):
    return 2.78e6 -51.6*T -3.62*T**2

#epsilon from vapour to liquid
#ln(alpha) = ln(1-epsilon) = -epsilon
def epsilon(T):
    return 1137 / T**2 - 0.4156 / T - 0.0020667

#calculate slope from starting Temperature
def S(T):
    return epsilon(T)*L(T) / (R_m * T**2)

T0 = np.array([5., 15., 25.]) + 273.15 #Kelvin

print(S(T0))
