import ptp2
import time
# import numpy as np
# import cv2
cam_address = ''
while not cam_address:
    try:
        cam_address = ptp2.util.list_ptp_cameras().__next__()  # Assuming only one device is attached.
    except:
        print("Waiting for camera...")
        time.sleep(1)


camera = ptp2.CHDKCamera(cam_address)
print("Camera is running version: " + str(camera.get_chdk_version()))  # Just to make sure it is working.

# a, live_data = camera.get_live_view_data(liveview=True, overlay=False, palette=False)

# Get viewport height & width
# vp_width = live_data.vp_desc.buffer_width
# vp_height = live_data.vp_desc.visible_height

# print('vp_width: ' + str(vp_width) + ", vp_height: " + str(vp_height))
2
# Create empty array to hold intensity values
# lv_image = np.empty((vp_height * vp_width,), dtype='uint16')

# Loop over raw values & discard color information from U,V values
# indx = 0
# for raw_indx, k in enumerate(live_data.vp_data):
#
#     # For my camera the data was packed UYVYYY, so we want to discard
#     # every 0'th and 2'nd indexed 2-byte short
#     if raw_indx % 6 in [0, 2]:
#         continue
#
#     lv_image[indx] = k
#     indx += 1

# Reshape the array into a rectangle
# lv_image.reshape((vp_height, vp_width), order='C')

print("Hit Ctrl+D to close shell.")

camera.execute_lua("switch_mode_usb(1)")

while True:
    try:
        cmd = input('chdk > ')
        camera.execute_lua(cmd)
    except EOFError:
        # camera.execute_lua("shut_down()")
        break
# camera.execute_lua("click(\"menu\")")

# np.set_printoptions(threshold=np.inf)
# print(lv_image)
# img = cv2.imread(lv_image)
# cv2.imshow('image', lv_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()