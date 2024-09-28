# FilmLibraryAPI

> Este projeto é uma API de um sistema que gerencia informações de filmes utilizando Django Rest Framework (DRF).

**Tecnologias Ultilizadas**: 
- ![djangorest-logo](https://img.shields.io/badge/djangorestframework-3.15.2-228B22?style=for-the-badge&logo=django&logoColor=white&labelColor=228B22)
- ![python-logo](https://img.shields.io/badge/python-3.12.4-blue?style=for-the-badge&logo=python&logoColor=white&labelColor=yellow)

## 🎯 Objetivo

O desafio consiste em desenvolver uma API de um sistema para gerenciamento de informações de filmes. O projeto tem como foco a criação de um sistema robusto e seguro, onde usuários poderão se autenticar e realizar operações sobre os dados dos filmes.

## 🚀 Principais funcionalidades da API

- Autenticação de usuários utilizando Django Rest Framework.

- CRUD (Create, Read, Update, Delete) para gerenciar informações de filmes.

- Utilização do authtoken para geração de tokens de acesso.

##  🔗 Endpoints

1. **Autenticação de Usuários**:

    - POST **/cadastro/**: Registro de novos usuários.
    
    nesse endpoint voce poderá criar um novo usuario enviando como body o seguinte `JSON`:
    
    ```JSON
    {
      "username": "usuario",
      "password": "senha"
    }
    ```
    
    com o usuario criado com sucesso, voce terá que solicitar o token para poder acessar os endpoints de filmes. para gerar o token basta acessar o seguinte endpoint:
    
    - POST **/generate-token/**: Geração do token.
    
    sendo enviado no body da requisição o `JSON` no seguinte formato:
    
    ```JSON
    {
      "username": "usuario",
      "password": "senha"
    }
    ```
    
---
2. **Filmes** (CRUD):

    Lembrando que para acessar todos os endpoints de Filmes da API voce deverá informar o token obtido anteriormente no cabeçalho HTTP de **authorization** de sua requisição. Veja essa exemplo em python:

    ```py
    import requests

    headers = {
      "Authorization": "Token abc123xyz"
    }
    
    response = requests.get('http://127.0.0.1:8000/api/endpoint_protegido/', headers=headers)
    ```

    - GET **/filmes/**: Listar todos os filmes.
    - GET **/filmes/{id}/**: Detalhar um filme específico.
    - POST **/filmes/**: Criar um novo filme.
    - PUT **/filmes/{id}/**: Atualizar as informações de um filme existente.
    - DELETE **/filmes/{id}/**: Deletar um filme.
    
---
3. **Categorias** (CRUD):

    - GET **/categorias/**: Listar todas as categorias.
    - GET **/categorias/{id}/**: Detalhar uma categoria específica.
    - POST **/categorias/**: Criar uma nova categoria.
    - PUT **/categorias/{id}/**: Atualizar as informações de uma categoria existente.
    - DELETE **/categoria/{id}/**: Deletar uma categoria.