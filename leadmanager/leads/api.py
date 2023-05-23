from leads.models import Lead
from rest_framework import viewsets, permissions
from rest_framework.authentication import BasicAuthentication
from .serializers import LeadSerializer
from rest_framework.permissions import IsAuthenticated

# Lead Viewset


class LeadViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LeadSerializer

    def get_queryset(self):
        return self.request.user.leads.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
