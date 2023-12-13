## Atividade Ponderada 8

O objetivo desta atividade é receber um arquivo de áudio, converter o mesmo para texto, traduzir este texto para algum idioma e mostrar como seria a voz desse texto. Assim, o aluno é capaz de entender melhor como funcionam as tecnologias de Speech to Text e Text to Speech. 

Ou seja, você só precisa enviar um arquivo de áudio e recebe uma tradução automática para italiano.

### Como configurar a solução 

Primeiramente, é preciso ressaltar a possibilidade de utilizar modelos locais, porém o nível da API do Whisper é bem mais superior e trás resultados muito bons. Assim, a configuração dessa solução é simples 

Após já ter clonado o repositório só basta colocar sua chave da api no arquivo **.env**

1 Criar um arquivo .env e inserir a chave 

```
KEY=sk-<restante da sua chave da api open ai>
```

Uma etapa muito importante é utilizar a máquina virtual. Assim, execute o seguinte comando no terminal : 

```
cd Scripts
```
```
activate
```

Instale os requisitos 

```
pip install -r requirements.txt
```

Pronto, o projeto já está configurado.

### Como utilizar a solução 

Após realizar a configuração já é possível utilizar a solução com o seguinte comando. 

```
# Não se esqueça de estar na raíz do projeto
python main.py
```

Pronto, agora você pode interagir com o modelo seja com um arquivo de áudio já disponibilizado no repositório ou enviar algum outro e testar. 

### Funcionamento da solução 

Para ver a solução em funcionamento acesse o link abaixo.


**https://youtu.be/-dTwzdNHixQ**


