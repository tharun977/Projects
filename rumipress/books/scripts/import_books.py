import os
import sys
import django # type: ignore

# Add the path to your Django project directory
sys.path.append('C:\\Users\\Tharun Raman\\OneDrive\\Documents\\tharun\\Project\\rumipress')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rumipress.settings')
django.setup()

# Import your models correctly
