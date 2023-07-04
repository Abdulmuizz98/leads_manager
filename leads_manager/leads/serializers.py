from rest_framework import serializers
from leads.models import Lead

class LeadSerializer(serializers.ModelSerializer):
	"""
	"""
	class Meta:
		model = Lead
		fields = '__all__'

	#def create(self, validated_data):
	#	return Lead(**validated_data)
