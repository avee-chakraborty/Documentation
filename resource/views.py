from django.shortcuts import render
from django.views import View
from .models import CommonFunction
from .serializers import CommonFunctionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class CommonFunctionView(View):

    def get(self, request):
        all_common_functions = CommonFunction.objects.all()
        context = {'all_common_functions':all_common_functions}
        return render(request, 'index.html', context)

    def post(self, request):
        common_function_serializer = CommonFunctionSerializer(data=request.data)
        if common_function_serializer.is_valid():
            common_function_serializer.save()
            return Response(common_function_serializer.data)
        else:
            return Response({'message': 'Form not valid'})

class CommonFunctionAPIView(APIView):

    def get(self, request):
        common_function_list = CommonFunction.objects.all()
        common_function_serializer = CommonFunctionSerializer(common_function_list, many=True)
        return Response(common_function_serializer.data)

    def post(self, request):
        common_function_serializer = CommonFunctionSerializer(data=request.data)
        if common_function_serializer.is_valid():
            common_function_serializer.save()
            return Response(common_function_serializer.data)
        else:
            return Response({'message': 'Form not valid'})
