# This project simulates large amplitude pendulum problem
# Physics basis: (second order derivative of phi) = -sin(phi)*g/R

# numpy: mathematical functions and arrays
# matplotlib: make plots
import math

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# set up the parameters of the system
g = 9.8
R = 1

# initialize the system. phi is in the radian unit
phi = 0.1
v = 0

# initialize time and time step
t =0
dt = 0.01

# initialize arrays
tvals = [t]
phivals = [phi]


#simulate 10 seconds
#the Euler-Cromer method is adopted here
while t < 10:
    a = -g/R * math.sin(phi)

    v = v + a*dt
    phi = phi + v*dt

    t = t + dt

    tvals.append(t)
    phivals.append(phi)

# plot
fig, axes = plt.subplots()
axes.set(title="Large Amplitude Pendulum", xlabel="Time (s)", ylabel="Phi (radians)")
axes.axhline(color='k',linewidth=1)
axes.plot(tvals, phivals)

plt.show()
plt.savefig('pendulum_plot.png')

# tried to only use "import matplotlib", but error occurs. Switched to matplotlib.use('TkAgg'). Didn't work.
# Then tried matplotlib.use('Agg'). The code could generate plots successfully but not in an interactive way.
# Error code ~ UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
# plt.show() is dead. plt.savefig('filename') is the only way to view the image.