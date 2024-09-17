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


# syncs.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def slow_signal(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(5)  # Simulate a slow task
    print("Signal finished")

# Create a user and trigger the signal
user = User.objects.create(username='testuser')
print("User created")