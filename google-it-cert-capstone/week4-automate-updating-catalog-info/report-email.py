#!/usr/bin/env python3
import os
import datetime
import reports
import emails


# read text entry:
def process_info(file):
    with open(file) as f:
        lines = f.read().strip().splitlines()
    name_field = "name: {}".format(lines[0])
    weight_field = "weight: {}".format(lines[1])
    return "{}<br/>{}<br/><br/>".format(name_field, weight_field)


def main():
    text_path = "supplier-data/descriptions/"
    files = os.listdir(text_path)

    report_file = "/tmp/processed.pdf"

    report_body = ""
    for file in files:
        report_body += process_info(file)

    today = datetime.datetime.today()
    report_title = "Processed Update on {} {}, {}".format(
        today.strftime("%B"), today.day, today.year
    )

    # generate report file:
    reports.generate_report(report_file, report_title, report_body)

    # generate & send email report:
    content = {
        "sender": "automation@example.com",
        "receiver": "{}@example.com".format(os.environ.get("USER")),
        "subject": "Upload Completed - Online Fruit Store",
        "body": "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        "attachment": report_file,
    }
    message = emails.generate_email(**content)
    emails.send_email(message)


if __name__ == "__main__":
    main()
