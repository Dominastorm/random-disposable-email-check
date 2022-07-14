from mail_project.backend import generate_email, get_inbox
from rest_framework.views import APIView
from rest_framework.response import Response

class GenerateMailView(APIView):
    def get(self, request):
        email = generate_email()
        return Response({'Go to: ': request.build_absolute_uri()[:-16] +'/get-inbox/'+email, 'Then send an email to: ': email})
    
class GetInboxView(APIView):
    def get(self, request, email):
        return Response({'Email Content: ': get_inbox(email)})
