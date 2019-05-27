from django.contrib import admin
from .models import Demanda
from django.utils.html import format_html


class DemandaAdmin(admin.ModelAdmin):
    list_display = ("descricao", "img_status", "anunciante", "estado", "cidade",
                    "cep", "endereco", "num_endereco", "comp_endereco")

    def img_status(self, obj):
        return format_html('<img src="/media/{0}" />'.format(
            'baseline-check_circle_outline.svg' if obj.status == 1
            else 'baseline-highlight_off.svg'))

    img_status.allow_tags = True


admin.site.register(Demanda, DemandaAdmin)
