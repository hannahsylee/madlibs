from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route('/')
def story_template():
    return render_template("select_story.html", stories=stories.values())


@app.route('/questions')
def ask_questions():
    """Shows question page"""
    story_id = request.args["story_id"]
    story = stories[story_id]

    prompts = story.prompts
    return render_template("questions.html", story_id=story_id, title=story.title, prompts=prompts)


@app.route('/story')
def show_story():
    """Shows story Form"""
    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)
    return render_template("stories.html", story_id=story_id, title=story.title, text=text)