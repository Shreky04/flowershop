from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name="Назва", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        app_label = 'flowershop'


class Comments(models.Model):
    text = models.TextField(max_length=400, verbose_name="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    item = models.ForeignKey('flowershop.Item', on_delete=models.CASCADE, related_name='comments')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата та час")

    def __str__(self):
        return f"{self.author} {self.publish_date}"

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"


class Item(models.Model):
    title = models.CharField(max_length=40, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Опис")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата та час")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категорія")
    picture = models.ImageField(upload_to='project/media/itempics', verbose_name="Постер")
    price = models.FloatField(verbose_name="Ціна")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cart_items = models.ManyToManyField(Item, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    dateofbirth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профіль"
        verbose_name_plural = "Профілі"



class Post(models.Model):
    title = models.CharField(max_length=40, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    post_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата та час")
    image = models.ImageField(upload_to='blogpics', verbose_name="Фото")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"


class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Товар")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Покупець")
    quantity = models.IntegerField(verbose_name="Кількість", default=1, choices=[(i, str(i)) for i in range(1, 6)])
    street = models.CharField(max_length=100, blank=False, default=1,  null=False, verbose_name="Вулиця")
    house = models.CharField(max_length=10, blank=False, default=1, null=False, verbose_name="Дім")
    apartment = models.CharField(max_length=10, default=1, blank=False, null=False, verbose_name="Квартира")
    order_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Дата і час замовлення")
    price = models.FloatField(default=0)

    def __str__(self):
        return f"Замовлення {self.id} - {self.item.title} - {self.customer.username}"

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"



