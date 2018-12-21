from django.db import models
from datetime import datetime
# Create your models here.


class Card(models.Model):
    GENDER_CHOICES = (
        ('valid', '有效'),
        ('invalid', '无效')
    )
    card_id = models.CharField(max_length=20, primary_key=True, verbose_name=u"卡号")
    state = models.CharField(max_length=10, verbose_name=u"状态", choices=GENDER_CHOICES)
    create_time = models.DateTimeField(verbose_name=u"创建时间", default=datetime.now)
    password = models.CharField(max_length=20, verbose_name=u"密码")
    card_Email = models.EmailField(max_length=100, blank=True, default='',verbose_name=u"邮件")



    class Meta:
        verbose_name = u"門卡信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.card_id)