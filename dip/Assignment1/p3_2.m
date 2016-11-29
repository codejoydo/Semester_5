% im = imread('car.png');
% imshow(p3_2(im,[277,60],[277,360,size(im,1)]));
% line param - line vertical point, line width
% circle param - center x, center y, circle diameter 
function out = p3_2(im,lineparam,circleparam)
    im = double(p3_1(im,lineparam));
    posx = circleparam(1);
    posy = circleparam(2);
    dia = circleparam(2);
    h = fspecial('gaussian',[2*size(im,1);2*size(im,2)],dia/1.5);
    midx = int32(size(h,1)/2);
    midy = int32(size(h,2)/2);
    h = h(midx+1-posx:midx+size(im,1)-posx,midy+1-posy:midy+size(im,2)-posy);
    h = h / max(h(:));
    im(:,:,1) = im(:,:,1) .* h;
    im(:,:,2) = im(:,:,2) .* h;
    im(:,:,3) = im(:,:,3) .* h;
    out = uint8(im);
end