% im = imread('myface.jpg');
% out = p3a(im);

function dp = p3a(im)
    dp = double(im);
    for i=2:size(im,1)
        dp(i,1,:) = dp(i,1,:)+dp(i-1,1,:);
    end
    for j=2:size(im,2)
        dp(1,j,:) = dp(1,j,:)+dp(1,j-1,:);
    end
    for i=2:size(im,1)
        for j=2:size(im,2)
            dp(i,j,:) = dp(i,j,:)+dp(i-1,j,:)+dp(i,j-1,:)-dp(i-1,j-1,:);
        end
    end
    figure,imshow(uint8(dp*255/max(dp(:))),[]);
end