from django.contrib import admin
from app_emprestimos.models import ObjetoEmprestimo
from app_emprestimos.models import Pessoa, RegistroEmprestimos

class ObjetoAdmin(admin.ModelAdmin):

    search_fields = [
        'nome',
    ]

    list_display = ('nome', 'data_aquisicao', 'tipo_objeto')

    def save_model(self, request, obj, form, change):
        super(ObjetoAdmin,  self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        super(ObjetoAdmin, self).delete_model(request, obj)

class PessoaAdmin(admin.ModelAdmin):

    search_fields = [
        'nome',
    ]
    list_display = ('nome', 'telefone')


class RegistroEmprestimoAdmin(admin.ModelAdmin):


    search_fields = [
        'pessoa__nome',
    ]
    list_display = ('data_emprestimo', 'pessoa', 'data_prevista_devolucao', 'status')


admin.site.register(ObjetoEmprestimo, ObjetoAdmin)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(RegistroEmprestimos, RegistroEmprestimoAdmin)