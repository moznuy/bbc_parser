from bbc_parser import app
from flask import jsonify, request
from bbc_parser.logic import parse_bbc


@app.route('/')
def hello_world():
    chapter = request.args.get('chapter', None)
    news = request.args.get('news', None)

    if not chapter or not news:
        return jsonify("Bad Params"), 400

    try:
        news = int(news)
    except Exception:
        return jsonify("Bad Params"), 400

    result = parse_bbc(chapter, news)
    if result is None:
        jsonify("Something bad happened"), 500

    result = {
        'chapter': chapter,
        'news': [{
            'title': tup[0],
            'URL': tup[1]
        } for tup in result]
    }
    return jsonify(result)

