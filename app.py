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
        
        return render_template("multi_result.html", family_member_1=family_member_1, adjective_1=adjective_1, clothing_item_1=clothing_item_1, adjective_2=adjective_2, clothing_item_2=clothing_item_2, location_1=location_1, location_2=location_2, room_1=room_1)
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

@app.route('/story_scene', methods=["GET", "POST"])
def story_scene():
    if request.method == "POST":
        celebrity_1: str = request.form['celebrity_1']
        location_1: str = request.form['location_1']
        adjective_1: str = request.form['adjective_1']
        noun_1: str = request.form['noun_1']
        if celebrity_1 == '' or location_1 == '' or adjective_1 == '' or noun_1 == '':
            return render_template("story_scene.html")
        return render_template("story_scene_result.html", celebrity_1=celebrity_1, location_1=location_1, adjective_1=adjective_1, noun_1=noun_1)
    return render_template("story_scene.html")
 

@app.route('/story_scene_result', methods=["GET", "POST"])
def story_scene_result():
    if request.method == "POST":
        choice_1: str = request.form['choice_1']
        if choice_1 == 'run':
            return render_template("story_run.html")
        return render_template("story_arrested.html")
    return render_template("story_scene_result.html")

 
 
@app.route('/story_run', methods=["GET", "POST"])
def story_run():
    if request.method == "POST":
        animal_1: str = request.form['animal_1']
        color_1: str = request.form['color_1']
        color_2: str = request.form['color_2']
        sound_effect_plural_1: str = request.form['sound_effect_plural_1']
        if animal_1 == '' or color_1 == '' or color_2 == '' or sound_effect_plural_1 == '':
            return render_template("story_run.html")
        return render_template("story_run_result.html", animal_1=animal_1, color_1=color_1, color_2=color_2, sound_effect_plural_1=sound_effect_plural_1)
    return render_template("story_run.html")
 
 
@app.route('/story_run_result', methods=["GET", "POST"])
def story_run_result():
    if request.method == "POST":
        choice_run: str = request.form['choice_run']
        if choice_run == 'hide':
            return render_template("story_hide.html")
        if choice_run == 'keep':
            return render_template("story_keep.html")
    return render_template("story_run_result.html")
 

@app.route('/story_hide', methods=["GET", "POST"])
def story_hide():
    if request.method == "POST":
        plural_body_part_1: str = request.form['plural_body_part_1']
        verb_1: str = request.form['verb_1']
        time_1: str = request.form['time_1']
        facial_feature_1: str = request.form['facial_feature_1']
        if plural_body_part_1 == '' or verb_1 == '' or time_1 == '' or facial_feature_1 == '':
            return render_template("story_hide.html")
        return render_template("story_hide_result.html", plural_body_part_1=plural_body_part_1, verb_1=verb_1, time_1=time_1, facial_feature_1=facial_feature_1)
    return render_template("story_hide.html")
 
 
@app.route('/story_keep', methods=["GET", "POST"])
def story_keep():
    if request.method == "POST":
        verb_1: str = request.form['verb_1']
        verb_2: str = request.form['verb_2']
        noun_1: str = request.form['noun_1']
        if verb_1 == '' or verb_2 == '' or noun_1 == '':
            return render_template("story_keep.html")
        return render_template("story_keep_result.html", verb_1=verb_1, verb_2=verb_2, noun_1=noun_1)
    return render_template("story_keep.html")
 
 
@app.route('/story_arrested', methods=["GET", "POST"])
def story_arrested():
    if request.method == "POST":
        adjective_1: str = request.form['adjective_1']
        adjective_2: str = request.form['adjective_2']
        verb_1: str = request.form['verb_1']
        if adjective_1 == '' or adjective_2 == '' or verb_1 == '':
            return render_template("story_arrested.html")
        return render_template("story_arrested_result.html", adjective_1=adjective_1, adjective_2=adjective_2, verb_1=verb_1)
    return render_template("story_arrested.html")
 
 
@app.route('/story_arrested_result', methods=["GET", "POST"])
def story_arrested_result():
    if request.method == "POST":
        choice_arrested: str = request.form['choice_arrested']
        if choice_arrested == '':
            return render_template("story_arrested_result.html")
        if choice_arrested == 'guilty':
            return render_template("story_guilty.html")
        if choice_arrested == 'insanity':
            return render_template("story_insanity.html")
    return render_template("story_arrested_result.html")
 
 
@app.route('/story_guilty', methods=["GET", "POST"])
def story_guilty():
    if request.method == "POST":
        location_1: str = request.form['location_1']
        time_1: str = request.form['time_1']
        question_1: str = request.form['question_1']
        if location_1 == '' or time_1 == '' or question_1 == '':
            return render_template("story_guilty.html")
        return render_template("story_guilty_result.html", location_1=location_1, time_1=time_1, question_1=question_1)
    return render_template("story_guilty.html")
 
 
@app.route('/story_insanity', methods=["GET", "POST"])
def story_insanity():
    if request.method == "POST":
        past_verb_1: str = request.form['past_verb_1']
        noun_1: str = request.form['noun_1']
        if past_verb_1 == '' or noun_1 == '':
            return render_template("story_insanity.html")
        return render_template("story_insanity_result.html", past_verb_1=past_verb_1, noun_1=noun_1)
    return render_template("story_insanity.html")
 

if __name__ == '__main__':
    app.run(debug=True)