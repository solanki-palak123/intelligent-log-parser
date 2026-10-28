import argparse
import logging

logging.basicConfig(
            filename="parser.log",
            level=logging.INFO,
            format="%(asctime)s-%(levelname)s-%(message)s"
)
parser = argparse.ArgumentParser()
parser.add_argument("--keyword",choices=["ERROR" ,"FAILED", "CRITICAL"])
args = parser.parse_args()

try:
    with open("server.log", "r") as file:
         result = file.read()

    with open("incident_report.txt", "w") as file:
         found=False
         for item in result.splitlines():
             if args.keyword in item:
                file.write(item + "\n")
                found=True
         if(found==False):
             logging.warning("keyword not found")
    logging.info("Log parser successfully run")

except(FileNotFoundError):
    logging.error("File not found")  

