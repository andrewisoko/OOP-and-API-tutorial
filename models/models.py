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

def save_to_db(object):

    model = object.__dict__
    
    with open("db.json", "w") as f:
        f.write(object)


# ================#
#                 #
#   USE CASES     #
#                 #
# ================#


def create_user(name):
    user = User(name)


def create_message(text, author):
    return Message(text, author)


def main():
    create_user("Kesler")


if __name__ == "__main__":
    main()
