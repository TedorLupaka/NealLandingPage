from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm



app = Flask(__name__)

app.config["SECRET_KEY"] = "43efbb9e183b17d9621ed309216df4f2"


#Home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("Home.html", posts = posts)

@app.route("/about")
def about():
    return render_template("About.html", title="About")   

#Registration page 
@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template("Register.html", title="Register", form=form)

#Login page
@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@tulale.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessful. Please check username or password", "danger")
                
    return render_template("Login.html", title="login", form=form)              

if __name__ == "__main__":
    app.run(debug=true)      

@app.route("/demo")
def demo():
    return render_template("demo.html", title="demo") 