# =============#
#              #
#   MODELS     #
#              #
# =============#


class Model(object):

    def __init__(self, **params) -> None:
        self.params = params

    def as_dict(self):
        return self.params


class Meme(Model):
    def __init__(self, url):
        self.url = url
        super().__init__(url=url)


class User(Model):
    def __init__(self, name):
        self.name = name
        super().__init__(name=name)


class Message(Model):
    def __init__(self, text, author: User):
        self.text = text
        self.author = author
        super().__init__(text=text, author=author)


# ================#
#                 #
#   UTILITIES     #
#                 #
# ================#


def save_to_db(object):
    with open("db.json", "w") as f:
        f.write(object)


# ================#
#                 #
#   USE CASES     #
#                 #
# ================#


def create_user(name):
    user = User(name)

    save_to_db(str(user.as_dict()))


def create_message(text, author):
    return Message(text, author)


def main():
    create_user("Kesler")


if __name__ == "__main__":
    main()
