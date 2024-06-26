import json

# =============#
#              #
#   MODELS     #
#              #
# =============#


class Meme:
    def __init__(self, url):
        self.url = url


class User:
    def __init__(self, name, age, image):
        self.name = name
        self.age = age
        self.image= image


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


def read_from_db():

# ================#
#                 #
#   USE CASES     #
#                 #
# ================#


def create_user(name, age, image):
    user = User(name, age, image)

    save_to_db(user, "user")


def create_message(text, author):
    message = Message(text, author)
    save_to_db(message, "message")


# ====================#
#                     #
#   CALL FUNCTIONS    #
#                     #
# ====================#



# create_message("This is the text", "Kesler")
