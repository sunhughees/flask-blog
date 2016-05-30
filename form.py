from flask import Flask, render_template

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

app =Flask(__name__)

class MyForm(Form):
    name = StringField('name', validators=[DataRequired])

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/sucess')
    return render_template('submit.html', form=form)

if __name__ == '__main__':

    app.run()
