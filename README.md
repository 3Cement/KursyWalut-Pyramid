# Kursy Walut - Pyramid

Jest to program synchronizujący aktualne kursy walut ze strony NBP.


Uruchamianie za pomocą PyPI:

1. Stworzenie nowego środowiska np z urzyciem virtualenvwrapper:
  https://virtualenvwrapper.readthedocs.io/en/latest/
  $ pip install virtualenvwrapper
  $ mkvirtualenv nowy_env

2. Instalacja i uruchomienie za pomocą PyPI:
  (nowy_env) $ pip install waitress pyramid-tm zope.sqlalchemy pyramid-chameleon pyramid-debugtoolbar
  (nowy_env) $ python3 -m pip install --index-url https://test.pypi.org/simple/ kursy

3. Uruchomienie i stworzenie nowej bazy danych:
  (nowy_env) $ initialize_kursy_db development.ini

4. Włączenie projektu:
  (nowy_env) $ kursy_run development.ini
  
  
Uruchamianie poprzez skolonowanie plików z Githuba:

1. Pobranie plików:
  $ git clone https://github.com/3Cement/KursyWalut-Pyramid

2. Instalacja, w folderze gdzie znajduje się setup.py:
 $ pip install -e .
 
3. Uruchomienie i stworzenie nowej bazy danych:
  (nowy_env) $ initialize_kursy_db development.ini

4. Włączenie projektu:
  (nowy_env) $ kursy_run development.ini
 
