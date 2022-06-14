from flask import  render_template, current_app as app, request, redirect, url_for
# from datetime import datetime as dt
# from app.Blueprint.blog.models import Post

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         print("This works")
#         redirect(url_for('home'))
    # Post._all = []
    
    # p1 = Post('Blog Post Body #1', 'Mike Jones')
    # p2 = Post('Blog Post Body #2', 'Mike Jones')
    # p3 = Post('Blog Post Body #3', 'Mike Jones')
    # p4 = Post('Blog Post Body #4', 'Mike Jones')

    # posts_list = [
    #     {
    #         'body' : 'Blog Post Body #1',
    #         'date_created' : dt.utcnow(),
    #         'author' : 'Mike Jones' ,

    #     },
    #     {
    #         'body' : 'Blog Post Body #2',
    #         'date_created' : dt.utcnow(),
    #         'author' : 'Mike Jones' ,

    #     },
    #     {
    #         'body' : 'Blog Post Body #3',
    #         'date_created' : dt.utcnow(),
    #         'author' : 'Mike Jones' ,

    #     },
    #     {
    #         'body' : 'Blog Post Body #4',
    #         'date_created' : dt.utcnow(),
    #         'author' : 'Mike Jones' ,

    #     },
#     # ]
#     return render_template('main/index.html', posts=[post.to_dict() for post in Post.query.order_by(Post.date_created.desc()).all()])

# @app.route('/profile')
# def profile():
#     return render_template('main/profile.html')
# @app.route('/contact')
# def contact():
#     return render_template('main/contact.html')

# @app.route('/user_list')
# def user_list():
#     return render_template('main/user_list.html')

# @app.route('/user/<id>')
# def user_single(id):
#     return render_template('main/user_list.html')











