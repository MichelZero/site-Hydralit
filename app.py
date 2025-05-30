#
# autor: Michel
# date: 2025-05-29

import streamlit as st
from streamlit_option_menu import option_menu

# 1. as sidebar menu
# Exemplo inspirado em ifbemnumeros.ifb.edu.br
with st.sidebar:
    selected = option_menu("Menu", ['Início', 'Ensino', 'Assistência Estudantil', 'Configurações'],	 
        icons=['house', 'book', 'people', 'gear'],  # Ícones Bootstrap
        menu_icon="cast", default_index=0) # cast também é um ícone Bootstrap

# 2. Exibe a opção selecionada
if selected == 'Início':
    # Para o Streamlit 1.28.0 e superior:
    st.switch_page("pages/inicio.py") 
    # Se você tiver outras páginas, adicione condições semelhantes:
    # elif selected == 'Ensino':
    #     st.switch_page("pages/ensino.py") 
    # ... e assim por diante

# if selected == 'Início':
#     st.switch_page("pages/inicio.py")
# elif selected == 'Ensino':
#     # Supondo que você tenha um pages/ensino.py
#     # st.switch_page("pages/ensino.py")
#     st.write("Página de Ensino selecionada (implementar pages/ensino.py)")
# elif selected == 'Assistência Estudantil':
#     st.write("Página de Assistência Estudantil selecionada (implementar)")
# elif selected == 'Configurações':
#     st.write("Página de Configurações selecionada (implementar)")
# else:
#     # Conteúdo padrão de app.py se nenhuma outra página for explicitamente chamada
#     # ou se 'Início' for o conteúdo padrão de app.py
#     # import pages.inicio # Alternativa se não usar switch_page
#     # pages.inicio.show_page() # Alternativa se não usar switch_page
    st.write("Selecione uma opção no menu.")


