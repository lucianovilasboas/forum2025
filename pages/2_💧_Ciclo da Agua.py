import streamlit as st



def main():
    st.title("💧 Cycle de l'eau/Ciclo da Água")

    col_fr, col_br = st.columns([1, 1])
    
    with col_fr:
        st.info("Étude de la dynamique du cycle de l'eau dans les forêts tempérées et tropicales")
    
    with col_br:
        st.info("Estudo da dinâmica do ciclo da água em florestas temperadas e tropicais")
  


if __name__ == "__main__":
    main()
