#!/usr/bin/env bash

command=$1

if [[ -z "$command" ]]; then
  command=serve
fi

if [[ -f .env ]]; then
  export "$(cmd .env | sed 's/#.*//g' | xargs)"
fi

export PYTHONPATH=$PWD

if [[ "$command" == test ]]; then
  export ENV=test
  pipenv run pytest --cov=app tests/
elif [[ "$command" == migrate ]]; then
  migrationName=$2

  if [[ -z "$migrationName" ]]; then
    echo "Add a name for the migration. Eg: start migrate new_migration"
  else
    pipenv run alembic revision --autogenerate -m "$migrationName"
  fi
elif [[ "$command" == upgrade ]]; then
  upgradeLevel=$2

  if [[ -z "$upgradeLevel" ]]; then
    upgradeLevel="head"
  fi

  pipenv run alembic upgrade "$upgradeLevel"

elif [[ "$command" == downgrade ]]; then
  downgradeLevel=$2

  if [[ -z "$downgradeLevel" ]]; then
    downgradeLevel="base"
  fi

  pipenv run alembic downgrade "$downgradeLevel"

elif [[ "$command" == install ]]; then
  env=$2

  if [[ -z "$env" ]]; then
    pipenv install --dev
  else
    pipenv install
  fi

elif [[ "$command" == run ]]; then
  PORT="${PORT:=8000}"
  pipenv run uvicorn app.main:app --port ${PORT} --root-path ./app --debug

elif [[ "$command" == current ]]; then
  pipenv run alembic current

elif [[ "$command" == serve ]]; then
  pipenv run uvicorn app.main:app --root-path ./app --reload
else

  echo "Unsupported command. Try start run or see README"
fi
