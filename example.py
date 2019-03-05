
#%%
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#Create a Derivatives Function
def Derivatives(State,ucontrol):
    m = 1.0
    c = 2.0
    k = 3.0
    A = np.asarray([[0.0,1.0],[-k/m,-c/m]])
    B = np.asarray([0.0,1.0/m])
    StateDot = np.dot(A,State) + B*ucontrol
    return StateDot

#Add Control After 5 Seconds
def Control(State,t):
    kp = 30.0
    kd = 10.0
    xcommand = 1.0
    xdotcommand = 0.0
    ucontrol = 0.0
    if t > 5:
        ucontrol = -kp*(State[0]-xcommand) - kd*(State[1]-xdotcommand)
    return ucontrol


print ('Spring Mass Damper Program')
#Initialize State Vector
State = np.asarray([1.0,-2.0])
#Initialize ucontrol in t = 0.0
ucontrol = Control(State,0.0)
#Initialize Derivatives StateDot
StateDot = Derivatives(State,ucontrol)
#Define Time Variables
tfinal = 10.0
tinitial = 0.0
timestep = 0.01
time = np.arange(tinitial,tfinal+timestep,timestep)
#Create State Array
StateOUT = np.zeros((2,len(time)))
for idx in range(0,len(time)):
    print('Simulation',time[idx]/tfinal*100,'Percent Complete')
    StateOUT[:,idx] = State
    ucontrol = Control(State,time[idx])
    StateDot = Derivatives(State,ucontrol)
    State += StateDot*timestep

#Plot Data Plot everything
position = StateOUT[0,:]
velocity = StateOUT[1,:]
plt.figure()
plt.subplot(121)
plt.plot(time,position)
plt.xlabel('Time(sec)')
plt.ylabel('Position(m)')
plt.figure()
plt.subplot(122)
plt.plot(time,velocity)
plt.xlabel('Time(sec)')
plt.ylabel('Velocity(m/s)')

