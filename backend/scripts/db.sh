#!/bin/bash
# Usage: ./scripts/db.sh migrate "Description"
# Usage: ./scripts/db.sh upgrade
# Usage: ./scripts/db.sh downgrade

case "$1" in
  migrate)
    docker-compose exec backend alembic revision --autogenerate -m "$2"
    ;;
  upgrade)
    docker-compose exec backend alembic upgrade head
    ;;
  downgrade)
    docker-compose exec backend alembic downgrade -1
    ;;
  *)
    echo "Usage: $0 {migrate|upgrade|downgrade}"
    exit 1
    ;;
esac
