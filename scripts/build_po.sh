#!/usr/bin/env bash

# Compile translations

export DOMAIN="message"

for lang in locales/*/;
do
    file="${lang}/LC_MESSAGES/${DOMAIN}"
    msgfmt -o "${file}.mo" "${file}.po"
    echo "Translated ${file}"
done
