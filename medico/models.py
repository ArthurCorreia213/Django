from django.db import models

# Create your models here.

#ARTHUR CORREIA
class MEDICO(models.Model):
    id_medico = models.IntegerField("Identificador único do médico", primary_key=True)
    nome = models.CharField("Nome completo do médico",max_length=50)
    endereco = models.CharField("Endereço de consultório ou residência do médico", max_length=50)
    telefone  = models.CharField("Número de telefone do médico", max_length=13)
    email = models.CharField("Endereço de e-mail do médico", max_length=50)
    data_nascimento = models.DateField("Data de nascimento do médico")
    crm = models.CharField()
    id_especialidade = models.ForeignKey("ESPECIALIDADE", on_delete=models.CASCADE)

#ARTHUR CORREIA
class ESPECIALIDADE(models.Model):
    id_especialidade = models.IntegerField("Identificador único da especialidade", primary_key=True)
    nome = models.CharField("Nome da especialidade", max_length=50)
    descricao = models.TextField("Descrição da especialidade")