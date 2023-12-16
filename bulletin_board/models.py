from django.db import models
from users.models import User


class Announcement(models.Model):
    CATEGORY = (
        ("work", "work"),
        ("house", "house"),
        ("car", "car"),
        ("other", "other"),
    )

    title = models.CharField(max_length=50, db_index=True)
    description = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    image = models.ImageField(upload_to="announcement_image/", null=True)
    created = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    town = models.CharField(max_length=50, null=True)
    type = models.CharField(null=True, choices=CATEGORY, max_length=10)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_announ")


class House(models.Model):
    rooms = models.PositiveSmallIntegerField()

    area = models.FloatField()

    announcement = models.ForeignKey(
        Announcement,
        on_delete=models.PROTECT,
        related_name="house",
        limit_choices_to={"type": "house"},
    )


class Work(models.Model):
    TYPE_WORK = (("LOCAL", "local"), ("REMOTE", "remote"))

    calary = models.DecimalField(max_digits=6, decimal_places=0)
    type_of_work = models.CharField(choices=TYPE_WORK, max_length=10)

    announcement = models.ForeignKey(
        Announcement,
        on_delete=models.PROTECT,
        related_name="work",
        limit_choices_to={"type": "work"},
    )


class Car(models.Model):
    CAR_CHOICE = (("BMW", "BMW"), ("MERS", "MERSEDES"), ("AUDI", "AUDI"))

    STATUS_CHOICE = (("NEW", "NEW"), ("USE", "IN_USE"))

    brand = models.CharField(choices=CAR_CHOICE, max_length=10)

    year = models.IntegerField()

    engine_power = models.FloatField()

    color = models.CharField(null=True)

    status = models.CharField(choices=STATUS_CHOICE, max_length=10)

    announcement = models.ForeignKey(
        Announcement,
        on_delete=models.PROTECT,
        related_name="car",
        limit_choices_to={"type": "car"},
    )


class Other(models.Model):
    announcement = models.ForeignKey(
        Announcement,
        on_delete=models.PROTECT,
        related_name="other",
        limit_choices_to={"type": "other"},
    )
