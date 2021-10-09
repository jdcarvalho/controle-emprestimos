from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app_emprestimos.forms import RelatorioForm


@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class RelatorioEmprestimosView(View):

    template = 'relatorio.html'
    template_filtro = 'relatorio_filtro.html'

    def get(self, request):
        form = RelatorioForm()
        return render(request, self.template_filtro, {
            'form': form,
        })

    def post(self, request):
        pass
