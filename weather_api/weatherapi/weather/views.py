from django.core.cache import cache
from django.http import JsonResponse
from django_ratelimit.decorators import ratelimit
from .services import fetch_weather_data

@ratelimit(key='ip', rate='10/m', block=True)
def get_weather(request, city):
    cache_key = f"weather:{city.lower()}"
    data = cache.get(cache_key)

    if not data:
        data = fetch_weather_data(city)

        if data and isinstance(data, dict) and "address" in data:
            cache.set(cache_key, data, timeout=600)  # cache for 10 minutes
        else:
            return JsonResponse({"error": "City not found or API error"}, status=400)

    return JsonResponse(data)
