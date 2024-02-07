from flask import Flask, request, jsonify, send_file
import pandas as pd
import os

# Lista de cidades com taxa de 7%
cidades_taxa_7 = [
    "BELO HORIZONTE", "BETIM", "BRUMADINHO", "CONFINS", "CONTAGEM",
    "ESMERALDAS", "IBIRITE", "IGARAPE", "JABOTICATUBAS", "LAGOA SANTA",
    "MARIO CAMPOS", "MATEUS LEME", "NOVA LIMA", "RAPOSOS", "RIBEIRAO DAS NEVES",
    "SABARA", "SANTA LUZIA", "SÃO JOAQUIM DE BICAS", "SARZEDO", "VESPASIANO", "SETE LAGOAS"
]

app = Flask(__name__)

@app.route('/')
def index():
    return open('calculadora_planilha.html').read()

@app.route('/calcular_tarifa_de_frete', methods=['POST'])
def calcular_tarifa_de_frete():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nenhum arquivo selecionado'}), 400

    taxa_capital = float(request.form.get('taxa-capital', '0.07'))
    taxa_interior = float(request.form.get('taxa-interior', '0.085'))
    taxa_geral = float(request.form.get('taxa-geral', '0.94'))

    if file and file.filename.endswith('.xlsx'):
        # Salva o arquivo temporariamente
        file_path = 'temp.xlsx'
        file.save(file_path)

        try:
            # Carrega a planilha XLSX
            df = pd.read_excel(file_path)
            print(df.head())  # Imprime as primeiras linhas do DataFrame
            print(df.columns)  # Imprime os nomes das colunas do DataFrame

            # Remove espaços em branco extras nos nomes das colunas
            df.columns = df.columns.str.strip()

            # Verifica se as colunas 'NF_VALOR' e 'MUNICIPIO' existem
            if 'NF_VALOR' not in df.columns or 'MUNICIPIO' not in df.columns:
                raise ValueError("Colunas 'NF_VALOR' e 'MUNICIPIO' são necessárias na planilha")

            # Calcula a tarifa de frete e arredonda para duas casas decimais
            df['TARIFA_FRETE'] = df.apply(lambda row: round(row['NF_VALOR'] * (taxa_capital if row['MUNICIPIO'].upper() in cidades_taxa_7 else taxa_interior) / taxa_geral, 2), axis=1)
            # Salva a nova planilha com a coluna de cálculo de frete
            output_file_path = 'planilha_com_frete.xlsx'
            df.to_excel(output_file_path, index=False, float_format="%.2f")  # Define o formato float para duas casas decimais

            # Remove o arquivo temporário
            os.remove(file_path)

            # Retorna o arquivo resultante
            return send_file(output_file_path, as_attachment=True)
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    else:
        return jsonify({'error': 'Formato de arquivo inválido, selecione uma planilha XLSX'}), 400


if __name__ == '__main__':
    app.run(debug=True)
