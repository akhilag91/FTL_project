import serializers
from rest_framework.views import APIView, Response
from .models import *

class UserDetailsView(APIView):
    def get(self, request):
        """
        To return the user details along with the activity period 
        """
        
        users = User.objects.all()
        serialized_data = serializers.UserSerializer(users, many=True).data
        data = {}
        data['ok'] = True
        data['members'] = serialized_data
        return Response(data)
            
