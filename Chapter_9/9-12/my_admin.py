from admin import Admin

marvin = Admin('marvin','tan',25)

marvin.describe_user()

marvin_priviledges = ['add','remove','update']

marvin.priviledges.priviledges = marvin_priviledges

marvin.priviledges.show_priv()