from minio import Minio
import os

MINIO_HOST = os.getenv("MINIO_HOST", "localhost:9000")
ACCESS_KEY = os.getenv("MINIO_ROOT_USER", "admin")
SECRET_KEY = os.getenv("MINIO_ROOT_PASSWORD", "admin123")
BUCKET = "audios"

client = Minio(MINIO_HOST, access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)

# Criar bucket se não existir
if not client.bucket_exists(BUCKET):
    client.make_bucket(BUCKET)
    print(f"Bucket '{BUCKET}' criado.")
else:
    print(f"Bucket '{BUCKET}' já existe.")

local_file = "Mamonas Assassinas - 1406.mp3"
object_name = os.path.basename(local_file)

# Faz upload (fput_object) - preserva o arquivo original
client.fput_object(BUCKET, object_name, local_file)
print(f"Upload concluído: {object_name} -> bucket '{BUCKET}'")
