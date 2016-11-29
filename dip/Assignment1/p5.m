A = imread('lena1.jpg');
h = fspecial('gaussian',5,2);
A = imfilter(A,h);
k = 4; % or 8
k1 = 256/k;
A = double(floor(double(A)/k1));
C = zeros(k*k*k,1);
for i=1:size(A,1)
    for j=1:size(A,2)
        val = A(i,j,1)+k*A(i,j,2)+k*k*A(i,j,3)+1;
        C(val) = C(val) + 1;
    end
end
[Maxima,MaxIdx] = findpeaks(C);
[~,idx] = sort(Maxima,'descend');
figure;
sid = int32(sqrt(size(idx,1)) + 1);
for i=1:size(idx,1);
    val = MaxIdx(idx(i)) - 1;
    disp([Maxima(idx(i)),val]);
    r = mod(val,k)*k1;
    val = val / k;
    g = mod(val,k)*k1;
    val = val / k;
    b = mod(val,k)*k1;
    out = uint8(zeros(500,500,3));
    out(:,:,1) = r;
    out(:,:,2) = g;
    out(:,:,3) = b;
    subplot(9,9,i);
    imshow(out,[]);
end
