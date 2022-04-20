from tkinter.tix import Select
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import GroceryStore, ItemCategory


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button

    title = StringField('Grocery Store',validators=[
            DataRequired(), 
            Length(min=3, max=80, message="Your message needs to be betweeen 3 and 80 chars")
        ])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')


class GroceryItemForm(FlaskForm):
  """Form for adding/updating a GroceryItem."""

  # TODO: Add the following fields to the form class:
  # - name - StringField
  # - price - FloatField
  # - category - SelectField (specify the 'choices' param)
  # - photo_url - StringField
  # - store - QuerySelectField (specify the `query_factory` param)
  # - submit button

  name = StringField('Item'
 )
  price = FloatField('Price')
  category = SelectField('Category', choices=ItemCategory.choices())
  photo_url = StringField('Photo')
  store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query, get_label='title')


  submit = SubmitField('Submit')

    
#  validators=[
      # Length(min=1, max=24, message="Item name needs to be betweeen 1 and 24 chars")
  # ]