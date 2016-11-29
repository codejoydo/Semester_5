function im = p3b(out)
    out1 = [zeros(1,size(out,2),size(out,3));out(1:end-1,:,:)];
    out2 = [zeros(size(out,1),1,size(out,3)),out(:,1:end-1,:)];
    out3 = [zeros(1,size(out2,2),size(out,3));out2(1:end-1,:,:)];
    im = out-out1-out2+out3;
    im = uint8(im);
end

% im = imread('myface.jpg');
% out = p3a(im);
% im1(:,:,1) = p3b(out(:,:,1));
% im1(:,:,2) = p3b(out(:,:,2));
% im1(:,:,3) = p3b(out(:,:,3));
% im1 = uint8(im1);
% imshow(im1);
