from __init__ import app, db
from forms import HelloForm
from models import Message
from flask import flash, redirect, url_for, render_template


@app.route('/', methods=['POST', 'GET'])
def index():
    # 从数据库拿数据，加载所有记录
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)  # 实例化模型类，创建记录
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))  # 重定向到index页面
    return render_template('index.html', form=form, messages=messages)
