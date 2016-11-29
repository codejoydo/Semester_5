A = imread('photo1.jpg');
n = size(A,1);
m = size(A,2);
h = fspecial('gaussian',5,2);
B= imfilter(A,h);
% imshow(A,[]);
out = bilateral_filter(double(B),1,2,10);
out = rgb2gray(uint8(out));
% imshow(uint8(255-out),[]);
% out = imfilter(out,h);
out = imadjust(uint8(255-out));
imshow(out);
c1 = out;
p1 = c1>90;
p2 = c1<=90;
c1(p1) = 255;
c1(p2) = 0;
imshow(uint8(c1),[]);
CC = bwconncomp(255-c1);
imshow(uint8(c1),[]);
for i=1:CC.NumObjects
    if size(CC.PixelIdxList{i},1) > 1000;
        siz = size(CC.PixelIdxList{i},1);
        pix = CC.PixelIdxList{i};
        rsum = uint8(sum(A(pix))/siz);
        gsum = uint8(sum(A(pix + n*m))/siz);
        bsum = uint8(sum(A(pix + 2*n*m))/siz);
        disp([rsum,gsum,bsum]);
        figure;
        out = uint8(ones(100,100,3));
        out(:,:,1) = rsum;
        out(:,:,2) = gsum;
        out(:,:,3) = bsum;
        imshow(out);
    end
end
