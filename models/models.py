import json

# =============#
#              #
#   MODELS     #
#              #
# =============#


class Chat:
    def __init__(self, users, messages):
        self.users= users
        self.messages = messages

class Meme:
    def __init__(self, url):
        self.url = url


class User:
    def __init__(self, name):
        self.name = name


class Message:
    def __init__(self, text, author):
        self.text = text
        self.author = author


# ================#
#                 #
#   UTILITIES     #
#                 #
# ================#


def save_to_db(object, object_name):
    """Save objects to the database. As a JSON file.

      # Example
      ```python
      message = Message("This is a messsage", "Kesler")
      save_to_db(message, "message")
      ```

      # Note
      The database structure is the following
      ```json
      {
        "user" : [
          { "name" : "Andrew" },
          { "name" : "Kesler"}
        ],
        "message" : [
          { "author" : "Kesler", "text" : "This is a message" }
        ]
      }
    ```
    """
    # Get the dictionary representation of the object.
    model = object.__dict__

    # Open the current json file.
    with open("db.json", "r") as db_file:

        # Load the json dictionary.
        current_db = json.load(db_file)

        current_entries = current_db.get(object_name, [])

        # List with the new model
        current_entries.append(model)

        current_db[object_name] = current_entries
        new_db = current_db

    # Write the dictionary representation to a json file.
    with open("db.json", "w") as db_file:
        db_file.write(json.dumps(new_db))


def read_from_db(object_name):
    
    # Open the json file as a dictionary.
    with open("db.json", "r") as db_file:
        current_db = json.load(db_file)

    return current_db[object_name]


# ====================#
#                     #
#   FUNCTIONALITY     #
#                     #
# ====================#


def create_user(name):
    user = User(name)

    save_to_db(user, "user")


def get_user(name):
    users = read_from_db("user")
    for user in users:
        if user.get("name") == name:
            return user


def create_message(text, author):
    message = Message(text, author)
    save_to_db(message, "message")


def get_message_by_author(author):
    messages = read_from_db("message")
    user_messages = []
    for message in messages:
        if message.get("author") == author:
            user_messages.append(message)

    return user_messages


# ====================#
#                     #
#   CALL FUNCTIONS    #
#                     #
# ====================#


# ANDREW


# Using the input() function from the user, 
# create a chat experience where the first user can see messages from the second user

# Create the chat with 2 users
# Prompt the user 1 to enter a message
# Prompt the user 2 to enter a message
# Figure out the replies 