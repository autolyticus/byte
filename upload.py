import dropbox


class TransferData:
    def __init__(self):
        self.access_token = '4gc0YhoYYVAAAAAAAAAACsHBfiNVDgSKDbtCOnJQRaR77j0rwVuMOoUbCnxSbJJY'

    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

    def download_file(self, file_from):
        dbx = dropbox.Dropbox(self.access_token)
        metadata, f = dbx.files_download(file_from)
        out = open(file_from[1:],'wb')
        out.write(f.content)
        out.close()


def main():
    access_token = '4gc0YhoYYVAAAAAAAAAACsHBfiNVDgSKDbtCOnJQRaR77j0rwVuMOoUbCnxSbJJY'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    # The full path to upload the file to, including the file name
    file_to = '/test_dropbox/test.txt'

    # API v2
    transferData.download_file(file_to)


if __name__ == '__main__':
    main()
