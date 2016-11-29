close all;
I = rgb2gray(imread('building_1.jpg'));

% W1 = gradientweight(I(:,:,3));
% W2 = gradientweight(I(:,:,2));
% W3 = gradientweight(I(:,:,1));
% W = min(W1,min(W2,W3));
% % W = W2;
% W = exp(-1*W);
% BW = uint8(zeros(size(W)));
% % BW = uint8(255*(double(W)/2) + double(im(:,:,1))/2); 
% thresh = 0.65;
% BW(W>thresh) = 255;
% BW(W<thresh) = 0;
% % BW = bwmorph(BW,'branchpoints');
% BW = imerode(BW,strel('diamond',1));
% imshow(BW);

% I = histeq(I);
I = imgaussfilt(I,2);
I = edge(I,'canny');
% h = fspecial('sobel');
% I1 = imfilter(I,h);
% I2 = imfilter(I,h');
% I3 = imfilter(I,-h);
% I4 = imfilter(I,-h');
% I1 = imopen(I1,strel('diamond',2));
% I2 = imopen(I2,strel('diamond',2));
% I3 = imopen(I3,strel('diamond',2));
% I4 = imopen(I4,strel('diamond',2));

% I1 = bwmorph(I1,'thin');
% I2 = bwmorph(I2,'thin');
% I3 = bwmorph(I3,'thin');
% I4 = bwmorph(I4,'thin');
I5 = I;
% figure,imshow(I1);figure,imshow(I2);figure,imshow(I3);figure,imshow(I4);
% I5 = max(max(I1,I2),max(I3,I4));
% I5 = imopen(I5,strel('disk',5));
imshow(I5);
I5 = im2bw(I5,0.6*(graythresh(I5)));
figure,imshow(I5);
s = regionprops(I5,'ConvexArea');

