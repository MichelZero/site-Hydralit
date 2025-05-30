#
# autor: Michel
# date: 2025-05-29

import streamlit as st
from streamlit_option_menu import option_menu


# from streamlit_option_menu import option_menu # Removido se o menu principal está em app.py e este é um menu secundário

# Conteúdo principal da página Início
st.title("Página Inicial")
st.write("Bem-vindo à página inicial!")
# Adicione aqui o conteúdo específico da página inicial

# Se você quiser um menu secundário nesta página, pode mantê-lo:
# Exemplo inspirado em ifbemnumeros.ifb.edu.br
selected_ifb_interno = option_menu(
    menu_title="Menu Interno da Página Início",
    options=["Detalhes Início", "Outra Seção Início"],
    icons=['info-circle', 'list-task'],
    menu_icon="caret-right-square",
    default_index=0,
    orientation="horizontal",
    # ... styles ...
)

if selected_ifb_interno == "Detalhes Início":
    st.write("Detalhes da página inicial.")
elif selected_ifb_interno == "Outra Seção Início":
    st.write("Outra seção da página inicial.")
