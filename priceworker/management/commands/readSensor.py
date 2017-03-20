from channels import Group
from django.core.management import BaseCommand
import time
import random

#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Show this when the user types help
    help = "Simulates reading sensor and sending over Channel."
    
    # A command must define handle()
    def handle(self, *args, **options):
        while True:
            x = random.random()*10
            Group("chat").send({'text': "price reading = " + str(x)})
            time.sleep(2)
            print "price reading..." + str(x)
