import scipy.integrate as inte
import scipy.misc as misc
import numpy as np
import matplotlib.pyplot as plt
class vo2_pattanayak:
    #all paremeters are using the same naming convention as the paper

    def __init__(self, R_LRS, R_HRS, V2, V1, C_e, R_e, r_f, c_f):
        #R_LRS resistance of the metallic state
        #R_HRS resistance of the insulator state
        #V2 voltage to trigger M2 to R transition
        #V1 voltage to trigger M1 to M2 transition
        #C_e capacitance of external RC
        #R_e resistance of the external RC
        self.R_LRS = R_LRS
        self.R_HRS = R_HRS
        self.V2 = V2
        self.V1 = V1
        self.C_e = C_e
        self.R_e = R_e
        self.r_f = r_f
        self.c_f = c_f
        self.V_ce = 0


    def set_biased(self, V_s):
        self.V_s = V_s
        if self.V_s >= 23.81:
            self.UorD = False
        else:
            self.UorD = True

    def R_D(self, V_ce):
        V_D = self.V_s - V_ce
        if V_D > 23.81:
            self.UorD = False
            return 50
        elif V_D < 23.81 and not UorD:
            return 2100
        elif V_D > 8.06 and UorD:
            return 50
        elif V_D < 8.06:
            self.UorD = True
            return 2100
        else:
            return -1

    def dV_ce_dt(self, V_ce, t, R_D):
        return -(self.R_e+R_D(V_ce))/(self.C_e*R_D(V_ce)*self.R_e)*V_ce + self.V_s/(self.C_e*R_D(V_ce))

    def solve(self):
        self.V_ce = inte.odeint(self.dV_ce_dt, 0, self.t, args=(self.R_D, ))

    def setTime(self, T, steps):
        self.t = np.linspace(0, T, steps)

    def I_s(self):
        return self.V_ce/self.R_e - self.C_e*misc.derivative(self.V_ce, 1.0)

    def plot_V_ce(self):
        plt.plot(self.t, self.V_ce)

    def plot_I_s(self):
        plt.plot(self.t, self.I_s())
