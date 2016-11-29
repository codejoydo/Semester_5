clear;
clc;

fid = fopen('DOROTHEA/dorothea_train.data');
np = 800;
nvar = 100000;
X = zeros(nvar,np);
for i=1:np
    tline = fgetl(fid);
    ind = int32(str2double(strsplit(tline)));
    ind = ind(1:end-1); 
    X(ind,i) = 1;
end
fclose(fid);
Y = load('DOROTHEA/dorothea_train.labels');

%PCA
k = 400;
X = X - mean(X,2)*ones(1,np);
K = X' * X;
[U,L] = eig(K);
[~,ind] = sort(diag(L),'descend');
PC = X * U(:,1:k);
X = PC' * X;

%LDA
% p = randperm(nvar, 10000);
% X = X(p,:);
% W1 = find(Y == -1);
% W2 = find(Y == 1);
% X_1 = X(:,W1);
% X_2 = X(:,W2);
% Xc_1 = X_1 - mean(X_1,2) * ones(1,size(W1,1));
% Xc_2 = X_2 - mean(X_2,2) * ones(1,size(W2,1));
% disp('done');
% Sw = Xc_1 * Xc_1' + Xc_2 * Xc_2';
% X = Sw \ (mean(X_1,2) - mean(X_2,2));

C = cvpartition(Y,'KFold',8);

meanacc = 0;

for epo=1:8

    tradat = X(:,training(C,epo));
    tralab = Y(training(C,epo));

    tesdat = X(:,test(C,epo));
    teslab = Y(test(C,epo));

    uniqlab = unique(tralab);
    nclass = length(uniqlab);
    nvar = size(X,1);
    ntest = length(teslab);

    for i=1:nclass
        ftralab(i) = sum(double(tralab==uniqlab(i)))/length(tralab);
    end

    for i=1:nclass
        tradat_i = tradat(:,(tralab==uniqlab(i)));
        tradat_mean(:,i) = mean(tradat_i,2);
        tradat_std(:,i) = std(tradat_i,0,2);
    end

    for i=1:ntest
        fteslab = normpdf(ones(nclass,1)*tesdat(:,i)',tradat_mean',tradat_std');
        fteslab = log(fteslab);
        for j=1:400
            P(i,:) = log(ftralab) + fteslab(:,j)';
        end
    end

    [pv0,id]=max(P,[],2);
    for i=1:length(id)
        pv(i,1)=uniqlab(id(i));
    end

    acc = sum(pv == teslab)/length(pv);
    meanacc = meanacc + acc;

end

disp(['accuracy = ',num2str(meanacc*(100/8)),'%'])