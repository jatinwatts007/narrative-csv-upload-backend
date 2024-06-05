import logging

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from UploadAPP.service import upload_file

logging.basicConfig()
logger = logging.getLogger(__name__)


# Create your views here.
class HealthCheck(APIView):
    def get(self, request):
        logger.info('GET: Health Check: Checking Health of a server')
        return Response("Server UP", status=status.HTTP_200_OK)



