import os, sys
site_user_root_dir = '/home/d/drsashka/pravozanamy/public_html'
sys.path.insert(0, site_user_root_dir + '/simple-site')
sys.path.insert(1, site_user_root_dir + '/venv/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'this_site.settings.dev'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
