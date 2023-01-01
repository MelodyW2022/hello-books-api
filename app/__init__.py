from flask import Flask




def create_app(test_config=None):
    # create Flask applicaton object
    app = Flask(__name__)

    from .routes import books_bp
    app.register_blueprint(books_bp)
   
    return app