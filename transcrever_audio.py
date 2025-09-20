from minio import Minio
from faster_whisper import whispermodel

# Configuração do MinIO
client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="admin123",
    secure=False
)

bucket_name = "audios"
object_name = "Mamonas Assassinas - 1406.mp3"
local_file = "audio.mp3"

# 1. Baixar o arquivo do MinIO
client.fget_object(bucket_name, object_name, local_file)
print(f"Arquivo baixado: {local_file}")

# 2. Carregar modelo Whisper (use 'base' para começar, pode trocar por 'small', 'medium', 'large')
model = whisper.load_model("base")

# 3. Transcrever o áudio
result = model.transcribe(local_file, language="pt")  # força português
print("Transcrição:")
print(result["text"])

# 4. Salvar em arquivo
with open("transcricao.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("Transcrição salva em transcricao.txt")
