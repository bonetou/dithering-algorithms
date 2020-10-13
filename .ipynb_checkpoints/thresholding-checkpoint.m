image = imread('C:\Users\hbone\dev\dithering-algorithms\images\cat1_grayscale.png');

level = multithresh(image, 3);

seg_image = imquantize(image, level);
imshow(seg_image, []);