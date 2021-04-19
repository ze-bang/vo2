import scipy.integrate as inte
import scipy.misc as misc
import numpy as np
import matplotlib.pyplot as plt

V_s = 25


UorD = True

def dV_ce_dt(V_ce, t, R_D, b):
    return b(V_ce)*(1000 + R_D(V_ce)) / (10*10**(-6) * R_D(V_ce) * 1000) * V_ce \
           + V_s / (10*10^(-6) * R_D(V_ce))

def b(V_ce):
    global UorD
    V_D = V_s - V_ce
    print(UorD, V_D)
    if V_D > 23.81:
        UorD = False
        return 1
    elif V_D > 8.06 and V_D < 23.81 and not UorD:
        return 1
    elif V_D > 8.06 and V_D < 23.81 and UorD:
        return -1
    elif V_D < 8.06:
        UorD = True
        return -1
    else:
        return 0

def R_D(V_ce):
    global UorD
    V_D = V_s-V_ce

    if V_D > 23.81:
        return 2100
    elif V_D > 8.06 and V_D < 23.81 and not UorD:
        return 50
    elif V_D > 8.06 and V_D < 23.81 and UorD:
        return 2100
    elif V_D < 8.06:
        return 50
    else:
        return -1

t = np.linspace(0,0.05,100000)
V_ce0 = V_s

sol = inte.odeint(dV_ce_dt, V_ce0, t, args=(R_D, b))

plt.plot(t, V_s-sol)
plt.show()