from django.contrib import admin
from learning_logs.models import Entry, Topic
# Register your models here.
#username: ll_admin
#password: firstblood2

admin.site.register(Topic)
admin.site.register(Entry)


