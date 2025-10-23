import tweepy, os, subprocess

# 🔑 Claves desde GitHub Secrets
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# 🧩 Autenticación API v2 (User Context)
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

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

# 🚀 Publicar frase correspondiente
if index < len(frases):
    frase = frases[index]
    try:
        client.create_tweet(text=frase)
        print(f"✅ Publicado: {frase}")

        # Incrementar índice
        index += 1
        with open(INDEX_FILE, "w") as f:
            f.write(str(index))

        # 🧩 Guardar el nuevo índice en el repositorio
        subprocess.run(["git", "config", "user.name", "github-actions"])
        subprocess.run(["git", "config", "user.email", "github-actions@github.com"])
        subprocess.run(["git", "add", INDEX_FILE])
        subprocess.run(["git", "commit", "-m", f"🔁 Actualizado índice a {index}"])
        subprocess.run(["git", "push"])
        print("📤 Índice actualizado en el repositorio.")

    except Exception as e:
        print(f"❌ Error al publicar: {e}")
else:
    print("✅ Todas las frases ya fueron publicadas.")
    # Si quieres que reinicie desde el inicio, descomenta:
    # with open(INDEX_FILE, "w") as f: f.write("0")
