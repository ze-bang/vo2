import scipy.integrate as inte
import scipy.misc as misc
import numpy as np
class vo2_pattanayak:
    #all paremeters are using the same naming convention as the paper
    def __init__(self, Rm, Ri, V2, V1, C_e, R_e, r_f, c_f):
        #R_LRS resistance of the metalic state
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

    def set_biased(self, V_s)
        self.V_s = V_s

    def R_D(V_ce)
        V_D = V_s-V_ce
        if V_D > V2:
            return self.R_HRS
        elif V_D < V1:
            return self.R_LRS
    
    def dV_ce_dt(V_ce, t, R_D, R_e, C_e):
        return -(R_e+R_D(V_ce)/(C_e*R_D(V_ce)*R_e)*V_ce + V_s/(C_e*R_D(V_ce))
        
    def solve(self):
        t = np.linspace(0,10,101)
        self.V_ce = inte.odeint(self.dV_ce_dt, 0, t, args=(R_D, self.R_e, self.C_e))
            

    def I_s(self)
        
        return self.V_ce/self.R_e - self.C_e*misc.derivative(self.V_ce, 1.0)

    
