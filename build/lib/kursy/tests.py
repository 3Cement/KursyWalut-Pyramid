import unittest
import transaction
from pyramid import testing


def _initTestingDB():
    from sqlalchemy import create_engine
    from .models import DBSession, Waluta, Base
    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)
    DBSession.configure(bind=engine)
    with transaction.manager:
        model = Waluta(code='XXX', name='Example', price='1,11')
        DBSession.add(model)
    return DBSession


class WalutyViewTests(unittest.TestCase):
    def setUp(self):
        self.session = _initTestingDB()
        self.config = testing.setUp()

    def tearDown(self):
        self.session.remove()
        testing.tearDown()

    def test_get_values_view(self):
        from kursy.views import WalutyViews

        request = testing.DummyRequest()
        inst = WalutyViews(request)
        response = inst.get_values()
        self.assertEqual(response['title'], 'Waluty View')


class WalutyFunctionalTests(unittest.TestCase):
    def setUp(self):
        from pyramid.paster import get_app
        app = get_app('development.ini')
        from webtest import TestApp
        self.testapp = TestApp(app)

    def tearDown(self):
        from .models import DBSession
        DBSession.remove()

    def test_it(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'Aktualne Kursy Walut', res.body)
        res = self.testapp.get('/get', status=200)
        self.assertIn(b'Aktualne Kursy Walut', res.body)