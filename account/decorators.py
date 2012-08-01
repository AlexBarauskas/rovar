from google.appengine.api import users
from django.http import HttpResponseRedirect

class My_User():
    def __init__(self,u):
        if u:
            self.email = u.email or u._User__email
            self.nickname = u.nickname
    def get_and_delete_messages(*args):
        return None


def login_required(view_func):
    def new(request, *args, **kwargs):
        u = users.get_current_user()
        if u:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(users.create_login_url('/'))
    return new

def get_user(view_func):
    def new(request, *args, **kwargs):
        u = users.get_current_user()
        request.user = My_User(u)
        return view_func(request, *args, **kwargs)
    return new
