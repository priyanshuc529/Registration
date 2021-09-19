from flask import Flask,request,render_template,flash,redirect,url_for,abort,send_file
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from smtplib import SMTP
from flask_login import login_user,UserMixin,login_required,LoginManager,current_user,logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import csv

from form import Info,Login,Register
my_email = "jameswang8667@gmail.com"
my_password = "Jambajuice@713"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'allyouwannadoiscocohangingoutwithyouisnogo'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///forms.db'
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)


def csv_data(data):
    csv_datas = data
    with open(f"list.csv", 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(csv_datas)





class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pinnumber = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(500), nullable=False)
    phone = db.Column(db.String(500),unique=True, nullable=False)
    Batch = db.Column(db.String(500), nullable=True)
    email = db.Column(db.String(250), nullable=True)
    branch = db.Column(db.String(250), nullable=True)
    department = db.Column(db.String(250), nullable=True)

class Admin(db.Model,UserMixin):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(500), nullable=False)
    password = db.Column(db.String(500), nullable=False)



@app.route("/",methods = ['GET','POST'])
def home():
    form = Info()
    filled = False
    if form.validate_on_submit():
        if "@gitam.in" in form.email.data:
            name = form.name.data
            filled = True
            new_user = User(name = form.name.data,
                            phone = form.phone.data,
                            pinnumber = form.Pinnumber.data,
                            Batch =form.Batch.data,
                            branch = form.Branch.data,
                            department = form.Department.data,
                            email = form.email.data)

            db.session.add(new_user)
            db.session.commit()
            with SMTP('smtp.gmail.com',587,timeout=180) as connection:
                connection.starttls()
                connection.login(user=my_email,password=my_password)
                info = f"Subject:INFO\n\nname{form.name.data}\nphone:{form.phone.data}\nbatch:{form.Batch.data}\nbranch:{form.Branch.data}\nemail:{form.email.data}\ndepartment:{form.Department.data}\ndepartment:{form.Pinnumber.data}"
                message = f"Subject:DONTREPLY APPLICATION RECIEVED\n\nThank you {name}\n we will get back to you as soon as possible till then enjoy our anime "
                connection.sendmail(from_addr=my_email,to_addrs="priyanshuc4423@gmail.com",msg=info)
                connection.sendmail(from_addr=my_email, to_addrs=f"{form.email.data}", msg=message)

            return render_template('index.html',name = name,filled = filled)
        else:
            flash("please enter a gitam maild in mail column")
            return render_template('index.html',filled = filled,form = form)


    return render_template('index.html',form = form,filled=filled)

@app.route('/video')
def video():
    return render_template('impossible.html')

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))



@app.route('/login',methods = ["GET","POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        password = form.password.data
        email = form.email.data
        user = Admin.query.filter_by(email=email).first()
        if user:
           if check_password_hash(user.password,password):
               login_user(user)
               return redirect(url_for('data'))
           else:
                flash("Invalid Password")

        else:
            flash("This email is not present in our database")
    return render_template('login.html',form=form,current_user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id == 1 and current_user.is_authenticated:
            return f(*args, **kwargs)
        else:
            return abort(403,description="Your dont have credibility")

    return decorated_function

@app.route("/8738930271",methods = ['GET','POST'])
@login_required
@admin_only
def data():
    form = db.session.query(User).all()
    csv_datas = [['id','pinnumber', 'name', 'phone', 'batch', 'branch', 'department', 'email']]
    for data in form:
        id = data.id
        pin = data.pinnumber
        name = data.name
        phone = data.phone
        batch = data.Batch
        branch = data.branch
        department = data.department
        email = data.email
        csv_datas.append([id,pin,name,phone,batch,branch,department,email])
    csv_data(csv_datas)


    return render_template('data.html',form =form)

@app.route("/39748743786")
@admin_only
@login_required
def download():
    return send_file('list.csv')


if __name__ == "__main__":
    app.run(debug=True)

