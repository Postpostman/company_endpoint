from rest_framework import serializers

from company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

    company_name = serializers.CharField(required=True)
    company_email = serializers.EmailField(required=True)
