from .models import Product, Category, SaleOrder, OrderItem
from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email']


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
	category = CategorySerializer(many=False, read_only=True)
	category_id = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset=Category.objects.all())
	class Meta:
		model = Product
		fields = '__all__'

	def create(self, validated_data):
		cat = validated_data.pop('category_id')
		product = Product.objects.create(category=cat, **validated_data)
		return product




class OrderItemSerializer(serializers.ModelSerializer):
	product = ProductSerializer(many=False, read_only=True)
	product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, required=True)
	class Meta:
		model = OrderItem
		fields = '__all__'



class SaleOrderSerializer(serializers.ModelSerializer):
	employee = UserSerializer(many=False, read_only=True, default=serializers.CurrentUserDefault())
	items = OrderItemSerializer(many=True)
	class Meta:
		model = SaleOrder
		fields = '__all__'

	def create(self, validated_data):
		print(validated_data)
		order_data = validated_data.pop('items')
		order = SaleOrder.objects.create(**validated_data)
		for o in order_data:
			print(o)
			p = o['product_id']
			q = o['quantity']
			OrderItem.objects.create(order=order,quantity=q, product=p)

		return order