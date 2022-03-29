class ActionNames:
    EmailSubject = "Your account has been activated."


class EmailHelper:
    EMAIL_HOST = "mx1.cs.umb.edu"
    EMAIL_PORT = 25

    # EMAIL_HOST = os.environ.get('EMAIL HOST')
    # EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    # EMAIL_USE_TLS = True
    # DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
    # EMAIL_PORT = 587
    # EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')