from django.shortcuts import render

# Create your views here.

def signup(request):
    if request.method == 'POST':
        print('post')
    else:
        print('just show form')
    return render(request, 'account/signup.html')