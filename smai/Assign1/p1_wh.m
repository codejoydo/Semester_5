%% Widrow-Hoff or Least Mean Squared (LMS) Rule
a = randi([-100 100],3,1);
disp(a);
w1 = [[2,7];[8,1];[7,5];[6,3];[7,8];[5,9];[4,5]];
w2 = [[4,2];[-1,-1];[1,3];[3,-2];[5,3.25];[2,4];[7,1]];
b = 0.03*ones(1,size(w1,1)+size(w2,1));
py = [ones(size(w1,1),1),w1];
ny = [-ones(size(w2,1),1),-w2];
y = [py;ny]';
k = 1;
n = size(y,2);
it = 0;
learningRate = 0.01;
theta = 0.2;
while 1
    dist = (a'*y(:,k) - b(k));
    if abs( learningRate * y(:,k) * dist) < theta
        break
    end
    if a'*y(:,k) - b(k) < 0
        a = a - learningRate * y(:,k) * dist;
    end
    k = mod(k+1,n+1);
    if k == 0
        k = 1;
    end
    it = it + 1;
end
disp(it);

for i=1:14
    if transpose(y(:,i))*a <= 0
        disp('Not Seperated');
        disp(i);
    end
end
% figure;
x=randi([-10 10],100,1);
A=a(2);
B=a(3);
C=a(1);
Y=(A*x +C)/(-1*B+0.000001);

plot(Y,x)
hold on;
plot(w1(:,2),w1(:,1),'.',w2(:,2),w2(:,1),'*');