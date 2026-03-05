from django.contrib import admin
from .models import Invoice


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):

    list_display = (
        "invoice_code",
        "user",
        "amount",
        "payment_complete",
        "created_at",
    )

    list_filter = (
        "payment_complete",
        "created_at",
    )

    search_fields = (
        "invoice_code",
        "user__username",
        "user__email",
    )