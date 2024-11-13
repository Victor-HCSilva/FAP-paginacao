curl -X POST -H "Content-Type: application/json" -d '{
  "date": "2024-11-14",
  "time": "10:00",
  "patient": 1,
  "doctor": 4,
  "description": "Consulta de rotina"
}' http://127.0.0.1:8000/api/consultations/

curl http://127.0.0.1:8888/api/consultations/?page=3  
[{"id":1,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":1},{"id":2,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":2,"doctor":3},{"id":3,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":4,"doctor":5},{"id":4,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":5,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":6,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":7,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":8,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":9,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":10,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":11,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":12,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":13,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":14,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":15,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":16,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":17,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":18,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":19,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":20,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":21,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":22,"date":"2024-11-14","time":"10:00:00","description":"Consulta de rotina","patient":1,"doctor":4},{"id":23,"date":"2024-11-13","time":"12:12:00","description":"teste_post","patient":1,"doctor":4}]

## DRF: Paginação e Filtros para APIs Eficazes

**Slide 1: Introdução ao DRF**

* **Título:**  DRF: Paginação e Filtros para APIs Eficazes
* **Introdução:**  O Django REST Framework (DRF) é uma ferramenta poderosa para construir APIs RESTful em Python.  Hoje, vamos explorar duas funcionalidades essenciais do DRF: paginação e filtros, que facilitam a construção de APIs eficientes e escaláveis.

**Slide 2: O Problema da Paginação**

* **Exemplo:** Imagine uma API que retorna todos os pacientes de um hospital. Se houver milhares de pacientes, retornar todos de uma vez seria ineficiente e lento. 
* **Desafios:** 
    * **Performance:** APIs lentas e com grande consumo de recursos.
    * **Experiência do Usuário:**  Respostas lentas e complexas.
* **Solução:** A paginação divide os dados em partes menores (páginas), tornando a resposta mais leve e rápida.

**Slide 3: Paginação no DRF**

* **Demonstração:** Usando o código `ConsultationListView` como exemplo, vamos mostrar como a classe `PageNumberPagination` do DRF divide os dados em páginas.
* **Explicação:**
    * `pagination_class = PageNumberPagination`: Define o tipo de paginação.
    * `page_size = 2`: Define o número de consultas por página.
    * A API retorna apenas as consultas da página atual (ex: `/api/consultations?page=2`).

**Slide 4:  Filtros no DRF**

* **Exemplo:** Imagine que você precisa filtrar as consultas por paciente ou médico.
* **Solução:** Os filtros do DRF permitem que você personalize as consultas à API.
* **Demonstração:** 
    * `filter_backends = [SearchFilter, OrderingFilter]`: Define os filtros disponíveis.
    * `search_fields = ['patient__name', 'doctor__name', 'description']`: Permite buscar por nome do paciente, médico ou descrição da consulta.
    * `ordering_fields = ['date', 'time']`: Permite ordenar as consultas por data e hora.

**Slide 5:  Combinando Paginação e Filtros**

* **Demonstração:**  Usando o código `ConsultationListView`, vamos mostrar como usar a paginação e os filtros juntos.
* **Exemplo:** `/api/consultations?page=2&search=João&ordering=-date`:  A API retorna as consultas da página 2, filtradas por pacientes com o nome "João" e ordenadas por data decrescente.

**Slide 6: Benefícios da Paginação e Filtros**

* **Performance:**  APIs mais rápidas e eficientes, otimizadas para grande quantidade de dados.
* **Escalabilidade:** APIs que podem lidar com um número crescente de dados e usuários.
* **Experiência do Usuário:** Respostas rápidas e personalizadas, proporcionando melhor usabilidade.

**Slide 7: Próximos Passos**

* **Exploração:** Incentivar os alunos a explorar outros tipos de filtros no DRF, como `DjangoFilterBackend`.
* **Personalização:**  Mostrar como personalizar os filtros e a paginação para necessidades específicas.
* **Documentação:**  Enfatizar a importância de documentar a API com detalhes sobre paginação e filtros.

**Fluxograma do Código:**

```
+-------------------------------------------------------+
|                                                       |
|  ConsultationListView                                 |
|                                                       |
+-------------------------------------------------------+
|                                                       |
|  queryset = Consultation.objects.all()                |
|  serializer_class = ConsultationSerializer           |
|                                                       |
+-------------------------------------------------------+
|                                                       |
|  pagination_class = PageNumberPagination            |
|  pagination_class.page_size = 2                     |
|                                                       |
+-------------------------------------------------------+
|                                                       |
|  filter_backends = [SearchFilter, OrderingFilter]    |
|                                                       |
+-------------------------------------------------------+
|                                                       |
|  search_fields = ['patient__name', 'doctor__name',   |
|                    'description']                      |
|                                                       |
+-------------------------------------------------------+
|                                                       |
|  ordering_fields = ['date', 'time']                   |
|                                                       |
+-------------------------------------------------------+
```

**Observação:** Este é um exemplo básico e pode ser adaptado de acordo com a complexidade da API e as necessidades do seu projeto. 

Espero que esta estrutura ajude você a construir uma apresentação interessante e informativa sobre a paginação e os filtros no DRF!


- mermaid
```mermaid
flowchart LR
 subgraph Usuário["Usuário"]
        A["Envia requisição"]
  end
 subgraph API["API"]
        C["Processa filtros"]
        B["Recebe requisição"]
        D["Processa paginação"]
        E["Consulta Banco de Dados"]
        F["Serializa dados"]
        G["Retorna resposta"]
  end
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    A --> B
    G --> A
```
![alt text](<Captura de tela_2024-11-12_21-04-44.png>)

- urls.py - appoinments(app)

![alt text](image-10.png)

- serializers.py

![alt text](image-7.png)

![alt text](image-12.png)

- Recebendo n dados da api:

![alt text](image-11.png)


- Recebendo apenas dois resultados por vez, configurando o settings.py:

![alt text](image-9.png)

![alt text](image.png)






- usando o filtro de data, criado no serializers.py


http://127.0.0.1:8000/api/consultations/?ordering=date


![alt text](image-1.png)

- usando 'rest_framework.pagination.PageNumberPagination':
![alt text](image-2.png)


![alt text](image-4.png)

- Uso do 'rest_framework.pagination.CursorPagination': 

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.CursorPagination',
    #'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,  # Exibe 2 itens por página
}
```
![alt text](image-3.png)


