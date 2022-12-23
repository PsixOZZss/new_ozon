TOKEN = '5959594800:AAGVorUcaBmOlO3oIFeR0xUentOkzaINeKU'
ID = 1148865286


class Auth:
    def __init__(self, token):
        # Initialize bot and dispatcher
        bot = Bot(token=token)
        dp = Dispatcher(bot)

    manager = OzonManager()