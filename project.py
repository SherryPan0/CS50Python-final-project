import pandas as pd
import re
import requests
import sys


def main():
    while True:
        name = input("Please enter an author name: ")
        if name_validate(name):
            valid_name = name_validate(name)
            authorIDs = get_authorID(valid_name)
            print(
                f"There are {len(authorIDs)} authors in the database named {valid_name}"
            )
            for authorID in authorIDs:
                papers_df = get_papers(authorID)
                print(f"AuthorID: {authorID}, number of papers: {len(papers_df)}")
                print(papers_df["title"])
                print("\n")
            break

        else:
            print("Invalide name")


def name_validate(name: str):
    # test if the name is a str, no digits no pucturations
    if re.search(r"[^\sa-zA-Z]", name):
        # print("Invalid name")
        return False
    else:
        fullname = [x.lower() for x in name.split(" ")]
        # print("+".join(fullname))
        return "+".join(fullname)


def get_authorID(name: str):
    authorIDs = []
    try:
        r = requests.get(
            f"https://api.semanticscholar.org/graph/v1/author/search?query={name}"
        )
        for i in r.json()["data"]:
            authorIDs.append(i["authorId"])
        return authorIDs
    except:
        sys.exit("request failed")


def get_papers(authorID: str):
    try:
        r = requests.get(
            f"https://api.semanticscholar.org/graph/v1/author/{authorID}?fields=aliases,papers"
        )
        paperIDs = []
        titles = []
        # print(r.json()["papers"])
        for i in r.json()["papers"]:
            paperIDs.append(i["paperId"])
            titles.append(i["title"])
        papers_df = pd.DataFrame()
        papers_df["paperID"] = paperIDs
        papers_df["title"] = titles
        return papers_df
    except:
        sys.exit("request failed")


if __name__ == "__main__":
    main()
