def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp4', '.wmv', '.mov', '.flv']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')