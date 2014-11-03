from django.contrib import admin
from django.contrib.admin.views.main import ChangeList as BaseChangeList
from django.utils.translation import ugettext as _

class ReadOnlyModelAdmin(admin.ModelAdmin):
    actions = None

    def get_readonly_fields(self, request, obj=None):
        if not self.fields:
            return [
                field.name
                for field in self.model._meta.fields
                if field != self.model._meta.pk
            ]
        else:
            return self.fields

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        if request.method not in ('GET', 'HEAD'):
            return False
        else:
            return super(ReadOnlyModelAdmin, self).has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        return super(ReadOnlyModelAdmin, self).changeform_view(request, object_id, form_url, {
            'title': _('View {}'.format(self.model._meta.verbose_name))
        })

    def get_changelist(self, request, **kwargs):
        model = self.model

        class ChangeList(BaseChangeList):
            def __init__(self, *args, **kwargs):
                super(ChangeList, self).__init__(*args, **kwargs)
                self.title = _('Select {} to view'.format(model._meta.verbose_name))

        return ChangeList
