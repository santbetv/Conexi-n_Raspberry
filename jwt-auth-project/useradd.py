#-*-coding: utf-8 -*-
import click

from jwtprueba.database import db_session
from jwtprueba.models import User
from passlib.hash import pbkdf2_sha256


@click.command()
@click.option('--username', prompt='Ingrese el usuario',
              help='Nombre de usuario')
@click.option('--password', prompt='Ingrese la contraseña',
              confirmation_prompt=True, hide_input=True,
              help='Contraseña para el usuario')
def useradd(username, password):
    db_session.add(User(username, pbkdf2_sha256.hash(password)))
    db_session.commit()


if __name__ == '__main__':
    useradd()