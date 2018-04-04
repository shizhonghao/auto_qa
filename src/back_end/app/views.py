from app import app
from flask import request, abort, jsonify, render_template
import json
from .text_processor.test import find_answer

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/query',methods = ['GET'])
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
