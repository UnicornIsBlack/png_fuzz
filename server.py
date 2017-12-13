from flask import Flask, request, json, render_template,jsonify
from flask_script import Manager
from flaskext.mysql import MySQL
from flask_bootstrap import Bootstrap
from app.main.file_manage import FileManage

app = Flask(__name__)
app.config['SECURE_KEY'] = 'HELLO'
manager = Manager(app)
bootstrap = Bootstrap(app)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'chai'
app.config['MYSQL_DATABASE_DB'] = 'fuzz_png'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ajaxpost', methods=['POST'])
def ajax_post():

    file_manage = FileManage()
    files = file_manage.search_dir()
    myJson = request.get_json()
    image = myJson['image']
    noimage = myJson['noimage']
    print(image)
    print(noimage)
    print(myJson)
    return jsonify(files=files)


if __name__ == '__main__':
    manager.run()