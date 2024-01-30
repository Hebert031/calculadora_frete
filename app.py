from flask import Flask, request, jsonify, send_file
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/calcular_tarifa_de_frete', methods=['POST'])
def calcular_tarifa_de_frete():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nenhum arquivo selecionado'}), 400

    if file and file.filename.endswith('.xlsx'):
        # Salva o arquivo temporariamente
        file_path = 'temp.xlsx'
        file.save(file_path)

        try:
            # Carrega a planilha XLSX
            df = pd.read_excel(file_path, sheet_name='TRADING CARE')
            print(df.head())  # Imprime as primeiras linhas do DataFrame
            print(df.columns)  # Imprime os nomes das colunas do DataFrame

            # Remove espaços em branco extras nos nomes das colunas
            df.columns = df.columns.str.strip()

            # Verifica se as colunas 'NF_VALOR' e 'MUNICIPIO' existem
            if 'NF_VALOR' not in df.columns or 'MUNICIPIO' not in df.columns:
                raise ValueError("Colunas 'NF_VALOR' e 'MUNICIPIO' são necessárias na planilha")

            # Calcula a tarifa de frete
            df['Tarifa_de_Frete'] = df.apply(lambda row: row['NF_VALOR'] * (0.07 if row['MUNICIPIO'] == 'Belo Horizonte' else 0.085) * 0.94, axis=1)

            # Salva a nova planilha com a coluna de cálculo de frete
            output_file_path = 'planilha_com_frete.xlsx'
            df.to_excel(output_file_path, index=False)

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
