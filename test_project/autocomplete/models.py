# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Person(models.Model):
	name = models.CharField(max_length = 150)

	def __str__(self):
		return self.name
