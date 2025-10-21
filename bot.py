import tweepy, os

# Autenticación con OAuth 2.0 User Context
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

# Leer frases
with open("frases.txt", "r", encoding="utf-8") as f:
    frases = [line.strip() for line in f if line.strip()]

# Leer índice actual
INDEX_FILE = "index.txt"
if os.path.exists(INDEX_FILE):
    with open(INDEX_FILE, "r") as f:
        index = int(f.read().strip())
else:
    index = 0

# Publicar la frase correspondiente
if index < len(frases):
    frase = frases[index]
    client.create_tweet(text=frase)
    print(f"Publicado: {frase}")
    
    # Incrementar índice para la próxima ejecución
    index += 1
    with open(INDEX_FILE, "w") as f:
        f.write(str(index))
else:
    print("Todas las frases ya fueron publicadas.")
