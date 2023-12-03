from fakepinterest import database, app
from fakepinterest.models import Usuarios, Foto


with app.app_context():
    database.create_all()