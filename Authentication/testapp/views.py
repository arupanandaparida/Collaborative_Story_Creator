from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignUpForm

def home_view(request):
    return render(request,'testapp/home.html')
from django.contrib.auth.decorators import login_required
@login_required

def java_view(request):
    return render(request,'testapp/java.html')
from django.contrib.auth.decorators import login_required
@login_required

def python_view(request):
    return render(request,'testapp/python.html')
from django.contrib.auth.decorators import login_required
def logout_view(request):
    return render(request,'testapp/logout.html')


def SignUp_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save the user yet
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()  
            return HttpResponseRedirect('/accounts/login')  
            print(form.errors)
    else:
        form = SignUpForm()
    
    return render(request, 'testapp/signup.html', {'form': form})
from django.shortcuts import render, get_object_or_404
from .models import Story  

def story_detail_view(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    
    if request.method == 'POST':
        new_line = request.POST.get('new_line')
        if new_line and story.contributions_count < 4: 
            story.add_line(new_line)  
    
    return render(request, 'testapp/story_detail.html', {'story': story})
