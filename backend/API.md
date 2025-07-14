# API Documentation

## Introduction

This document provides details about the backend API for todo-app-backend. The API allows users to manage PostgreSQL databases and their associated users.

## Endpoints

### Authentication


### CRUD Operations

- **GET /{username}**
    - Return all todo-list items ordered by due dates

- **GET /{username}/create**
    - Return a the create todo-list item page

- **POST /{username}/create**
    - Submit the written todo-list item
    - return to "/{username}"

