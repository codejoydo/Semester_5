function out = p2a1(im,k)
%      im = double(im);
    out = cell(k,1);
%     figure;
    for i=1:k
        out(i) = {im};
%         subplot(1,k,i);imshow(uint8(im),[]);
        if i==k
            break;
        end
        im = imresize(im,0.5);
%         im = imgaussfilt(im);
%         x = 1:2:size(im,1);
%         y = 1:2:size(im,2);
%         im = im(x,y,:);
    end
end