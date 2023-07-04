from .serializers import LeadSerializer
from .models import Lead
from rest_framework import viewsets, permissions


class LeadViewSet(viewsets.ModelViewSet):
	""" Lead ViewSet
	"""
	serializer_class = LeadSerializer
	permission_classes = [
		permissions.AllowAny
	]
	queryset = Lead.objects.all()
