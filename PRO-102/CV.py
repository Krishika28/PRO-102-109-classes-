import cv2, random, time, dropbox

start_time  = time.time()

print(start_time)

def cilck_pics():
    videoObject = cv2.VideoCapture(0)

    result = True

    while (result):
        ret,frame = videoObject.read()
        image_name = "img"+ str(random.randint(0,100))+".png"
        cv2.imwrite(image_name,frame)
        start_time = time.time
        result = False

    return image_name 
    videoObject.release()
    cv2.destroyAllWindows()
class TransferData:
    def init(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        openFile = open(file_from, 'rb')
        dbx.files_upload(openFile.read(), file_to)

def upload(image_name):
    access_token = 'sl.AzQyBr2OneqFFekTG5aDpZVHmLUHW2WmyXuTV5QTlZpBPNypGi6L5fO8B9l4B_B-UvhDR-DQx5E-uhNTAZ8fDgG-01lLmYsuU71GbK6gVontTLmPTC-Pvy3ILG_lxMy3X_92I_pOw3uY'
    transferData = TransferData(access_token)

    file_from = image_name
    file_to = "/NewFolder/" + image_name  
    transferData.upload_file(file_from, file_to)
    print("File has been moved !!!")


def main():
    while(True):
        if(time.time() - start_time >= 60):
            name = cilck_pics()
            upload(name)

main()