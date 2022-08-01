from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def contact(request):
    return render(request, 'core/contact.html')
@api_view()
def sample(request):
    return Response({
        'status' : 200,
        'message':"Yes! Django rest framework is working!!!!"
    })
@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)

        print(data)
        return Response({
        'status' : 200,
        'message':"Success todo created"
    })
    except Exception as e:
        print(e)
    return Response({
        'status' : 200,
        'message':"Something went wrong"
    })





