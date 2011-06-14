Requirements
============
* Django
	* sudo apt-get install python-django
* mod\_wsgi
	* sudo apt-get install libapache2-mod-wsgi
	* sudo a2enmod wsgi # enable it in apache.
* pylast
	* svn checkout http://pylast.googlecode.com/svn/trunk/ pylast-read-only
	* cd pylast-read-only
	* sudo python setup.py install

You will also need a LastFM account and a API account (http://www.last.fm/api/account).

Install with Apache
===================
* Get the code
	* $ git clone git://github.com/nikolaik/oliver\_screen.git
* Make available static files under oliver\_screen/oliver\_screen/static by symlinking or setup a <Directory> and Alias in your Apache config.
* Then setup a WSGIScriptAlias in your apache config pointing to the full path of django.wsgi.
	* sudo /etc/init.d/apache restart # load new Apache configuration settings
* Copy settings-sample.py to settings.py and edit to suit your needs.
	* Set MEDIA\_URL to the URL where static files are served.
	* Set LASTFM\_APIKEY and LASTFM\_API\_SECRET
* Create the database.
	* $ python manage.py syncdb (creating an admin user)
* Make sure the files have correct permission (readable by www-data).
	* If you created a sqlite database, make sure the file is writeable by www-data.
* Goto /admin and login with the admin user, then add a LastFMUser and make it active.
* Setup your music player (f.ex Spotify) to scrobble to that account Last.fm account.
* Goto / and you should be set :=)
