#Dinu Ion Irinel 315CA

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index")


def home():
    
    education = {'university': 'UNIVERSITY : 2020-2024 The Faculty of Automatic Control and Computers UPB ', 
    'high_s': 'HIGH-SCHOOL : 2016 -2020 LTAC Anghel Saligny Cernavoda', 'primary_s' : "PRIMARY-SCHOOL : School 2, Com.Rasova,Constanta"}

    projects = {'project1' : "Some games created using C++/C", 'project2': "A simple To-do list site for a programmer", 
    'project3': "A schedule site for University", 'projects4' : "A calculator and a modern clock created using P5.js",
    'git': "https://github.com/dinuionica08", 'languages' : "Languages: C++/C, Javascript, Python"}
    
    work_exp = {'position:' : "Junior Software Developer", 'company' : "Mystery", 'period': 'June 2021 - September 2021'}
    
    courses = {'type' : "Coursera, Udemy, Wellcode "}

    return render_template('index.html', title = 'Home', intro = "I'm Dinu Ion Irinel", education = education, projects = projects,
    work_exp = work_exp, courses = courses)



@app.route("/contact",methods=["POST", "GET"])

def contact():

    info = {'message' : "I'm Dinu Ion Irinel"}

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        f = open("contact-mail.txt", "a")
        f.write("Name : " + name + "\n" + "Email : " + email + "\n" + "Message : " + message + "\n")
        f.close()

    return render_template('contact.html', title = 'Contact', intro = "Send Me A Message")

  


if __name__ == "__main__":

    app.run(host = '0.0.0.0', debug = True , port = 5000);