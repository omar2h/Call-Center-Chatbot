from rivescript import RiveScript

bot = RiveScript(utf8=True)

bot.load_directory("brain")
bot.sort_replies()


def chat(message):
    if message == "":
        return "No message found "
    else:
        responce = bot.reply("user", message)
    if responce:
        return responce
    else:
        return "No responce found"
