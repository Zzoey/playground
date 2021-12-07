import argparse
from unified_api import UnifiedApi


def main(api_name):
    api_obj = UnifiedApi()
    messenger_object = api_obj.selectApi(api_name)
    msg = messenger_object.Subscriber()
    print(msg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_type", "-a")
    args = parser.parse_args()
    main(args.api_type)
