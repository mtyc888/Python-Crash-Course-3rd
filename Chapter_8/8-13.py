def build_profile(first, last, **user_info):
    """Build a dictonary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert','einstein', location='princeton', field='physics')

marvin = build_profile('marvin','tan',age='25',location='penang', nationality='malaysia')
print(marvin)