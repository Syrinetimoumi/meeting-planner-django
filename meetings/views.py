from django.shortcuts import render, get_object_or_404,redirect

from .models import Meeting,Room

from .forms import MeetingForm

# Create your views here.


def detail(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

#def detail(request, id):
#    meeting = get_object_or_404(Meeting,id)
#    return render(request, "meetings/detail.html", {"meeting": meeting})

def rooms_list(request):
    return render(request, "meetings/rooms_list.html",
            {"rooms": Room.objects.all()})


def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})

def meetings_list_view(request):
        meetings = Meeting.objects.all()  # Get all meetings
        return render(request, 'meetings.html', {'meetings': meetings, })
    
def detail(request, id):
    meeting = get_object_or_404(Meeting, id=id)  # Correct model name and function
    return render(request, "detail.html", {"meeting": meeting})