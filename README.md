# Kursy Walut - Pyramid

Jest to program synchronizujący aktualne kursy walut ze strony NBP.

Uruchamianie:
1. Stworzenie Virualenvironment:
	$ mkvirtualenv example_venv	
2. Instalacja, znajdując się w folderze /kursy w którym znajduje się setup.py:
	$ $VENV/bin/pip install -e .
3. Stworzenie bazy danych:
	$ $VENV/bin/initialize_kursy_db development.ini
4. Uruchomienie aplikacji:
	$ $VENV/bin/pserve development.ini
