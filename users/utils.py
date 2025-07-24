from .models import User

def get_logged_in_user(request):
    user_id = request.session.get('user_id')
    if user_id:
        return User.objects(id=user_id).first()
    return None
