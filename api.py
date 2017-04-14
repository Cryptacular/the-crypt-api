from flask import Flask
from flask import jsonify
import requests

baseUri = 'https://the-crypt-1047.firebaseio.com/'
jsonUri = '.json'
pageUri = baseUri + 'page/' + jsonUri
postUri = baseUri + 'post/' + jsonUri


def getAllPosts():
    r = requests.get(postUri)
    if r.status_code == 200:
        return r.json()
    return {}


def getAllPages():
    r = requests.get(pageUri)
    if r.status_code == 200:
        return r.json()
    return {}


def getList(allPages):
    pageList = []
    for key in allPages:
        pageList.append({key: allPages[key]['title']})
    return pageList


def getKeywords(allPages):
    allKeywords = {}
    for key in allPages:
        page = allPages[key]
        keywords = page.get('categories')
        if keywords == None:
            continue
        if type(keywords) == str:
            keywords = [keywords]

        for keyword in keywords:
            if keyword in allKeywords:
                allKeywords[keyword].append(key)
            else:
                allKeywords[keyword] = [key]

    return allKeywords


posts = getAllPosts()
pages = getAllPages()

pageList = getList(pages)
postList = getList(posts)

keywords = getKeywords(posts)

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found'
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.route('/pages', methods=['GET'])
def getPages():
    return jsonify(pages)


@app.route('/posts', methods=['GET'])
def getPosts():
    return jsonify(posts)


@app.route('/post/<postid>', methods=['GET'])
def getPost(postid):
    if postid in posts:
        return jsonify(posts[postid])
    else:
        return not_found()


if __name__ == '__main__':
    app.run()
