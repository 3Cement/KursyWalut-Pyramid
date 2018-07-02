# Kursy Walut - Pyramid

Jest to program synchronizujący aktualne kursy walut ze strony NBP.

Instalacja i uruchamianie:

1. Stworzenie virualenvironment:

	$ mkvirtualenv example_venv	
2. Sklonowanie repozytorium:

 	$ git clone https://github.com/3Cement/KursyWalut-Pyramid
3. Instalacja, znajdując się w folderze /kursy w którym znajduje się setup.py:
	
	$ $VENV/bin/pip install -e .
4. Stworzenie bazy danych:
	
	$ $VENV/bin/initialize_kursy_db development.ini
5. Uruchomienie testów:
	
	$ py.test tutorial/tests.py -q
6. Uruchomienie aplikacji:
	
	$ $VENV/bin/pserve development.ini

7. Pobranie i wyświetlenie aktualnych kursów walut następuje po kliknięciu linku "Pobierz aktualne kursy walut"

8. Wyczyszczenie bazy danych następuje po kliknięciu linku "Wyczyść bazę danych"


Instalacja za pomocą PyPI https://test.pypi.org/project/kursy/

1. Stworzenie virualenvironment:
	
	$ mkvirtualenv example_venv
2. Instalacja za pomocą pip:

	$ mkvirtualenv python -m pip install --index-url https://test.pypi.org/simple/ kursy
