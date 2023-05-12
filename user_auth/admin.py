from django.contrib import admin
from .models import *

# Register your models here.

admin.site.index_title="Site-Administration"
admin.site.site_header="Admin-Dashboard"
admin.site.site_title="Dashboard"

admin.site.register((Rent,Teacher,Tution,Contact,Poster,RentComment,RentPayment))
