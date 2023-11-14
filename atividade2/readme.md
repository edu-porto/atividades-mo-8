
Para realizar o pré-mapeamento do ambiente foram utilizados duas ferramentas. A primeira é o gazebo que simula um ambiente junto ao robô. ALém disso, o Rvis que permite ter acesso aos dados dos sensores do robô.

Para ter acessp ao mapa gerado, entre na pasta assets .
O objetivo desta atividade é realizar o mapeamento e navegação com o turtlebot 3 

### Configurando o ambiente  

Para utilizar o projeto é preciso realizar os seguintes passos. 
Após já ter clonado o repositório e estando com o terminal aberto na pasta raíz 

1 Buildar o projeto 


```
colcon build
```
2 Instalar o setup 

```
# Caso você esteja usando bash  troque a extensão do arquivo para .bash

source install/setup.zsh 
```

Com esses passos completos já está configurado  o projeto .

### Mapeando um ambiente 

Nesta etapa foi construido um launch file para realizar o mapeamento. 
Para executar o mesmo processo que é demonstrado no vídeo abaixo realize os seguintes passos. 

1 Acessar a pasta do mapeamento 


```
cd atividade2/workspace/src/my_package/launch

```

2 Rodar o launch file 

```
ros2 launch test_launch.py

```

Pronto, agora o mapeamento pode ser feito localmente. 
Abaixo segue o vídeo mostrando como foi realizado o processo 


https://youtu.be/Di1VJd6txpU 


### Navegando por um ambiente 

WIP 

