function [x1,y1] = getpoints(corners)
    xmax = max(corners(1,:));
    xmin = min(corners(1,:));
    ymax = max(corners(2,:));
    ymin = min(corners(2,:));
    xrange = xmin:xmax;
    yrange = ymin:ymax;
    [x1,y1] = ndgrid(xrange,yrange);
end