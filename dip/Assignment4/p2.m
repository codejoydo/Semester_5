close all;
clear;
clc;
I = imread('bottles.tif');
O = I;
thresh = multithresh(I,2);
I = imquantize(I,thresh);
I = I==2;
I = imclose(I,strel('disk',5));
I = imopen(I,strel('disk',5));
CC = bwconncomp(I);
S = regionprops(CC,'BoundingBox');
height = zeros(1,size(S,1));
for i = 1:size(S,1)
    thisBB = S(i).BoundingBox;
    height(i) = thisBB(4);
end
mdheight = (max(height)+min(height))/2;
inds = find(height<mdheight);
imshow(O);
hold on;
for i = 1:size(inds,2)
    thisBB = S(inds(i)).BoundingBox;
    rectangle('Position', [thisBB(1),thisBB(2),thisBB(3),thisBB(4)],...
        'EdgeColor','r','LineWidth',2 )
    pause(0.1);
end
