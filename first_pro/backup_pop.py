from faker import Faker
import random
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_pro.settings')
import django
django.setup()

from first_app.models import Topic, WebPage, AccessRecord
from django.contrib.auth.models import User

fake = Faker()

# Create topics
fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
	t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
	t.save()
	return t 
	
def populate(N=5):
    for _ in range(N):
        # Get the topic for the entry
        top = add_topic()

        # Create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create a random user
        user = User.objects.order_by('?').first()

        # Create a fake access record for that webpage with a random user
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date, user=user)[0]
        


if __name__ == '__main__':
	print("populating script!")
	populate(20)
	print("populating complete")







