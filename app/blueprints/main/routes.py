
   
from flask import render_template, current_app as app, request, redirect, url_for, flash
from datetime import datetime as dt
from app.blueprints.blog.models import Post, User
from app import db, mail
from flask_login import current_user, login_required

@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # if current_user.is_authenticated:
    #     print(current_user.is_authenticated)
    #     print(current_user.is_anonymous)
    #     print(current_user.is_active)
    #     print(current_user.get_id())
    if request.method == 'POST':
        data = request.form.get('blog_post')

        p = Post(body=data, author=current_user.get_id())
        
        db.session.add(p)

        db.session.commit()

        flash('Post created', 'info')
        return redirect(url_for('home'))
    return render_template('main/home.html', posts=[post.to_dict() for post in current_user.followed_posts().all()])

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        form_data = request.form

        user = User.query.get(current_user.get_id())
    
        user.first_name = form_data.get('first_name')
        user.last_name = form_data.get('last_name')
        user.email = form_data.get('email')

        if len(form_data.get('password')) == 0:
            pass
        elif form_data.get('password') == form_data.get('confirm_password'):
            user.generate_password(form_data.get('password'))
        else:
            flash('Error updating your password', 'danger')
            return redirect(url_for('profile'))

        db.session.commit()
        # print(form_data.get('first_name'))
        # print(form_data.get('last_name'))
        # print(form_data.get('email'))
        # print(form_data.get('password'))
        # print(form_data.get('confirm_password'))
        flash('Your information has been updated', 'primary')
        return redirect(url_for('profile'))
    return render_template('main/profile.html', posts=[post.to_dict() for post in Post.query.filter_by(author=current_user.get_id()).order_by(Post.date_created.desc()).all()])
