import sys
import logging

# Path to your app folder on the server
sys.path.insert(0, '/var/www/audrey/IMBUKA')

from app import app as application
