import streamlit as st

# Adicionando o CSS personalizado
st.markdown("""
    <style>
       .cartao-pokemon{
            display: none;
            box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
            border-radius: 10px;
        }

        .cartao-pokemon .cartao-topo{
            padding: 30px 40px 0;
        }

        .cartao-pokemon .nome{
            margin-bottom: 5px;
        }

        .cartao-pokemon .tipo{
            font-size: 12px;
            background-color: #fff;
            opacity: 0.7;
            border-radius: 10px;
            padding: 2px 10px;
            box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
        }

        .cartao-pokemon .detalhes{
            color: #fff;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .cartao-pokemon .cartao-imagem{
            width: 350px;
            height: 350px;
        }

        .cartao-pokemon img{
            max-height: 100%;
        }

        .cartao-pokemon .cartao-informacoes{
            display: flex;
            justify-content: space-between;
            background-color: #fff;
            padding: 80px 30px 50px;
            margin-top: -70px;
            border-bottom-left-radius: 8px;
            border-bottom-right-radius: 8px;
        }

        .cartao-pokemon .cartao-informacoes h3{
            font-size: 20px;
            margin-bottom: 15px;
            border-bottom: 1px solid #6B727A;
        }

        .cartao-pokemon .cartao-informacoes .status,
        .cartao-pokemon .cartao-informacoes .habilidades{
            padding: 0 10px;
            width: 180px;
        }

        .cartao-pokemon .cartao-informacoes .status ul li,
        .cartao-pokemon .cartao-informacoes .habilidades ul li{
            border-bottom: 1px solid #C3C4C5;
            padding: 0 0 5px;
            margin-bottom: 5px;
            font-size: 15px;
        }

        .cartao-pokemon.aberto{
            display: block;
        }

        .tipo-fogo{
            background-color: #ED8A8B;
        }

        .tipo-eletrico{
            background-color: #FCC719;
        }

        .tipo-agua{
            background-color: #76BEFE;
        }

        .tipo-grama{
            background-color: #49D0B0;
        }

        .tipo-trevas{
            background-color: #dd3863;
        }

        .tipo-dragao{
            background-color: #C29791;
        }
    </style>
""", unsafe_allow_html=True)

# Função para renderizar os Pokémon como cartões
def render_pokemon(nome, tipo, imagem_url, status, habilidades):
    st.markdown(f"""
        <div class="cartao-pokemon tipo-{tipo}">
            <div class="cartao-topo">
                <div class="detalhes">
                    <h2 class="nome">{nome}</h2>
                    <span>#{tipo[0]}</span>
                </div>
                <span class="tipo">{tipo[1]}</span>
                <div class="cartao-imagem">
                    <img src="{imagem_url}" alt="Imagem do {nome}">
                </div>
            </div>
            <div class="cartao-informacoes">
                <div class="status">
                    <h3>Status</h3>
                    <ul>
                        {"".join([f"<li>{s}</li>" for s in status])}
                    </ul>
                </div>
                <div class="habilidades">
                    <h3>Habilidades</h3>
                    <ul>
                        {"".join([f"<li>{h}</li>" for h in habilidades])}
                    </ul>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Dados dos Pokémon
pokemons = {
    'Pikachu': {
        "status": ['HP:300', 'Ataque:600', 'Defesa:500', 'Velocidade:300', 'Total:1.700'],
        'habilidades': ['Choque do Trovão', 'Cabeçada'],
        "tipo": ['#025', 'Elétrico', 'https://raw.githubusercontent.com/creativequeen/pokedex-streamlit/main/pokemons/pikachu.png', '#FCC719'],
    },

    'Bulbasaur': {
        "status": ['HP:320', 'Ataque:500', 'Defesa:520', 'Velocidade:400', 'Total:1.740'],
        'habilidades': ['Chicote de Vinha', 'Folha Navalha'],
        "tipo": ['#001', 'Planta/Veneno', 'https://raw.githubusercontent.com/creativequeen/pokedex-streamlit/main/pokemons/bulbasaur.png', '#49D0B0'],
    },

    'Charmander': {
        "status": ['HP:309', 'Ataque:520', 'Defesa:430', 'Velocidade:530', 'Total:1.789'],
        'habilidades': ['Lança-Chamas', 'Garra de Dragão'],
        "tipo": ['#004', 'Fogo', 'https://raw.githubusercontent.com/creativequeen/pokedex-streamlit/main/pokemons/Charmander.png', '#ED8A8B'],
    },

    'Cubone': {
        "status": ['HP:350', 'Ataque:540', 'Defesa:600', 'Velocidade:300', 'Total:1.790'],
        'habilidades': ['Arremesso de Osso', 'Terremoto'],
        "tipo": ['#104', 'Terrestre', 'https://raw.githubusercontent.com/creativequeen/pokedex-streamlit/main/pokemons/Cubone.png', '#C29791'],
    },

    'Psyduck': {
        "status": ['HP:400', 'Ataque:450', 'Defesa:420', 'Velocidade:400', 'Total:1.670'],
        'habilidades': ['Confusão', 'Jato d\'Água'],
        "tipo": ['#054', 'Água', 'https://raw.githubusercontent.com/creativequeen/pokedex-streamlit/main/pokemons/psyduck.png', '#76BEFE'],
    },

    'Squirtle': {
        "status": ['HP:310', 'Ataque:480', 'Defesa:560', 'Velocidade:350', 'Total:1.700'],
        'habilidades': ['Jato d\'Água', 'Casco Giratório'],
        "tipo": ['#007', 'Água', 'https://raw.githubusercontent.com/creativequeen/pokedex-streamlit/main/pokemons/Squirtle.png', '#76BEFE'],
    },

    'Togepi': {
        "status": ['HP:280', 'Ataque:300', 'Defesa:450', 'Velocidade:320', 'Total:1.350'],
        'habilidades': ['Metronomo', 'Charme'],
        "tipo": ['#175', 'Fada', 'https://raw.githubusercontent.com/creativequeen/pokedex-streamlit/main/pokemons/togepi.png', '#dd3863'],
    }
}

# Renderizando os cartões de Pokémon
for pokemon in pokemons.values():
    render_pokemon(pokemon['nome'], pokemon['tipo'], pokemon['tipo'][2], pokemon['status'], pokemon['habilidades'])
