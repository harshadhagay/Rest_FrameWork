from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.
class EmployeeList(APIView):
    def get(self,request):
        lst=Employee.objects.all()
        #converting in to json format
        slst=EmployeeSerializer(lst,many=True)
        return Response(slst.data)
    def post(self,request):
      #converting into json format
        sobj=EmployeeSerializer(data=request.data)
        if sobj.is_valid():
            sobj.save()
            return Response(sobj.data,status=status.HTTP_201_CREATED)
        else:
            return Response(sobj.errors,status=status.HTTP_400_BAD_REQUEST)

class Employeemodify(APIView):
    def get_object(self,id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return Response({"error":"given employee with id doesnot exit"},status=status.HTTP_404_NOT_FOUND)
 
    def get(self,request,id):
        emp=self.get_object(id)
        sobj=EmployeeSerializer(emp)
        return Response(sobj.data)
    def put(self,request,id):
        emp=self.get_object(id)
        sobj=EmployeeSerializer(emp,data=request.data)
        if sobj.is_valid():
            sobj.save()
            return Response(sobj.data,status=status.HTTP_200_OK)
        else:
            return Response(sobj.data,status=status.HTTP_400_BAD_RQUEST)
 
    def delete(self,request,id):
        emp=self.get_object(id)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        