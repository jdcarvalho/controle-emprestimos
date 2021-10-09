from django import forms
from app_emprestimos.models import RegistroEmprestimos


class RegistroDeEmprestimoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        from app_emprestimos.models import ObjetoEmprestimo
        super(RegistroDeEmprestimoForm, self).__init__(*args, **kwargs)
        if not self.instance.id:
            # Se não existe ID na instância do form é porque é um
            # registro de empréstimo novo, logo só pode listar objetos
            # não emprestados ou devolvidos
            self.fields['objeto'].queryset = \
                ObjetoEmprestimo.listar_objetos_nao_emprestados()

    class Meta:
        model = RegistroEmprestimos
        fields = (
            'objeto',
            'pessoa',
            'data_prevista_devolucao',
            'data_devolucao',
            'status',
        )


class RelatorioForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(RelatorioForm, self).__init__(*args, **kwargs)
        self.fields['data_inicial'].widget.attrs['class'] = 'date-input'
        self.fields['data_final'].widget.attrs['class'] = 'date-input'

    tipo_data = forms.ChoiceField(
        label='Tipo de Data',
        required=True,
        choices=(
            (1, 'Data de Empréstimo'),
            (2, 'Data de Entrega'),
        )
    )

    data_inicial = forms.DateField(
        label='Data Inicial de Empréstimo',
        required=True,
    )

    data_final = forms.DateField(
        label='Data Final de Empréstimo',
        required=True,
    )
