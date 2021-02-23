from app import application
from users import Users
from flask import render_template

@application.route('/list')
def index():
    users = Users.query.order_by(Users.id).all()
    return render_template('list.html', users=users)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port='8080')
