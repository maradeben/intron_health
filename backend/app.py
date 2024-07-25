from flask import Flask
import sqlite3

con = sqlite3.connect('intron_db')
print(con)
print('c')

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

# if __name__ == '__main__':
#     app.run(debug=True)
