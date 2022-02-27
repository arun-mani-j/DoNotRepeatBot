#!/usr/bin/env bash

# Update translations.

export DOMAIN="message"

# First update POT
xgettext -d "${DOMAIN}" -o "locales/temp.pot" "DoNotRepeatBot/constants/message.py"
cd "locales" || exit
msgmerge "${DOMAIN}.pot" "temp.pot" > "final.pot"
mv "final.pot" "${DOMAIN}.pot"
rm "temp.pot"
echo "Updated POT"

# Update English PO
msgen "${DOMAIN}.pot" -o "en/LC_MESSAGES/temp.po"
msgmerge "en/LC_MESSAGES/${DOMAIN}.po" "en/LC_MESSAGES/temp.po" > "en/LC_MESSAGES/final.po"
mv "en/LC_MESSAGES/final.po" "en/LC_MESSAGES/${DOMAIN}.po"
rm "en/LC_MESSAGES/temp.po"
echo "Updated English"

# Update other language PO
for lang in */;
do
    msgmerge "${lang}/LC_MESSAGES/${DOMAIN}.po" "${DOMAIN}.pot" > "${lang}/LC_MESSAGES/temp.po"
    mv "${lang}/LC_MESSAGES/temp.po" "${lang}/LC_MESSAGES/${DOMAIN}.po"
    echo "Updated ${lang}"
done
