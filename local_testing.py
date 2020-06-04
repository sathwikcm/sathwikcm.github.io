from flask import Flask
import os


app = Flask(__name__, static_url_path='',static_folder='./',)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
port = int(os.getenv("PORT", 8080))




@app.route("/")
def main():

    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
