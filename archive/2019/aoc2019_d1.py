import math
import pathlib

input_file = (
    f"{pathlib.Path(__file__).parent.absolute()}"
    f"/data/{pathlib.Path(__file__).stem}.data"
)


def main():

    with open(input_file) as input_data:
        module_masses = input_data.read().split("\n")

    print(f"\nPart 1\n*******\nTotal required fuel: {part1(module_masses)}\n")
    print(f"\nPart 2\n*******\nTotal required fuel: {part2(module_masses)}\n")


def part1(module_masses):
    total_required_fuel = 0

    for module_mass in module_masses:
        try:
            total_required_fuel += math.floor(int(module_mass) / 3) - 2
        except ValueError:
            pass

    return total_required_fuel


def part2(module_masses):
    total_required_fuel = 0

    for module_mass in module_masses:
        try:
            total_required_fuel += calc_fuel_recursive(int(module_mass))
        except ValueError:
            pass

    return total_required_fuel


def calc_fuel_recursive(module_mass, debug=False, depth=0):
    required_fuel = math.floor(module_mass / 3) - 2

    if debug:
        print(f"[{depth}]: {required_fuel}")

    if math.floor(required_fuel / 3) - 2 > 0:
        required_fuel += calc_fuel_recursive(required_fuel, debug, depth + 1)

    return required_fuel


if __name__ == "__main__":
    main()
