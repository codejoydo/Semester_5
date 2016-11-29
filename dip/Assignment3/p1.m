h = fspecial('sobel');
f = rgb2gray(imread('soccer_4.png'));
fd = double(f);
g = sqrt(imfilter(fd, h, 'replicate') .^ 2 + imfilter(fd, h', 'replicate') .^ 2);
L = watershed(g);
wr = L == 0;
% g2 = imclose(imopen(g, ones(3,3)), ones(3,3));
% L2 = watershed(g2);
% wr2 = L2 == 0;
% f2 = f;
% f2(wr2) = 255;
% imshow(f2);
rm = imregionalmin(g);



A = imread('soccer_10.png');
g = im2bw(A,graythresh(A));
C = A;
h = ones(10,10)/100;
A = imfilter(A,h);
B = zeros(size(A,1),size(A,2),size(A,3));
D = 255*ones(size(A,1),size(A,2),size(A,3));
siz = [size(A,1),size(A,2)];
A = imresize(A,siz);
B = imresize(B,siz);
a = rgb2hsv(A);
out = hsv2rgb(a);
imshow(out);
for i = 1:siz(1)
    for j = 1:siz(2)
        if (a(i,j,1)*360>60 & a(i,j,1)*360<=150) % removing green color
            A(i,j,:) = uint8(double(B(i,j,:))); % replacing with background
            a(i,j,3) = 1;
        else
            A(i,j,:) = uint8(double(D(i,j,:)));
        end
    end
end
subplot(1,2,1),imshow(C);
subplot(1,2,2),imshow(A);