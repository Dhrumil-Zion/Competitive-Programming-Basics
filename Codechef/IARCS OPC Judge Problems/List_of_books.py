num_of_books_in_total = int(input())
books_arr = [0]+list(map(int,input().split()))
no_of_borrowed_books = int(input())
for _ in range(no_of_borrowed_books):
    id = int(input())
    print(books_arr.pop(id))