#encoding: utf-8

from django.contrib.auth import login,logout,authenticate
from django.views.decorators.http import require_POST
from .forms import LoginForm
from django.http import JsonResponse

@require_POST
def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        password = form.cleaned_data.get('password')
        remember = form.cleaned_data.get('remember')
        user = authenticate(request, username = telephone, password = password)

        if user:
            if user.is_active:
                logout(request, user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                print('1')
                return JsonResponse({"code": 200, "message":"", "data": {}})
            else:
                print('2')
                return JsonResponse({"code": 405, "message": "您的账户已经被冻结", "data": {}})
        else:
            print('3')
            return JsonResponse({"code": 400, "message": "手机或密码错误", "data": {}})
    else:
        errors = form.get_errors()
        return JsonResponse({"code": 400, "message": "", "data": errors})
