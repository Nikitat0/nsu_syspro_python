PYTHONPATH=$(find ./build/ -maxdepth 1 -mindepth 1 -type d | tr "\n" ":" | sed "s/:$//") python3 main.py
