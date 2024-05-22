import re

string = "joli je suis joli"
pattern = r"(joli)"  # L'expression régulière avec le mot à conserver

result = re.split(pattern, string)
result = [segment for segment in result if segment]  # Enlever les segments vides si nécessaire

print(result)