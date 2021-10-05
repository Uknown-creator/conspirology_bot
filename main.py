from manage import Server
from config import vk_api_token


server = Server(vk_api_token, 202553267, "Conspirology_bot")
server.start()