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



# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def check_thread(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")

# Main code
def create_user():
    print(f"Main code running in thread: {threading.current_thread().name}")
    user = User.objects.create(username='testuser')

# Trigger the signal
create_user()