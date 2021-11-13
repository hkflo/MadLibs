from flask import Flask, render_template, request
# from helpers import

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/multi_quiz', methods=["GET", "POST"])
def multi_quiz():
    if request.method == "POST":
        family_member_1: str = request.form['family_member_1']
        adjective_1: str = request.form['adjective_1']
        clothing_item_1: str = request.form['clothing_item_1']
        adjective_2: str = request.form['adjective_2']
        clothing_item_2: str = request.form['clothing_item_2']
        location_1: str = request.form['location_1']
        location_2: str = request.form['location_2']
        room_1: str = request.form['room_1']
      
        if family_member_1 == '' or adjective_1 == '' or clothing_item_1 == '' or adjective_2 == '' or clothing_item_2 == '' or location_1 == '' or location_2 == '' or room_1 == '':
            return render_template("multi_quiz.html")
        return render_template("multi_result.html")
    return render_template("multi_quiz.html")


@app.route('/basic_quiz', methods=["GET", "POST"])
def basic_quiz():
    if request.method == "POST":
       holiday_1: str = request.form['holiday_1']
       noun_1: str = request.form['noun_1']
       name_1: str = request.form['name_1']
       noun_2: str = request.form['noun_2']
       plural_noun_1: str = request.form['plural_noun_1']
       verb_1: str = request.form['verb_1']
       adjective_1: str = request.form['adjective_1']
       name_2: str = request.form['name_2']
       noun_3: str = request.form['noun_3']
       adjective_2: str = request.form['adjective_2']
       name_3: str = request.form['name_3']
       past_tense_verb_1: str = request.form['past_tense_verb_1']
       past_tense_verb_2: str = request.form['past_tense_verb_2']
 
 
       if holiday_1 == '' or noun_1 == '' or name_1 == '' or noun_2 == '' or plural_noun_1 == '' or verb_1 == '' or adjective_1 == '' or noun_3 == '' or name_2 == '' or adjective_2 == '' or name_3 == '' or past_tense_verb_1 == '' or past_tense_verb_2 == '':
           return render_template("basic_quiz.html")
       return render_template("basic_result.html", holiday_1=holiday_1, noun_1=noun_1, name_1=name_1, noun_2=noun_2, plural_noun_1=plural_noun_1, verb_1=verb_1, adjective_1=adjective_1, name_2=name_2, noun_3=noun_3, adjective_2=adjective_2, name_3=name_3, past_tense_verb_1=past_tense_verb_1, past_tense_verb_2=past_tense_verb_2)
    return render_template("basic_quiz.html")

if __name__ == '__main__':
    app.run(debug=True)