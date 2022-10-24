from rest_framework.response import Response
from rest_framework.views import APIView
from api.mixins import ApiAuthMixin
from rest_framework.views import APIView
from rest_framework import serializers
from drf_spectacular.utils import extend_schema

from api.pagination import get_paginated_response, LimitOffsetPagination

from core.models import TimeLog
from core.selectors.time_log import log_list 
from core.services.time_log import logger 


class TimeTrackApi(ApiAuthMixin, APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 10

    class FilterSerializer(serializers.Serializer):
        all_members = serializers.BooleanField(required=False, default=True)
        name        = serializers.CharField(required=True)
        status      = serializers.CharField(required=False)

    class InputSerializer(serializers.Serializer):
        project   = serializers.CharField(required=True)

    class OutputSerializer(serializers.ModelSerializer):

        project = serializers.SerializerMethodField('get_project')
        member  = serializers.SerializerMethodField('get_member')
        class Meta:
            model = TimeLog 
            fields = (
                'project',
                'member',
                'start_at',
                'finish_at'
            )

        def get_project(self, time_log):
            return time_log.project_member.project.name

        def get_member(self, time_log):
            return time_log.project_member.member.email


    @extend_schema(
            parameters=[FilterSerializer,],
            responses=OutputSerializer,
            )
    def get(self, request):
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        logs = log_list(filters=filters_serializer.validated_data, user=request.user)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=logs,
            request=request,
            view=self
        )
 
    @extend_schema(
            request=InputSerializer,
            responses=OutputSerializer,
            )
    def post(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        time_log = logger(user= request.user, project=serializer.validated_data.get("project"))

        return Response(self.OutputSerializer(time_log).data)

