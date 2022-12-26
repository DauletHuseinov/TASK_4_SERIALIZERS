from rest_framework import serializers
from .models import Product, Firm, Category


class FirmSerializers(serializers.Serializer):
    name_firm = serializers.CharField(max_length=25)
    address = serializers.CharField(max_length=25)

    def create(self, validated_data):
        firm = Firm.objects.create(
            name_firm=validated_data['name_firm'],
            address=validated_data['address'])
        return firm

    def update(self, instance, validated_data):
        instance.name_firm = validated_data['name_firm']
        instance.address = validated_data['address']
        instance.save()
        return instance


class CategorySerializers(serializers.Serializer):
    name_category = serializers.CharField(max_length=25)

    def create(self, validated_data):
        category = Category.objects.create(name_category=validated_data['name_category'])
        return category

    def update(self, instance, validated_data):
        instance.name_category = validated_data['name_category']
        instance.save()
        return instance


class ProductSerializers(serializers.Serializer):
    product_name = serializers.CharField(max_length=25)
    price = serializers.IntegerField()
    firm_id = serializers.IntegerField()
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        product = Product.objects.create(product_name=validated_data['product_name'], price=validated_data['price'],
                                         firm_id=validated_data['firm_id'], category_id=validated_data['category_id'])
        return product

    def update(self, instance, validated_data):
        instance.product_name = validated_data['product_name']
        instance.price = validated_data['price']
        instance.firm_id = validated_data['firm_id']
        instance.category_id = validated_data['category_id']
        instance.save()
        return instance
