function out = p2b(lp)
    k = size(lp,1);
    for i=k-1:-1:1
        lp{i} = lp{i} + imresize(lp{i+1},[size(lp{i},1),size(lp{i},2)]);
    end
    out = uint8(lp{1});
    imshow(out);
end