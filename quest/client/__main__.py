import sys
from quest.client import application

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def main() -> int:
    """
    Main entry point into the Questlike MMO client application
    """

    return application.main(development=True)

# Main entry point into the Questlike MMO client application
if __name__ == '__main__':
    sys.exit(main())

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
