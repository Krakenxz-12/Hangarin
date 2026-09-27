from django import template

register = template.Library()


@register.simple_tag
def social_profile_picture(user):

    if not user.is_authenticated:
        return None

    try:
        social_account = user.socialaccount_set.first()

        if social_account:
            return social_account.get_avatar_url()

    except Exception:
        pass

    return None