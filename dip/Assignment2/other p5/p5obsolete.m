im = imread('bell.jpg');
xc = size(im,1)/2;
yc = size(im,2)/2;
rmax = 250;
for alpha =-10:1:10
X = zeros(size(im,1),size(im,2));
Y = X;
for x=1:size(im,1)
    for y=1:size(im,2)
        dx = x-xc;
        dy = y-yc;
        r = norm([dx;dy],2);
        beta = atan2(dy,dx) + alpha * ( (rmax-r) / rmax );
        if r <= rmax
            X(x,y) = xc + r * cos(beta);
            Y(x,y) = yc + r * sin(beta);
        else
            X(x,y) = x;
            Y(x,y) = y;
        end
    end
end
out = zeros(size(im,1),size(im,2),size(im,3));
out(:,:,1) = interp2(double(im(:,:,1)),Y,X);
out(:,:,2) = interp2(double(im(:,:,2)),Y,X);
out(:,:,3) = interp2(double(im(:,:,3)),Y,X);
out = uint8(out);
imshow(out,[]);
end