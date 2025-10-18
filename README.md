# Postit

#### A simple blog website with server-rendered pages and a REST API for posts. Built with Django + Django REST Framework. The backend provides JWT authentication and CRUD operations for posts so the API can be used by other frontends.

## Key points

  #### Uses environs to load environment variables from a .env file (or system environment).
  #### Default Django secret seen in history is the standard djangoinsecure key — ok for local/dev, rotate if used in any production system.
  #### API supports JWT authentication and full CRUD for posts.
