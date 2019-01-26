 # Copyright PT
"""
This script is the main script to read and process traffic data
"""
import sys
from traffic_lib import read_data


def main():
    directory = sys.argv[1]
    read_data.reading_data(directory)


if __name__ == "__main__":
    """Calling the main() function and writing fatal errors in the log file"""

    try:
        # calling the main function
        main()
    except:
        raise
