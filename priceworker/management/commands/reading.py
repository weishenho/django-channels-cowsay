from channels import Group
from django.core.management import BaseCommand
import time
import random
import subprocess
import json


#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Show this when the user types help
    help = "Simulates reading sensor and sending over Channel."
    
    # A command must define handle()
    def handle(self, *args, **options):
        while True:
            #x = subprocess.check_output(['fortune'])

            #cmd = "/usr/games/fortune | /usr/games/cowsay"
            cmd = "fortune | cowsay"
            ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            x = ps.communicate()[0]
            #xl = x.split("\n")
            Group("chat").send({'text': x})
            time.sleep(5)
            #print x
