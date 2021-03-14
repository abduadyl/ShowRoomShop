from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'stock', 'category')

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user.profile_designer
        product = Product.objects.create(author=user, **validated_data)
        return product

    def to_representation(self, instance):
        representation = super(ProductSerializer, self).to_representation(instance)
        representation['author'] = instance.author.email
        representation['images'] = ProductImageSerializer(instance.images.all(), many=True, context=self.context).data
        representation['reviews'] = ReviewSerializer(instance.reviews.all(), many=True).data
        representation['likes'] = LikeSerializer(instance.likes.all(), many=True).data
        return representation

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image', )

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('product', 'text', )

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user.profile_customer
        review = Review.objects.create(user=user, **validated_data)
        return review


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('user', 'like', )


