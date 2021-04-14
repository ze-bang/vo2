import scipy.integrate as inte
import scipy.misc as misc
import numpy as np
import matplotlib.pyplot as plt

V_s =

if V_s >= 23.81:
    UorD = False
else:
    UorD = True

def dV_ce_dt(V_ce, t, R_D):
    return -(1000 + R_D(V_ce)) / (10*10^(-6) * R_D(V_ce)*1000) * V_ce \
           + V_s / (10*10^(-6) * R_D(V_ce))

def R_D(V_ce):
    global UorD
    V_D = V_s-V_ce
    print(UorD, V_D)
    if V_D > 23.81:
        UorD = False
        return 50
    elif V_D < 23.81 and not UorD:
        return 2100
    elif V_D > 8.06 and UorD:
        return 50
    elif V_D < 8.06:
        UorD = True
        return 2100
    else:
        return -1

t = np.linspace(0,10,100000)
V_ce0 = 0

sol = inte.odeint(dV_ce_dt, V_ce0, t, args=(R_D,))

plt.plot(t, V_s - sol)
plt.show()