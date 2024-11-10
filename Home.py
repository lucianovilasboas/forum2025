import streamlit as st

st.set_page_config(page_title="Fórum França-Brasil", page_icon=":earth_americas:", layout="wide")

def main():
    st.title("Fórum França-Brasil")
    st.header("Sobre o Fórum")
    st.write("""
    O Fórum França-Brasil é um evento anual que reúne especialistas, acadêmicos, 
    empresários e autoridades dos dois países para discutir temas de interesse comum. 
    O objetivo é fortalecer as relações bilaterais e promover a cooperação em diversas áreas, 
    como economia, cultura, ciência e tecnologia.
    """)

if __name__ == "__main__":
    main()