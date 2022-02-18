import sys
from quest.ai import application

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def main() -> int:
    """
    Main entry point into the Programmer's Quest MMO UberDOG server application
    """

    return application.main(development=False)

# Main entry point into the Programmer's Quest MMO UberDOG server application
if __name__ == '__main__':
    sys.exit(main())

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
