#!/usr/bin/env python
# coding: utf-8 
# @Time   : forms.py
# @Author : Derek
# @File   : 2018/12/17 09:57
from __future__ import absolute_import, unicode_literals
from utils.mixin import ModelForm
from .models import Command


class CommandCreateForm(ModelForm):
    class Meta:
        model = Command
        fields = ['name', 'team', 'command']
