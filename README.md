# Graph Lib - Computação Gráfica

Biblioteca de rotinas matemáticas e estruturas geométricas elementares construída para a disciplina de Computação Gráfica. O projeto fornece ferramentas para a manipulação de pontos, segmentos de reta e matrizes quadradas no espaço 2D e 3D.

## Estrutura do Projeto

- `point.py`: Representação de pontos (2D e 3D).
- `segment.py`: Definição e análise de segmentos de reta (2D e 3D).
- `matrix.py`: Operações com matrizes quadradas.
- `test.py`: Exemplos práticos e testes de uso.

## Módulos

### 1. Pontos (`Point2d` e `Point3d`)

Classes para representar coordenadas no espaço.

- **`length()`**: Retorna a distância do ponto até à origem (0,0 ou 0,0,0).
- **`distance_to(outro_ponto)`**: Retorna a distância exata entre o ponto atual e um segundo ponto fornecido.

**Exemplo de uso:**

```
from graph_lib_ei01.point import Point2d

p1 = Point2d(0, 0)
p2 = Point2d(3, 4)

print(p2.length())          # Retorna o módulo do vetor
print(p1.distance_to(p2))   # Retorna a distância entre p1 e p2

```

### 2. Segmentos (`Segment2d` e `Segment3d`)

Classes que representam uma linha finita a ligar dois pontos. A versão 2D possui funções avançadas de análise espacial.

- **`length()`**: Retorna o tamanho total do segmento.
- **`midpoint()`**: Retorna um novo Ponto localizado exatamente no meio do segmento.
- **`orientation(ponto)`** _(Apenas 2D)_: Informa a orientação de um ponto em relação à reta do segmento (útil para saber de que lado da linha o ponto se encontra).
- **`is_parallel_to(outro_segmento)`** _(Apenas 2D)_: Retorna `True` se os dois segmentos forem paralelos.
- **`intersection_with(outro_segmento)`** _(Apenas 2D)_: Retorna o Ponto exato onde as retas dos dois segmentos se cruzam (retorna `None` se não houver cruzamento).
- **`contains_point(ponto)`** _(Apenas 2D)_: Verifica se um determinado ponto está contido dentro dos limites físicos do segmento.
- **`classify_intersection(outro_segmento)`** _(Apenas 2D)_: Avalia e retorna um texto a descrever o estado da colisão entre dois segmentos (ex: "Parallel", "Collinear", "Intersecting at..." ou "Not intersecting").

**Exemplo de uso:**

```
from graph_lib_ei01.point import Point2d
from graph_lib_ei01.segment import Segment2d

s1 = Segment2d(Point2d(0, 0), Point2d(3, 4))
s2 = Segment2d(Point2d(6, -2), Point2d(1, 4))

print(s1.length())                      # Retorna o tamanho da linha
print(s1.is_parallel_to(s2))            # Verifica paralelismo
print(s1.classify_intersection(s2))     # Informa como/se as linhas se tocam

```

### 3. Matrizes (`SquareMatrix`)

Classe para manipulação de matrizes quadradas ($N \times N$).

- **Soma (`+`)**: Permite somar duas matrizes instanciadas usando o operador padrão de adição.
- **Multiplicação (`*`)**: Permite multiplicar duas matrizes usando o operador padrão de multiplicação. Ambas as operações exigem que as matrizes tenham o mesmo tamanho.

**Exemplo de uso:**

```
from graph_lib_ei01.matrix import SquareMatrix

m1 = SquareMatrix(2, data=[[1, 2], [3, 4]])
m2 = SquareMatrix(2, data=[[5, 6], [7, 8]])

resultado_soma = m1 + m2
resultado_mult = m1 * m2

print(resultado_mult) # Imprime a matriz resultante da multiplicação

```

## Como testar o projeto

Pode visualizar todas estas funcionalidades a correr o script base de testes incluído no projeto:

```
python test.py
```
