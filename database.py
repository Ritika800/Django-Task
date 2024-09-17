import django
from django.conf import settings

settings.configure(
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',  # Or provide a file-based database name for persistence
        }
    }
)

django.setup()

# Run migrations to create necessary tables
from django.core.management import call_command
call_command('migrate')


# database.py
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def save_signal(sender, instance, **kwargs):
    print("Signal executed")

# Main code
try:
    with transaction.atomic():
        user = User.objects.create(username='testuser')
        print("User created")
        raise Exception("Rolling back transaction")
except Exception as e:
    print(e)

