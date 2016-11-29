dat = load('data.txt');
ell = size(dat,1);
N = 2;

X = dat(:,1:2)';
K = X'*X;
% original kernel matrix stored in variable K
% clustering given by a ell x N binary matrix A
% and cluster allocation function f
% d gives the distances to cluster centroids
A = zeros(ell,N);
f = ceil(rand(ell,1)* N);
for i=1,ell;
    A(i,f(i)) = 1;
end
change = 1;
while change == 1
    change = 0;
    E=A*diag(1./sum(A));
    Z = ones(ell,1)* diag(E'*K*E)'- 2*K*E;
    [d, ff] = min(Z, [], 2);
    for i=1,N;
        if f(i) ~= ff(i)
            A(i,ff(i)) = 1;
            A(i, f(i)) = 0;
            change = 1;
        end
    end
    f = ff;
end
