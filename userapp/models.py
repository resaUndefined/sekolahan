# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
JK_CHOICES = (
    ('laki', 'Laki-Laki'),
    ('perempuan', 'Perempuan'),
)
AGAMA_CHOICES = (
    ('islam', 'ISLAM'),
    ('kristen', 'KRISTEN'),
    ('katholik', 'KHATOLIK'),
    ('hindu', 'HINDU'),
    ('budha', 'BUDHA'),
    ('other', 'OTHER'),
)


class Siswa(models.Model):
    nis = models.CharField(
        'No Induk Siswa', unique=True, max_length=10)
    nama = models.CharField('Nama', max_length=100)
    ttl = models.DateField(
        'Tanggal Lahir', help_text='Format Tanggal: YYYY-MM-DD')
    jk = models.CharField('Jenis Kelamin', max_length=15,
                          choices=JK_CHOICES, default='laki')
    agama = models.CharField('Agama', max_length=10, choices=AGAMA_CHOICES,
                             default='islam')
    nama_ortu = models.CharField(max_length=100)
    alamat = models.TextField(blank=True, null=True)
    jurusan = models.ForeignKey(sekolahapp.Jurusan, verbose_name='Jurusan')
    #jur = models.ForeignKey(Jurusan, on_delete=models.CASCADE, null=True)
    #kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return self.nama

    class Meta:
        verbose_name_plural = 'Siswa'


class Guru(models.Model):
    nip = models.CharField('NIP', unique=True, max_length=10)
    nama = models.CharField('Nama', max_length=100)
    ttl = models.DateField('Tanggal Lahir',
                           help_text='Format tanggal YYYY-MM-DD')
    jk = models.CharField('Jenis Kelamin', max_length=15,
                          choices=JK_CHOICES, default='laki')
    agama = models.CharField('Agama', max_length=10, choices=AGAMA_CHOICES,
                             default='islam')
    alamat = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.nip + '-' + self.nama

    class Meta:
        verbose_name_plural = 'Guru'
