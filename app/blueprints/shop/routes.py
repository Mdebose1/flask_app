from flask import current_app as app, render_template



@app.route('/shop')
def shop():
    return render_template('main/shop.html')

@app.route('/shop/<id>')
def shop_single(id):
    return render_template('main/shop.html')

@app.route('/shop/cart')
def shop_cart():
    return render_template('main/shop.html')

@app.route('/shop/checkout')
def shop_checkout():
    return render_template('main/shop.html')