function out = p2c1(im,k)
    im = double(im)*255;
    out = cell(k,1);
%      figure;
    for i=1:k
        out(i) = {im/255};
%         subplot(1,k,i);imshow(uint8(im),[]);
        if i==k
            break;
        end
        im = imresize(im,0.5);
        im = imgaussfilt(im,4);
    end
end