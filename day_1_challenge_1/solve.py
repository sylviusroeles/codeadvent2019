def main():
    with open('input.txt') as f:
        masses = [line.strip() for line in f.readlines()]

    total_fuel = 0

    for mass in masses:
        total_fuel += mass_to_fuel(mass)

    print total_fuel


def mass_to_fuel(mass):
    return int(mass) / 3 - 2


if __name__ == "__main__":
    main()
