import argparse
import os
import boto3


def get_client():
    access_key_id = os.environ.get("AMAZON_ACCESS_KEY_ID")
    secret_key = os.environ.get("AMAZON_SECRET_KEY")
    return boto3.client(
        "ses",
        region_name="us-east-1",
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_key,
    )


def verify_email_address(email):
    print("Verifying {0}".format(args.email))
    client = get_client()
    print(client.verify_email_address(email))


def list_verified_email_addresses():
    client = get_client()
    print(client.list_verified_email_addresses())


def send_email(sender, subject, body, recipients):
    client = get_client()
    # print locals()
    subject = subject.replace("\n", " ")
    subject = subject.replace("\r", " ")
    client.send_email(
        Source=sender,
        Destination={"ToAddresses": recipients},
        Message={
            "Subject": {"Data": subject, "Charset": "UTF-8"},
            "Body": {"Text": {"Data": body, "Charset": "UTF-8"}},
        },
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser("python ses.py")
    parser.add_argument("command", nargs="*")
    parser.add_argument(
        "-e", "--email", required=False, dest="email", type=str, help="Email to verify."
    )
    parser.add_argument("--sender", dest="sender", type=str)
    parser.add_argument("--subject", dest="subject", type=str)
    parser.add_argument("--body", dest="body", type=str)
    parser.add_argument("--to", dest="to", type=str)
    args = parser.parse_args()
    # print args
    command = args.command[0]
    if command == "verify_email_address":
        verify_email_address(args.email)
    elif command == "list_verified_email_addresses":
        list_verified_email_addresses()
    elif command == "send_email":
        send_email(
            sender=args.sender,
            subject=args.subject,
            body=args.body,
            recipients=[args.to],
        )
    else:
        print(args)
        raise ValueError("Unkown command.")
