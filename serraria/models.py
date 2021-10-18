from datetime import date
from django.conf.urls import url
from django.contrib.admin.sites import DefaultAdminSite
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import CharField, DecimalField
from django.db.models.fields.related import ForeignKey
from django.utils.regex_helper import Group
from django.utils import timezone
from django.utils.tree import Node
from django.contrib.auth.models import User
from serraria.models import *
from producao.models import *


# Create your models here.


