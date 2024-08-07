import logging

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from UploadAPP.service import upload_file
from UploadAPP.models import StudentProfile

logging.basicConfig()
logger = logging.getLogger(__name__)


# Create your views here.
class UploadCSVFile(APIView):
    def post(self, request):
        permission_classes = IsAuthenticated
        data = request.data
        csv_file = data.get('csvFile')
        logger.info('POST: Upload CSV: Request received for uploading csv')
        try:
            response = upload_file(csv_file=csv_file)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error('Upload CSV: Error while uploading error : %s', e)
            return Response("Failed", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

