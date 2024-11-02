from user import Admin

marvin = Admin('marvin','tan',25)
marvin.describe_user()

marvin_priviledges = ['add','delete','update']

marvin.priviledges.priviledges = marvin_priviledges

marvin.priviledges.show_priv()