import os
import django
import secrets
import sys
import traceback
from pathlib import Path

print('PWD=', os.getcwd())
print('PYTHON=', sys.executable)

try:
    # Ensure project root is on sys.path so 'mysite' can be imported when this
    # script is executed from the scripts/ directory.
    proj_root = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(proj_root))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    django.setup()

    from django.contrib.auth import get_user_model
    User = get_user_model()

    email = 'lekalderonicky@gmail.com'
    username = email.split('@')[0]

    if User.objects.filter(email=email).exists():
        print('EXISTS')
    else:
        pwd = secrets.token_urlsafe(12)
        User.objects.create_superuser(username=username, email=email, password=pwd)
        print('CREATED', username, email)
        print('PASSWORD', pwd)
except Exception:
    print('ERROR creating superuser', file=sys.stderr)
    traceback.print_exc()
