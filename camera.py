import cv2
from PIL import Image

from ai import image_model, flash_model
from speak import speak


cv= cv2
_resp= False


video= cv2.VideoCapture(0)



def describe():
    global _resp

    _resp= True
    try:
        text= image_model.generate_content(["describe the image", Image.open("temp.png")]).text
        speak(text)
        print("Response:", text, "\n", "-"*35, "\n")
    except:
        pass
    _resp= False



def capture_image():
    
    ret, image= video.read()
    
    return image


def show_image(image):
    cv.imshow("camera", image)
        
    cv2.imwrite("temp.png", image)


def close_camera():
    video.release()
    cv.destroyAllWindows()
