# ses-emailer-cli

Simple command line script for sending emails from the command line.

## Dependencies

    pip install boto

## Configure Environment Variable for Amazon
    
    export AMAZON_ACCESS_KEY_ID='your key id'
    export AMAZON_SECRET_KEY='your secret key'

## For `note-to-self.sh` / Alfred, Configure

    export NOTE_TO_SELF_FROM=" your from email"
    export NOTE_TO_SELF_TO=" your to email "
    export NOTE_TO_SELF_LOG=" file to log notes sent (set to /dev/null to skip logging)"

I put all of the above in `~/.ses_conf_private` and source from my `~/.bash_profile`


## Usage

### Basic
    
    python ses.py send_email --sender="davinci@lab.co"  --to="goethe@lab.net" --subject="hi there" --body="how are you?"


### `note-to-self.sh`

    echo "hello" | ./note-to-self.sh

