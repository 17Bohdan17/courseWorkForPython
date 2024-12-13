from django.http import HttpResponse
from django.db import connection

def test_connection(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
        return HttpResponse("Connection successful!")
    except Exception as e:
        return HttpResponse(f"Error: {e}")
