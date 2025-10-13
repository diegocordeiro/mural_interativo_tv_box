from django.db import models
from django.core.validators import FileExtensionValidator

class Banner(models.Model):
    titulo = models.CharField('Título', max_length=200, blank=True)
    imagem = models.ImageField(
        upload_to='banners/images/',
        blank=True, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','gif'])]
    )
    ativo = models.BooleanField('Ativo', default=True)
    ordem = models.PositiveIntegerField('Ordem', default=0, help_text='Ordem de exibição no carrossel (menor primeiro)')
    criado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordem', '-criado']

    def __str__(self):
        return self.titulo or f'Banner {self.pk}'
