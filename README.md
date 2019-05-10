# Law 2.0 Spring 2019 Final Project - Peter Zhu
A repository designed to leverage `git` for comparing changes in statutes over time. Title 26 of the United States Code before and after the passage of the Tax Cut and Jobs Act (TCJA) is used here as proof of concept.

## Motivation

The law [changes all the time](http://uscode.house.gov/download/priorreleasepoints.htm). As of May 2019, Title 26, the Internal Revenue Code, has already iterated twice in the year to date. For lawyers to identify what changed in each iteration is a significant burden. The IRC has over 2100 operating sections, each with their own subsections, paragraphs, subparagraphs, and so on. 

Luckily, the U.S. Legislature publishes all titles of its Code in XML format, both [current](http://uscode.house.gov/download/download.shtml) and [previous](http://uscode.house.gov/download/priorreleasepoints.htm) versions. But even so, a simple diff-check between XML files will be fruitless. A diff of the contents still require plenty of effort to determine if the changes were as small as fixing grammar or adding/removing entire sections.

`git` is the ideal tool for tracking changes in a repository of well-structured files. This project aims to translate the XML files into a file tree of individual files and directories mirroring the Code's hierarchy. Because each level of the Code, from the section to the the smallest subclause, occupies its own directory, we can easily leverage `git --diff` to find differences at each of the levels.

## Getting Started

This repository holds several branches, described below. "Data branches" are branches that only contain the parsed Code in the form of a file tree structure.

Branches | Description 
----------|-----------
master | Contains the parser code and README. Clone this branch if you intend to create your own repositories using the parser.
pre-tcja | Data branch containing all of the provisions of Title 26 as of October 6, 2017
post-tcja | Data branch containing all of the provisions of Title 26 as of April 4, 2019
... | Any number of additional branches may be added using the parser in `master/parser`

### Comparing Existing Branches

To run the example queries (see below), clone this repo and checkout the data branches using the following commands:

```
> git checkout pre-tcja
> git checkout post-tcja
```

Data branches have the following file structure

- **t26**: Title 26, root directory
  - **s1, s2, ..., s1014, ...**: sections. These would correspond, for example, [Section 1014](https://www.law.cornell.edu/uscode/text/26/1014).
    - header
    - chapeau
    - content
    - **subsections** (a), (b), ...
      - header
      - chapeau
      - content
      - continuation
    

## Example Queries

Tracking all changes between two data branches.
```
> git diff --name-only --diff-filter=A pre-tcja..post-tcja

t26/s1/f/2/A/chapeau
t26/s1/f/2/A/i/content
t26/s1/f/2/A/ii/content
t26/s1/f/3/A/chapeau
t26/s1/f/3/A/heading
t26/s1/f/3/A/i/content
t26/s1/f/3/A/ii/content
t26/s1/f/3/B/chapeau
t26/s1/f/3/B/heading
t26/s1/f/3/B/i/content
t26/s1/f/3/B/ii/content
t26/s1/f/3/C/content
t26/s1/f/3/C/heading
t26/s1/f/6/chapeau
t26/s1/f/7/A/content
t26/s1/f/7/A/heading
t26/s1/f/7/B/content
t26/s1/f/7/B/heading
t26/s1/h/11/C/iii/I/content
t26/s1/h/11/C/iii/II/content
t26/s1/h/11/C/iii/chapeau
t26/s1/j/1/A/content
t26/s1/j/1/B/content
t26/s1/j/1/chapeau
t26/s1/j/1/heading
...
```




## Interesting Statistics

## Next Steps

This repository holds several branches, each containing a version of the Internal Revenue Code. The branches and their descriptions are as follows:

- pre-tcja (Internal Revenue Code as of January 2018)
- post-tcja (Internal Revenue Code as of April 2019)

Each segment of the code (i.e. section, subsection, paragraph, subparagraph, clause, subclause) are stored as individual directories.

You can leverage `git` to find changes and differences between these two versions of the Code. For example, the following command will show you all new provisions added as a result of the Tax Cut and Jobs Act.

