from django.shortcuts import render
from first_app.models import Topic, WebPage, AccessRecord

def index(request):
    access_records = AccessRecord.objects.select_related('user').order_by('date')  # Ensure to select related user
    my_dict = {"access_records": access_records}
    return render(request, 'first_app/index.html', context=my_dict)
