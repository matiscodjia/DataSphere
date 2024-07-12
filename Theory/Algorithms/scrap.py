import gzip
import json

# Chemin vers le fichier JSON compressé
chemin_fichier_gz = 'Firefox 2024-05-05 16.06 test_le_monde profile.json.gz'

# Décompression du fichier .gz
with gzip.open(chemin_fichier_gz, 'rb') as fichier_gz:
    # Lecture du JSON décompressé
    contenu_decompresse = fichier_gz.read()
    # Conversion du JSON en objet Python (dictionnaire)
    objet_json = json.loads(contenu_decompresse.decode('utf-8'))

# Maintenant, vous pouvez utiliser objet_json comme un dictionnaire Python
print(objet_json)
