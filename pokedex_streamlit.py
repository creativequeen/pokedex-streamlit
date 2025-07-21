import streamlit as st

# Adicionando o CSS personalizado
st.markdown("""
    <style>
        .cartao-pokemon {
            display: none;
            box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
            border-radius: 10px;
        }

        .cartao-pokemon .cartao-topo {
            padding: 30px 40px 0;
        }

        .cartao-pokemon .nome {
            margin-bottom: 5px;
        }

        .cartao-pokemon .tipo {
            font-size: 12px;
            background-color: #fff;
            opacity: 0.7;
            border-radius: 10px;
            padding: 2px 10px;
            box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
        }

        .cartao-pokemon .detalhes {
            color: #fff;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .cartao-pokemon .cartao-imagem {
            width: 350px;
            height: 350px;
        }

        .cartao-pokemon img {
            max-height: 100%;
        }

        .cartao-pokemon .cartao-informacoes {
            display: flex;
            justify-content: space-between;
            background-color: #fff;
            padding: 80px 30px 50px;
            margin-top: -70px;
            border-bottom-left-radius: 8px;
            border-bottom-right-radius: 8px;
        }

        .cartao-pokemon .cartao-informacoes h3 {
            font-size: 20px;
            margin-bottom: 15px;
            border-bottom: 1px solid #6B727A;
        }

        .cartao-pokemon .cartao-informacoes .status,
        .cartao-pokemon .cartao-informacoes .habilidades {
            padding: 0 10px;
            width: 180px;
        }

        .cartao-pokemon .cartao-informacoes .status ul li,
        .cartao-pokemon .cartao-informacoes .habilidades ul li {
            border-bottom: 1px solid #C3C4C5;
            padding: 0 0 5px;
            margin-bottom: 5px;
            font-size: 15px;
        }

        .cartao-pokemon.aberto {
            display: block;
        }

        .tipo-fogo {
            background-color: #ED8A8B;
        }

        .tipo-eletrico {
            background-color: #FCC719;
        }

        .tipo-agua {
            background-color: #76BEFE;
        }

        .tipo-grama {
            background-color: #49D0B0;
        }

        .tipo-trevas {
            background-color: #dd3863;
        }

        .tipo-dragao {
            background-color: #C29791;
        }
    </style>
""", unsafe_allow_html=True)

# Exibindo os Pokémon como cartões
st.markdown("""
    <main>
        <div class="pokedex">
            <div class="cartoes-pokemon">
                <div class="cartao-pokemon aberto tipo-eletrico" id="cartao-pikachu">
                    <div class="cartao-topo">
                        <div class="detalhes">
                            <h2 class="nome">Pikachu</h2>
                            <span>#025</span>
                        </div>
                        <span class="tipo">elétrico</span>
                        <div class="cartao-imagem">
                            <img src="https://raw.githubusercontent.com/creativequeen/pokedex-streamlit/main/pokemons/pikachu.png" alt="Imagem do Pikachu">
                        </div>
                    </div>
                    <div class="cartao-informacoes">
                        <div class="status">
                            <h3>Status</h3>
                            <ul>
                                <li>HP: 300</li>
                                <li>Ataque: 600</li>
                                <li>Defesa: 500</li>
                                <li>Velocidade: 300</li>
                                <li>Total: 1.700</li>
                            </ul>
                        </div>
                        <div class="habilidades">
                            <h3>Habilidades</h3>
                            <ul>
                                <li>Choque do trovão</li>
                                <li>Cabeçada</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="cartao-pokemon tipo-grama" id="cartao-bulbasaur">
                    <div class="cartao-topo">
                        <div class="detalhes">
                            <h2 class="nome">Bulbasaur</h2>
                            <span>#001</span>
                        </div>
                        <span class="tipo">grama</span>
                        <div class="cartao-imagem">
                            <img src="https://raw.githubusercontent.com/creativequeen/pokedex-streamlit/main/pokemons/bulbasaur.png" alt="Imagem do Bulbasaur">
                        </div>
                    </div>
                    <div class="cartao-informacoes">
                        <div class="status">
                            <h3>Status</h3>
                            <ul>
                                <li>HP: 320</li>
                                <li>Ataque: 510</li>
                                <li>Defesa: 400</li>
                                <li>Velocidade: 200</li>
                                <li>Total: 1.430</li>
                            </ul>
                        </div>
                        <div class="habilidades">
                            <h3>Habilidades</h3>
                            <ul>
                                <li>Folhas navalha</li>
                                <li>Raio solar</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Adicionar mais Pokémon aqui -->
            </div>
        </div>
    </main>
""", unsafe_allow_html=True)
