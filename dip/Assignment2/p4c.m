% im - input image
% s1 - sigma of normal gaussian
% s2 - sigma of intensity gaussian
% w - window size
% function appiles bilateral to only 1 channel
function out = p4a(im,s1,s2,w)
    im = double(im);
    h = fspecial('gaussian',[2*w+1;2*w+1],s1);
    out = zeros(size(im));
    for i=1:size(im,1)
        for j=1:size(im,2)
            subim = im(max(i-w,1):min(i+w,size(im,1)),max(j-w,1):min(j+w,size(im,2)));
            u = i - max(i-w,1);
            d = min(i+w,size(im,1)) - i;
            l = j - max(j-w,1);
            r = min(j+w,size(im,2)) - j;
            difim = abs(subim - im(i,j));
            fr = exp((difim.*difim)/(2*s2*s2)); % finds edges(variation in intensity) to blur them
            gs = h(w+1-u:w+1+d,w+1-l:w+1+r);
            val = fr.*gs.*subim;
            tmp = fr.*gs;
            out(i,j) = sum(val(:))/sum(tmp(:));
        end
    end
    out = uint8(out);
end

% applications of inverse bilateral filter  
% edge detection
% object detection in image(provided object has more features than
% background
% image segmentation