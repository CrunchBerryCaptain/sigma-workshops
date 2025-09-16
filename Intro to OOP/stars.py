class Star:
    def __init__(self, planets: list[str], name: str, mass: float, temperature: int):
        self.planets = planets
        self.name = name
        self.mass = mass
        self.temperature = temperature

    def add_planet(self, planet: str) -> None:
        self.planets.append(planet)
        # TODO: Show added planet to console

    def get_classification(self) -> str:
        classification_dict = {
            "O": (40000, 50), "B": (20000, 10), "A": (8500, 2), "G": (5700, 1)}
        # TODO: Add rest of classification

        print(classification_dict.values())

        if self.temperature not in classification_dict.values():
            return "Invalid Classification"

        for key, value in classification_dict.items():
            if self.temperature == value[0] and self.mass == value[1]:
                return f"Type: {key}"


Star1 = Star(["mars", "venus"],
             "sun",
             1,
             5700)

print(Star1.get_classification())
