function [im,fl] = dfs(im,vs,x,y,lenx,leny,fl)
    if im(x,y,1)==50 && im(x,y,2)==255 && im(x,y,3)==50
        fl = 1;
    end
    if fl>=1
        if fl==1
            fl = fl + 1;
            imshow(im);
        end
        return;
    end
    im(x:x+lenx,y:y+leny,1) = 0;
    im(x:x+lenx,y:y+leny,2) = 0;
    im(x:x+lenx,y:y+leny,3) = 0;
    if check(im,x+1+lenx,y) == 1
        [im,fl] = dfs(im,x+2+leny,y,lenx,leny,fl);
    end
    if check(im,x,y+1+leny) == 1
        [im,fl] = dfs(im,x,y+2+leny,lenx,leny,fl);
    end
    if check(im,x-1,y) == 1
        [im,fl] = dfs(im,x-2-lenx,y,lenx,leny,fl);
    end
    if check(im,x,y-1) == 1
        [im,fl] = dfs(im,x,y-2-leny,lenx,leny,fl);
    end
end