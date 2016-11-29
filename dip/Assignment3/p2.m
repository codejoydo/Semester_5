I = rgb2gray(imread('building_5.jpg'));
I = 1-im2bw(I);
I1 = imdilate(I,strel('disk',2));
I2 = imerode(I,strel('disk',2));
imshow(abs(I2-I1));
% BW = edge(I,'canny');
% angular_spacing = 0.1;
% [H, theta, rho] = hough(BW);
% peaks = houghpeaks(H,100);
% c = peaks(:,1);
% r = peaks(:,2);
% lines = houghlines(f, theta, rho, peaks);
% figure, imshow(zeros(size(BW))), hold on
% for i = 1:length(lines)
%     xy = [lines(i).point1 ; lines(i).point2];
%     plot(xy(:,2), xy(:,1), 'LineWidth', 1, 'Color', [.6 .6 .6]);
% end
