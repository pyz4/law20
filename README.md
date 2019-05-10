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

The U.S.C Code have the following hierarchy, ordered from top-down.

Directory Name | Description | Example Result
---------------|-------------|-----------------
t26 | Title 26, root directory | 
section | s1, s2, ..., s1014, ... | "1014"
subsection | (a), (b), ... | 1014(a): "Except as otherwise provided in this section,..."
paragraph | (1), (2), ... | 1014(a)(1): "the fair market value of the property..."
subparagraph | (A), (B), ... | 1014(b)(9)(A): "annuities described in section 72;"
clause | (i), (ii), ... | 1(g)(2)(A)(i): "has not attained age 18..."
subclause | (I), (II), ... | 1(g)(2)(A)(i)(I): "has attained age 18 before..."

These form the directories in each of the data branches. The text of the statutes themselves are stored in files representing each of the components of the text. The components are shown in the table below. Note that not all components are substantive law.

Component | Description | Substantive Law?
------- | ---- | ----
`heading` | bold leading text | No
`chapeau` | preamble when there are sub-provisions | Yes
`content` | text of the provision itself | Yes
`continuation` | follow-on text when the content is broken into pieces | Yes

Below gives an example of [1(g)(7)](https://www.law.cornell.edu/uscode/text/26/1) (one of the few paragraphs that cover all the levels of the hierarchy).

```
s1/g/2
├── A
│   ├── chapeau: "such child—"
│   ├── i
│   │   └── content: "has not attained age 18 before the close of the taxable year, or"
│   └── ii
│       ├── I
│       │   └── content: "has attained age 18 before the close of the taxable year..."
│       └── II
│           └── content: "whose earned income (as defined in section 911(d)(2))..."
├── B
│   └── content: "either parent of such child is alive at the close of the taxable year, and"
├── C
│   └── content: "such child does not file a joint return for the taxable year."
├── chapeau: "This subsection shall apply to any child for any taxable year if—"
└── heading: "Child to whom subsection applies"
```


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

