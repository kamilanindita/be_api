from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .scraper.scraper import Scraper
from .serializers import RequestScrapProductSerializer, SaveScrapProductSerializer, ScrapProductResponseSerializer, TotalScrapProductSerializer

class ScrapApiView(APIView):
    # Scrap endpoint
    def post(self, request, *args, **kwargs):
        url = request.data.get('url')
        # validator
        validator = RequestScrapProductSerializer(data={"url":url})
        if validator.is_valid():
            scraper = Scraper(url)
            result = scraper.get_data()

            if  type(result) != str and result['name'] != "" and result["price"] !="":
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

            elif type(result) == str:
                return Response({ "message": result }, status=status.HTTP_400_BAD_REQUEST)
                
            else:    
                return Response({ "message": "product not found" }, status=status.HTTP_400_BAD_REQUEST)

        return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)

class ScrappedTotalProductGrupBy(APIView):
    def get_group_by(self, params):
        # group by default without date system and only by marketplace
        query_group = "SELECT id, marketplace, COUNT(id) as total FROM api_product GROUP by marketplace"

        # group by date and marketplace
        if(params['date'] != None and params['date_start'] == None and params['date_end'] == None and params['month'] == None):
            query_group = "SELECT id, marketplace, COUNT(id) as total FROM api_product WHERE DATE(created_at) = '%s' GROUP by marketplace" % (params['date'])
       
        # group by range date and marketplace
        elif (params['date_start'] != None and params['date_end'] != None and params['date'] == None and params['month'] == None):
            query_group = "SELECT id, marketplace, COUNT(id) as total FROM api_product WHERE DATE(created_at) >= '%s' AND DATE(created_at)  <= '%s' GROUP by marketplace" % (params['date_start'], params['date_end'])
        
        # goup by month and marketplace
        elif (params['month'] != None and abs(int(params['month'])) > 0 and abs(int(params['month'])) <= 12 and params['date'] == None and params['date_start'] == None and params['date_end'] == None):
            month = '0'+str(abs(int(params['month']))) if abs(int(params['month'])) < 10 else str(abs(int(params['month'])))
            
            query_group = "SELECT id, marketplace, COUNT(id) as total FROM api_product WHERE strftime('%m',created_at) = " + " '%s' GROUP by marketplace" % (month)

        try:
            products = Product.objects.raw(query_group)
            serializer = TotalScrapProductSerializer(products, many=True)

            return serializer.data

        except Product.DoesNotExist:

            return False

    # Scrapped group by endpoint
    def get(self, request, *args, **kwargs):
        # get query params
        date = self.request.query_params.get('date')
        date_start = self.request.query_params.get('from')
        date_end = self.request.query_params.get('to')
        month = self.request.query_params.get('month')

        params = {
            "date": date,
            "date_start": date_start,
            "date_end": date_end,
            "month": month
        }

        results = self.get_group_by(params)

        return Response(results, status=status.HTTP_200_OK)