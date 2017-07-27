def count_to_10():
    for i in range(1,11):
        print(i);

count_to_10();


def count_to_n(n):
    for i in range(1, n+1):
        print(i);

count_to_n(5);

def count_to_n(n=10):
    for i in range(1, n+1):
        print(i);

count_to_n();

def count(from_num=1, to_num=10):
    for i in range(from_num, to_num +1):
        print(i);

count()
count(5);
count(5,10);
    
