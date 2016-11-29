A = imread('soccer_10.png');
R = A(:,:,1);
G = A(:,:,2);
B = A(:,:,3);
out = 255*uint8(1-(logical(G>R) & logical(R>B)));
out = imclose(out,strel('diamond',5));
maxwhite = bwareafilt(im2bw(out),1);
out(maxwhite) = 0;
figure,imshow(out);