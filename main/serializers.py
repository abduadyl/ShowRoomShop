from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

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

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'stock', 'category', 'images')

    def create(self, validated_data):
        request = self.context.get('request')
        images_data = request.FILES
        user = request.user.profile_designer
        product = Product.objects.create(author=user, **validated_data)
        for image in images_data.getlist('images'):
            ProductImage.objects.create(product=product, image=image)
        return product

    def update(self, instance, validated_data):
        request = self.context.get('request')
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.images.delete()
        images_data = request.FILES
        for image in images_data.getlist('images'):
            ProductImage.objects.create(product=instance, image=image)
        return instance

    def to_representation(self, instance):
        representation = super(ProductSerializer, self).to_representation(instance)
        representation['author'] = instance.author.email
        representation['images'] = ProductImageSerializer(instance.images.all(), many=True, context=self.context).data
        representation['reviews'] = ReviewSerializer(instance.reviews.all(), many=True).data
        representation['likes'] = LikeSerializer(instance.likes.all(), many=True).data
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

    def to_representation(self, instance):
        representation = super(ReviewSerializer, self).to_representation(instance)
        representation['user'] = instance.user.email
        return representation

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.email
        return representation


