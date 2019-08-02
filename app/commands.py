import click

from . import app
from . import db


@app.cli.command()
def initdb():
    db.create_all()
    click.echo("数据库初始化中。。。")
