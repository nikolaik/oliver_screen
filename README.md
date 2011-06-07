Requirements
============
* python-django
* python-pylast

You will also need a LastFM account and a API account (http://www.last.fm/api/account).

Install with Apache
===================
* $ git clone git://github.com/nikolaik/oliver_screen.git
* Move and edit settings-sample.py to suit your needs.
* Make available static files under oliver_screen/oliver_screen/static by symlinking or setup a <Directory> and Alias in your Apache config.
* Set MEDIA_URL to the URL where static files are served.
* Set LASTFM_APIKEY and LASTFM_API_SECRET
* Make sure mod_wsgi is installed and enabled in Apache. First rename and edit django-sample.wsgi. Then setup a WSGIAlias in your apache config pointing to the .wsgi-file.
* $ python manage.py syncdb (creating an admin user)
* Make sure the files have correct permission (readable by www-data).
* Goto /admin and login with the admin user, then add a LastFMUser and make it active.
* Setup your music player (f.ex Spotify) to scrobble to that account Last.fm account.
* Goto / and you should be set :=)
