function Out = bilateral_filter(In,N,sigma_d,sigma_r)
[X,Y] = meshgrid(-N:N,-N:N);
G = exp(-(X.^2+Y.^2)/(2*sigma_d^2));
Len = size(In);
for i = 1:Len(1)
   iMin = max(i-N,1);
   iMax = min(i+N,Len(1));
   for j = 1:Len(2)
       jMin = max(j-N,1);
       jMax = min(j+N,Len(2));
       I = In(iMin:iMax,jMin:jMax,:);
       dL = I(:,:)-In(i,j);
       H = exp(-(dL.^2+da.^2+db.^2)/(2*sigma_r^2));
       tmp = H.*G((iMin:iMax)-i+N+1,(jMin:jMax)-j+N+1);
       norm_tmp = sum(tmp(:));
       Out(i,j,1) = sum(sum(tmp));
       Out(i,j,2) = sum(sum(tmp));
       Out(i,j,3) = sum(sum(tmp));          
   end
end


