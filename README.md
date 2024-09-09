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

- Integração com OAuth2 para geração e gerenciamento de tokens de acesso.

##  🔗 Endpoints

1. **Autenticação de Usuários**:

    - POST **/api/register/**: Registro de novos usuários.
    - POST **/api/login/**: Autenticação de usuários e geração de token de acesso.
    - POST **/api/logout/**: Logout e invalidação do token de acesso.

---
2. **Filmes** (CRUD):

    - GET **/api/movies/**: Listar todos os filmes.
    - GET **/api/movies/{id}/**: Detalhar um filme específico.
    - POST **/api/movies/**: Criar um novo filme.
    - PUT **/api/movies/{id}/**: Atualizar as informações de um filme existente.
    - DELETE **/api/movies/{id}/**: Deletar um filme.

---
3. **Tokens de Autorização OAuth2**:

    - POST **/api/token/**: Geração de token OAuth2.
    - POST **/api/token/refresh/**: Atualizar um token expirado.
    - POST **/api/token/revoke/**: Revogar um token de acesso.


