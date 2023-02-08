from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HomeApiView(APIView):
    # Home endpoint
    def get(self, request, *args, **kwargs):
        results = {
            "status": 200,
            "message": "success",
            "data": "home app",
        }

        return Response(results, status=status.HTTP_200_OK)