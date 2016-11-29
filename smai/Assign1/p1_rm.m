%% Relaxation algorithm with margin
a = randi([-100 100],3,1);
w1 = [[2,7];[8,1];[7,5];[6,3];[7,8];[5,9];[4,5]];
w2 = [[4,2];[-1,-1];[1,3];[3,-2];[5,3.25];[2,4];[7,1]];
py = [ones(size(w1,1),1),w1];
ny = [-ones(size(w2,1),1),-w2];
y = [py;ny]';
k = 1;
n = size(y,2);
learningRate = 0.001;
b = 0.01;
theta = 0.0001;
it = 0;
while 1
    dist = a'*y - b;
    ind = find(dist<0);
    miscfd = y(:,ind);
    miscfd_dist = dist(ind);
    miscfd_norm = diag(miscfd'*miscfd)';
    miscfd_err = repmat(miscfd_dist ./ miscfd_norm,size(y,1),1);
    miscfd_err = miscfd_err .* miscfd;
    final_err = sum(miscfd_err')';
  
    if abs(sum(learningRate * final_err)) < theta
        break
    else 
        disp(abs(sum(learningRate * final_err)));
    end
    a = a - learningRate * final_err;
    it = it + 1;
end
disp(it);

for i=1:14
    if transpose(y(:,i))*a <= 0
        disp('Not Seperated');
        disp(i);
    end
end

x=randi([-10 10],100,1);
A=a(2);
B=a(3);
C=a(1);
Y=(A*x +C)/(-1*B+0.000001);

plot(Y,x)
hold on;
plot(w1(:,2),w1(:,1),'*',w2(:,2),w2(:,1),'*');