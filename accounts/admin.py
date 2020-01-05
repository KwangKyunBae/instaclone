from django.contrib import admin
from .models import Profile
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','nickname','user'] #id는 장고에서 자동생성
    list_display_links = ['nickname','user']
    search_fields = ['nickname']