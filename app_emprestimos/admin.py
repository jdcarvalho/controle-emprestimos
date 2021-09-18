from django.contrib import admin
from app_emprestimos.models import ObjetoEmprestimo


class ObjetoAdmin(admin.ModelAdmin):

    search_fields = [
        'nome',
    ]

    list_display = ('nome', 'data_aquisicao', 'tipo_objeto')

    def save_model(self, request, obj, form, change):
        super(ObjetoAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        super(ObjetoAdmin, self).delete_model(request, obj)


admin.site.register(ObjetoEmprestimo, ObjetoAdmin)
