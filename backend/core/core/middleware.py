from rest_framework.response import Response

def permission_required(permission):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user = request.user

            if not user.is_authenticated:
                return Response({"error":"Unauthorized"}, status=401)

            if permission not in request.auth.get('permissions', []):
                return Response({"error":"Forbidden"}, status=403)

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
