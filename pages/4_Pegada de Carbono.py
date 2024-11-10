import streamlit as st

def main():
    st.title("Empreinte Carbone/Pegada de Carbono")

    col_fr, col_br = st.columns([1, 1])

    with col_fr:
        st.info("Comment diminuer son empreinte carbone par des solutions alternatives")
    
    with col_br:
        st.info("Reduzindo sua pegada de carbono através de soluções alternativas")
  

if __name__ == "__main__":
    main()
