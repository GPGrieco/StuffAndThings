# StuffAndThings

This repository contains a simplified Django project with a single `core` app
that bundles models for hazards, patrols, and inventory management. The code is
minimal but Dockerized for quick startup.

The project is Dockerized with PostgreSQL. Copy `.env.example` to `.env` and run:

```bash
docker-compose up --build
```

The Django admin is available at `http://localhost:8000/admin/`.

This code is a simplified starting point and does not implement all functionality
from the feature list.
