%% single sample perceptron
a = rand(3,1);
w1 = [[2,7];[8,1];[7,5];[6,3];[7,8];[5,9];[4,5]];
w2 = [[4,2];[-1,-1];[1,3];[3,-2];[5,3.25];[2,4];[7,1]];
py = [ones(size(w1,1),1),w1];
ny = [-ones(size(w2,1),1),-w2];
y = [py;ny]';
k = 1;
n = size(y,2);
it = 0;
while it<10000
    dist = a'*y;
    if size(find(dist<0),2) == 0
        break
    end
%     disp(find(dist<0));
    if a'*y(:,k) < 0
        a = a + y(:,k);
    end
    k = mod(k+1,n);
    if k == 0
        k = 1;
    end
    it = it + 1;
end

for i=1:14
    if transpose(y(:,i))*a <= 0
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