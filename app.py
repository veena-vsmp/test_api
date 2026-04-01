from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"


# POSTS
# -----------------------------

# GET all posts (with pagination)
@app.route('/posts')
def get_posts():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    res = requests.get(f"{BASE_URL}/posts")
    posts = res.json()

    start = (page - 1) * limit
    end = start + limit

    return jsonify(posts[start:end])


# GET single post
@app.route('/posts/<int:post_id>')
def get_post(post_id):
    res = requests.get(f"{BASE_URL}/posts/{post_id}")
    return jsonify(res.json())


# GET comments of a post
@app.route('/posts/<int:post_id>/comments')
def get_post_comments(post_id):
    res = requests.get(f"{BASE_URL}/comments?postId={post_id}")
    return jsonify(res.json())


# -----------------------------
# COMMENTS
# -----------------------------

# GET all comments
@app.route('/comments')
def get_comments():
    res = requests.get(f"{BASE_URL}/comments")
    return jsonify(res.json())


# GET single comment
@app.route('/comments/<int:comment_id>')
def get_comment(comment_id):
    res = requests.get(f"{BASE_URL}/comments/{comment_id}")
    return jsonify(res.json())


# -----------------------------
# ALBUMS
# -----------------------------

# GET all albums
@app.route('/albums')
def get_albums():
    res = requests.get(f"{BASE_URL}/albums")
    return jsonify(res.json())


# GET single album
@app.route('/albums/<int:album_id>')
def get_album(album_id):
    res = requests.get(f"{BASE_URL}/albums/{album_id}")
    return jsonify(res.json())


# GET albums of a user
@app.route('/users/<int:user_id>/albums')
def get_user_albums(user_id):
    res = requests.get(f"{BASE_URL}/albums?userId={user_id}")
    return jsonify(res.json())


# -----------------------------
# RUN
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
