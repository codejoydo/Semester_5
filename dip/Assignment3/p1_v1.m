I = imread('soccer_2.png');
siz = [size(I,1),size(I,2)];
W1 = gradientweight(I(:,:,3));
W2 = gradientweight(I(:,:,2));
W3 = gradientweight(I(:,:,1));
W = min(W1,min(W2,W3));
% W = W2;
W = exp(-1*W);
BW = uint8(zeros(size(W)));
BW = uint8(255*(double(W)/2) + double(im(:,:,1))/2); 
thresh = 0.63;
BW(W>thresh) = 255;
BW(W<thresh) = 0;


BW = imdilate(BW,strel('diamond',3));
BW = imerode(BW,strel('diamond',1));

imshow(BW);
[H,T,R] = hough(BW);
P  = houghpeaks(H,20,'threshold',ceil(0.3*max(H(:))));
lines = houghlines(BW,T,R,P,'FillGap',5,'MinLength',7);
imfigure, imshow(BW), hold on
max_len = 0;
for k = 1:length(lines)
    xy = [lines(k).point1; lines(k).point2];
    plot(xy(:,1),xy(:,2),'LineWidth',10,'Color','black');
    len = norm(lines(k).point1 - lines(k).point2);
    if ( len > max_len)
       max_len = len;
       xy_long = xy;
    end
end


k = 100;
for i = 0:size(I,1)/k
    for j = 0:size(I,2)/k
        tmp_im = I(i*k+1:min(size(I,1),(i+1)*k+1),j*k+1:min(size(I,2),(j+1)*k+2));
        tmp_im = histeq(tmp_im);
        I(i*k+1:min(size(I,1),(i+1)*k+1),j*k+1:min(size(I,2),(j+1)*k+2)) = tmp_im;
    end
end
imshow(I);