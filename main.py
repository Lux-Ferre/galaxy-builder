from galactic_classes import *
import random
import PySimpleGUI as sg


def create_classification():
    new_classification = None

    while not new_classification:
        new_classification = gui_get_info("Classification")

        if new_classification.casefold() == "random":
            body_classifications = ["M", "K", "G", "F", "A", "B", "O"]
            classification = random.choice(body_classifications)
            new_classification = StellarClassification(classification)

    return new_classification


def create_name():
    name = None

    while not name:
        name = gui_get_info("Name")

        if name.casefold() == "random":
            name = f"Alpha-Ocelot{random.randint(0, 9)}"

    return name


def create_satellites():
    sat_number = None

    while not sat_number:
        sat_number = gui_get_info("Satellite Number")

        if sat_number.casefold() == "random":
            sat_number = random.randint(0, 15)

    return sat_number


def create_colonization_state():
    colonization_state = None

    while not colonization_state:
        colonization_state = gui_get_info("Colonization State")

        if colonization_state.casefold() == "random":
            colonization_state = random.choice([True, False])

    return colonization_state


def create_owner(colonization_state: bool):
    owner = None

    while not owner:
        owner = gui_get_info("Owner")

        if owner.casefold() == "random":
            if colonization_state:
                owner = f"Beta-Serval{random.randint(0, 9)}"
            else:
                owner = None

    return owner


def create_location():
    theta_angle = None
    lambda_angle = None
    distance = None

    while not theta_angle:
        theta_angle = gui_get_info("Location-Theta")
        if theta_angle.casefold() == "random":
            theta_angle = random.randint(-180, 180)

    while not lambda_angle:
        lambda_angle = gui_get_info("Location-Lambda")
        if lambda_angle.casefold() == "random":
            lambda_angle = random.randint(-90, 90)

    while not distance:
        distance = gui_get_info("Location-Distance")
        if distance.casefold() == "random":
            distance = random.randint(0, 10000)

    new_location = GalacticPosition(theta_angle, lambda_angle, distance)

    return new_location


def gui_get_info(info_type: str) -> str:
    layout = [[sg.Text("Enter a name: "), sg.InputText(), sg.Button("OK")]]
    window = sg.Window(f"Celestial Body: {info_type}", layout, margins=(10, 10))

    event, values = window.read()
    window.close()
    data = values[0]

    return data


def create_celestial_body():
    name = create_name()
    classification = create_classification()
    satellites = create_satellites()
    colonized = create_colonization_state()
    owner = create_owner(colonized)
    location = create_location()

    new_celestial_body = CelestialBody(name, classification, satellites, colonized, owner, location)

    return new_celestial_body


def gui_display_body(celestial_body):
    left_col = [[sg.Text("Name: ")],
                [sg.Text("Class: ")],
                [sg.Text("Satellites: ")],
                [sg.Text("Colonized: ")],
                [sg.Text("Owner: ")],
                [sg.Text("Location: ")]]

    right_col = [[sg.Text(celestial_body.name)],
                 [sg.Text(celestial_body.classification)],
                 [sg.Text(celestial_body.satellites)],
                 [sg.Text(celestial_body.colonized)],
                 [sg.Text(celestial_body.owner)],
                 [sg.Text(celestial_body.location)]]

    layout = [[sg.Column(left_col),
               sg.Column(right_col)],
              [sg.Button("OK")]]

    window = sg.Window("Celestial Body Information", layout, margins=(10, 10))

    window.read()


def main():
    sg.theme("DarkGrey13")

    new_celestial_body = create_celestial_body()
    gui_display_body(new_celestial_body)


if __name__ == "__main__":
    main()
