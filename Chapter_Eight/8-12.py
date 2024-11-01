def make_sandwich(*items):
    """Make a sandwich with the given item"""
    print("\nI'll make you a great sandwich")
    for item in items:
        print(f"...adding {item} to your sandwich")
    print("Your sandwich is ready")

make_sandwich('roast beef','cheddar cheese','onion','bacon')
make_sandwich('peanut butter','grape jelly')
make_sandwich('turkey slices','apples sauce','honey mustard')