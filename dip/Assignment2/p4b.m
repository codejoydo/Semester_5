im = imread('boy_smiling.jpg');
sz = 7;
s1 = 3;
s2 = 10;
% figure,imshow(im);
out = im;
out(:,:,1) = p4a(out(:,:,1),s1,s2,sz);
out(:,:,2) = p4a(out(:,:,2),s1,s2,sz);
out(:,:,3) = p4a(out(:,:,3),s1,s2,sz);
figure,imshow(out);

% observations
% increasing sigma increases the blurring factor of each homogeneous region
% increasing window size decreases the noise in the homogeneous regions by
% a very small amount, not generally visible directly, taking the
% difference between 2 images with varying window size shows the
% difference
