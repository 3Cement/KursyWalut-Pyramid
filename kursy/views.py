import transaction, datetime, json, requests, sys
from pyramid.response import Response
from pyramid.view import view_config
from .models import DBSession, Waluta

class WalutyViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name='get_values', renderer='waluty_view.pt')
    def get_values(self):
        with transaction.manager:
            DBSession.query(Waluta).delete()
            transaction.commit()
            sys.stdout.write(u'Pobieram dane... ')
            sys.stdout.flush()
            try:
                page = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/')
            except Exception:
                print(u'Błąd pobrania danych z API NBP')
                sys.exit(1)

            page.raise_for_status
            currencies = json.loads(page.text)
            currencies_list = currencies[0]['rates']
            for i in currencies_list:
                with transaction.manager:
                    new_currency = Waluta(code=i['code'], name=i['currency'], price=i['mid'])
                    print(new_currency.name+' created!')
                    DBSession.add(new_currency)
                czas = datetime.datetime.now().time()

            waluty = DBSession.query(Waluta).order_by(Waluta.uid)
            return dict(title='Waluty View', waluty=waluty, czas=czas)

    @view_config(route_name='clean_database', renderer='clean_database.pt')
    def clean_database(self):
        DBSession.query(Waluta).delete()
        print('All Currencies deleted')
        return dict(title='Waluty View')

def walutypage_create():
    with transaction.manager:
        new_currency = Waluta(code='KOD5', name='Waluta1', price='1,11')
        DBSession.add(new_currency)
        print(new_currency.name+' created!')
        waluty = DBSession.query(Waluta).order_by(Waluta.uid)
        return dict(title='Waluty View', waluty=waluty, czas=czas)
