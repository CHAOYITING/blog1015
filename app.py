
from flask import Flask, render_template, abort

app = Flask(__name__)

# 暫時用 list 儲存文章資料
posts = [
    {
        "id": 1,
        "title": "我的第一篇文章",
        "author": "小明",
        "content": "大家好！這是我的第一篇部落格文章。"
    },
    {
        "id": 2,
        "title": "學習 Python Flask",
        "author": "小華",
        "content": "Flask 是一個輕量級的 Python Web 框架，"
                   "可以用來開發網站與 Web API。"
    },
    {
        "id": 3,
        "title": "今天的生活日記",
        "author": "小美",
        "content": "今天開始學習製作自己的部落格，感覺很有趣！"
    }
]


# 首頁：顯示所有文章
@app.route("/")
def index():
    return render_template("index.html", posts=posts)


# 文章詳細頁面
@app.route("/post/<int:post_id>")
def post_detail(post_id):
    # 根據 id 找出指定文章
    post = next(
        (p for p in posts if p["id"] == post_id),
        None
    )

    if post is None:
        abort(404)

    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
