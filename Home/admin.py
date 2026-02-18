from django.contrib import admin


from .models import Contact_master

admin.site.register(Contact_master)

admin.site.site_header="EHRS Header"
admin.site.site_title="EHRS Title"
admin.site.index_title="Welcome to Your EHRS Panel"
