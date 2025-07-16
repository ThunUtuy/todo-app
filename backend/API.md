# API Documentation

## Introduction

This document provides details about the backend API for todo-app-backend. The API allows users to manage PostgreSQL databases and their associated users.

## Endpoints

### Authentication
- **GET /login**
    - Redirect to login page

- **POST /login**
    - Try to login with the written username and password

- **GET /signup**
    - Redirect to signup page

- **POST /signup**
    - Attempt to signup with the written username and password

- **GET /logout**
    - Logout

### CRUD Operations

- **GET /index**
    - Return all tasks ordered by due dates

- **GET /create**
    - Return a the create task page

- **POST /create**
    - Submit the written task
    - return to "/{username}"

