def list_public_attributes(obj):
    return [attr for attr in dir(obj) if not attr.startswith("_")]