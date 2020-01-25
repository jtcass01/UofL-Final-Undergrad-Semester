import numpy as np
import matplotlib.pyplot as plt

def calculate_mobility(mu_min, mu_max, n_ref, gamma, n):
    return mu_min + ((mu_max - mu_min) / (1 + (n/n_ref)**gamma))

def calculate_conductivity(mu_p, p_o, q=1.6e-19):
    return q*mu_p*p_o

def calculate_resistivity(mu_p, p_o, q=1.6e-19):
    return 1/calculate_conductivity(mu_p, p_o, q)

def calculate_volume(length, width, thickness):
    return length*width*thickness

def calculate_current(voltage, resistance):
    return voltage/resistance

def calculate_intrinsic_carrier_concentration(T):
    return 5.29e19* (T/300)**2.54 * np.exp(-6726/T)

if __name__ == "__main__":
    print("A piece of silicon is doped with donor atoms at a concentration of 1e18.  The piece is 1 mm long, 10 micro-m wide, and 10 micro-m thick.")
    N_D = 1e18
    n_i = 1e10
    length=0.1
    width=0.001
    thickness=0.001
    print("\tWhat is the electron concentration?")
    n_o = N_D
    print("\t\tn_o = N_D = ", n_o)

    print("\tWhat is the hole concentration?")
    p_o = n_i**2 / n_o
    print("\t\tp_o = n_i**2 / n_o = ", p_o)

    print("\tWhat is the elctron mobility?")
    mu_min = 88.3
    mu_max = 1330.3
    n_ref = 1.295e17
    gamma = 0.891
    n = N_D
    mu_n = calculate_mobility(mu_min, mu_max, n_ref, gamma, n)
    print("\t\tmu_n = ", mu_n)

    print("\tWhat is the hole mobility?")
    mu_min = 54.3
    mu_max = 461.2
    n_ref = 2.35e17
    gamma = 0.88
    n = N_D
    mu_p = calculate_mobility(mu_min, mu_max, n_ref, gamma, n)
    print("\t\tmu_p = ", mu_p)

    print("\tWhat is the resistivity?")
    resistivity = calculate_resistivity(mu_p, p_o)
    print("\t\tresistivity = ", resistivity)

    print("\tWhere is the Fermi level located relative to the middle of the bandgap?")
    print("\t\tThe fermi level is above the middle of the bandgap.")

    print("\tWhat is the resistance of the piece of silicon?")
    volume = calculate_volume(length=length, width=width, thickness=thickness)
    resistance = volume*resistivity
    print("\t\tresistance = volume*resistivity =", resistance)

    print("\t1V is applied across the length.  How much current flows?")
    print("\t\t", calculate_current(voltage=1, resistance=resistance), "A")

    print("\t1000V is applied across the length.  How much current flows?")
    print("\t\t", calculate_current(voltage=1000, resistance=resistance), "A")

    print("\nA piece of silicon is doped with acceptor atoms at a concentration of 1e17.  The piece is 10 micro-m long, 2 micro-m wide, and 2 micro-m thick.")
    N_A = 1e17
    n_i = 1e10
    length=0.001
    width=0.0002
    thickness=0.0002

    print("\tWhat is the hole concentration?")
    p_o = N_A
    print("\t\tp_o = N_A = ", p_o)

    print("\tWhat is the electron concentration?")
    n_o = n_i**2 / p_o
    print("\t\tn_o = n_i**2 / p_o = ", n_o)

    print("\tWhat is the elctron mobility?")
    mu_min = 88.3
    mu_max = 1330.3
    n_ref = 1.295e17
    gamma = 0.891
    n = N_A
    mu_n = calculate_mobility(mu_min, mu_max, n_ref, gamma, n)
    print("\t\tmu_n = ", mu_n)

    print("\tWhat is the hole mobility?")
    mu_min = 54.3
    mu_max = 461.2
    n_ref = 2.35e17
    gamma = 0.88
    n = N_A
    mu_p = calculate_mobility(mu_min, mu_max, n_ref, gamma, n)
    print("\t\tmu_p = ", mu_p)

    print("\tWhat is the resistivity?")
    resistivity = calculate_resistivity(mu_p, p_o)
    print("\t\tresistivity = ", resistivity)

    print("\tWhere is the Fermi level located relative to the middle of the bandgap?")
    print("\t\tThe fermi level is below the middle of the bandgap.")

    print("\tWhat is the resistance of the piece of silicon?")
    volume = calculate_volume(length=length, width=width, thickness=thickness)
    resistance = volume*resistivity
    print("\t\tresistance = volume*resistivity =", resistance)

    print("\t1V is applied across the length.  How much current flows?")
    print("\t\t", calculate_current(voltage=1, resistance=resistance), "A")

    print("\t1000V is applied across the length.  How much current flows?")
    print("\t\t", calculate_current(voltage=1000, resistance=resistance), "A")

    print("USING EQUATIONS 3.35, 3.36, AND 3.37, PLOT THE INTRINSIC CARRIER CONCENTRATION AS A FUNCTION OF TEMPERATURE FOR SILICON.  THE TEMPERATURE SHOULD RANGE FROM 200K TO 600K.  THE Y-AXIS (INTRINSIC CARRIER CONCENTRATION) SHOULD BE A LOG SCALE.  USE A COMPUTER TO GENERATE THE PLOT AND TURN IN YOUR CODE.")
    temperature = np.linspace(200, 600, 200)
    intrinsic_carrier_concentration = np.array(map(calculate_intrinsic_carrier_concentration, temperature))
    plt.plot(temperature, intrinsic_carrier_concentration)
    plt.yscale('log')
    plt.xlabel('Temperature (K)')
    plt.ylabel("Intrinsic Carrier Concentration (cm^-3)")
    plt.show()
