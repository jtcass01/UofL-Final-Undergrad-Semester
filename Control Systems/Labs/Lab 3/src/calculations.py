import numpy as np

WEIGHT = False

# Constants
Rm = 2.6               # Motor armature resistance
Lm = 180e-6            # Motor inductance
Kt = 0.00767           # Motor torque constant
Eff_m = 1              # Motor efficiency
Km = 0.00767           # Back-EMF Constant
Jm = 3.9e-07           # Rotor moment of inertia
Kg = 3.71              # Gearbox ratio
Eff_g = 1              # Gearbox efficiency
Mc = 0.57              # Cart mass without the weight
Mw = 0.37              # Weight mass
Pr = 1.664e-03         # Rack pitch
r_mp = 6.35e-3         # Motor pinion radius
N_mp = 24              # Motor pinion number of teeth
r_pp = 0.01482975      # Position pinion radius
N_pp = 56              # Position pinion number of teeth
K_EC = 2.275e-5        # Cart position encoder resolution
Mp = 0.23              # Pendulum mass with fitting
Lp = 0.6413            # Pendulum full length
Lc = 0.3302            # Pendulum length from pivot to Center of gravity
Ip = 7.88e-3           # Pendulum moment of inertia about its center of gravity
Bp = 0.0024            # Viscous damping coefficient as seen at the pendulum axis
g = 9.81
Bc = 4.3
Bw = 1.1
if WEIGHT:
    M = Mc + Mw            # Total mass
    Beq = Bc + Bw
else:
    M = Mc
    Beq = Bc
Ml = M + (Eff_g * Kg**2 * Jm) / r_mp**2
print("Ml", Ml)

def calculate_frequency(angular_frequency):
    return angular_frequency / (2*np.pi)

if __name__ == "__main__":
    print("1 / (Ml + Mp)", 1 / (Ml + Mp))
    print("mp*lc", Mp*Lc)
    print("mp*lc*g", Mp*Lc*g)
    print("1/Ip+MpLc**2", 1/(Ip+Mp*Lc**2))

    print("angular frequency 10 rad/s", calculate_frequency(angular_frequency=10))
    print("angular frequency 4.84 rad/s", calculate_frequency(angular_frequency=4.84))
