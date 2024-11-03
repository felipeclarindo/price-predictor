import streamlit as st
from .modules.generate_machine_model import generate_machine_model
from sklearn.linear_model import LinearRegression
from pathlib import Path

class App:
    def __init__(self):
        self.model = self._get_machine_model()
        self.configure()

    @classmethod
    def _get_machine_model(cls):
        return generate_machine_model()

    def _predict_price(self, diametro):
        return self.model.predict([[diametro]])[0][0]

    def configure(self):
        st.set_page_config(page_title="Pizza Price Predictor", page_icon="🍕")

    def button_command_predict(self, diametro: float):
        preco = self._predict_price(diametro)
        return f"O preço estimado da pizza é de R$ {preco:.2f}!"

    def run(self):
        st.title("🍕 Pizza Price Predictor 🍕")
        st.markdown("### Descubra o preço estimado de uma pizza com base em seu diâmetro!")
        st.divider()

        diametro = st.number_input(
            "Digite o diâmetro da pizza (em cm):", 
            min_value=0, max_value=100, value=0, step=1, 
            help="Escolha um diâmetro entre 1 e 100 cm"
        )

        if st.button("Calcular preço", key="predict", help="Clique para calcular o preço estimado"):
            if diametro > 0:
                message = self.button_command_predict(diametro)
                st.success(message)
            else:
                st.warning("Por favor, insira um diâmetro válido maior que zero.")
