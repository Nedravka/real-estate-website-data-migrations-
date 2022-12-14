from django.contrib import admin

from .models import Complaint, Flat, Owner


class FlatInLine(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = [
        'flat',
        'owner'
    ]


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = [
        'town',
        'address',
        'owner'
    ]
    readonly_fields = [
        'created_at',
    ]
    list_display = [
        'address',
        'price',
        'is_new_building',
        'construction_year',
        'town',

    ]
    list_editable = [
        'is_new_building'
    ]
    list_filter = [
        'is_new_building',
        'rooms_number',
        'has_balcony'
    ]
    raw_id_fields = [
        'like'
    ]
    inlines = [
        FlatInLine,
    ]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = [
        'flat'
    ]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = [
        'flat'
    ]
    inlines = [
        FlatInLine,
    ]
    exclude = ['flat']
