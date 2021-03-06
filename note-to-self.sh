#!/usr/bin/env bash

# You should configure the following to run this script:
# export NOTE_TO_SELF_FROM=" your from email"
# export NOTE_TO_SELF_TO=" your to email "
# export NOTE_TO_SELF_LOG=" file to log notes sent (set to /dev/null to skip logging)"
#
# I define all of these in ~/.ses_conf_private and source that from my .bash_profile

RAW=$(cat) # read from STDIN
touch $NOTE_TO_SELF_LOG
echo -e "$RAW" >> $NOTE_TO_SELF_LOG
BODY="$RAW"
SUBJECT=$(echo "$RAW" | tr '\n' ' ' | tr '\r' ' ' | head -c 80) # truncate to 80 chars
cd "$( dirname "${BASH_SOURCE[0]}" )" # change to cwd
python ses.py send_email \
    --sender="$NOTE_TO_SELF_FROM"  \
    --to="$NOTE_TO_SELF_TO" \
    --subject="$SUBJECT" \
    --body="$BODY"
echo -e "To: $NOTE_TO_SELF_TO\n$BODY"
