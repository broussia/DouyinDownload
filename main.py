import download
import appium_operation
import database


def main():
    appium_operation.operation()
    database.save_in_database()
    download.download()
    return


if __name__ == "__main__":
    main()
