close all;
I = rgb2gray(imread('building_3.jpg'));
imlp = imgaussfilt(I,3);
k = 2;
imhp = uint8(double(I - imlp)*k);
I = uint8(double(I) + double(imhp));
l = double(size(I,2));
b = ceil(double(size(I,1)) * (1200 / l));
I = imresize(I,[b,1200]);
orig = I;
I = imgaussfilt(I,3);
h = fspecial('sobel');
I1 = imfilter(I,h);
I2 = imfilter(I,h');
I3 = imfilter(I,-h);
I4 = imfilter(I,-h');

I1 = imopen(I1,strel('disk',1));
I2 = imopen(I2,strel('disk',1));
I3 = imopen(I3,strel('disk',1));
I4 = imopen(I4,strel('disk',1));
figure,imshow(I1);figure,imshow(I2);figure,imshow(I3);figure,imshow(I4);
I5 = max(max(I1,I2),max(I3,I4));
I5 = imerode(I5,strel('disk',2));


I5 = im2bw(I5,0.7*(graythresh(I5)));
I5 = imclose(I5,strel('diamond',1));
imshow(I5);
s = regionprops(I5,'ConvexArea');
areas = [];
for i=1:size(s,1)
    areas = [areas,s(i).ConvexArea];
end
h = histogram(areas,1000);
val = h.Values;
inds = find(areas>680 & areas < 15000);
% [~,I] = sort(val,'descend');
% disp(I(2));
s1 = regionprops(I5,'BoundingBox');
imshow(orig);
hold on
for i = 1:size(inds,2)
  thisBB = s1(inds(i)).BoundingBox;
  rectangle('Position', [thisBB(1),thisBB(2),thisBB(3),thisBB(4)],...
  'EdgeColor','y','LineWidth',2 )
    pause(0.1);
end
