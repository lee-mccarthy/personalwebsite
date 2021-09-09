from django.contrib import admin
from django.contrib.sessions.models import Session

from .models import Contact, Spam, Link, Project


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):

    def _session_data(self, obj):
        return obj.get_decoded()

    list_display = ['session_key', '_session_data', 'expire_date']
    readonly_fields = ['_session_data']
    exclude = ['session_data']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['subject', 'name', 'email', 'contact_time', 'ip_address']
    readonly_fields = [
        'subject',
        'name',
        'email',
        'contact_time',
        'message',
        'ip_address',
        'user_agent',
    ]


@admin.register(Spam)
class SpamAdmin(admin.ModelAdmin):
    list_display = ['subject', 'name', 'email', 'contact_time', 'ip_address']
    readonly_fields = [
        'subject',
        'name',
        'email',
        'contact_time',
        'message',
        'website',
        'ip_address',
        'user_agent',
    ]


class LinkInline(admin.TabularInline):
    model = Link


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        LinkInline,
    ]


admin.site.register(Link)
