from django.contrib import admin
from roma import ReadOnlyModelAdmin

from testproject.testapp.models import Test

class TestAdmin(ReadOnlyModelAdmin):
    pass

admin.site.register(Test, TestAdmin)
