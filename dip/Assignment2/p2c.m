im1 = imread('source.jpg.jpg');
im2 = imread('target.jpg.jpg');
mask = double(imread('mask.png'));
figure;
for k = 2:4
    gp = p2c1(mask,k);
    lp1 = p2a2(im1,k);
    lp2 = p2a2(im2,k);
    for i=1:k
        mat = zeros(size(gp{i},1),size(gp{i},2),3);
        mat(:,:,1) = gp{i};
        mat(:,:,2) = gp{i};
        mat(:,:,3) = gp{i};
        lp1{i} = mat.*double(lp1{i}) + (1-mat).*double(lp2{i});
    end
    out = p2b(lp1);
    subplot(3,1,k-1),imshow(out);
end
% as k increases, transition gets smoother. 