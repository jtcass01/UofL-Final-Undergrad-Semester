import numpy as np
import matplotlib.pyplot as plt

def convert_ev_to_joules(electron_volts):
    return electron_volts * 1.60218e-19

def convert_joule_to_ev(joules):
    return joules * 6.242e18

def fermi_dirac_distribution(E, Ef=0, T=300):
    boltzmann_constant = 1.38064852e-23 # m^2*kg*s^-2*K^-1
    # E and Ef are expected to be in eV
    exp_value = (convert_ev_to_joules(E) - convert_ev_to_joules(Ef)) / (boltzmann_constant * T)

    return 1 / ( 1 + np.exp(exp_value))

def maxwell_boltzmann_distribution(E, Ef=0, T=300):
    boltzmann_constant = 1.38064852e-23 # m^2*kg*s^-2*K^-1
    # E and Ef are expected to be in eV
    exp_value = convert_ev_to_joules(E - Ef) / (boltzmann_constant * T)
    return np.exp(-exp_value)


if __name__ == "__main__":
    print("A SEMICONDUCTOR HAS A BANDGAP OF 0.5 EV.  WHAT IS THE BANDGAP IN JOULES?")
    print("0.5 Ev = ", convert_ev_to_joules(0.5), "J")

    print("A SEMICONDUCTOR HAS A BANDGAP OF 2e−19 J.  WHAT IS THE BANDGAP IN EV?")
    print("2e−19 J = ", convert_joule_to_ev(2e-19), "eV")

    energies = np.linspace(-1, 1, 10000)
    fermi_dirac_distributions = np.array(list(map(fermi_dirac_distribution, energies))) * 100
    maxwell_boltzmann_distributions = np.array(list(map(maxwell_boltzmann_distribution, energies))) * 100

    plt.plot(energies, fermi_dirac_distributions, label="Fermi-Dirac Distribution")
    plt.plot(energies, maxwell_boltzmann_distributions, label="Maxwell-Boltzman Distribution")
    plt.legend()
    plt.title("Distribution Functions")
    plt.xlabel("energy [eV], Ef=0")
    plt.ylabel("probability [%]")
    plt.ylim((0, 200))
    plt.show()
