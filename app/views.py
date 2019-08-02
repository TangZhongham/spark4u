from . import app, db
from .models import Idea
from .forms import IdeaForm

from flask import redirect, flash, render_template, url_for


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Idea.query.order_by(Idea.timestamp.desc()).all()
    form = IdeaForm()
    if form.validate_on_submit():
        topic = form.topic.data
        idea = form.idea.data
        writer = form.writer.data
        msg = Idea(topic=topic, idea=idea, writer=writer)
        db.session.add(msg)
        db.session.commit()
        flash("你的好点子已经提交！")
        return redirect(url_for('index'))
    return "Hello World"
