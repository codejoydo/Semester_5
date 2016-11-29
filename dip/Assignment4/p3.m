close all;
clear;
clc;
D=dir('tic*');
for f=1:size(D,1)
    I=imread(D(f).name);
    O=I;
    I=rgb2gray(I);
    I=1-im2bw(I);
    CC=bwconncomp(I);
    S=regionprops(CC,'Perimeter');
    P=[S(:).Perimeter];
    [~,indexOfMax]=max(P);
    I(CC.PixelIdxList{indexOfMax})=0;
    CC=bwconncomp(I);
    S=regionprops(CC,'EulerNumber');
    S1=regionprops(CC,'Centroid');
    Enum=[S(:).EulerNumber];
    Cent=floor([S1(:).Centroid]);
    I1=zeros(size(I));
    I2=I1;
    for i=1:size(Enum,2)
        if Enum(i)==1
            I1(Cent(i*2),Cent((i-1)*2+1))=1;
        else
            I2(Cent(i*2),Cent((i-1)*2+1))=1;
        end
    end
    I1=bwmorph(I1,'thicken',5);
    I2=bwmorph(I2,'thicken',5);
    [H1,~,~]=hough(I1);
    [H2,~,~]=hough(I2);
    M1=max(H1(:));
    M2=max(H2(:));
    if M1>M2
        disp('X won');
    elseif M1<M2
        disp('O won');
    else
        disp('Draw');
    end
    subplot(2,2,f),imshow(O);
end