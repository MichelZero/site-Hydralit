




# Exemplo inspirado em ifbemnumeros.ifb.edu.br
selected_ifb = option_menu(
    menu_title=None,  # Não precisamos de um título principal para o menu horizontal
    options=["Início", "Cursos", "Servidores", "Discentes", "Extensão", "Pesquisa"],
    icons=['house', 'book', 'person-badge', 'people', 'arrows-angle-expand', 'search'],  # Ícones do Bootstrap
    menu_icon="cast",  # Ícone opcional para o menu em si
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#ffffff"}, # Cor de fundo similar
        "icon": {"color": "#00693C", "font-size": "20px"}, # Cor verde do IFB
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px 5px",
            "--hover-color": "#e0e0e0", # Cor ao passar o mouse
            "color":  "#333" # Cor do texto
        },
        "nav-link-selected": {"background-color": "#007bff", "color": "white"}, # Cor de item selecionado (azul como exemplo)
    }
)

# Exibe a opção selecionada
if selected_ifb == "Início":
    st.write("Você selecionou Início.")
elif selected_ifb == "Cursos":
    st.write("Você selecionou Cursos.")
elif selected_ifb == "Servidores":
    st.write("Você selecionou Servidores.")
elif selected_ifb == "Discentes":
    st.write("Você selecionou Discentes.")
elif selected_ifb == "Extensão":
    st.write("Você selecionou Extensão.")
elif selected_ifb == "Pesquisa":
    st.write("Você selecionou Pesquisa.")


