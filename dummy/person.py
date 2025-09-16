def get_age() -> int:
    return int(input("Enter your age: "))


def get_name() -> list:
    return input("Enter a name: ")


def get_person():
    name = get_name()
    age = get_age()
    return {
        "name": name,
        "age": age
    }
