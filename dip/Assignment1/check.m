function ret = check(im,vs,x,y)
    
    ret = 0;
    if x<1 || x>size(im,1)
        ret = 0;
        return;
    end
    if y<1 || y>size(im,2)
        ret = 0;
        return;
    end
    if vs(x,y)==1
        ret = 0;
        return;
    end
    if im(x,y,1)==255 && im(x,y,2)==255 && im(x,y,3)==255
        ret = 1;
        return;
    end
    if im(x,y,1)==255 && im(x,y,2)==255 && im(x,y,3)==0
        ret = 1;
        return;
    end
    %     disp(ret);
end