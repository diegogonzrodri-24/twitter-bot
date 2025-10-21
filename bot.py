import tweepy, random, time

# Conexión a la API (usa variables de entorno)
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# Autenticación
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Lista de frases 
with open("frases.txt", "r", encoding="utf-8") as f:
    frases = [line.strip() for line in f if line.strip()]

# Publicar una frase aleatoria
frase = random.choice(frases)
api.update_status(frase)
print(f"Publicado: {frase}")

