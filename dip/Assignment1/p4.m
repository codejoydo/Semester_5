im = imread('lotus.jpg');
s = size(im);
figure,subplot(1,2,1),imshow(im);
n = 5;
out = uint8(zeros(s(1)-n,s(2)-n,3));
for k = 1:3
    for i = 1+n:s(1)-n
        for j = 1+n:s(2)-n
            %find mode in each window.
            m = im((i-n):(i+n),(j-n):(j+n),k);
            cnt = zeros(1,256);
            for ii = 1:(2*n+1)^2
                col = m(ii) + 1;
                cnt(col) = cnt(col) + 1;
            end
            [mxval,mxcol] = max(cnt);
            out(i-n,j-n,k) = mxcol-1;
        end
    end
end
subplot(1,2,2),imshow(out);
% imwrite(out,'out.jpg');