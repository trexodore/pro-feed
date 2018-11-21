import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MindMap_Labs_Website.settings')

import django
django.setup()

from Product_Feed.models import Feed
