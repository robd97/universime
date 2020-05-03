from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate, login


def home(request):
    template = loader.get_template('startpage.html')
    # TODO: check if the user is logged in before showing sign up page.

    context = {
        'title': 'UniversaMe',
        'bg_pic': 'pictures/home_bg_wp.jpg',
        'sign_up': SignUpForm,
        'sign_in': SignInForm,
    }
    return HttpResponse(template.render(context, request=request))


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.full_clean():
            form.save()
            user = authenticate(email=form['email'], password=['password'])
            if user:
                login(request, user)
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


