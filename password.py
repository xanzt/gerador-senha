import streamlit as st
import random
import string


# Função para gerar a senha
def generate_password(length, use_uppercase, use_numbers, use_symbols):
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    # Garantir que os requisitos sejam atendidos
    if not chars:
        return "Por favor, escolha ao menos um tipo de caractere."

    return ''.join(random.choice(chars) for _ in range(length))


# Função principal do aplicativo
def main():
    # CSS para forçar o tema escuro
    dark_mode_css = """
    <style>
        body {
            background-color: #0E1117;
            color: #ffffff;
        }
    </style>
    """
    st.markdown(dark_mode_css, unsafe_allow_html=True)

    # Exibe o logo no topo da página
    logo_url = "https://i.ibb.co/qBwfjTX/LOGO-BRANCO.png"
    st.image(logo_url, width=200)

    # Título e descrição
    st.title("Gerador de Senhas Seguras")
    st.write("Use este gerador para criar senhas seguras e personalizadas.")

    # Entrada do usuário
    length = st.slider("Comprimento da senha", min_value=6, max_value=20, value=8)
    use_uppercase = st.checkbox("Incluir letras maiúsculas")
    use_numbers = st.checkbox("Incluir números")
    use_symbols = st.checkbox("Incluir símbolos")

    # Gerar senha
    if st.button("Gerar senha"):
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        st.text_input("Sua senha gerada é:", password, key="generated_password")

    # Dica de segurança
    st.write("⚠️ **Dica de segurança:** Não esqueça de anotar ou salvar sua senha.")

    # Adicionando o texto de rodapé
    st.markdown(
        """
        <p style="font-size: 12px; color: gray; text-align: center; margin-top: 10px;">
        By: Alexandre Carvalho.
        </p>
        """, unsafe_allow_html=True
    )


# Executa o aplicativo
if __name__ == "__main__":
    main()
