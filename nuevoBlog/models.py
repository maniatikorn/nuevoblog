from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Articulo(models.Model):
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	imagen = models.ImageField(upload_to="nuevoBlog/static/images-articles/")
	slug = models.SlugField(editable=False)
	fecha = models.DateTimeField()

	class Meta:
		ordering = ["-fecha"]

	def __unicode__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Articulo, self).save(*args, **kwargs)