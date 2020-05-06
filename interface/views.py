from django.http import HttpResponse
from django.template import loader
from .forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate, login
from interface.models import User
from django.conf import settings


def home(request):
    if request.user.is_authenticated:
        user = User.objects.get(email=request.user.email)
        #return HttpResponse(settings.MEDIA_ROOT + user.profile_image.url)
    else:
        user = None

    template = loader.get_template('startpage.html')
    # TODO: check if the user is logged in before showing sign up page.

    context = {
        'title': 'UniversaMe',
        'bg_pic': 'pictures/home_bg_wp.jpg',
        'sign_up': SignUpForm,
        'sign_in': SignInForm,
        'user': user,
    }
    return HttpResponse(template.render(context, request=request))


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request,
                            username= form.cleaned_data.get('email'),
                            password= form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return home(request)
            else:
                # TODO: create login failed
                return HttpResponse('User does not exist.')

        else:
            # TODO: invalid sign up credentials.

            return HttpResponse('Form is invalid')

    else:
        template = loader.get_template('sign_up.html')
        context = {
            'title': 'Sign Up',
            'bg_pic': 'pictures/home_bg_wp.jpg',
            'sign_up': SignUpForm,
            'sign_in': SignInForm,
        }
        return HttpResponse(template.render(context, request=request))


def signin(request):
    template = loader.get_template('sign_in.html')
    context = {
        'title': 'Sign In',
        'bg_pic': 'pictures/home_bg_wp.jpg',
        'sign_in': SignInForm,
    }
    return HttpResponse(template.render(context, request=request))


