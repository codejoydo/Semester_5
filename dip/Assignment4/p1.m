close all;
clear;
clc;
D=dir('cloud*');
for f=1:1
    I=imread(D(f).name);
    O = I;
    I = rgb2gray(I);
    I = im2bw(I,0.7*graythresh(I));
    dp = zeros(size(I));
    for i=1:size(dp,1)
        if I(i,end) == 0
            dp(i,end) = 1;
        end
    end
    for i=1:size(dp,2)
        if I(end,i) == 0
            dp(end,i) = 1;
        end
    end
    for i=size(dp,1)-1:-1:1
        for j=size(dp,2)-1:-1:1
            if I(i,j) == 0
                dp(i,j) = min(dp(i+1,j),min(dp(i,j+1),dp(i+1,j+1)))+1;
            end
        end
    end
    [a,b]=max(dp(:));
    x = floor(b/size(I,1));
    y = mod(b,size(I,1))+1;
    figure,imshow(O);
    hold on;
    rectangle('Position',[x,y,a,a],...
        'LineWidth',1,'LineStyle','-')
    hold off;
    pause(0.08); % for display purposes only
end