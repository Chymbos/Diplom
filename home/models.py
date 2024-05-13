from django.db import models


from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class MenuItem(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField('Ссылка', max_length=255)
    position = models.PositiveIntegerField('Позиция', default=1)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    delivery_date = models.DateField()
    quantity = models.IntegerField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Items'


