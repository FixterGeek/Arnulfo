# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.

# class Category(models.Model):
# 	name = models.CharField(max_length=200)

# 	def __str__(self):
# 		return self.name


# class Product(models.Model):
# 	name = models.CharField(max_length=200)
# 	sell_price = models.DecimalField(max_digits=10, decimal_places=2)
# 	buy_price = models.DecimalField(max_digits=10, decimal_places=2)
# 	offer_price = models.DecimalField(max_digits=10, decimal_places=2)
# 	in_offer = models.BooleanField(default=False)
# 	in_stock = models.DecimalField(max_digits=20, decimal_places=2, default=0)
# 	unity = models.CharField(max_length=100, blank=True, null=True)
# 	description = models.TextField()
# 	image = models.ImageField(upload_to="product_images")
# 	category = models.ForeignKey(Category, on_delete=models.PROTECT)
# 	registered = models.DateTimeField(auto_now_add=True)

# 	def __str__(self):
# 		return self.name

# class SaleOrder(models.Model):
# 	employee = models.ForeignKey(User, related_name='sale_orders', on_delete=models.PROTECT, blank=True, null=True)
# 	total = models.DecimalField(max_digits=10, decimal_places=2)
# 	paid = models.BooleanField(default=False)
# 	date = models.DateTimeField(auto_now_add=True)

# 	def __str__(self):
# 		return 'order {} of user {}'.format(self.id, self.user.username)

# class OrderItem(models.Model):
# 	order = models.ForeignKey(SaleOrder, related_name='items', on_delete=models.PROTECT, blank=True, null=True)
# 	product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT)
# 	quantity = models.IntegerField()

# 	def __str__(self):
# 		return 'item {} of order {}'.format(self.product.id, self.order.id)

# ##missing order of the ranch purchases and others

