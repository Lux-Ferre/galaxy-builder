from galactic_classes import *
import random
import PySimpleGUI as sg


def create_classification():
    new_classification = None

    while not new_classification:
        new_classification, is_random = gui_get_info("Classification")

        if is_random:
            body_classifications = ["M", "K", "G", "F", "A", "B", "O"]
            classification = random.choice(body_classifications)
            new_classification = StellarClassification(classification)

    return new_classification


def create_name():
    name = None

    while not name:
        name, is_random = gui_get_info("Name")

        if is_random:
            name = f"Alpha-Ocelot{random.randint(0, 9)}"

    return name


def create_satellites():
    sat_number = None

    while not sat_number:
        sat_number, is_random = gui_get_info("Satellite Number")

        if is_random:
            sat_number = random.randint(0, 15)

    return sat_number


def create_colonization_state():
    colonization_state = None

    while not colonization_state:
        colonization_state, is_random = gui_get_info("Colonization State")

        if is_random:
            colonization_state = random.choice([True, False])

    return colonization_state


def create_owner():
    owner = None

    while not owner:
        owner, is_random = gui_get_info("Owner")

        if is_random:
            owner = f"Beta-Serval{random.randint(0, 9)}"

    return owner


def create_location():
    theta_angle = None
    lambda_angle = None
    distance = None

    while not theta_angle:
        theta_angle, is_random = gui_get_info("Location-Theta")
        if is_random:
            theta_angle = random.randint(-180, 180)

    while not lambda_angle:
        lambda_angle, is_random = gui_get_info("Location-Lambda")
        if is_random:
            lambda_angle = random.randint(-90, 90)

    while not distance:
        distance, is_random = gui_get_info("Location-Distance")
        if is_random:
            distance = random.randint(0, 10000)

    new_location = GalacticPosition(theta_angle, lambda_angle, distance)

    return new_location


def gui_get_info(info_type: str) -> str, bool:
    is_random = False
    layout = [[sg.Radio(" ", "random_select", default=True), sg.Text(f"Enter {info_type}: "), sg.InputText(key="data"),],
    [sg.Radio("Random", "random_select", default=True, key="is_random")],
    [sg.Button("OK")]]
    window = sg.Window(f"Celestial Body: {info_type}", layout, margins=(10, 10))

    event, values = window.read()
    window.close()
    if values["is_random"]:
        is_random = True
    
    data = values["data"]

    return data, is_random


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
