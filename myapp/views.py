from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.db import models
from .models import User, Clue, Message
from .forms import HuntForm
from django.contrib.auth.decorators import login_required


#from django.http import HttpResponse


def login(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return redirect("/")

def create_hunt(request):
    if request.method == 'POST':
        form = HuntForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            clue_text = form.cleaned_data.get('clue_text')
            hint_text = form.cleaned_data.get('hint_text')
            location = form.cleaned_data.get('location')
            created_by = form.cleaned_data.get('created_by')

            latitude = request.POST.get('latitude', '')  
            longitude = request.POST.get('longitude', '')  

            new_submission = Clue.objects.create(
                title=title,
                clue_text=clue_text,
                hint_text=hint_text,
                location=location,
                created_by=created_by,
                submitted_by=request.user,
                latitude=latitude,
                longitude=longitude,
            )

            messages.success(request, 'Hunt created successfully.')
            return redirect('pending_submissions')  
    else:
        form = HuntForm()

    return render(request, 'create.html', {'form': form})

def view_submissions(request):
    submissions = Clue.objects.filter(was_verified=Clue.PENDING)
    return render(request, 'view_submissions.html', {'submissions': submissions})

def accept_submission(request, submission_id):
    submission = Clue.objects.get(id=submission_id)
    if request.method == 'POST':
        submission.was_verified = Clue.ACCEPTED
        submission.save()
        return redirect('view_submissions')
    return render(request, 'view_submissions.html', {'submissions': submission})

def decline_submission(request, submission_id):
    submission = Clue.objects.get(id=submission_id)
    if request.method == 'POST':
        decline_reason = request.POST.get('decline_reason')
        submission.was_verified = Clue.DENIED
        submission.decline_reason = decline_reason
        submission.save()
        decline_reason = f"Your submission has been declined. Reason: {decline_reason}"
    return render(request, 'view_submissions.html', {'submission': submission, 'decline_reason': decline_reason})

def pending_submissions(request):
    submissions = Clue.objects.filter(was_verified=Clue.PENDING, submitted_by=request.user)
    return render(request, 'pending_submissions.html', {'submissions': submissions, 'user': request.user})

def accepted_submissions(request):
    submissions = Clue.objects.filter(was_verified=Clue.ACCEPTED, submitted_by=request.user)
    return render(request, 'accepted_submissions.html', {'submissions': submissions, 'user': request.user})

def declined_submissions(request):
    submissions = Clue.objects.filter(was_verified=Clue.DENIED, submitted_by=request.user)
    return render(request, 'declined_submissions.html', {'submissions': submissions, 'user': request.user})

def choose_hunt(request):
    options = Clue.objects.exclude(submitted_by=request.user)
    options = options.filter(was_verified=Clue.ACCEPTED)
    return render(request, 'choose_hunt.html', {'options': options, 'user': request.user})

def activate_hunt(request, submission_id):
    submission = Clue.objects.get(id=submission_id) 
    if request.method == 'POST':
        submission.is_active = True
        Clue.objects.exclude(id=submission_id).update(is_active=False)
        submission.save()
        return redirect('choose_hunt')
    return render(request, 'choose_hunt.html')

def deactivate_hunt(request, submission_id):
    hunt = get_object_or_404(Clue, id=submission_id)
    hunt.is_active = False
    hunt.save()
    return redirect('choose_hunt')

#ADDED HERE
def map_with_hunt(request, submission_id):
    option = get_object_or_404(Clue, id=submission_id)
    active_hunt = Clue.objects.all()
    return render(request, 'map.html', {'o_lat':option.get_lat, 'o_lon':option.get_lon, 'user':request.user, 'active_hunt' : active_hunt})