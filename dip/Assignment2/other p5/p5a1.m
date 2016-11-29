% normal twirl implementation 
im = imread('bell.jpg');
xc = size(im,1)/2;
yc = size(im,2)/2;
rmax = 250;
alpha = 1;
[x,y] = ndgrid(1:size(im,1),1:size(im,2));
dx = x-xc;dy = y-yc;
r = sqrt(dx.*dx+dy.*dy);
beta = atan2(dy,dx) + alpha*((rmax-r)/rmax);
reg = find(r<=rmax);
xout = x;
yout = y;
xout(reg) = xc + r(reg).*cos(beta(reg));
yout(reg) = yc + r(reg).*sin(beta(reg));
out = zeros(size(im,1),size(im,2),size(im,3));
out(:,:,1) = interp2(double(im(:,:,1)),yout,xout);
out(:,:,2) = interp2(double(im(:,:,2)),yout,xout);
out(:,:,3) = interp2(double(im(:,:,3)),yout,xout);
out = uint8(out);
imshow(out,[]);

% twirl using general transformation function
im = imread('bell.jpg');
xc = size(im,1)/2;
yc = size(im,2)/2;
rmax = 250;
alpha = 1;
[x,y] = ndgrid(1:size(im,1),1:size(im,2));
dx = x-xc;dy = y-yc;
r = sqrt(dx.*dx+dy.*dy);
inds = find(r<=rmax);
x = x-xc;
y = y-yc;
t = [1,-1*alpha/rmax,alpha;0,1,0;0,0,1];
out = p5f(im,x,y,t,inds,1,1);
