import download
import appium_operation
import database
import upload


def main():
    appium_operation.operation()
    database.save_in_database()
    download.download()
    upload.upload()
    return


if __name__ == "__main__":
    main()
