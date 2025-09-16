# Challenge:
# In pairs, you should add functionality that will let the user

# Ask the user for their name and set it

# Get the microblogs only for that username
# Get all the messages, only get the ones whose key is "from" and value is "username"
# add to list, return list when finished
# Post a message as that username

# If the trainees finish this task they should then
# Add a loop so they can keep on posting new messages
# Implement the DELETE endpoint so they can delete messages
# Implement the PATCH endpoint so they can update messages that have already been posted

import requests as reqz

MICROBLOG_URL = "https://sigma-micro-blogging.herokuapp.com/"


def get_username() -> str:
    username = input("Enter your username: ")
    return username


def get_blogs_from_username(username: str) -> list[dict]:
    blog = get_messages()
    messages = blog["messages"]

    blogs_from_user = []

    for message in messages:
        if message.get("from") == username:
            blogs_from_user.append(message)

    return blogs_from_user


def get_messages() -> dict:
    response = reqz.get(MICROBLOG_URL)
    json_resp = response.json()
    return json_resp


def send_message(message: str, user: str) -> None:
    response = reqz.post(
        f"{MICROBLOG_URL}/{user}", data={"message": message, "from": user}
    )
    print(response.status_code)


def delete_message(message: str, user: str) -> None:
    response = reqz.delete(MICROBLOG_URL)


if __name__ == "__main__":

    while True:

        go_again = input("Do you want to post a message? [Y/N]: ").lower()

        if go_again == "n":
            break

        message = input("What do you want to send? ")
        username = input("What is your username? ")

        send_message(message, username)
