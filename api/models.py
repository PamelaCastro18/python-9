# -*- coding: utf-8 -*-

from django.db import models
from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50, validators=[MinLengthValidator(8)])
    email = models.EmailField (max_length=254, blank=True, unique=True, \
            null=True)
    last_login = models.DateField(auto_now_add=True)

class Agent(models.Model):
    name = models.CharField(max_length=50)
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    address = models.GenericIPAddressField(
        protocol = 'IPv4',
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
    agent = models.ForeignKey('Agent', on_delete = models.PROTECT)
    user = models.ForeignKey('User', on_delete = models.PROTECT)
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
    group = models.ForeignKey('Group', on_delete = models.PROTECT )
    user = models.ForeignKey('User', on_delete = models.PROTECT )

