import os
import django
from pathlib import Path

proj_root = Path(__file__).resolve().parent.parent
import sys
sys.path.insert(0, str(proj_root))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from portfolio.models import Project

samples = [
    {
        'title': 'TaskMaster Pro',
        'description': 'A productivity app to manage tasks, deadlines, and team collaboration with a minimal interface.',
        'link': ''
    },
    {
        'title': 'EcoMarket',
        'description': 'A small marketplace prototype focused on eco-friendly products with search and basic checkout flow.',
        'link': ''
    }
]

for s in samples:
    p, created = Project.objects.get_or_create(title=s['title'], defaults={'description': s['description'], 'link': s['link']})
    if created:
        print('Created', p.title)
    else:
        print('Exists', p.title)

