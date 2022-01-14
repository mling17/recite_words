#!/usr/bin/env python
# -*- coding:utf-8 -*-
from apps.stark.service.v1 import site
from apps.word import models
from apps.word.views import WordHandler

site.register(models.Words, WordHandler)
