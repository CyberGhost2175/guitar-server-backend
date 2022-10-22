from django.contrib import admin

from apps.guitar_server.models import Guitar, Amplifier, Capo, Pick
from apps.guitar_server.models import User

admin.site.register(Guitar)
admin.site.register(User)
admin.site.register(Amplifier)
admin.site.register(Capo)
admin.site.register(Pick)

