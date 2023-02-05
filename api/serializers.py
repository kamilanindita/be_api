from rest_framework import serializers
from .models import Product

class RequestScrapProductSerializer(serializers.ModelSerializer):
    url = serializers.CharField(allow_blank=False)
    
    class Meta:
        model = Product
        fields = ["url"]

class SaveScrapProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "currency_code", "image_url", "url_site", "marketplace"]
    
class ScrapProductResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "currency_code", "image_url", "marketplace"]