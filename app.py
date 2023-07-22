from flask import Flask, request, redirect


app = Flask(__name__, static_url_path='/static')


@app.route("/quiz")
def Quiz():
    page=""
    f=open("Quiz.html","r")
    page=f.read()
    f.close()
    return page
    

@app.route("/")
def MainPage():
    page=""
    f=open("mainpage.html","r")
    page=f.read()
    f.close()
    return page

@app.route("/united")
def United2026():
    page=""
    f=open("united.html","r")
    page=f.read()
    f.close()
    return page

@app.route("/champions")
def Winners():
    page=""
    f=open('winners.html',"r")
    page=f.read()
    f.close()
    return page

@app.route("/history")
def History():
    page=""
    f=open("history.html","r")
    page=f.read()
    f.close()
    return page


@app.route("/good_score")
def GoodScore():
    page=""
    f=open("goodscore.html",'r')
    page=f.read()
    f.close()
    return page

@app.route("/bad_score")
def BadScore():
    page=""
    f=open("badscore.html")
    page=f.read()
    f.close()
    return page


@app.route("/submit", methods=["POST"])
def submit():
    form = request.form
    score = 0
    page = ""
    if form["q1_answer"] == "1-2":
        score += 1

    if form["q2_answer"] == "Mbappe":
        score += 1
    
    if form["q3_answer"] == "No":
        score += 1

    if form["q4_answer"] == "morocco":
        score += 1
    
    if form["q5_answer"] == "no":
        score += 1

    if form["q6_answer"] == "mbappe":
        score += 1

    if form["q7_answer"] == "3-2":
        score += 1

    if form["q8_answer"] == "1-2":
        score += 1

    if form["q9_answer"] == "japan":
        score += 1

    if form["q10_answer"] == "QauterFinals":
        score += 1
    
    if score >= 5:
       page=""
       f=open("goodscore.html",'r')
       page=f.read()
       page = page.replace("{{score}}", str(score))
       f.close()
       return page
    else:
      page=""
      f=open("badscore.html","r")
      page=f.read()
      f.close()
      page = page.replace("{{score}}", str(score))
      return page
        

app.run(host='0.0.0.0', port=81, debug=True)
