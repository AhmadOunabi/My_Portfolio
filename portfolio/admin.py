from django.contrib import admin
from .models import User,Project,Education,Experience,Skill,Language
# Register your models here.

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Language)
