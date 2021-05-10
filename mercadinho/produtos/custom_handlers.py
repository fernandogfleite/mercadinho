from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data['status_code'] = response.status_code
        if response.data['status_code'] == 400 and response.data['id_category'][0].startswith("Invalid pk"):
            return Response({"error": "Categoria não existente"}, status=400)
        else:
            return response

    exc_list = str(exc).split("DETAIL: ")
    
    return Response({"error":exc_list[-1]})