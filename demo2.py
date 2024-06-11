from miscellaneous import run_in_background



from camera import *



while 1==1:

    image= capture_image()

    show_image(image)

    # no threading ----
    # describe()

    # with threading ----
    # run_in_background(describe)


close_camera()
