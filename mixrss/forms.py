import logging

logger = logging.getLogger(__name__)

from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class PortForm(FlaskForm):
    port = IntegerField("port of quorum", validators=[DataRequired()])
    submit = SubmitField("submit")

