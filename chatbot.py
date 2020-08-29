import os
import re
import logging



from logging import FileHandler, Formatter

from flask import Flask, render_template, jsonify, request, Response
from rivescript import RiveScript
import pymongo
from pymongo import MongoClient
import json
from bson import json_util

cluster = MongoClient("mongodb+srv://Omar:123321@cluster0.tyyw9.mongodb.net/Callcenter?retryWrites=true&w=majority")
db = cluster["callcenter1"]
collection = db["food orders"]

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

@app.route('/orders', methods=['GET'])
def get_orders():
    z = list(collection.find({"Order Number":"16118"}))
    return json.dumps(z, default=json_util.default)
    
