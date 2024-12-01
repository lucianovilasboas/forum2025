import streamlit as st
import user # Import the user.py file


# acesse a pagina se o 'role' for um 'user'
if 'logged_in' not in st.session_state or 'role' not in st.session_state or st.session_state.role != 'user':
    st.session_state.logged_in = False


def login():
    user.init_db()
    user.main()

    # if st.button("Log in"):
    #     st.session_state.logged_in = True
    #     st.rerun()

def logout():
    st.write("Clique no botão abaixo para sair do sistema.")
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.session_state['role'] = None
        st.session_state['username'] = None
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

home = st.Page("home/Forum.py", title="Fórum", icon=":material/dashboard:", default=True)
ods = st.Page("home/Ods.py", title="ODS", icon="🎯")



agua_home = st.Page("agua/Ciclo_Agua.py", title="Ciclo da Agua", icon="💧")
agua_equipes = st.Page("agua/Equipes1.py", title="Equipes", icon="👥")
agua_links = st.Page("agua/Links1.py", title="Links", icon="🔗")
agua_coleta_dados = st.Page("agua/Coleta_Dados1.py", title="Coleta de Dados", icon="📊")


carbono_home = st.Page(page="carbono/Pegada_Carbono.py", title="Pegada de Carbono", icon="🌍")
carbono_equipes = st.Page(page="carbono/Equipes2.py", title="Equipes", icon="👥")
carbono_links = st.Page("carbono/Links2.py", title="Links", icon="🔗")
carbono_coleta_dados = st.Page("carbono/Coleta_Dados2.py", title="Coleta de Dados", icon="📊")

carbon_calc = st.Page("tools/Calculadora_Carbono.py", title="Calculadora de Carbono", icon="🌳")
monitor = st.Page("tools/Acoes_Sustentabilidade.py", title="Ações de Sustentabilidade", icon="🌍")

# history = st.Page("tools/history.py", title="History", icon=":material/history:")

pg = st.navigation(
    {
        "Home": [home, ods],
        "Agua": [agua_home, agua_equipes, agua_links, agua_coleta_dados],
        "Carbono": [carbono_home, carbono_equipes,carbono_links, carbono_coleta_dados],
        "Tools": [carbon_calc, monitor],
    }
)
    


pg.run()