import cv2
import json
import numpy as np
import pickle

cv2.setUseOptimized(True)
cv2.setNumThreads(4)
ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()

result = {"images": [], "boxes": []}

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized, r

images = json.load(open("/mnt/cvgroupsouthcentral/fsod/annotations/fsod_200_train2.json", "r"))["images"]
for j, image in enumerate(images):
    HEIGHT = 800

    name = image["file_name"]
    result["images"].append([name])

    fname = "/mnt/cvgroupsouthcentral/fsod/images/" + name
    img = cv2.imread(fname)
    big = img.shape[0] > HEIGHT

    if big:
        img, r = image_resize(img, height=HEIGHT)
    ss.setBaseImage(img)
    ss.switchToSelectiveSearchFast()

    print(f"{j + 1} / {len(images)}")
    rects = ss.process()

    if big:
        scale_fct = np.array([[1/r, 1/r, 1/r, 1/r]])
        scale_fct = np.repeat(scale_fct, len(rects), axis=0)
        rects = rects * scale_fct
    result["boxes"].append(rects)

pickle.dump(result, open("/mnt/cvgroupsouthcentral/fsod/fsod_200_train2_ss_boxes.pkl", "wb"))
