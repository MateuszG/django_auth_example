from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse


def login_view(request):
    language = 'en'
    session_language = 'en'

    context = {}
    context.update(csrf(request))
    if 'lang' in request.COOKIES:
        lang = request.COOKIES['lang']
        context.update({'language': lang})

    if 'lang' in request.session:
        session_lang = request.session['lang']
        context.update({'session_language': session_lang})

    return render_to_response('login.html', context)


def auth_and_login(request, onsuccess='/', onfail='/login/'):
    user = authenticate(
        username=request.POST['email'], password=request.POST['password']
    )
    if user is not None:
        login(request, user)
        return redirect(onsuccess)
    else:
        return redirect(onfail)


def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user


def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True


def register(request):
    post = request.POST
    if not user_exists(post['email']):
        create_user(
            username=post['email'], email=post['email'],
            password=post['password']
        )
        return auth_and_login(request)
    else:
        return redirect("/login/")


@login_required(login_url='/login/')
def secured(request):
    lang = 'en'
    session_lang = 'en'
    context = {}

    if 'lang' in request.COOKIES:
        lang = request.COOKIES['lang']

    if 'lang' in request.session:
        session_lang = request.session['lang']

    return HttpResponse(
        'Access OK, Cookie language is {}, Session Language is {}'
        .format(lang, session_lang)
    )


def logout_view(request):
    logout(request)
    return redirect("/login/")


def language(request, lang='en'):
    response = HttpResponse('Setting language to {}'.format(lang))
    response.set_cookie('lang', lang)
    request.session['lang'] = lang

    return response
