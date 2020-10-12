from django.shortcuts import render
from .models import Job

def home(request):
    jobs = Job.objects
    # for i in jobs.all():
        # print ("iiiiisssjksfjldjfklasjdflkajsdlfj================",i,i.summary)
    return render(request=request,template_name='jobs/home.html',context={'jobs':jobs})

# Create your views here.
