import tweepy, os

# 🔑 Claves desde GitHub Secrets
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# 🔐 Autenticación OAuth 1.0a
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# 📄 Leer frases
with open("frases.txt", "r", encoding="utf-8") as f:
    frases = [line.strip() for line in f if line.strip()]

# 📌 Archivo para guardar índice actual
INDEX_FILE = "index.txt"
if os.path.exists(INDEX_FILE):
    with open(INDEX_FILE, "r") as f:
        index = int(f.read().strip())
else:
    index = 0

# 🔹 Publicar frase correspondiente
if index < len(frases):
    frase = frases[index]
    api.update_status(frase)
    print(f"Publicado: {frase}")

    # Incrementar índice para la próxima ejecución
    index += 1
    with open(INDEX_FILE, "w") as f:
        f.write(str(index))
else:
    print("Todas las frases ya fueron publicadas.")
    # 🔄 Para reiniciar el ciclo, descomenta la siguiente línea
    # with open(INDEX_FILE, "w") as f: f.write("0")
