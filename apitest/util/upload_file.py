from apitest.util.rootpath import rootpath


def upload_file(file_path):
    path = rootpath + file_path
    file = open(path, "rb")
    return file


if __name__ == "__main__":
    result = upload_file("/images/营业执照.png")
    print(type(result), result)
