# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Tipo(models.Model):

    #__Tipo_FIELDS__
    descricao = models.CharField(max_length=255, null=True, blank=True)

    #__Tipo_FIELDS__END

    class Meta:
        verbose_name        = _("Tipo")
        verbose_name_plural = _("Tipo")


class Subtipo(models.Model):

    #__Subtipo_FIELDS__
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    #__Subtipo_FIELDS__END

    class Meta:
        verbose_name        = _("Subtipo")
        verbose_name_plural = _("Subtipo")


class Equipamento(models.Model):

    #__Equipamento_FIELDS__
    subtipo = models.ForeignKey(Subtipo, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=255, null=True, blank=True)

    #__Equipamento_FIELDS__END

    class Meta:
        verbose_name        = _("Equipamento")
        verbose_name_plural = _("Equipamento")


class Entrada_Saida_Equipamentos(models.Model):

    #__Entrada_Saida_Equipamentos_FIELDS__
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    data = models.DateTimeField(blank=True, null=True, default=timezone.now)
    responsavel_entrada = models.CharField(max_length=255, null=True, blank=True)

    #__Entrada_Saida_Equipamentos_FIELDS__END

    class Meta:
        verbose_name        = _("Entrada_Saida_Equipamentos")
        verbose_name_plural = _("Entrada_Saida_Equipamentos")


class Anexo(models.Model):

    #__Anexo_FIELDS__
    formato = models.CharField(max_length=255, null=True, blank=True)

    #__Anexo_FIELDS__END

    class Meta:
        verbose_name        = _("Anexo")
        verbose_name_plural = _("Anexo")



#__MODELS__END
