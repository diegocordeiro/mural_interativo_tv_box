from django.contrib import admin
from django.utils.html import format_html, mark_safe
from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'preview', 'ativo', 'ordem', 'criado')
    list_editable = ('ativo', 'ordem')
    readonly_fields = ('criado', 'preview')

    def preview(self, obj):
        if obj.imagem:
            return mark_safe('<img src="{}" style="max-height: 100px;"/>'.format(obj.imagem.url))
        return "(sem mídia)"

    preview.short_description = "Pré-visualização"
