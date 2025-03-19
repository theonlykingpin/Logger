from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    """
    Handle user registration.
    
    :param request: HttpRequest object
    :return: HttpResponse object
    """
    try:
        if request.method == 'POST':
            form = UserCreationForm(data=request.POST)
            if form.is_valid():
                new_user = form.save()
                login(request, new_user)
                messages.success(request, "Registration successful. Welcome!")
                return redirect('core:index')
            else:
                messages.error(request, "Please correct the error below.")
        else:
            form = UserCreationForm()
        
        context = {'form': form}
        return render(request, 'registration/register.html', context)
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
        return redirect('core:index')
