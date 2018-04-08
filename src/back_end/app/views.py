from app import app
from flask import request, abort, jsonify, render_template
import json
from .text_processor.test import find_answer, add_QA_pairs, get_questions


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/query', methods = ['GET'])
def query():
    sentence = request.args.get('question')
    print("question:",sentence)
    if not sentence:
        abort(400)
    result = find_answer(sentence)
    '''
    answer = []
    for line in result:
        answer.append({"answer":line,"percentage":80})
    print(json.dumps(answer,indent=4))
    '''
    print(json.dumps(result, indent=4))
    return jsonify(result)
    #return jsonify(Success=True)

#-----admin pages below--------
@app.route('/admin', methods = ['GET'])
def admin():
    return render_template('admin.html')


@app.route('/login', methods = ['GET'])
def login():
    if request.method == 'GET':
        return jsonify(get_questions())


@app.route('/answer', methods = ['PATCH'])
def add_answer():
    if request.method == 'PATCH':
        req = request.get_json()
        print(req)
        if 'question' in req and 'answer' in req:
            add_QA_pairs(req['question'], req['answer'])
            return jsonify(Success=True)
        else:
            return jsonify(Success=False)