def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        dictionary = {}
        alpha_list =[]
        for x in file_contents:
            x = x.lower()
            if x not in dictionary:
                dictionary[x] = 1
            else:
                dictionary[x] += 1
        for x,y in dictionary.items():
            if x.isalpha():
                alpha_list.append({"name":x, "num":y})
        def sort_on(dict):
             return dict["num"]

        alpha_list.sort(reverse=True, key=sort_on)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document\n")
        for x in alpha_list:
            print(f"The '{x['name']}' character was found {x['num']} times")
        print("--- End report ---")


main()