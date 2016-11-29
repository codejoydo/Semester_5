close all;
clear;
clc;
D = dir('Tone_mapping/*.pfm');
for f=1:size(D,1)
    if D(f).name == '.'
        continue;
    end
    I = getpfmraw(strcat('Tone_mapping/',D(f).name));
%     %radiance is proportional to intensity.
%     figure,imshow(I);
%     for k=1:3
%         ch = I(:,:,k);
%         ch = ch - min(ch(:));
%         ch = ch / max(ch(:));
%         ch = ch * 255;
%         I(:,:,k) = ch;
%     end
%     figure,imshow(I);
    imwrite(I,strcat('Tone_mapping/',strcat(D(f).name(1:end-4),'.bmp')));
end