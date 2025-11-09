from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "سلام عرفان! 🌷 رباتت الان روی Render با موفقیت اجرا شد!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
