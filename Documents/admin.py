from django.contrib import admin



from Documents.models import Paragraph,InvertedMap

# Register your models here.
admin.site.register(Paragraph)
admin.site.register(InvertedMap)