import io


class Document:

    def write_into_file(self, filename, data):
        try:
            with open(filename, "a+") as file:
                file.writelines(data)
            return True
        except IOError:
            return IOError

    def read_to_check(self, filename, data_to_checked):
        flag = False
        try:
            flag = False
            with open(filename, "r+") as file:
                flag = False
                for line in file:
                    if line.strip() == data_to_checked:
                        flag = True
                        break
            return flag
        except IOError:
            return IOError

    def delete_name(self, filename, data_to_be_deleted):
        with open(filename, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.strip() != data_to_be_deleted:
                    file.write(line)
            file.truncate()


doc = Document()
doc.delete_name("list_of_user.txt", "lashkdf")
