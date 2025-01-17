from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, pagination, permissions, viewsets

from posts.models import Group, Post

from .permissions import AuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          AuthorOrReadOnly,)
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          AuthorOrReadOnly,)
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          AuthorOrReadOnly,)
    pagination_class = pagination.LimitOffsetPagination

    def _get_object(self):
        return get_object_or_404(
            Post, pk=self.kwargs.get('post_id')
        )

    def perform_create(self, serializer):
        post = self._get_object()
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = self._get_object()
        return post.comments.all()


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follow.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
