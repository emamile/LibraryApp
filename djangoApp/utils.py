from django.core.exceptions import ObjectDoesNotExist
from django.db import OperationalError
from rest_framework import status
from rest_framework.response import Response

from djangoApp.constants import ERROR_MESSAGE_CONNECTION_TO_SERVER_FAILED, ERROR_MESSAGE_OBJECT_WITH_ID_DOES_NOT_EXIST


def exception_handler(exc, context):
    response = None

    if isinstance(exc, OperationalError):
        response = Response(status=status.HTTP_503_SERVICE_UNAVAILABLE,
                            data=ERROR_MESSAGE_CONNECTION_TO_SERVER_FAILED)
    elif isinstance(exc, ObjectDoesNotExist):
        response = Response(status=status.HTTP_400_BAD_REQUEST,
                            data=ERROR_MESSAGE_OBJECT_WITH_ID_DOES_NOT_EXIST.format(context.get("view").model.__name__, context.get("kwargs").get("id")))
    elif isinstance(exc, ValueError):
        response = Response(status=status.HTTP_400_BAD_REQUEST,
                            data=exc.__str__())
    elif isinstance(exc, Exception):
        response = Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data=exc.__str__())

    if response:
        return response
    return exception_handler(exc, context)
