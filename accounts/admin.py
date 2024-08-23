from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Property, Booking, Tenant, Payment, Availability, Review, Account

class CustomUserAdmin(UserAdmin):
    model = Account
    # Customize the fields displayed in the admin panel
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )
    list_display = ('username', 'email', 'phone_number', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'price')
    search_fields = ('name', 'address')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('property', 'start_date', 'end_date', 'guest_name')
    search_fields = ('guest_name', 'property__name')
    list_filter = ('start_date', 'end_date', 'property')

class TenantAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')
    search_fields = ('user__username', 'phone_number')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'payment_date')
    search_fields = ('booking__guest_name', 'amount')
    list_filter = ('payment_date',)

class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('property', 'available_from', 'available_to')
    search_fields = ('property__name',)
    list_filter = ('available_from', 'available_to')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('property', 'user', 'rating', 'comment')
    search_fields = ('property__name', 'user__username', 'rating')
    list_filter = ('rating',)

admin.site.register(Property, PropertyAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Tenant, TenantAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Availability, AvailabilityAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Account)