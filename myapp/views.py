from rest_framework.views import APIView
#response will be given from response function
from rest_framework.response import Response

class SampleApiView(APIView):
    ''' The get method is responsible for handling the get responses'''
    def get(self,request,format=None):
        #always response should in the form of dictionary
        return Response({'name':"SampleAPIView",'message':"Hello Akhil"})
