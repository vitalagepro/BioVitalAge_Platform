"""
API view configuration
"""
from rest_framework import viewsets, filters
from drf_spectacular.utils import (
    extend_schema, 
    extend_schema_view,
    OpenApiResponse
)

from .models import Note
from .serializers import NoteSerializer


@extend_schema_view(
    list=extend_schema(summary="Elenco note", tags=["Note"]),
    create=extend_schema(summary="Crea nota", tags=["Note"]),
    retrieve=extend_schema(summary="Dettaglio nota", tags=["Note"]),
    update=extend_schema(summary="Aggiorna nota (PUT)", tags=["Note"]),
    partial_update=extend_schema(summary="Aggiorna nota (PATCH)", tags=["Note"]),
    destroy=extend_schema(
        summary="Elimina nota",
        tags=["Note"],
        responses={204: OpenApiResponse(description="Cancellazione OK")},
    ),
)
class NoteViewSet(viewsets.ModelViewSet):
    """CRUD completo per le note."""
    queryset = Note.objects.all().order_by("-created")
    serializer_class = NoteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]