import sys
import hashlib
def encrypt(file_name: str):
    """
    datei öffnen | OK -> inhalt verschlüsseln | OK -> als neue datei speichern -> pushen und committen
    """
    with open(file_name, "rb") as f:
        file = f.read()
    print(file)
    encrypted = hashlib.md5(file, usedforsecurity=False)
    print(encrypted.hexdigest())
    with open(f"".join(file_name.split(".")[:-1]) + "-enc." + file_name.split(".")[-1], "wb") as f:
        f.write(encrypted.hexdigest().encode())

if __name__ == "__main__":
    file_or_dir = sys.argv[1]
    print(file_or_dir)
    encrypt(file_or_dir)