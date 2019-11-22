from django.contrib import admin



from Documents.models import Paragraph,InvertedMap,FileUpload

# Register your models here.
admin.site.register(Paragraph)
admin.site.register(InvertedMap)
admin.site.register(FileUpload)