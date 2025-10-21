import tweepy, random, time

# Conexión a la API (usa variables de entorno)
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# Autenticación
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Lista de frases (puedes reemplazarlas por tu archivo de frases.txt)
frases = [
    "El éxito no llega solo, se construye paso a paso. 💪",
    "Hoy es un buen día para comenzar algo nuevo.",
    "No esperes a que pase: haz que ocurra. 🚀",
]

# Publicar una frase aleatoria
frase = random.choice(frases)
api.update_status(frase)
print(f"Publicado: {frase}")
