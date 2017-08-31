# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
KELAS_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)
SIFAT_CHOICES = (
    ('adaptif', 'Adaptif'),
    ('produktif', 'Produktif'),
)


class Jurusan(models.Model):
    kode_jur = models.CharField('Kode Jurusan', unique=True, max_length=10)
    nama = models.CharField('Nama Jurusan', max_length=50)
    # kelas = models.CharField('Kelas',max_length=1,choices=KELAS_CHOICES,
    # default='1')

    def __unicode__(self):
        return self.nama

    class Meta:
        verbose_name_plural = 'Jurusan'


class Mapel(models.Model):
    kode_mapel = models.CharField('Kode Mapel', unique=True, max_length=10)
    nama = models.CharField('Nama Mapel', max_length=50)
    sifat_mapel = CharField('Sifat Mapel', choices=SIFAT_CHOICES,
                            max_length=50, default='adaptif')
    jurusan = models.ForeignKey(Jurusan, verbose_name='Jurusan', null=True,
                                default='Umum')

    def __unicode__(self):
        return self.nama

    class Meta:
        verbose_name_plural = 'Mapel'
