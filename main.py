from re import M
from flask import Flask,jsonify,request
from storage import all_articles, liked_articles, notliked_articles


app = Flask(__name__)

@app.route("/get-article")
def get_article():

    article_data = {
        "title": all_articles[0][12],
        "url": all_articles[0][11],
        "text": all_articles[0][13]
    }

    return jsonify({
        "data":article_data,
        "status":"Success"
    })


@app.route("/liked-article",methods = ["POST"])
def liked_article():
    articles = all_articles[0]
    liked_articles.append(articles)
    all_articles.pop(0)
    return jsonify({
        "status":"Success"
    }),201

@app.route("/unliked-article",methods = ["POST"])
def unliked_article():
    articles = all_articles[0]
    notliked_articles.append(articles)
    all_articles.pop(0)
    return jsonify({
        "status":"Success"
    }),201

if __name__ == "__main__":
    app.run()