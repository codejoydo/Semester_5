function im = p3d(out)
    out1 = [zeros(1,size(out,2),size(out,3));out(1:end-1,:,:)];
    out = out-out1;
    out2 = [zeros(size(out,1),1,size(out,3)),out(:,1:end-1,:)];
    out = out - out2;
    im = uint8(out);
end