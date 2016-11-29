% normal twirl implementation 
im = imread('14206207_1192339817472488_5713676830361873821_o.jpg');
xc = 378;
yc = 755;
rmax = 500;
rmin = 120;
alpha = -1.2;
[x,y] = ndgrid(1:size(im,1),1:size(im,2));
dx = x-xc;dy = y-yc;
r = sqrt(dx.*dx+dy.*dy);
beta = atan2(dy,dx) + alpha*((rmax-r)/rmax);
reg = logical(r<=rmax) & logical(r>=rmin);
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
rmax = 100;
alpha = 1;
[x,y] = ndgrid(1:size(im,1),1:size(im,2));
dx = x-xc;dy = y-yc;
r = sqrt(dx.*dx+dy.*dy);
inds = find(r<=rmax);
x = x-xc;
y = y-yc;
t = [1,-1*alpha/rmax,alpha;0,1,0;0,0,1];
out = p5a(im,x,y,t,inds,1,1);
