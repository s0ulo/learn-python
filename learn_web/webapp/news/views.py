from flask import (
    abort,
    Blueprint,
    flash,
    current_app,
    render_template,
    redirect,
)
from flask_login import current_user, login_required

from webapp.db import db
from webapp.news.forms import CommentForm
from webapp.news.models import Comment, News
from webapp.weather import weather_by_city
from webapp.utils import get_redirect_target

blueprint = Blueprint("news", __name__)


@blueprint.route("/")
def index():
    title = "Python News"
    weather = weather_by_city(current_app.config["WEATHER_DEFAULT_CITY"])
    news_list = (
        News.query.filter(News.text.isnot(None))
        .order_by(News.published.desc())
        .all()
    )
    return render_template(
        "news/index.html",
        page_title=title,
        weather=weather,
        news_list=news_list,
    )


@blueprint.route("/news/<int:news_id>")
def single_news(news_id):
    my_news = News.query.filter(News.id == news_id).first()
    form = CommentForm(news_id=my_news.id)
    if not my_news:
        abort(404)

    return render_template(
        "news/single_news.html",
        page_title=my_news.title,
        news=my_news,
        comment_form=form,
    )


@blueprint.route("/news/comment", methods=["POST"])
@login_required
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(
            text=form.comment_text.data,
            news_id=form.news_id.data,
            user_id=current_user.id,
        )
        db.session.add(comment)
        db.session.commit()
        flash("Comment added!")
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(
                    'Error in field "{}": - {}'.format(
                        getattr(form, field).label.text, error
                    )
                )
    return redirect(get_redirect_target())
