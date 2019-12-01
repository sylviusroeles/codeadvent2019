def main():
    with open('input.txt') as f:
        masses = [line.strip() for line in f.readlines()]

    total_fuel = 0

    for mass in masses:
        fuel_needed = mass_to_fuel(mass)
        total_fuel += fuel_needed
        while fuel_needed > 0:
            fuel_needed = mass_to_fuel(fuel_needed)
            if fuel_needed > 0:
                total_fuel += fuel_needed


    print total_fuel


def mass_to_fuel(mass):
    return int(mass) / 3 - 2

if __name__ == "__main__":
    main()
