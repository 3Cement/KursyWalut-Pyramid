from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models import DBSession, Base, Waluta

name = "kursy"

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings, root_factory='kursy.models.Root')
    config.include('pyramid_chameleon')
    config.add_route('clean_database', '/')
    config.add_route('get_values', '/get')
    config.scan('.views')
    return config.make_wsgi_app()