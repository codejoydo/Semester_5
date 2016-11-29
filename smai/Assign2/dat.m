fid = fopen('DOROTHEA/dorothea_train.data');
Z = load('DOROTHEA/dorothea_train.labels');
classes = [-1,1];
n_classes = 2;
np = 800;
nfeat = 100000;
k = 0.01;
X = zeros(nfeat,np);
for i=1:np
    tline = fgetl(fid);
    ind = int32(str2double(strsplit(tline)));
    ind = ind(1:end-1); 
%     disp(size(ind));
    X(ind,i) = 1;
end
fclose(fid);

%% PCA
K = X' * X;
[U,L] = eig(K);
[~,ind] = sort(diag(L),'descend');
PC = X * U(:,1:k);
X1 = PC' * X;

%% LDA
W1 = find(Z == 1);
W2 = find(Z == -1);
X_1 = X(:,W1);
X_2 = X(:,W2);
Xc_1 = X_1 - mean(X_1')' * ones(1,size(W1,1));
Xc_2 = X_2 - mean(X_2')' * ones(1,size(W2,1));
w = Xc_1 * (Xc_1' * mean(X_1')') + Xc_2 * (Xc_2' * mean(X_2')');
% X2 = X' * w;

%% Naive Bayes Classifier
training_vectors = X1';
likelihood_matrix = zeros(n_classes, size(training_vectors,2));
priors = zeros(n_classes, 1);
% evidences = zeros(size(training_vectors,2), 1);
for class=1:n_classes
    fm = training_vectors(Z == classes(class), :);
    likelihoods = (sum(fm,1) + k) ./ (size(fm,1) + k * size(training_vectors,2));
    likelihood_matrix(class, :) = likelihoods;
    priors(class) = (size(fm,1) + k) / (size(training_vectors,1) + k*n_classes);
end
evidences = ( (sum(training_vectors,1)+ k) ./ (size(training_vectors,1)+k*2) )';

n_classes = size(priors, 1);
n_vectors = size(training_vectors, 1);
predicted_classes = zeros(n_vectors, 1);
posteriors = zeros(n_vectors, n_classes);

for i=1:n_vectors
    vector = find(training_vectors(i, :)' ~= 0);
    likelihood_frame = likelihood_matrix(:, vector);
    post = prod(likelihood_frame,2) .* priors ./ prod(evidences(vector),1);
    [max_val, class] = max(post);
    predicted_classes(i) = class;
    posteriors(i,:) = post';
end
