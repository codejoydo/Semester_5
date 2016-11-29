%% Single-sample perceptron with margin
a = rand(3,1);
w1 = [[2,7];[8,1];[7,5];[6,3];[7,8];[5,9];[4,5]];
w2 = [[4,2];[-1,-1];[1,3];[3,-2];[5,3.25];[2,4];[7,1]];
py = [ones(size(w1,1),1),w1];
ny = [-ones(size(w2,1),1),-w2];
y = [py;ny]';
k = 1;
n = size(y,2);
it = 0;
b = 0.1;
eta = 1;
while 1
    dist = a'*y;
    if size(find(dist<b),2) == 0
        break
    end
    if a'*y(:,k) < b
        a = a + eta*y(:,k);
    end
    k = mod(k+1,n);
    if k == 0
        k = 1;
    end
    it = it + 1;
end
disp(it);
for i=1:14
    if transpose(y(:,i))*a <= b
        disp('Not Seperated');
    end
end
figure;
x=randi([-10 10],100,1);
A=a(2);
B=a(3);
C=a(1);
Y=(A*x +C)/(-1*B+0.000001);

plot(Y,x)
hold on;
plot(w1(:,2),w1(:,1),'*',w2(:,2),w2(:,1),'*');