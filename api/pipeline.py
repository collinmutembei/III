from api.models import UserProfile


def get_profile_picture(strategy, user, response, is_new=False, *args, **kwargs):
    img_url = None
    backend = kwargs['backend']

    if backend.name == 'twitter':
        img_url = response.get('profile_image_url', '').replace('_normal', '')

    profile = UserProfile.objects.get_or_create(user=user)[0]
    profile.avatar = img_url
    profile.save()
