# Pizza Price Predictor

Este projeto é uma aplicação de aprendizado de máquina que estima o preço de uma pizza com base no diâmetro em centímetros. Usando `scikit-learn` e `Streamlit`, ele oferece uma interface amigável e intuitiva para visualizar as predições de preços em tempo real.

## Funcionalidades

- **Entrada do Diâmetro**: Permite ao usuário inserir o diâmetro da pizza em centímetros.
- **Predição de Preço**: Baseado em um modelo de regressão linear, o aplicativo estima o preço da pizza e exibe o valor estimado.
- **Interface Intuitiva**: Desenvolvido com `Streamlit`, o app possui uma interface simples e amigável para fácil uso.

## Tecnologias

- **Linguagem**: Python
- **Bibliotecas Principais**:
  - [Streamlit](https://streamlit.io/) - Interface da aplicação
  - [scikit-learn](https://scikit-learn.org/stable/) - Treinar o modelo de regressão linear
  - [Pandas](https://pandas.pydata.org/) - Manipulação de dados

## Instalação e Execução

1. Clone o repositório:

```bash
git clone https://github.com/felipeclarindo/pizza-price-predictor.git
cd pizza-price-predictor
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Inicie a aplicação:

```bash
streamlit run app/main.py
```

4. Uso

- Abra o navegador e vá para http://localhost:8501.
- Insira o diâmetro da pizza em centímetros.
- Clique em Calcular preço para ver a predição.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor

**Felipe Clarindo**

- [LinkedIn](https://www.linkedin.com/in/felipeclarindo)
- [Instagram](https://www.instagram.com/lipethecoder)
- [GitHub](https://github.com/felipeclarindo)

## Licença

Este projeto está licenciado sob a [GNU Affero License](https://www.gnu.org/licenses/agpl-3.0.html).
