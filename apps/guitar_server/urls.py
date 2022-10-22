from django.urls import re_path, path
from apps.guitar_server import views
from .views import *


app_name = 'guitar_server'

urlpatterns= [

    re_path(r'api/guitarzone/guitars', views.guitars_list),
    re_path(r'api/guitarzone/guitar/(?P<id>[0-9]+)', views.guitar_by_id),
	re_path(r'api/guitarzone/amplifiers', views.amplifier_list),
	re_path(r'api/guitarzone/amplifier/(?P<id>[0-9]+)', views.amplifier_by_id),
    re_path(r'api/guitarzone/picks', views.pick_list),
    re_path(r'api/guitarzone/pick/(?P<id>[0-9]+)', views.pick_by_id),
    re_path(r'api/guitarzone/capos', views.capos_list),
    re_path(r'api/guitarzone/capo/(?P<id>[0-9]+)', views.capo_by_id),
    path('api/register', RegisterView.as_view()),
    path('api/login', LoginView.as_view()),
    path('api/user', UserView.as_view()),
    path('api/logout', LogoutView.as_view()),
	path('api/contact', views.contact),
	path('api/user', UserView.as_view())
]


		
# {
# "brand":"гитара Fender Stratocaster",
# "type": "electric",
# "quantity_string"	:6,
# "hull_shape":"stratocaster"	,
# "color":"black",
# "image":"https://thumbs.static-thomann.de/thumb/padthumb600x600/pics/bdb/439053/13206276_800.jpg",
# "price":2000	
# }

	# "fist_name": "Asanali",
	# "last_name": "Karabek",
	# "email":"asanali.itstep@mail.ru",
	# "password":"123"


