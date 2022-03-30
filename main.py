from galactic_classes import *
import random


def create_classification():
    body_classifications = ["M", "K", "G", "F", "A", "B", "O"]
    classification = random.choice(body_classifications)
    new_classification = StellarClassification(classification)

    return new_classification


def create_name():
    name = f"Alpha-Ocelot{random.randint(0, 9)}"

    return name


def create_satellites():
    sat_number = random.randint(0, 15)

    return sat_number


def create_colonization_state():
    colonization_state = random.choice([True, False])

    return colonization_state


def create_owner(colonization_state: bool):
    if colonization_state:
        owner = f"Beta-Serval{random.randint(0, 9)}"
    else:
        owner = None

    return owner


def create_location():
    theta_angle = random.randint(0, 180)
    lambda_angle = random.randint(0, 180)
    distance = random.randint(0, 10000)

    new_location = GalacticPosition(theta_angle, lambda_angle, distance)

    return new_location


def create_celestial_body():
    name = create_name()
    classification = create_classification()
    satellites = create_satellites()
    colonized = create_colonization_state()
    owner = create_owner(colonized)
    location = create_location()

    new_celestial_body = CelestialBody(name, classification, satellites, colonized, owner, location)

    return new_celestial_body


def main():
    print(create_celestial_body())


if __name__ == "__main__":
    main()
