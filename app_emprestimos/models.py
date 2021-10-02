from django.db import models
from django.db.models.deletion import PROTECT


class ObjetoEmprestimo(models.Model):
    TIPO_LIVRO = 1
    TIPO_CD = 2
    TIPO_ROUPA = 3
    TIPO_JOGO = 4
    TIPO_ELETRONICO = 5
    TIPO_GERAL = 6
    TIPO_FERRAMENTA = 7

    TIPO_OBJETO_CHOICES = (
        (TIPO_LIVRO, 'Livro'),
        (TIPO_CD, 'CD'),
        (TIPO_ROUPA, 'Roupa'),
        (TIPO_JOGO, 'Jogo'),
        (TIPO_ELETRONICO, 'Eletrônicos'),
        (TIPO_GERAL, 'Objetos em Geral'),
        (TIPO_FERRAMENTA, 'Ferramentas em Geral'),
    )

    nome = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Nome do Objeto',
    )

    data_aquisicao = models.DateField(
        null=False, blank=False,
        verbose_name='Data de Aquisição',
    )

    tipo_objeto = models.PositiveSmallIntegerField(
        null=False, blank=False,
        verbose_name='Tipo do Objeto',
        choices=TIPO_OBJETO_CHOICES,
    )

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'OBJ_001OBJ'
        verbose_name = 'Objeto para Empréstimo'
        verbose_name_plural = 'Objetos para Empréstimo'



class Pessoa(models.Model):
    nome = models.CharField(
        null=False, blank=False,
        max_length=200,
    )
    telefone = models.CharField(
        null=False, blank=False,
        max_length=20,
    )

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'PES_001PES'
        



class RegistroEmprestimos(models.Model):
    ST_EMPRESTADO = 1
    ST_DEVOLVIDO = 2
    ST_EXTRAVIADO = 3


    ST_STATUS_CHOICES = (
        (ST_EMPRESTADO, 'Objeto Emprestado'),
        (ST_DEVOLVIDO, 'Objeto Devolvido'),
        (ST_EXTRAVIADO, 'Objeto Extraviado'),
    )
    data_emprestimo = models.DateTimeField(
        null=False, blank=False, auto_now_add=True,
        verbose_name='Data De Emprestimo'
    )
    objeto = models.ForeignKey(
        'app_emprestimos.ObjetoEmprestimo',
        null=False, blank=False, 
        on_delete=models.PROTECT,
        verbose_name='Objeto Emprestado'
    )
    pessoa = models.ForeignKey(
        'app_emprestimos.Pessoa',
        null=False, blank=False,   
        on_delete=models.PROTECT,
        verbose_name='Nome Da Pessoa'
    )
    data_prevista_devolucao = models.DateField(
        null=True, blank=True,
        verbose_name='Previsão De Entrega'
    )
    data_devolucao = models.DateField(
        null=True, blank=True,
        verbose_name='Data Da Entrega'
    )
    status = models.PositiveSmallIntegerField(
        null=False, blank=False,
        verbose_name='Status',
        choices=ST_STATUS_CHOICES,
    )
    class Meta:
        db_table='REG_001EMP'