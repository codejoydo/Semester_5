a = double(imread('lena1.jpg'));
b = double(imread('lena2.jpg'));
c = b(:,:,3) - a(:,:,3);
c = c - min(c(:));
c = c / max(c(:));
c = c * 255;
h = fspecial('gaussian',5);
c = imresize(c,[128,128]);
c1 = imfilter(c,h);
p11 = c1>115;
p2 = c1<=115;
c1(p11) = 255;
c1(p2) = 0;
c2 = imfilter(c1,h);
c2 = imfilter(c2,h);
c2 = imfilter(c2,h);
c3 = c2;
p11 = find(c3>90);
p2 = find(c3<=90);
c3(p11) = 255;
c3(p2) = 0;
imshow(c3,[]);]

% ans - "what is your roll number" - 201401074