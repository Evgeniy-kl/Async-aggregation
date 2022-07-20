def image_validate(name: str):
    formats = ('png', 'jpg', 'jpeg',)
    if name.endswith(formats):
        return True
    return False
