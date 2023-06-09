from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Project_Api.models import Devices, Project, Template

from Project_Api.serializers import  DevicesSerializer, ProjectSerializer, TemplateSerializer

# Create your views here.

class ProjectListApiView(APIView):
    #Lista todos los registros
    def get( self, request, *args, **kwargs):
        '''
        List all the project items for given requeted user
        '''
        project = Project.objects
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    #Crea un nuevo registro
    def post(self, request, *args, **kwags):
        '''
        Create the Project wint given project data
        '''
        data = {
            'idrandom': request.data.get('idrandom'),
            'name' : request.data.get('name'),
            'location': request.data.get('location'),
            'description' : request.data.get('description'),
        }
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailApiView(APIView):
    #Método auxiliar para obtener el objecto con project_id dado
    def get_objects(self, project_id):
        try:
            return Project.objects.get(id= project_id)
        except Project.DoesNotExist:
            return None
    #Recupera el elemento Project con project_id dado
    def get(self, request, project_id, *args, **kwargs):
        project_instance = self.get_objects(project_id)
        if not project_instance:
            return Response(
                {"res": "Object with project id does not exists"},
                status=status.HTTP_400_BAD_REQUEST    
            )
        serializer = ProjectSerializer(project_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #Actualiza el elemento Project con project_id dado, si existe
    def put(self, request, project_id, *args, **kwargs):
        project_instance = self.get_objects(project_id)
        if not project_instance:
            return Response(
                {"res": "Object with project id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data ={
            'idrandom': request.data.get('idrandom'),
            'name' : request.data.get('name'),
            'location': request.data.get('location'),
            'description' : request.data.get('description'),
        }
        serializer = ProjectSerializer(
            instance = project_instance,
            data=data,
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #Elimina el elemento Project con project_id dado, si existe
    def delete(self, request, project_id, *args, **kwargs):
        project_instance = self.get_objects(project_id)
        if not project_instance:
            return Response(
                {"res": "Object with project id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        project_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )   


class DevicesListApiView(APIView):
     #Lista todos los registros
    def get( self, request, *args, **kwargs):
        '''
        List all the project items for given requeted user
        '''
        devices = Devices.objects
        serializer = DevicesSerializer(devices, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    #Crea un nuevo registro
    def post(self, request, *args, **kwags):
        '''
        Create the Project wint given project data
        '''
        data = {
            'id' : request.data.get('id'),
            'name' : request.data.get('name'),
            'location': request.data.get('location'),
        }
        serializer = DevicesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DevicesDetailApiView(APIView):
    #Método auxiliar para obtener el objecto con project_id dado
    def get_objects(self, device_id):
        try:
            return Devices.objects.get(id= device_id)
        except Devices.DoesNotExist:
            return None
    #Recupera el elemento Project con project_id dado
    def get(self, request,device_id, *args, **kwargs):
        device_instance = self.get_objects(device_id)
        if not device_instance:
            return Response(
                {"res": "Object with project id does not exists"},
                status=status.HTTP_400_BAD_REQUEST    
            )
        serializer = DevicesSerializer(device_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #Actualiza el elemento Project con project_id dado, si existe
    def put(self, request,device_id, *args, **kwargs):
        device_instance = self.get_objects(device_id)
        if not device_instance:
            return Response(
                {"res": "Object with project id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data ={
            'id' : request.data.get('id'),
            'name' : request.data.get('name'),
            'description': request.data.get('location'),
        }
        serializer = DevicesSerializer(
            instance = device_instance,
            data=data,
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #Elimina el elemento Project con project_id dado, si existe
    def delete(self, request,device_id, *args, **kwargs):
        device_instance = self.get_objects(device_id)
        if not device_instance:
            return Response(
                {"res": "Object with project id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        device_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )   

class TemplateListApiView(APIView):
    # Lista todos los registros
    def get(self, request, *args, **kwargs):
        '''
        List all the project items for given requested user
        '''
        templates = Template.objects.all()
        serializer = TemplateSerializer(templates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Crea un nuevo registro
    def post(self, request, *args, **kwargs):
        '''
        Create the Project with given project data
        '''
        data = {
            'id': request.data.get('id'),
            'name': request.data.get('name'),
            'sensor': request.data.get('sensor'),
            'red' : request.data.get('red'),
            'descripcion': request.data.get('descripcion'),
        }
        serializer = TemplateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TemplateDetailApiView(APIView):
    # Método auxiliar para obtener el objeto con project_id dado
    def get_object(self, template_id):
        try:
            return Template.objects.get(id=template_id)
        except Template.DoesNotExist:
            return None

    # Recupera el elemento Project con project_id dado
    def get(self, request, template_id, *args, **kwargs):
        template_instance = self.get_object(template_id)
        if not template_instance:
            return Response(
                {"res": "Object with template id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = TemplateSerializer(template_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Actualiza el elemento Project con project_id dado, si existe
    def put(self, request, template_id, *args, **kwargs):
        template_instance = self.get_object(template_id)
        if not template_instance:
            return Response(
                {"res": "Object with template id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'id': request.data.get('id'),
            'name': request.data.get('name'),
            'sensor': request.data.get('sensor'),
            'red' : request.data.get('red'),
            'descripcion': request.data.get('descripcion'),
        }
        serializer = TemplateSerializer(
            instance=template_instance,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Elimina el elemento Project con project_id dado, si existe
    def delete(self, request, template_id, *args, **kwargs):
        template_instance = self.get_object(template_id)
        if not template_instance:
            return Response(
                {"res": "Object with template id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        template_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

# Create your views here.
