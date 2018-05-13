from .models import Issue
from .serializers import IssueSerializer
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions

class IssueList(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class IssueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticated)