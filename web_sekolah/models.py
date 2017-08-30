# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
JK_CHOICES = (
	('laki','Laki-Laki'),
	('perempuan','Perempuan'),
	)
class Jurusan(models.Model):
	nama = models.CharField('Nama Jurusan',max_length=100)
	

	def __unicode__(self):
		return self.nama

	class Meta:
		db_table = 'jurusan'
		verbose_name_plural = 'Jurusan'

class Agama(models.Model):
	nama = models.CharField('Nama Agama',max_length=100)
	#aktif = models.BooleanField('Ya/Tidak',help_text = 'Centang jika ingin mengaktifkan')

	def __unicode__(self):
		return self.nama

	class Meta:
		db_table = 'agama'
		verbose_name_plural = 'Agama'

class Kelas(models.Model):
	nama = models.CharField('Kelas',max_length=5)

	def __unicode__(self):
		return self.nama

	class Meta:
		db_table = 'kelas'
		verbose_name_plural = 'Kelas'

class Siswa(models.Model):
	no_induk = models.CharField('No Induk Siswa',primary_key=True,max_length=10)
	nama = models.CharField('Nami',max_length=100)
	ttl = models.DateField('Tanggal Lahir', help_text = 'Format Tanggal: YYYY-MM-DD')
	jk = models.CharField('Jenis Kelamin', max_length=15,choices=JK_CHOICES,default='laki')
	agama = models.ForeignKey(Agama,verbose_name='Agama')
	nama_ortu = models.CharField(max_length=100)
	alamat = models.TextField(blank=True,null=True)
	jur = models.ForeignKey(Jurusan,on_delete=models.CASCADE, null=True)
	kelas = models.ForeignKey(Kelas,on_delete=models.CASCADE,null=True)

	def __unicode__(self):
		return self.nama

	class Meta:
		db_table = 'siswa'
		verbose_name_plural = 'Siswa'
