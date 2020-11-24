from django.db.models import Model, ForeignKey, ManyToManyField, FloatField, CharField, EmailField, TextField, BooleanField, CASCADE


class User(Model):
    first_name = CharField(
        verbose_name="Ism",
        max_length=64,
        help_text="64 ta belgidan oshmasligi kerak"
    )
    last_name = CharField(
        verbose_name="Familiya",
        max_length=64,
        help_text="64 ta belgidan oshmasligi kerak"
    )
    email = EmailField()
    categories = ManyToManyField(
        'Category',
        related_name="followers",
        verbose_name="Yoqtirgan bo'limlari",
        blank=True
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"


class Category(Model):
    name = CharField(
        verbose_name="Nomi",
        max_length=64,
        help_text="64 belgidan oshmasligi kerak"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"


class Product(Model):
    category = ForeignKey(
        Category,
        CASCADE,
        verbose_name="Bo'lim",
        related_name="products",
        help_text="Mahsulot mansub bo'lgan bo'lim, biriktirilishi shart"
    )
    name = CharField(
        verbose_name="Nomi",
        max_length=64,
        help_text="64 belgidan oshmasligi kerak"
    )
    description = TextField(
        verbose_name="Qisqacha ma'lumot",
        help_text="Mahsulot haqida qisqacha ma'lumot, kiritilishi shart"
    )
    price = FloatField(
        verbose_name="Narxi",
        default=0.0
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

