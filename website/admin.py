from django.contrib import admin
from .models import Branch,Subject,File,UploadLogs
admin.site.register(Branch)
admin.site.register(File)
admin.site.register(Subject)
admin.site.register(UploadLogs)
