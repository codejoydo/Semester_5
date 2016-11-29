A = imread('green_screen.jpg');
B = imread('background.jpg');
siz = [1000,1000];
A = imresize(A,siz);
B = imresize(B,siz);
a = rgb2hsv(A);
for i = 1:siz(1)
    for j = 1:siz(2)
        if (a(i,j,1)>0.28 & a(i,j,1)<=0.43 & a(i,j,3)>0.6) % removing green color
            A(i,j,:) = uint8(double(B(i,j,:))); % replacing with background
        end
    end
end
A(730:end,:,:) = B(730:end,:,:); % manually
imshow(A);
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  