from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    news_id = HiddenField("News ID", validators=[DataRequired()])
    comment_text = StringField(
        "Comment text",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    submit = SubmitField("Submit", render_kw={"class": "btn btn-primary"})
