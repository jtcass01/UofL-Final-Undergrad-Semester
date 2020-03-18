import math

def calculate_built_in_electric_potential(Na, Nd, ni, es, eo=8.854e-14, kbt_q = 0.0259):
    return kbt_q * math.log(Na * Nd / ni**2)

def calculate_extent_of_depltion_region_in_p_region(Na, Nd, ni, es, eo=8.854e-14, q=1.6e-19):
    Vbi = calculate_built_in_electric_potential(Na, Nd, ni, es)
    return (((2*es*eo)/(q*Na)) * (Nd / (Na+Nd)) * Vbi)**0.5

def calculate_extent_of_depltion_region_in_n_region(Na, Nd, ni, es, eo=8.854e-14, q=1.6e-19):
    Vbi = calculate_built_in_electric_potential(Na, Nd, ni, es)
    return (((2*es*eo)/(q*Nd)) * (Na / (Na+Nd)) * Vbi)**0.5

def calculate_maximum_electric_field(Na, Nd, ni, es, eo=8.854e-14, q=1.6e-19):
    Vbi = calculate_built_in_electric_potential(Na, Nd, ni, es)
    return ( ((2*q)/(es*eo)) * ((Na * Nd) / (Nd + Na)) * Vbi  )**0.5


if __name__ == "__main__":
    # Constants
    silicon_ni = 10e10
    silicon_es = 11.8
    galium_nitride_ni = 2.01e-10
    galium_nitride_es = 9.5

    # Given
    Na = 10e15
    Nd = 10e18

    print("Built-in Electric Potential")
    print("\tSilicon: " + str(calculate_built_in_electric_potential(Na, Nd, silicon_ni, silicon_es)))
    print("\tGaN: " + str(calculate_built_in_electric_potential(Na, Nd, galium_nitride_ni, galium_nitride_es)))

    print("Extent of Depletion region")
    print("\tSilicon: ")
    print("\t\txp: " + str(calculate_extent_of_depltion_region_in_p_region(Na, Nd, silicon_ni, silicon_es)))
    print("\t\txn: " + str(calculate_extent_of_depltion_region_in_n_region(Na, Nd, silicon_ni, silicon_es)))
    print("\tGaN: ")
    print("\t\txp: " + str(calculate_extent_of_depltion_region_in_p_region(Na, Nd, galium_nitride_ni, galium_nitride_es)))
    print("\t\txn: " + str(calculate_extent_of_depltion_region_in_n_region(Na, Nd, galium_nitride_ni, galium_nitride_es)))

    print("Maximum Electric Field")
    print("\tSilicon: " +  str(calculate_maximum_electric_field(Na, Nd, silicon_ni, silicon_es)))
    print("\tGaN: " + str(calculate_maximum_electric_field(Na, Nd, galium_nitride_ni, galium_nitride_es)))
