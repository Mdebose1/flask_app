from .import bp as posts
from app.blueprints.blog.models import Post
from flask import js

@posts.route('/posts', methods=['GET'])
def get_posts():
    posts = [p.to_dict() for p in Post.query.all()]
    return jsonify(posts)



    {
        "firstName": "Mike",
        "lastName": "Jones",
        "email": "mikej@thisemail.com",
        "occupation": "Full Stack Developer",
        "skills": {
            "AWS": 9,
            "HTML/CSS": 10,
            "Bootstrap": 10,
            "PHP": 7,
            "Flask": 8
        }
    }