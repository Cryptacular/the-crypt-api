import requests

baseUri = "https://the-crypt-1047.firebaseio.com/"
jsonUri = ".json"
pageUri = baseUri + "page/" + jsonUri
postUri = baseUri + "post/" + jsonUri


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
