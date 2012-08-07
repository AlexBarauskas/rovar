from google.appengine.api import users
from django.http import HttpResponseRedirect
from account.models import Account


def login_required(view_func):
    def new(request, *args, **kwargs):
        u = users.get_current_user()
        if u:
            a = Account.objects.filter(email = u._User__email)
            if a:
                request.user = a[0]
                return view_func(request, *args, **kwargs)
        return HttpResponseRedirect(users.create_login_url('/accounts/login'))
    return new
