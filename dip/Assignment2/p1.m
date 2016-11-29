function out = p1(im,sz,k)
    imlp = imgaussfilt(im,sz);
    imhp = uint8(double(im - imlp)*k);
    out = uint8(double(im) + double(imhp));
end

% both increasing window size and vale of k lead to
% boosting of features in images. 
% window size controls the amount of edges to be boosted.
% k controls the boost factor.
% 
% im = imread('bell.jpg');
% cnt = 1;
% for i=1:4
%     for j=3:3:12
%         subplot(4,4,cnt);
%         cnt = cnt+1;
%         imshow(p1(im,j,i));
%     end
% end
