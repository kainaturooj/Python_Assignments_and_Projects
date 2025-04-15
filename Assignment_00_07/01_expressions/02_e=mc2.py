C = 299792458  # Speed of light in m/s

def main():
    # ask user to enter the mass in kg
    mass_in_kg : float = float(input("\033[1;3mEnter kilos of mass: \033[0m"))
    
    # calculate the energy in joules using the formula e = mc^2
    energy_in_joules : float = mass_in_kg * (C ** 2)
    
    # print the result
    print("e = m * C^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    print(f"{energy_in_joules} joules of energy!")

if __name__ == '__main__':
    main()