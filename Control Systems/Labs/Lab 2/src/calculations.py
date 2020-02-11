WEIGHT = False

# Constants
Rm = 2.6               # Motor armature resistance
Lm = 180e-6            # Motor inductance
Kt = 0.00767           # Motor torque constant
Eff_m = 100            # Motor efficiency
Km = 0.00767           # Back-EMF Constant
Jm = 9.3e-07           # Rotor moment of inertia
Kg = 3.71              # Gearbox ratio
Eff_g = 100            # Gearbox efficiency
Mc = 0.57              # Cart mass without the weight
Mw = 0.37              # Weight mass
Pr = 1.664e-03         # Rack pitch
r_mp = 6.35e-3         # Motor pinion radius
N_mp = 24              # Motor pinion number of teeth
r_pp = 0.01482975      # Position pinion radius
N_pp = 56              # Position pinion number of teeth
K_EC = 2.275e-5        # Cart position encoder resolution
Bc = 4.3
Bw = 1.1
if WEIGHT:
    M = Mc + Mw            # Total mass
    Beq = Bc + Bw
else:
    M = Mc
    Beq = Bc

def calculate_time_domain_coefficients():
    A = M
    B = (Eff_g * Kg * Eff_m * Kt) / (r_mp * Rm)
    C = ((Eff_g * Kg**2 * Eff_m * Km * Kt) / (r_mp**2 * Rm)) * Beq
    print("A/B", A/B, "B/B", 1, "C/B", C/B)

if __name__ == "__main__":
    calculate_time_domain_coefficients()
