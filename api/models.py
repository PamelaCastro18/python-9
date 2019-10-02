# -*- coding: utf-8 -*-

from django.db import models
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email, validate_ipv4_address


def validate_password_min(value):
    if len(value) < 8 :
        raise ValidationError(
            (' A senha deve ter mínimo 8 caracteres')
        )

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50,validators=[validate_password_min])
    email = models.CharField(max_length=254, blank=True, unique=True, \
            null=True, validators=[validate_email])
    last_login = models.DateField(auto_now_add=True)

class Agent(models.Model):
    name = models.CharField(max_length=50)
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    address = models.CharField(
        max_length=39, 
        validators= [validate_ipv4_address],
        help_text = 'Endereço IP',
        blank=True, 
        null=True
    )
    status = models.BooleanField()

    
     
class Event(models.Model):
     
    OPTIONS_LEVEL = (
        ('c', 'CRITICAL'),
        ('d', 'DEBUG'),
        ('e', 'ERROR'),
        ('w', 'WARNING'),
        ('i', 'INFO'),
    )

    level = models.CharField (
        max_length=20,
        choices=OPTIONS_LEVEL,
        blank=True,
        default='i',
        help_text='Opções '
    )
 
    data = models.TextField()
    arquivado = models.BooleanField()
    agent = models.ForeignKey('Agent', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """ String para representar o objeto."""
        return self.level



class Group(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        """ String para representar o objeto."""
        return self.name


class GroupUser(models.Model):
    group = models.ForeignKey('Group', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

