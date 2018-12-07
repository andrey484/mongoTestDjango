from djongo import models


class Water(models.Model):
    _id = models.ObjectIdField()
    weight = models.CharField(max_length=255, blank=True)
    objects = models.DjongoManager()

    class Meta:
        app_label = 'admin_page'


class Beer(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=255, blank=False)
    value = models.EmbeddedModelField(model_container=Water)
    objects = models.DjongoManager()

    class Meta:
        app_label = 'admin_page'
