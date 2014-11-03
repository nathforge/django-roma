Django ReadOnlyModelAdmin
=========================

``django-roma`` is a read-only ``ModelAdmin``.


Django's admin interface is designed for editing, not viewing. But sometimes
you want read-only models, and the admin is a convenient place to put them.


Installation:
-------------

::

    pip install django-roma


Usage:
------

Edit the relevant `admin.py` in your project. e.g:

::

    from roma import ReadOnlyModelAdmin
    from myproject.myapp.models import MyModel

    admin.site.register(MyModel, ReadOnlyModelAdmin)

Or if you want a bit more customisation:

::

    from roma import ReadOnlyModelAdmin
    from myproject.myapp.models import MyModel

    class MyModelAdmin(ReadOnlyModelAdmin):
        fields = ("title",)

    admin.site.register(MyModel, MyModelAdmin)
