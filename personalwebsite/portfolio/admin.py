from django.contrib import admin
from django.contrib.sessions.models import Session

from .models import Link, Project


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):

    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
    readonly_fields = ['_session_data']
    exclude = ['session_data']


class LinkInline(admin.TabularInline):
    model = Link


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        LinkInline,
    ]


admin.site.register(Link)
