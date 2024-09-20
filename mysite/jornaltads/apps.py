from django.apps import AppConfig  # Importa a classe base AppConfig, usada para configurar aplicativos no Django

# Define uma classe de configuração para o aplicativo 'jornaltads'
class JornaltadsConfig(AppConfig):
    # Define o campo padrão para chaves primárias nos modelos como BigAutoField (inteiro maior)
    default_auto_field = 'django.db.models.BigAutoField'

    # Define o nome do aplicativo como 'jornal', que o Django usará para identificá-lo
    name = 'jornaltads'

