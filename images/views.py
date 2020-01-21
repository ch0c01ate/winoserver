from .serializers import ImageSerializer
from .models import Image
from rest_framework import mixins, generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

class ImageList(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):

    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)