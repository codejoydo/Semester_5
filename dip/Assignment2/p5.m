im = imread('bell.jpg');
theta = 10;
theta = (pi*theta) / 180;
T = [cos(theta),sin(theta),0;-sin(theta),cos(theta),0;0,0,1];
corners = [1,size(im,2),size(im,2),1;1,size(im,1),1,size(im,1);1,1,1,1];
new_corners = T * corners;
xmax = max(new_corners(1,:));
xmin = min(new_corners(1,:));
ymax = max(new_corners(2,:));
ymin = min(new_corners(2,:));
xrange = xmin : xmax;
yrange = ymin : ymax;
x1 = repmat(xrange,size(yrange,2),1);
y1 = repmat(yrange,size(xrange,2),1)';
out_pts = [x1(:), y1(:), ones(size(x1,1) * size(y1,2),1)];
inv_pts = T \ out_pts';
x2 = reshape(inv_pts(1,:),size(x1,1),size(x1,2));
y2 = reshape(inv_pts(2,:),size(y1,1),size(y1,2));
out = zeros(size(x1,1),size(x1,2),3);
out(:,:,1) = interp2(double(im(:,:,1)),x2,y2);
out(:,:,2) = interp2(double(im(:,:,2)),x2,y2);
out(:,:,3) = interp2(double(im(:,:,3)),x2,y2);
out = uint8(out);
imshow(out,[]);