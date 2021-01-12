#!/usr/bin/env bash

command=$1

if [[ ! -f .env ]]; then
  cp .env.example .env
fi

export $(cat .env | sed 's/#.*//g' | xargs)

if [[ -z "$command" ]]; then
  command=run
fi

export PYTHONPATH=$PWD

if [[ "$command" == test ]]; then
  export env=test
  pipenv run pytest --cov=app tests/

elif [[ "$command" == install ]]; then
  env="${ENV:=dev}"

  if [[ "$env" == dev ]]; then
    pipenv install --dev
  else
    pipenv install
  fi

elif [[ "$command" == run ]]; then
  debug=""
  env="${ENV:=dev}"
  port="${PORT:=8000}"
  reload=""

  if [[ "$env" == dev ]]; then
    debug="--debug"
    reload="--reload"
  fi

  pipenv run uvicorn app.main:app --port ${port} --root-path ./app ${debug} ${reload}

else
  echo "Unsupported command. Try start run or see README"
fi
