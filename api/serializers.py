from rest_framework import serializers
from .models import Product

class RequestScrapProductSerializer(serializers.ModelSerializer):
    url = serializers.CharField(allow_blank=False)
    
    class Meta:
        model = Product
        fields = ["url"]

class SaveScrapProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(allow_blank=False)
    price = serializers.FloatField()
    currency_code = serializers.CharField(allow_blank=False)
    image_url = serializers.CharField(allow_blank=False)
    url_site = serializers.CharField(allow_blank=False)
    marketplace = serializers.CharField(allow_blank=False)

    class Meta:
        model = Product
        fields = ["name", "price", "currency_code", "image_url", "url_site", "marketplace"]
    
class ScrapProductResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "currency_code", "image_url", "marketplace"]

class TotalScrapProductSerializer(serializers.ModelSerializer):
    total =  serializers.IntegerField()

    class Meta:
        model = Product
        fields = [ "marketplace", "total"]