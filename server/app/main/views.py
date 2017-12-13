
from . import main
from flask import render_template,request,jsonify
from .file_manage import FileManage
@main.route('/')
def index():
    return render_template('index.html')


@main.route('/ajaxpost', methods=['POST'])
def ajax_post():

    file_manage = FileManage()
    files = file_manage.search_dir()
    return jsonify(files=files)