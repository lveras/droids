from django.contrib import admin
from .models import Demanda


class DemandaAdmin(admin.ModelAdmin):
    list_display = ("descricao", "img_status", "anunciante", "estado", "cidade",
                    "cep", "endereco", "num_endereco", "comp_endereco")

    def img_status(self, obj):
        return obj.status

    img_status.allow_tags = True


admin.site.register(Demanda, DemandaAdmin)
