from django.shortcuts import render, redirect
from .forms import UserForm

def user(request):
    user = {}
    form = UserForm
    if request.POST:
        form = UserForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # print(cd)
            # user['first_name'] = cd['first_name']
            # # print(user)
            User.object.create(
                first_name=cd['first_name'],
                last_name=cd['last_name'],
                age=cd['age'],
                email=cd['email'],
            )
            return redirect('user')
    return render(request, 'base.html', {'form': form})


