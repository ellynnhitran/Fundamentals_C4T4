from mongoengine import Document, StringField, ListField

class User(Document):
  username = StringField(max_length=200)
  password = StringField()
  favorite = ListField()
  