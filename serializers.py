from rest_framework import serializers
from .models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
 #it gives description of other classes    
    class Meta:
        model=Employee
        #fields=('first_name','last_name')
     #getting fields and converted into json object
        fields='__all__'
        