import ImageGrab
import Image
import ImageEnhance
import ImageChops
import cv
import cv2
import pytesser.pytesser as tesser

def capture(left, top, right, bottom):
    img = ImageGrab.grab((left, top, right, bottom))
    return img

def findImg(left, top, right, bottom, targetSource, threshould = 0.03):
    '''
    left, top, right, bottom: the region you want to search
    targetSource: target bitmap file path
    threshould: range from 0.0 to 1.0,
                smaller threshould means more accurate
    '''
    temppath = 'img/temp.bmp'
    img = capture(left, top, right, bottom)
    img.save(temppath)
    source = cv2.imread(temppath)
    target = cv2.imread(targetSource)
    result = cv2.matchTemplate(source, target, cv.CV_TM_SQDIFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    if minVal <= threshould:
        return (minLoc[0] + left, minLoc[1] + top)
    else:
        return None

def findImgR(rect, targetSource, threshould = 0.03):
    return findImg(rect[0], rect[1], rect[2], rect[3],
        targetSource, threshould)

def findColor(left, top, right, bottom, colstr):
    match = (int(colstr[:2], 16), int(colstr[2:4], 16), int(colstr[4:], 16))
    img = capture(left, top, right, bottom)
    data = img.getdata()
    find = False
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if data[x + y * img.size[0]] == match:
                find = True
                break
        if find:
            break

    if not find:
        return None
    return x + left, y + top

def findColorR(rect, colstr):
    return findColor(rect[0], rect[1], rect[2], rect[3], colstr)

def extractText(left, top, right, bottom, scale = 2):
    im = capture(left, top, right, bottom)
    im = im.resize([scale * i for i in im.size])
    return tesser.image_to_string(im)

def extractTextR(rect, scale = 2):
    return extractText(rect[0], rect[1], rect[2], rect[3], scale)

def test():
    print findColor(0, 0, 500, 500, 'c11313')
    pass

if __name__ == '__main__':
    test()