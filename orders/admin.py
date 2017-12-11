# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from .models import Order, OrderItem

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response =HttpResponse(content_type='text/csv')
    response['Content-disposition'] = 'attachment; filename{}.csv'.format(opts.verbose_name)
    write = csv.writer(response)




class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = (['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid',
                    'created', 'updated'])
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)