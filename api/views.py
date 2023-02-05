from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .scraper.scraper import Scraper
from .serializers import RequestScrapProductSerializer, SaveScrapProductSerializer, ScrapProductResponseSerializer

class ScrapApiView(APIView):
    # Scrap endpoint
    def post(self, request, *args, **kwargs):
        url = request.data.get('url')
        # validator
        validator = RequestScrapProductSerializer(data={"url":url})
        if validator.is_valid():
            scraper = Scraper(url)
            result = scraper.get_data()

            data = {
                'name': result['name'], 
                'price': result["price"], 
                'currency_code': result["currency_code"],
                'image_url':result["image_url"],
                'url_site': url,
                'marketplace': result["marketplace"]
            }

            # validator before save to db 
            serializer = SaveScrapProductSerializer(data=data)
            if serializer.is_valid():
                # save scrap product data
                serializer.save()

                scrapProductResponseSerializer = ScrapProductResponseSerializer(serializer.data)

                return Response(scrapProductResponseSerializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)