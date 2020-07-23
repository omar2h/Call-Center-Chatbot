import os

from chatbot import app

if __name__ == '__main__':
    app.run(host='localhost', port=int(os.environ.get('PORT', 5000)), debug=True)

