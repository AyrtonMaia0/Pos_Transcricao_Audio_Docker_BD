from minio import Minio
from faster_whisper import WhisperModel

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

# 2. Carregar modelo Whisper (faster-whisper)
model = WhisperModel("base")

# 3. Transcrever o áudio
segments, info = model.transcribe(local_file, language="pt")

# Junta os textos
full_text = " ".join([segment.text for segment in segments])

print("Transcrição:")
print(full_text)

# 4. Salvar em arquivo
with open("transcricao.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print("Transcrição salva em transcricao.txt")
