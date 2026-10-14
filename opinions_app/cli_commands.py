import csv

import click

from . import app, db
from .models import Opinion


@app.cli.command('load_opinions')
def load_opinions_command():
    """Загружает мнения из CSV-файла в базу данных."""
    with open('opinions.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            opinion = Opinion(
                title=row['title'],
                text=row['text'],
                source=row.get('source'),
                added_by=row.get('added_by'),
            )
            db.session.add(opinion)
        db.session.commit()
    click.echo('Мнения загружены в базу данных.')
