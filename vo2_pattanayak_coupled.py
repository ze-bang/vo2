#This is an example for 2 coupled voltage biased vo2 devices
#The behaviour of the VO2 device is based on the Pattanayak Paper
#The coupling scheme is according to the paper "Scaled Resistively Coupled VO2 oscillators for Neuromorphic Computing"
from vo2_pattanayak import vo2_pattanayak
Vin_1
Vin_2
R_s1
R_s2
R_C
V_th #or V_2 in pattanayak paper
V_1

#Vin1 - R_s1*I_1 =  V_OSC1
#Vin2 - R_s2*I_2 =  V_OSC2
#V_OSC1 = V_OSC2+R_C*I_C
#I_1 = I_S1(V_OSC1)+I_C
#I_2 = I_S2(V_OSC2)-I_C
#I_S1 and I_S2 can be modelled as purely a function of V_OSC1 and V_OSC2

#Vin1 - R_s1*(I_S1(V_OSC1)+I_C) = Vin2 - R_s2*(I_S2(V_OSC2)-I_C)+R_C*I_C

vo2_1 = vo2_pattanayak()
vo2_2 = vo2_pattanayak()

