def image_validate(name: str):
    formats = ['png', 'jpg', 'jpeg']
    name = name.split('.')
    if name[len(name)-1] in formats:
        return True
    return False
