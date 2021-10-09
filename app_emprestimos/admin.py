from django.contrib import admin
from django.contrib.admin import AdminSite

from app_emprestimos.forms import RegistroDeEmprestimoForm
from app_emprestimos.models import ObjetoEmprestimo
from app_emprestimos.models import Pessoa, RegistroEmprestimos
from app_emprestimos.views import RelatorioEmprestimosView


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

    form = RegistroDeEmprestimoForm

    search_fields = [
        'pessoa__nome',
    ]
    list_display = ('data_emprestimo', 'pessoa',
                    'data_prevista_devolucao', 'status')
    change_list_template = 'emprestimos_lista.html'


class MyAdminSite(AdminSite):
    def get_urls(self):
        from django.conf.urls import url
        urls = super(MyAdminSite, self).get_urls()
        urls = [
            url(r'^visualizar-relatorio/$',
                self.admin_view(RelatorioEmprestimosView.as_view()),
                )
        ] + urls
        return urls


admin_site = MyAdminSite()

admin_site.register(ObjetoEmprestimo, ObjetoAdmin)
admin_site.register(Pessoa, PessoaAdmin)
admin_site.register(RegistroEmprestimos, RegistroEmprestimoAdmin)
