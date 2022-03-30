class GalacticPosition:
    def __init__(self, theta_angle, lambda_angle, distance):
        self.theta_angle = theta_angle
        self.lambda_angle = lambda_angle
        self.distance = distance

    def __str__(self):
        stringified_obj = f"Theta={self.theta_angle}, Lambda={self.lambda_angle}, Distance={self.distance}"

        return stringified_obj


class StellarClassification:
    def __init__(self, classification):
        self.classification = classification

    def __str__(self):
        return f"{self.classification}"


class CelestialBody:
    def __init__(self, name: str, classification: StellarClassification, satellites: int, colonized: bool, owner: str,
                 location: GalacticPosition):
        self.name = name
        self.classification = classification
        self.satellites = satellites
        self.colonized = colonized
        self.owner = owner
        self.location = location

    def __str__(self):
        stringified_obj = (f"{self.name = }\n" +
                           f"{str(self.classification) = }\n" +
                           f"{self.satellites = }\n" +
                           f"{self.colonized = }\n" +
                           f"{self.owner = }\n" +
                           f"{str(self.location) = }\n")

        return stringified_obj

    def set_name(self, name: str):
        self.name = name

    def set_classification(self, classification: StellarClassification):
        self.classification = classification

    def set_satellite_number(self, satellites: int):
        self.satellites = satellites

    def set_colonization_status(self, colonized: bool):
        self.colonized = colonized

    def set_ownership(self, owner: str):
        self.owner = owner

    def set_location(self, location: GalacticPosition):
        self.location = location

