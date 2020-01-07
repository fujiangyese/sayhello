from sayhello import app, db
import click


# 初始化数据库
@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    '''Initialize the database'''
    if drop:
        click.confirm('This operation will delete the data,do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized the database.')
