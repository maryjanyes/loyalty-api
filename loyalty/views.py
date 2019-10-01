from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def auth(request):

    if 'logout' in request.GET:
        request.session['auth_key'] = None
        return HttpResponse('Since logout successfully.')

    else:
        auth_key = request.session.get('auth_key', None)

        if not auth_key:
            username = request.GET['username']
            email = request.GET['email']
            user = User.objects.filter(email=email)

            if not user or not user[0]:
                return HttpResponse('User with provided email does not found.')
            else:
                password = request.GET['password']
                user_alias = authenticate(username=username, password=password)

                if user_alias:
                    request.session['auth_key'] = user_alias.email
                    response = HttpResponse('User logged in!')
                    return response
                else:
                    return HttpResponse('Password that you provide do not valid.')