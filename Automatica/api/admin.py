from django.contrib import admin
from api.models import Worker, Store, Visit


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'date')
    list_display_links = ('id', 'date')
    search_fields = ('store__worker__name', 'store__title')
