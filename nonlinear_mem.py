import math
import numpy as np
#define

kb = 1.38064852 * 10**(-23)
q = 1.60217662 * 10**(-19)
T_amp = 300
T_c = 340
d = 
A = 
c_th = 1050*10^(-12)
e = q
mu =  #electron mobility
N_c = #effective density of state in conduction band
N_d = #density of state of donor
N_t = #density of state of traps
E_d = #donor energy
E_t = #trap energy
epsilon_0 =  8.85418782 * 10*(-12)#permisivity of free space
epsilon_i =  #high frequency dielectric constant
T = T_amp
t_L = #time evolve
N = #steps
dt = t_L/N#time step
t = 0

def r_th(temp):
	if temp >= T_c:
		return 93000
	else:
		return 18000
def sigma_0(temp):
	return e*mu*N_c*(N_d/N_t)^2*exp(-(E_d+E_t)/(2*kb*temp))

def omega(temp):
	return sqrt(q^3/(math.pi*epsilon_i*epsilon_0))

def dT_dt(i_m, v_m, T):
	return (i_m*v_m)/c_th - (T-Tamp)/(c_th*r_th(T))

def i_m(v_m, T)
	return (sigma_0(T)*exp(-0.301/(2*kb*T))*A*(kb*T^2/omega(T))*(1+(omega(T)*sqrt(v_m/d)/(kb*T)-1)*exp((omega(T)*sqrt(v_m/d)/(kb*T))+1/(2*d))))*v_m

def evolve(v_m, T, dt, t, counter):
	T = T + dT_dt(i_m(v_m,T),v_m,T)*dt
	t = t+dt
	evolve_v_m(v_m, t)
	counter = counter + 1

def evolve_v_m(v_m, t):
	#to control v_m

i = np.zeros((1,N))
v = np.zeros((1,N))
counter = 0
while(t < t_L):
	i[counter] = i_m(v_m,T)
	v[counter] = v_m
	evolve(v_m, T, dt, t, counter)
