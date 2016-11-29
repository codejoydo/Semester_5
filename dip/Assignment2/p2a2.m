function out = p2a2(im,k)
    gp = p2a1(im,k);
    out = cell(k,1);
    figure;
    for i=1:k-1
        out(i) = {gp{i}-imresize(gp{i+1},[size(gp{i},1),size(gp{i},2)])};
        subplot(1,k,i);imshow(uint8(out{i}),[]);
    end
    out(k) = gp(k);
    subplot(1,k,k);imshow(uint8(out{k}),[]);
end