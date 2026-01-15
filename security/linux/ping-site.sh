#!/bin/bash

# Este script verifica a conectividade com um site específico usando ping.

SITE="profthomas.com.br"

echo "Verificando a conectividade com $SITE ..."
ping -c 4 $SITE

if [ $? -eq 0 ]; then
    echo "Conectividade com $SITE está OK."
else
    echo "Falha na conectividade com $SITE."
fi