from django.shortcuts import render
from django.http import JsonResponse
import os

# Create your views here.
def test(request):
    if request.POST['command'] == 'restart':
        print('chongqi')
        # os.system(r'C:\Users\Administrator\Desktop\illum\s.bat')
        return JsonResponse({'msg':'success'})
    else:
        return JsonResponse({'msg':'err'})