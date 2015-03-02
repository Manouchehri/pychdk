import ptp2
import numpy as np
# import cv2

cam_address = ptp2.util.list_ptp_cameras().__next__() # Only one device is attached.
# print(cam_address)
camera = ptp2.CHDKCamera(cam_address)
print("test " + str(camera.get_chdk_version()))  # Just to make sure it is working.

a, live_data = camera.get_live_view_data(liveview=True, overlay=False, palette=False)

# Get viewport height & width
vp_width = live_data.vp_desc.buffer_width
vp_height = live_data.vp_desc.visible_height

print('vp_width: ' + str(vp_width) + ", vp_height: " + str(vp_height))

# Create empty array to hold intensity values
lv_image = np.empty((vp_height * vp_width,), dtype='uint16')

# Loop over raw values & discard color information from U,V values
indx = 0
for raw_indx, k in enumerate(live_data.vp_data):

    # For my camera the data was packed UYVYYY, so we want to discard
    # every 0'th and 2'nd indexed 2-byte short
    if raw_indx % 6 in [0, 2]:
        continue

    lv_image[indx] = k
    indx += 1

# Reshape the array into a rectangle
lv_image.reshape((vp_height, vp_width), order='C')
camera.execute_lua("click(\"menu\")")

# np.set_printoptions(threshold=np.inf)
# print(lv_image)
# img = cv2.imread(lv_image)
# cv2.imshow('image', lv_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()