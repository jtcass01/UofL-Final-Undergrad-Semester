import math

import numpy as np
import matplotlib.pyplot as plt

# Constants
KBT_Q = 0.0259
q = 1.6e-19
e_0 = 8.854e-14

def calculate_built_in_voltage(n_i, Nd, Na):
    return KBT_Q*math.log(Na * Nd / n_i**2)

def calculate_xp(n_i, Nd, Na, e_s):
    # Calculate Vbi
    Vbi = calculate_built_in_voltage(n_i, Nd, Na)

    return ((2*e_s*e_0/(q*Na))*(Nd/(Nd+Na))*Vbi)**0.5

def calculate_xn(n_i, Nd, Na, e_s):
    # Calculate Vbi
    Vbi = calculate_built_in_voltage(n_i, Nd, Na)

    return ((2*e_s*e_0/(q*Nd))*(Na/(Nd+Na))*Vbi)**0.5

def calculate_D(mu):
    return KBT_Q * mu

def calculate_L(D, t):
    return (D * t)**0.5

def calculate_total_width_of_depletion_region(n_i, Nd, Na, e_s):
    xp = calculate_xp(n_i, Nd, Na, e_s)
    xn = calculate_xn(n_i, Nd, Na, e_s)

    return xp+xn

def calculate_Js(n_i, D_p, L_p, Nd, D_n, L_n, Na):
    return q * n_i**2 * ((D_p / (L_p * Nd)) + (D_n / (L_n * Na)))

def calculate_J(Vapp, n_i, D_p, L_p, Nd, D_n, L_n, Na):
    Js = calculate_Js(n_i, D_p, L_p, Nd, D_n, L_n, Na)
    return Js * (math.exp(Vapp/KBT_Q) - 1)

def calculate_optical_current_density(n_i, e_s, L_p, Nd, L_n, Na, G):
    W = calculate_total_width_of_depletion_region(n_i, Nd, Na, e_s)
    return q * G * (L_p + L_n + W)

def calculate_total_current_density(Vapp, n_i, e_s, D_p, L_p, Nd, D_n, L_n, Na, G):
    Js = calculate_Js(n_i, D_p, L_p, Nd, D_n, L_n, Na)
    Jop = calculate_optical_current_density(n_i, e_s, L_p, Nd, L_n, Na, G)
    return Js * (math.exp(Vapp/KBT_Q) - 1) - Jop

def problem_1():
    print("For light to be absorbed, what relation between the energy of a photon and the semiconductor bandgap must be satisfied?")
    print("The energy of the photon must be larger or equal to the semiconductor bandgap.")

def problem_2():
    print("Consider a Silicon p-n junction with 𝑁𝐴 = 1017 cm-3 and 𝑁𝐷 = 1016 cm-3 . The minority carrier lifetime on the p-side is 1 micro-s, and the minority carrier lifetime on the n-side is 10 micro-s")
    # GIVEN
    Na = 1e17
    Nd = 1e16
    t_p = 1e-6
    t_n = 10e-6
    G = 1e18

    # Element properties
    e_s = 11.8
    n_i = 10e10
    mu_n = 1314
    mu_p = 143

    # Perform intermediate calculations
    D_n = calculate_D(mu_n)
    L_n = calculate_L(D_n, t_p)

    D_p = calculate_D(mu_p)
    L_p = calculate_L(D_p, t_n)

    W = calculate_total_width_of_depletion_region(n_i, Nd, Na, e_s)
    print("What is the depletion region width, W?", W)

    Js = calculate_Js(n_i, D_p, L_p, Nd, D_n, L_n, Na)
    print("What ist he reverse saturation current density, Js?", Js)

    Vapp = -3
    J = calculate_J(Vapp, n_i, D_p, L_p, Nd, D_n, L_n, Na)
    print("What is the current density for Vapp = -3 V", J)

    Vapp = 0.5
    J = calculate_J(Vapp, n_i, D_p, L_p, Nd, D_n, L_n, Na)
    print("What is the current density for Vapp = -3 V", J)

    print("Using a computer, plot the current density for an applied voltage ranging from -3 V to 0.7 V")
    applied_voltages = np.linspace(-3, 0.7, 4000)
    current_densities = list([])
    for Vapp in applied_voltages:
        current_densities.append(calculate_J(Vapp, n_i, D_p, L_p, Nd, D_n, L_n, Na))

    plt.plot(applied_voltages, current_densities)
    plt.xlabel("Applied Voltages [V]")
    plt.ylabel("Current Density")
    plt.title("2e")
    plt.show()

    Jop = calculate_optical_current_density(n_i, e_s, L_p, Nd, L_n, Na, G)
    print("Light shines on the semiconductor with uniform illumination.  The generation rate is 1e18.  What is Jop?", Jop)

    print("Redo the plot for part 3. On the same plot, show the current density when light is applied.  Rescale as necessary")
    current_densities_without_light = list([])
    current_densities_with_light = list([])
    for Vapp in applied_voltages:
        current_densities_without_light.append(calculate_J(Vapp, n_i, D_p, L_p, Nd, D_n, L_n, Na))
        current_densities_with_light.append(calculate_total_current_density(Vapp, n_i, e_s, D_p, L_p, Nd, D_n, L_n, Na, G))

    plt.plot(applied_voltages, current_densities_without_light, label="current density w/o light")
    plt.plot(applied_voltages, current_densities_with_light, label='current density w/ light')
    plt.xlabel("Applied Voltages [V]")
    plt.ylabel("Current Density")
    plt.title("Problem 2g")
    plt.legend()
    plt.show()

    print("What is the SC current density?", -0.002)
    print("What is the OC Voltage", 0.410)

    print("Using a computer, plot the power density versus applied voltage ranging from -3 V to 0.7 V. Pdensity = Vapp*J")
    power_densities = list([])
    for Vapp in applied_voltages:
        power_densities.append(calculate_total_current_density(Vapp, n_i, e_s, D_p, L_p, Nd, D_n, L_n, Na, G) * Vapp)
    plt.plot(applied_voltages, power_densities)
    plt.xlabel("Applied Voltages [V]")
    plt.ylabel("Power Density")
    plt.title("2i")
    plt.legend()
    plt.show()

    print("What is the maximum amount of power that may be obtained from this level of illumination?", max(power_densities))


if __name__ == "__main__":
    problem_1()
    problem_2()
