import os
import re
import logging



from logging import FileHandler, Formatter

from flask import Flask, render_template, jsonify, request, Response
from rivescript import RiveScript



app = Flask(__name__, template_folder='templates')


# initialize RiveScript stuff
bot = RiveScript()
bot.load_directory(os.path.join(os.getcwd(), 'brain'))
bot.sort_replies()

# setup log file
file_handler = FileHandler('error_log.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(
    Formatter('%(asctime)s,%(msecs)d %(levelname)-5s [%(filename)s:%(lineno)d] %(message)s',
              datefmt='%d-%m-%Y:%H:%M:%S'
              )
)
app.logger.addHandler(file_handler)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reply', methods=['POST'])
def reply():
    # capture what the user said
    user_msg = request.json['userMsg']
    botreply = bot.reply('localuser', user_msg)
    return jsonify({"reply": botreply})