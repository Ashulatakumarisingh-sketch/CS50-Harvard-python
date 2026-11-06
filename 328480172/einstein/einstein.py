def calculate_energy(mass):
    speed_of_light = 300000000
    return mass * (speed_of_light ** 2)

def main():
    user_mass = int(input("m:"))
    joules = calculate_energy(user_mass)
    print(f"E: {joules}")

if __name__ == "__main__":
    main()
