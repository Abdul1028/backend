from flask_mongoengine import MongoEngine

database = MongoEngine()

def initialize_db(app):
    app.config['MONGODB_SETTINGS'] = {
        'db': 'test',
        'host': 'mongodb+srv://adwaitthakur100:Adwait%40100@cluster0.ybcyebv.mongodb.net/?retryWrites=true&w=majority',
    }
    database.init_app(app)
