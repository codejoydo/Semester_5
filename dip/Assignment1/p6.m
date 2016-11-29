im = imread('maze1.png');
N = size(im,1);
yellow = reshape([255,255,0],[1,1,3]);
white = reshape([255,255,255],[1,1,3]);
green = reshape([50,255,50],[1,1,3]);
pixels = logical(im(:,:,1)==255) & logical(im(:,:,2)==255) & logical(im(:,:,3)==0);
coords = find(pixels == 1);
starty = uint32(coords(1) / N) + 1;
startx = mod(coords(1),N) + 1 ;
q = zeros(2,N*N);
q(1,1) = startx;
q(2,1) = starty;
im(startx,starty,1) = 0;
im(startx,starty,2) = 0;
im(startx,starty,3) = 0;
par = zeros(N,N,2);
vs = zeros(N,N);
figure;
ctr = 1;
len = 1;
while ctr<=len;
    y = q(2,ctr);
    x = q(1,ctr);
    if im(x,y,1)==50 && im(x,y,2)==255 && im(x,y,3)==50
        break;
    end
    im(x,y,1) = 0;
    im(x,y,2) = 0;
    im(x,y,3) = 0;
    vs(x,y) = 1;
%     disp(size(q));
    if mod(ctr,1000)==0
        imshow(im,[]);
    end
%     disp([x,y]);
    if x+1>=1 && x+1<=size(im,1) && y>=1 && y<=size(im,2)
        if vs(x+1,y)==0
            if logical(im(x+1,y,:)==yellow) | logical(im(x+1,y,:)==white) | logical(im(x+1,y,:)==green)
                len = len + 1;
                q(:,len) = [x+1;y];
                vs(x+1,y) = 1;
                par(x+1,y,1) = x;
                par(x+1,y,2) = y;
            end
        end
    end
    if x>=1 && x<=size(im,1) && y+1>=1 && y+1<=size(im,2)
        if vs(x,y+1)==0
            if logical(im(x,y+1,:)==yellow) | logical(im(x,y+1,:)==white) | logical(im(x,y+1,:)==green)
                len = len + 1;
                q(:,len) = [x;y+1];
                vs(x,y+1) = 1;
                par(x,y+1,1) = x;
                par(x,y+1,2) = y;
            end
        end
    end
    if x-1>=1 && x-1<=size(im,1) && y>=1 && y<=size(im,2)
        if vs(x-1,y)==0
            if logical(im(x-1,y,:)==yellow) | logical(im(x-1,y,:)==white) | logical(im(x-1,y,:)==green)
                len = len + 1;
                q(:,len) = [x-1;y];
                vs(x-1,y) = 1;
                par(x-1,y,1) = x;
                par(x-1,y,2) = y;
            end
        end
    end
    if x>=1 && x<=size(im,1) && y-1>=1 && y-1<=size(im,2)
        if vs(x,y-1)==0
            if logical(im(x,y-1,:)==yellow) | logical(im(x,y-1,:)==white) | logical(im(x,y-1,:)==green)
                len = len + 1;
                q(:,len) = [x;y-1];
                vs(x,y-1) = 1;
                par(x,y-1,1) = x;
                par(x,y-1,2) = y;
            end
        end
    end
    ctr = ctr + 1;
end
while par(x,y,1) ~= startx || par(x,y,2) ~= starty
    im(x,y,3) = 255;
    im(x,y,2) = 255;
    px = par(x,y,1);
    py = par(x,y,2);
    x = px;
    y = py;
    disp([x,y]);
end
imshow(im);