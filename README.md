# StuffAndThings

This repository contains a simplified Django project with a single `core` app
that bundles models for hazards, patrols, and inventory management. The code is
minimal but Dockerized for quick startup.

The project is Dockerized with PostgreSQL. Copy `.env.example` to `.env` so the
web container receives the database settings, then run:

```bash
docker-compose up --build
```

The Django admin is available at `http://localhost:8000/admin/`.

If the environment variables are not provided, the app will use SQLite instead
of PostgreSQL, which is handy for local testing without Docker.

This code is a simplified starting point and does not implement all functionality from the feature list.
