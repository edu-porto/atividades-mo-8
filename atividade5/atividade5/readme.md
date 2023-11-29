## Atividade Ponderada 5

O objetivo desta atividade é integrar o chatbot desenvolvido na ponderada 4 com a opção de contexto a partir do seguinte [contexto](https://www.deakin.edu.au/students/study-support/faculties/sebe/abe/workshop/rules-safety).

Ou seja, se for realizada uma pergunta como " What i have to do to use some paint ?  " a IA precisa utilizar o documento que contém o contexto para responder. O mesmo está localizado na pasta <code>data/rules.txt</code> A resposta esperada é algo nas linhas de <q>All chemicals (e.g. glues and paints) must be checked through Chemwatch and with workshop staff before use.</q> visto que essa frase está no contexto 

### Como configurar a solução 

Após já ter clonado o repositório e estando com o terminal aberto na pasta raíz 

1 Buildar o model file 

```
ollama create eike -f Modelfile
```

Uma etapa muito importante é utilizar a máquina virtual. Assim, execute o seguinte comando no terminal : 

```
source bin/activate
```

Instale os requisitos 

```
pip3 install -r requirements.txt
```

Pronto, o projeto já está configurado.

### Como utilizar a solução 

Após realizar a configuração já é possível utilizar a solução com o seguinte comando. 

```
# Não se esqueça de estar na raíz do projeto
python3 core.py
```

Pronto, agora você já pode interagir com o chatbot. 

### Funcionamento da solução 

Para ver a solução em funcionamento acesse o link abaixo.


**https://www.youtube.com/watch?v=QGYnLwndgFU**

Devido ao modelo ser bem pesado a resposta ao input só acontece por volta de 7 minutos no vídeo. 

