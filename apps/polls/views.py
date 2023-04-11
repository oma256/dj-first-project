import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def polls(request):
    if request.method == 'GET':
        return JsonResponse({'status': 'Get OK'}, status=200)
    elif request.method == 'POST':
        print(json.loads(request.body).get('name'))
        return JsonResponse({'status': 'Post OK'}, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class PollsView(View):

    def get(self, *args, **kwargs):
        return JsonResponse({'status': 'Get OK'})

    def post(self, *args, **kwargs):
        return JsonResponse({'status': 'Post OK'})
