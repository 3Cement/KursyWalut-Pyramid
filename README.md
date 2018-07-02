# Kursy Walut - Pyramid

Jest to program synchronizujący aktualne kursy walut ze strony NBP.

Wymagania:
requirments.txt
	Chameleon==3.3
	hupper==1.3
	kursy==0.0.1
	Mako==1.0.7
	MarkupSafe==1.0
	PasteDeploy==1.5.2
	plaster==1.0
	plaster-pastedeploy==0.5
	Pygments==2.2.0
	pyramid==1.9.2
	pyramid-chameleon==0.3
	pyramid-debugtoolbar==4.4
	pyramid-mako==1.0.2
	pyramid-tm==2.2
	repoze.lru==0.7
	requests==2.5.4.1
	SQLAlchemy==1.2.9
	transaction==2.2.1
	translationstring==1.3
	venusian==1.1.0
	waitress==1.1.0
	WebOb==1.8.2
	zope.deprecation==4.3.0
	zope.interface==4.5.0
	zope.sqlalchemy==1.0

Uruchamianie:
1. Stworzenie Virualenvironment
	$ mkvirtualenv my_pyramid2	
2. Instalacja, w folderze /kursy
	$ $VENV/bin/pip install -e .
3. Stworzenie bazy danych
	$ $VENV/bin/initialize_kursy_db development.ini
4. Uruchomienie aplikacji
	$ $VENV/bin/pserve development.ini
