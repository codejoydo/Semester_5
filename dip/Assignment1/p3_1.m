% im = imread('car.png');
% imshow(p3_1(im,[277,60]));
% line param - line vertical point, line width
function out = p3_1(im,lineparam)
    pos = lineparam(1);
    width = lineparam(2);
    x1 = pos - width;
    x2 = pos + width;
    h = fspecial('gaussian',5,2);
    blur_im = double(imfilter(im,h));
    h1 = fspecial('gaussian',[size(im,1); 1],size(im,2)/3);
    h1mat = repmat(h1,1,size(im,2));
    h1mat = h1mat / max(h1mat(:));
    blur_im(:,:,1) = blur_im(:,:,1).*h1mat;
    blur_im(:,:,2) = blur_im(:,:,2).*h1mat;
    blur_im(:,:,3) = blur_im(:,:,3).*h1mat;
    imshow(h1mat,[]);
    out = zeros(size(im));
    out(1:x1,:,:) = blur_im(1:x1,:,:);
    out(x1:x2,:,:) = im(x1:x2,:,:);
    out(x2:end,:,:) = blur_im(x2:end,:,:);
    out = uint8(out);
end