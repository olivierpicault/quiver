function dev {
    poetry run flask --app app run --debug
}

function linter {
    poetry run ruff check --fix
    poetry run ruff format 
    poetry run ruff format 
    poetry run ty check src/
    poetry run ty check tests/
}

if [[ "$1" == "" ]]; then
   echo "No args provided"
   usage
   exit 1
fi

case "$1" in
        dev)
            dev
            ;;
        linter)
            linter
            ;;
esac
