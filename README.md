# Calculadora de Frete - Erika

Este é um simples script em HTML e JavaScript para calcular tarifas de frete com base no valor da nota fiscal e na localização (capital ou interior).
Instruções de Uso

    Abra o arquivo calculadora_de_frete.html em um navegador da web.
    Preencha os campos obrigatórios no formulário:
        Valor da nota fiscal (R$): Insira o valor total da nota fiscal.
        Localização (capital/interior): Insira a localização onde será entregue a mercadoria (capital ou interior).
    Clique no botão "Calcular Tarifa de Frete".
    O resultado do cálculo será exibido abaixo do formulário.

# Detalhes do Cálculo

    A tarifa de frete é calculada com base no valor da nota fiscal e na localização da entrega.
    Para localizações na capital, a tarifa é de 7% do valor da nota fiscal.
    Para localizações no interior, a tarifa é de 8.5% do valor da nota fiscal.
    Uma taxa de 6% de desconto é aplicada à tarifa calculada.

# Requisitos do Sistema

    Navegador da web compatível com HTML5 e JavaScript.

Nota Importante

    Este script foi desenvolvido como um exemplo educacional e pode não ser adequado para ambientes de produção sem considerar possíveis ajustes e validações adicionais.

# Script 2

Este é um aplicativo que calcula tarifas de frete com base no valor da nota fiscal e na localização (capital ou interior) dos destinatários. O aplicativo agora suporta a leitura de uma planilha XLSX para calcular as tarifas de frete.
Instruções de Uso

    Certifique-se de ter um navegador da web compatível com HTML5 e JavaScript.
    Execute o aplicativo Flask digitando python app.py no terminal.
    Abra o navegador da web e vá para http://localhost:5000/.
    Selecione a planilha XLSX contendo os detalhes das faturas e a localização dos destinatários.
    Clique no botão "Enviar" para calcular as tarifas de frete.
    O arquivo com as tarifas de frete calculadas será baixado automaticamente.

# Detalhes do Cálculo

    A tarifa de frete é calculada com base no valor da nota fiscal e na localização da entrega.
    Para localizações na capital, a tarifa é de 7% do valor da nota fiscal.
    Para localizações no interior, a tarifa é de 8.5% do valor da nota fiscal.
    Uma taxa de 6% de desconto é aplicada à tarifa calculada.

# Requisitos do Sistema

    Python 3.x
    Flask
    pandas
    Um navegador da web compatível com HTML5 e JavaScript

# Nota Importante

Este aplicativo foi desenvolvido como um exemplo educacional e pode não ser adequado para ambientes de produção sem considerar possíveis ajustes e validações adicionais.
# Observação: A planilha fornecida deve incluir obrigatoriamente as colunas NF_VALOR e MUNICIPIO.
# Autor

Desenvolvido por Hebert Ribeiro - JAN-2024
