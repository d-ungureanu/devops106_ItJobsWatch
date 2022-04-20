from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods =["GET"])
def homepage():
    homepages = print("Homepage")


    return f"{"index.html}"

@app.route("/jobs",methods = ["GET","POST"])
def jobs():
    if request.method == "POST":
        job= print("Welcome to jobs")

        return redirect("/")
    else:
        return render_template (f"{jobs.html}")



@app.route("/roles", methods=["GET","POST"])
def roles():
    if request.method == "POST":
        role = print("Welcome to Roles")

        return redirect("/")

    else:
        return render_template("jobs.html")


@app.route("/skills",methods=["GET","POST"])
def skills():
    if request.method == "POST":
        role = print("Welcome to Skills")

        return redirect("/")

    else:
        return render_template("skills.html")

if__name__=="main":
    app.run()