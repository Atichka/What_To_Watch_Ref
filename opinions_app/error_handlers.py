from flask import render_template

from . import app


@app.errorhandler(404)
def page_not_found(error):
    """Обработчик ошибки 404 — страница не найдена."""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Обработчик ошибки 500 — внутренняя ошибка сервера."""
    return render_template('500.html'), 500
