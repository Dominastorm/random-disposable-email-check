from mail_project.backend import generate_email
from rest_framework.views import APIView
from rest_framework.response import Response

class GenerateMailView(APIView):
    def get(self, request):
        return Response({'Send an email to: ': generate_email()})
    
