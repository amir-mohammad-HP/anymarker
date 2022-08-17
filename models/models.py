from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from authentification.models import User
import datetime
from django.core.exceptions import SuspiciousOperation
from uuid import uuid1


class Collection(models.Model):
    name = models.CharField(
        _('name'),
        max_length= 150,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name


class Mark(models.Model):
    collection = models.ForeignKey(
        Collection, 
        on_delete=models.CASCADE
    )

    name = models.CharField(
        _('name'),
        max_length=150,
        blank=True,
        null=True,
    )

    create_on = models.DateField(
        _('create on'),
        auto_now_add=True,
        editable=False,
    )

    MODELS = (
        ('url', _('url')),
        ('image', _('image')),
        ('file', _('file')),
        ('note', _('note')),
    )
    
    model = models.CharField(
        choices = MODELS,
        default = 'url',
        max_length=5,
    )

    def __str__(self):
        if self.name:
            return self.name
        return f'{self.id} {self.model}'

class MODEL(models.Model):
    mark = models.OneToOneField(
        Mark, 
        on_delete=models.CASCADE,
    )
    
    create_on = models.DateField(
        _('create on'),
        auto_now_add=True,
        editable=False,
    )

    url = None
    image = None
    file = None
    note = None

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.model[1]

    @property
    def model(self):
        if self.url:
            model_type = Mark.MODELS[0][0]
            model = self.url
        elif self.image:
            model_type = Mark.MODELS[1][0]
            model = str(self.image)
        elif self.file:
            model_type = Mark.MODELS[2][0]
            model = self.file
        elif self.note:
            model_type = Mark.MODELS[3][0]
            model = self.note
        else:
            raise SuspiciousOperation(self.__class__.__name__,)
        
        return model_type , model

class URL(MODEL):
    url = models.URLField(
        _("url"), 
        max_length=200
    )

    class Meta:
        verbose_name = 'mark url'
        verbose_name_plural = 'mark urls'


def user_directory_path(instance, filename, *args, **kwargs):
    
    # return 'media/%Y/%m'
    now = datetime.datetime.now()
    return f'users/user_{instance.mark.collection.user.id}/{now.year}/{now.month}/{now.day}/{str(uuid1())}/{filename}'

class IMAGE(MODEL):
    image = models.ImageField(
        _("image"), 
        upload_to =user_directory_path, # 'media/%Y/%m/',#
        blank=True
        # needs to add location
    )

    class Meta:
        verbose_name = 'mark image'
        verbose_name_plural = 'mark images'


# class FILE(MODEL):
#     file = models.FileField(
#         _("file"), 
#         # needs to add location
#     )

#     class Meta:
#         verbose_name = 'mark file'
#         verbose_name_plural = 'mark files'

class NOTE(MODEL):
    note = models.TextField(
        _("note"),
    )

    class Meta:
        verbose_name = 'mark note'
        verbose_name_plural = 'mark notes'


