function out = p3(im,lines)
    % A is list of line parameters - line position, line height
    n = size(lines,2);
    out = im;
    for i=1:n
        out = p3_1(out,lines(:,i));
    end
end