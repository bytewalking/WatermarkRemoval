import cv2
import numpy

test_dir = '/Users/zhaopenghui/Documents/WorkSpace/WatermarkRemoval/test_dir/16024112_9DP6.jpg'
mask_dir = '/Users/zhaopenghui/Documents/WorkSpace/WatermarkRemoval/mask_dir/16024130_9Gxg.png'
save_dir = '/Users/zhaopenghui/Documents/WorkSpace/WatermarkRemoval/save_dir/result.jpg'

src = cv2.imread(test_dir)
mask = cv2.imread(mask_dir)
save = numpy.zeros(src.shape, numpy.uint8)
for row in range(src.shape[0]):
    for col in range(src.shape[1]):
        for channel in range(src.shape[2]):
            if mask[row, col, channel] == 0:
                val = 0
            else:
                reverse_val = 255 - src[row, col, channel]
                val = 255 - reverse_val * 256 / mask[row, col, channel]
                if val < 0:
                    val = 0
            save[row, col, channel] = val
cv2.imwrite(save_dir, save)
