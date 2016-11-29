close all;
clear;
clc;
D=dir('doc*');
for f=4:4
    I=imread(D(f).name);
    I=255-rgb2gray(I);
    I1=I;
    I=imopen(I,strel('disk',floor(max(size(I))/200)));
    I=255-(I1-I);
    O=ones(size(I));
    k=20;
    l=floor(size(I,1)/k);
    b=floor(size(I,2)/k);
    for i=0:k-1
        for j=0:k-1
            win=I(i*l+1:min(size(I,1),(i+1)*l),j*b+1:min(size(I,2),(j+1)*b));
            s=std(std(double(win)));
            if s>1 %experimentally found
                O(i*l+1:min(size(I,1),(i+1)*l),j*b+1:min(size(I,2),(j+1)*b))=im2bw(win,graythresh(win));
            end
        end
    end
    figure,imshow(logical(O));
end