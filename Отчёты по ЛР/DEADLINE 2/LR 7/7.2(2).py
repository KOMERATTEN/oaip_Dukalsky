def build_user_profile(user_id, **kwargs):
    return {'user_id': user_id, **kwargs}

profile = build_user_profile(101, name="Анна", status="online")
print(profile)