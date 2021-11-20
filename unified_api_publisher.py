import argparse
from unified_api import UnifiedApi


def main(api_name):
    api = UnifiedApi()
    messenger_object = api.selectApi(api_name)
    messenger_object.Publisher("Heya, this is a test")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_type", "-a")
    args = parser.parse_args()
    main(args.api_type)
