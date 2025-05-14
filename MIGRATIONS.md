# Database Migrations

FFLIQ uses Alembic for database migrations. Here's how to work with migrations:

## Creating Migrations

When you make changes to the SQLAlchemy models, create a new migration:

```bash
docker-compose exec backend alembic revision --autogenerate -m "Description of your changes"
```
This will create a new migration file in `backend/alembic/versions/`.

## Applying Migrations
To apply all pending migrations:
```bash
docker-compose exec backend alembic upgrade head
```

## Reverting Migrations
To revert the most recent migration:
```bash
docker-compose exec backend alembic downgrade -1
```
To revert to a specific migration:
```bash
docker-compose exec backend alembic downgrade <migration_id>
```

## Migration Best Practices
- Always review auto-generated migrations before applying them
- Keep migrations small and focused on specific changes
- Test migrations in development before deploying to production
- Include both "upgrade" and "downgrade" logic for all migrations
