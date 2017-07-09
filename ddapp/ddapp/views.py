from django.shortcuts import render_to_response
# from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required


# @login_required
def home(request):
   # context = RequestContext(request,
   #                         {'request': request,
   #                         'user': request.user})
   context = {'request': request,
            'user': request.user}
   return render_to_response('home.html',
                             context=context)
