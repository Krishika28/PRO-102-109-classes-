import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AzOuULU4q9w9FElmpXLW0vnWqAeL54il8wPFH4rPWQORVr6Oa76ZKqTqaFjpARqADwCOwWRXiUH8jtG4u1VWXPJB26X4F-xqS4KfErFpyhZ8BN9Ql-_I_fIOlydncAOYpbXnteWq-To'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt' 

    
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()