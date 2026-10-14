from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from settings import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# Импорт маршрутов, моделей, форм, обработчиков и CLI-команд
from . import views, models, forms, error_handlers, cli_commands
