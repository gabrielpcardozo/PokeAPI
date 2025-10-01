#!/bin/sh
# Diretório dos arquivos .puml (volume compartilhado)
DOC_DIR=/PokeAPI_Django/Doc

# Diretório de saída (mesmo local, gera PNGs junto)
OUTPUT_DIR=$DOC_DIR

echo "Gerando imagens dos diagramas PlantUML..."

for f in "$DOC_DIR"/*.puml; do
    # Pega o nome base do arquivo
    filename=$(basename "$f" .puml)
    echo "Gerando $filename.png"
    # Envia via POST para o PlantUML-server interno (docker container plantuml)
    curl -X POST --data-binary @"$f" http://plantuml:8080/png > "$OUTPUT_DIR/$filename.png"
done

echo "Todos os diagramas foram atualizados!"
