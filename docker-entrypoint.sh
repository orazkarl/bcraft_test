#!/bin/sh

container_type=${CONTAINER_TYPE-FAST_API};
if [ "$container_type" = "FAST_API" ]; then
  alembic upgrade head
  uvicorn bcraft.main:app --host 0.0.0.0 --port "$PORT" --forwarded-allow-ips '*'
fi;
