"""
Paramètres Django – projet immo
Docker + PostgreSQL + Allauth
"""

from pathlib import Path
from decouple import config

# ───────────────────────────────
# BASE
# ───────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("DJANGO_SECRET_KEY", default="dev-secret")
DEBUG = config("DJANGO_DEBUG", default=True, cast=bool)
ALLOWED_HOSTS = ["*"]

# ───────────────────────────────
# APPS
# ───────────────────────────────
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Allauth ↓↓↓
    "django.contrib.sites",
    "allauth",
    "allauth.account",
]

# ───────────────────────────────
# MIDDLEWARE
# ───────────────────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "allauth.account.middleware.AccountMiddleware",     # ← ajouté
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ───────────────────────────────
# URL & WSGI
# ───────────────────────────────
ROOT_URLCONF = "immo.urls"
WSGI_APPLICATION = "immo.wsgi.application"

# ───────────────────────────────
# TEMPLATES
# ───────────────────────────────
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ───────────────────────────────
# DATABASE
# ───────────────────────────────
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME":     config("POSTGRES_DB", default="immo"),
        "USER":     config("POSTGRES_USER", default="postgres"),
        "PASSWORD": config("POSTGRES_PASSWORD", default="postgres"),
        "HOST":     config("POSTGRES_HOST", default="db"),
        "PORT":     config("POSTGRES_PORT", default="5432"),
    }
}

# ───────────────────────────────
# INTERNATIONALISATION
# ───────────────────────────────
LANGUAGE_CODE = "fr-fr"
TIME_ZONE = "Europe/Paris"
USE_I18N = True
USE_TZ = True

# ───────────────────────────────
# FICHIERS STATIQUES
# ───────────────────────────────
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

# ───────────────────────────────
# DJANGO-ALLAUTH
# ───────────────────────────────
SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",                # admin
    "allauth.account.auth_backends.AuthenticationBackend",      # allauth
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"   # "mandatory" pour forcer validation
LOGIN_REDIRECT_URL = "/health/"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # e-mails en console

# ───────────────────────────────
# AUTRES
# ───────────────────────────────
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
