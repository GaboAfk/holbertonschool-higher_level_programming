#!/bin/bash

_autocomplete_files() {
    local cur=${COMP_WORDS[COMP_CWORD]}
    COMPREPLY=( $(compgen -A file -- "$cur") )
}

complete -F _autocomplete_files -o filenames read

echo 'file.py name?'
read -e -i "" files_to_add

#files_to_add=$(echo "$files_to_add" | sed 's/\.py$//')

# Function to check and print docstrings
check_docstrings() {
    local module="$1"
    python3 -c "

try:
    print(__import__("$files_to_add").__doc__)
except AttributeError:
    print('modules should have a documentation')

try:
    print(__import__("$files_to_add").MyClass.__doc__)
except AttributeError:
    print('classes should have a documentation')

try:
    print(__import__("$files_to_add").my_function.__doc__)
except AttributeError:
    print('functions (inside and outside a class) should have a documentation')

try:
    print(__import__("$files_to_add").MyClass.my_function.__doc__)
except AttributeError:
    print('functions (inside and outside a class) should have a documentation')
"
}

# Call the function with the user input
check_docstrings "$files_to_add"
