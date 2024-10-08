web: gunicorn proyecto.wsgi --log-file -

web: python app.py

web: node server.js

web: daphne -b 0.0.0.0 -p $PORT marvicare.asgi:application
