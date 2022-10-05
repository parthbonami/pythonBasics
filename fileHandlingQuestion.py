def main():
    count = 0
    with open("story.txt","r+") as f: 
        for line in f:
            if line[0] not in 'T':
                count = count+1

    print(count)

if __name__ == "__main__":
    main()