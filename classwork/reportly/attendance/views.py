from django.shortcuts import render, HttpResponse

# Create your views here.

# def test_view(request):
#     return HttpResponse('i am a very nice view!')
# def test_second(request):
#     return HttpResponse('i am learning view')    
def test_view(request):
    #print(request.user)
    return render(request, 'test.html')
