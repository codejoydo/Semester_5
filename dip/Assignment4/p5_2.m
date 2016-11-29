close all;
clear;
clc;
D = dir('Tone_mapping/*.pfm');
for f=5:5
    if D(f).name == '.'
        continue;
    end
    I = getpfmraw(strcat('Tone_mapping/',D(f).name));
    figure,imshow(I);
    L = (0.2126*I(:,:,1) + 0.7152*I(:,:,2) + 0.0722*I(:,:,3));
    disp(max(I(:)));
    d = 1;
    a = 0.80;
    N = numel(L);
    L1 = log(L+d);
    Lw = sum(L1(:))/N;
    I = (a/Lw)*I;
    figure,imshow(I);
    imwrite(I,strcat('Tone_mapping/',strcat(D(f).name(1:end-4),'_key_0.80.bmp')));
end