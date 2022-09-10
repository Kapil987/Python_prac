## Coroutines : we use this when our funtion take more time to read/initialise 
# at the begining
def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
next(search)
search.send("book")
input("press any key")
search.send("This")
search.close()  # to free up resources

## Conclusion
# for first call to searcher() will take 4 sec after that next call to searcher()
#  will start from while this saves our time consumed in some task, This optimises 
# our code




