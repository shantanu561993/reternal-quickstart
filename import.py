from imports import ImportMetta, ImportMitre, ImportUser, ImportCommand
import argparse, getpass


function_mapping = {
    "mitre": {
        "import":ImportMitre.update
    },
    "metta": {
        "import":ImportMetta.update
    },
    "user":{
        "create":ImportUser.create
    },
    "command":{
        "create": ImportCommand.create
    }
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", help="Action to perform: delete||import||create", required=True)
    parser.add_argument("-t", "--type", help="Action to perform: mitre||metta||user", required=True)
    args = parser.parse_args()
    try:
        result = function_mapping[args.type][args.action]()
    except KeyError as error:
        result = {"result":"failed", "data":"Invalid option, use --help for an overview of types and options"}

    print(result)
