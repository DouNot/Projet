"""
Initialisation de l’app « core ».

Le seul but est d’indiquer à Django quelle classe AppConfig utiliser,
afin que la méthode ready() (qui importe core.signals) soit exécutée.
"""

# Charge CoreConfig pour que ready() importe les signaux
default_app_config = "core.apps.CoreConfig"
