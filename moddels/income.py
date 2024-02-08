from mongoengine import Document, StringField, DecimalField, DateTimeField

class Income(Document):
    title = StringField(required=True)
    amount = DecimalField(required=True)
    category = StringField(required=True)
    description = StringField(required=True)
    date = DateTimeField(required=True)
