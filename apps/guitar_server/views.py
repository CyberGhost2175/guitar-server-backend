from django.shortcuts import render
from rest_framework import status
from apps.guitar_server.models import *
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from apps.guitar_server.serializers import *
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from django.core.mail import send_mail
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.utils import timezone
import jwt, datetime
import pickle
import re


@api_view(['GET', 'POST', 'DELETE'])
def guitars_list(request):
    if request.method == 'GET':
        guitars= Guitar.objects.all()
        brand = request.GET.get('brand', None)
        if brand is not None:
            guitars = guitars.filter(guitar__icontains=brand)
        guitars_serializers= GuitarSerializer(guitars, many=True)
        return JsonResponse(guitars_serializers.data, safe=False)
    elif request.method =='POST':
        guitar_data = JSONParser().parse(request)
        guitar_serializer= GuitarSerializer(data = guitar_data)
        if guitar_serializer.is_valid():
            guitar_serializer.save()
            return  JsonResponse(guitar_serializer.data , status=status.HTTP_201_CREATED)
        return JsonResponse(guitar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        counter = Guitar.objects.all().delete()
        return JsonResponse({'message': 'deleted'.format(counter[0])})    


@api_view(['GET', 'PUT', 'DELETE'])
def guitar_by_id(request, id):
    try:
        guitar= Guitar.objects.get(id= id)
    except Guitar.DoesNotExist:
        return JsonResponse({'message: Guitar does not exist'}, status=status.HTTP_404_NOT_FOUND,safe=False)

    if request.method == 'GET':
        guitar_serializer = GuitarSerializer(guitar)
        return JsonResponse(guitar_serializer.data)

    elif request.method == 'PUT':    
        new_data= JSONParser().parse(request)
        guitar_serializer= GuitarSerializer(guitar, data= new_data)
        if guitar_serializer.is_valid():
            guitar_serializer.save()
            return  JsonResponse(guitar_serializer.data)
        return JsonResponse(guitar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        guitar.delete()
        return JsonResponse({'message: the guitar was deleted'})    


@api_view(['GET', 'POST', 'DELETE'])
def amplifier_list(request):
    if request.method == 'GET':
        amplifiers= Amplifier.objects.all()
        brand = request.GET.get('brand', None)
        if brand is not None:
            amplifiers = amplifiers.filter(amplifier__icontains=brand)
        amplifier_serializer= AmplifierSerializer(amplifiers, many=True)
        return JsonResponse(amplifier_serializer.data, safe=False)
    elif request.method =='POST':
        amplifier_data = JSONParser().parse(request)
        amplifier_serializer= AmplifierSerializer(data = amplifier_data)
        if amplifier_serializer.is_valid():
            amplifier_serializer.save()
            return  JsonResponse(amplifier_serializer.data , status=status.HTTP_201_CREATED)
        return JsonResponse(amplifier_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        counter = Amplifier.objects.all().delete()
        return JsonResponse({'message': 'deleted'.format(counter[0])})    


@api_view(['GET', 'PUT', 'DELETE'])
def amplifier_by_id(request,id):
    try:
        amplifier= Amplifier.objects.get(id= id)
    except Amplifier.DoesNotExist:
        return JsonResponse({'message': 'Amplifier does not exist'}, status=status.HTTP_404_NOT_FOUND, safe=False)

    if request.method == 'GET':
        amplifier_serializer = AmplifierSerializer(amplifier)
        return JsonResponse(amplifier_serializer.data)

    elif request.method == 'PUT':    
        new_data= JSONParser().parse(request)
        amplifier_serializer= AmplifierSerializer(amplifier, data= new_data)
        if amplifier_serializer.is_valid():
            amplifier_serializer.save()
            return  JsonResponse(amplifier_serializer.data)
        return JsonResponse(amplifier_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        amplifier.delete()
        return JsonResponse({'message: the amplifier was deleted'})    


@api_view(['GET', 'POST', 'DELETE'])
def pick_list(request):
    if request.method == 'GET':
        picks= Pick.objects.all()
        brand = request.GET.get('brand', None)
        if brand is not None:
            picks = picks.filter(pick__icontains=brand)
        pick_serializer= PickSerializer(picks, many=True)
        return JsonResponse(pick_serializer.data, safe=False)
    elif request.method =='POST':
        pick_data = JSONParser().parse(request)
        pick_serializer= PickSerializer(data = pick_data)
        if pick_serializer.is_valid():
            pick_serializer.save()
            return  JsonResponse(pick_serializer.data , status=status.HTTP_201_CREATED)
        return JsonResponse(pick_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        counter = Pick.objects.all().delete()
        return JsonResponse({'message': 'deleted'.format(counter[0])})   


@api_view(['GET', 'PUT', 'DELETE'])
def pick_by_id(request,id):
    try:
        pick= Pick.objects.get(id= id)
    except Pick.DoesNotExist:
        return JsonResponse({'message': 'Pick does not exist'}, status=status.HTTP_404_NOT_FOUND, safe=False)

    if request.method == 'GET':
        pick_serializer = PickSerializer(pick)
        return JsonResponse(pick_serializer.data)   

    elif request.method == 'PUT':    
        new_data= JSONParser().parse(request)
        pick_serializer= PickSerializer(pick, data= new_data)
        if pick_serializer.is_valid():
            pick_serializer.save()
            return  JsonResponse(pick_serializer.data)
        return JsonResponse(pick_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        pick.delete()
        return JsonResponse({'message: the pick was deleted'})

@api_view(['GET', 'POST', 'DELETE'])
def capos_list(request):
    if request.method == 'GET':
        capos= Capo.objects.all()
        brand = request.GET.get('brand', None)
        if brand is not None:
            capos = capos.filter(capo__icontains=brand)
        capo_serializer= CapoSerializer(capos, many=True)
        return JsonResponse(capo_serializer.data, safe=False)
    elif request.method =='POST':
        capo_data = JSONParser().parse(request)
        capo_serializer= CapoSerializer(data = capo_data)
        if capo_serializer.is_valid():
            capo_serializer.save()
            return  JsonResponse(capo_serializer.data , status=status.HTTP_201_CREATED)
        return JsonResponse(capo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        counter = Capo.objects.all().delete()
        return JsonResponse({'message': 'deleted'.format(counter[0])})     

@api_view(['GET', 'PUT', 'DELETE'])
def capo_by_id(request,id):
    try:
        capo= Capo.objects.get(id= id)
    except Capo.DoesNotExist:
        return JsonResponse({'message': 'Capo does not exist'}, status=status.HTTP_404_NOT_FOUND, safe=False)

    if request.method == 'GET':
        capo_serializer = CapoSerializer(capo)
        return JsonResponse(capo_serializer.data)   

    elif request.method == 'PUT':    
        new_data= JSONParser().parse(request)
        capo_serializer= CapoSerializer(capo, data= new_data)
        if capo_serializer.is_valid():
            capo_serializer.save()
            return  JsonResponse(capo_serializer.data)
        return JsonResponse(capo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        capo.delete()
        return JsonResponse({'message: the capo was deleted'})            





           













class RegisterView(APIView):
    
    def post(self, request):
        email = request.data['email']
        serializer = UserSerializer(data=request.data)
        pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net|ru)"
        if re.search(pattern, email):
            serializer.is_valid(raise_exception=True)
            serializer.save()
            print("OK")
            return Response(serializer.data)
        else:
            raise AuthenticationFailed("Error email")

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.get(email=email)

        if user is None:
            raise AuthenticationFailed("Пользователь не найден")

        if not user.check_password(password):
            raise AuthenticationFailed("Не правильный пароль")

        user.is_active = True
        user.last_login = datetime.datetime.utcnow()
        user.save()
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response       


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Пользователь не авторизован')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Пользователь не авторизован')

        user = User.objects.filter(id=payload['id']).first()

        serializer = UserSerializer(user)
        return Response(serializer.data)       

class LogoutView(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user = User.objects.filter(id=payload['id']).first()
        user.is_active = False
        user.save()
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'вышли успешно'
        }
        return response 

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            # html = render_to_string('emails/contactform.html', {
            #     'name': name,
            #     'email': email,
            #     'content': content
            # })

            send_mail('The contact form subject', 'Ваша заявка успешно создана ! Спасибо что обратились в Guitar Zone', 'karabek_asanali@mail.ru',
                      ['asanali.itstep@mail.ru'])

            return JsonResponse({"message": "success"})
    else:
        form = ContactForm()

                                 
        


       







