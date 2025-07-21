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
                            <img src="./src/images/pikachu.png" alt="Imagem do Pikachu">
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
                                    <img src="./pokemons/bulbasaur.png" alt="Imagem do Bulbasaur">
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

                <div class="cartao-pokemon tipo-fogo" id="cartao-charmander">
                    <div class="cartao-topo">
                        <div class="detalhes">
                            <h2 class="nome">Charmander</h2>
                            <span>#004</span>
                        </div>
                        <span class="tipo">fogo</span>

                        <div class="cartao-imagem">
                            <img src="./pokemons/Charmander.png" alt="Imagem do Charmander">
                        </div>

                    </div>
                    <div class="cartao-informacoes">
                        <div class="status">
                            <h3>Status</h3>
                            <ul>
                                <li>HP: 200</li>
                                <li>Ataque: 300</li>
                                <li>Defesa: 400</li>
                                <li>Velocidade: 320</li>
                                <li>Total: 1.220</li>
                            </ul>
                        </div>

                        <div class="habilidades">
                            <h3>Habilidades</h3>
                            <ul>
                                <li>Lança-chamas</li>
                                <li>Ataque rápido</li>
                            </ul>

                        </div>
                    </div>
                </div>

              
                <!-- Squirtle -->
                <div class="cartao-pokemon tipo-agua" id="cartao-squirtle">
                    <div class="cartao-topo">
                        <div class="detalhes">
                            <h2 class="nome">Squirtle</h2>
                            <span>#007</span>
                        </div>
                        <span class="tipo">água</span>

                        <div class="cartao-imagem">
                            <img src="./pokemons/Squirtle.png" alt="Imagem do Squirtle">
                        </div>
                    </div>
                    <div class="cartao-informacoes">
                        <div class="status">
                            <h3>Status</h3>
                            <ul>
                                <li>HP: 250</li>
                                <li>Ataque: 300</li>
                                <li>Defesa: 400</li>
                                <li>Velocidade: 200</li>
                                <li>Total: 1.150</li>
                            </ul>
                        </div>

                        <div class="habilidades">
                            <h3>Habilidades</h3>
                            <ul>
                                <li>Jato d'água</li>
                                <li>Retrair-se</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Psyduck -->
                <div class="cartao-pokemon tipo-agua" id="cartao-psyduck">
                    <div class="cartao-topo">
                        <div class="detalhes">
                            <h2 class="nome">Psyduck</h2>
                            <span>#054</span>
                        </div>
                        <span class="tipo">psíquico</span>

                        <div class="cartao-imagem">
                            <img src="./pokemons/psyduck.png" alt="Imagem do Psyduck">
                        </div>
                    </div>
                    <div class="cartao-informacoes">
                        <div class="status">
                            <h3>Status</h3>
                            <ul>
                                <li>HP: 270</li>
                                <li>Ataque: 290</li>
                                <li>Defesa: 330</li>
                                <li>Velocidade: 250</li>
                                <li>Total: 1.140</li>
                            </ul>
                        </div>

                        <div class="habilidades">
                            <h3>Habilidades</h3>
                            <ul>
                                <li>Confusão</li>
                                <li>Tiro de água</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Cubone -->
                <div class="cartao-pokemon tipo-terra" id="cartao-cubone">
                    <div class="cartao-topo">
                        <div class="detalhes">
                            <h2 class="nome">Cubone</h2>
                            <span>#104</span>
                        </div>
                        <span class="tipo">terra</span>

                        <div class="cartao-imagem">
                            <img src="./pokemons/Cubone.png" alt="Imagem do Cubone">
                        </div>
                    </div>
                    <div class="cartao-informacoes">
                        <div class="status">
                            <h3>Status</h3>
                            <ul>
                                <li>HP: 260</li>
                                <li>Ataque: 280</li>
                                <li>Defesa: 350</li>
                                <li>Velocidade: 180</li>
                                <li>Total: 1.070</li>
                            </ul>
                        </div>

                        <div class="habilidades">
                            <h3>Habilidades</h3>
                            <ul>
                                <li>Ataque de osso</li>
                                <li>Raiva</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Togepi -->
                <div class="cartao-pokemon tipo-fada" id="cartao-togepi">
                    <div class="cartao-topo">
                        <div class="detalhes">
                            <h2 class="nome">Togepi</h2>
                            <span>#175</span>
                        </div>
                        <span class="tipo">fada</span>

                        <div class="cartao-imagem">
                            <img src="./pokemons/togepi.png" alt="Imagem do Togepi">
                        </div>
                    </div>
                    <div class="cartao-informacoes">
                        <div class="status">
                            <h3>Status</h3>
                            <ul>
                                <li>HP: 200</li>
                                <li>Ataque: 150</li>
                                <li>Defesa: 300</li>
                                <li>Velocidade: 100</li>
                                <li>Total: 750</li>
                            </ul>
                        </div>

                        <div class="habilidades">
                            <h3>Habilidades</h3>
                            <ul>
                                <li>Encantar</li>
                                <li>Metronomo</li>
                            </ul>
                        </div>
                    </div>
                </div>

            </div>

            <nav class="listagem">
                <ul>
                    <!-- Adicione os botões de cabeça correspondentes abaixo -->
                    <li class="pokemon ativo" id="pikachu">
                        <img src="./pokemons/cabecapikachu.png" alt="Cabeça do Pikachu">
                        <span>Pikachu</span>
                    </li>
                    <li class="pokemon" id="bulbasaur">
                        <img src="./pokemons/bulbasaurcabeca.png" alt="Cabeça do Bulbasaur">
                        <span>Bulbasaur</span>
                    </li>
                    <li class="pokemon" id="charmander">
                        <img src="./pokemons/Charmandercabeca.png" alt="Cabeça do Charmander">
                        <span>Charmander</span>
                    </li>
                    <li class="pokemon" id="squirtle">
                        <img src="./pokemons/Squirtlecabeca.png" alt="Cabeça do Squirtle">
                        <span>Squirtle</span>
                    </li>
                    <li class="pokemon" id="psyduck">
                        <img src="./pokemons/psyduckcabeca.png" alt="Cabeça do Psyduck">
                        <span>Psyduck</span>
                    </li>
                    <li class="pokemon" id="cubone">
                        <img src="./pokemons/Cubonecabeca.png" alt="Cabeça do Cubone">
                        <span>Cubone</span>
                    </li>
                    <li class="pokemon" id="togepi">
                        <img src="./pokemons/togepicabeca.png" alt="Cabeça do Togepi">
                        <span>Togepi</span>
                    </li>
                </ul>
            </nav>
        </div>
    </main>
""", unsafe_allow_html=True)