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

These form the directories in each of the data branches. The text of the statutes themselves are stored in files corresponding to each of the components of the text. The components are shown in the table below. Note that not all components are substantive law---they are for purposes of making the text easy to read but effectively ignored when the statute is construed by courts.

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

### Parsing Your Own Statutes

The code to parse statutes are in the `master` branch. Download the XML versions of the U.S. Code you wish to parse from the following links

* [Current Versions](http://uscode.house.gov/download/download.shtml)
* [Previous Versions](http://uscode.house.gov/download/priorreleasepoints.htm)

Unzip the files and run the parser (while in the directory) using the following command. Make sure the specified output directory exists

```
> python -m parser.cli <file to parse.xml> -o <output directory>
```

Create a new branch by forking an existing data branch. Delete all files and copy in the parsed files.

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
Listing all provisions that were added
```
> git diff --name-only --diff-filter=A pre-tcja:t26..post-tcja:t26 | grep  -E "s[0-9]+/[a-z]+/content"
s1031/h/content
s1061/b/content
s1061/e/content
s1061/f/content
s11/b/content
s118/c/content
s1248/k/content
s1271/c/content
s1286/e/content
s1371/f/content
s1561/a/content
s1561/b/content
s196/d/content
s217/k/content
s247/a/content
s247/d/content
s250/c/content
s3111/d/content
s3221/c/content
s423/d/content
s447/d/content
s4481/d/content
s451/e/content
s451/f/content
s471/d/content
s4960/b/content
...
```

Listing changes on specific provisions
```
> git diff --diff-filter=M pre-tcja:t26/s163/j/heading..post-tcja:t26/s163/j/heading

diff --git a/pre-tcja:t26/s163/j/heading..post-tcja:t26/s163/j/heading b/post-tcja:t26/s163/j/heading
index 47d2c3b..c5fa312 100644
--- a/pre-tcja:t26/s163/j/heading..post-tcja:t26/s163/j/heading
+++ b/post-tcja:t26/s163/j/heading
@@ -1 +1 @@
-Limitation on deduction for interest on certain indebtedness
+Limitation on business interest
```

Listing provisions with the most changes (see [--dirstat parameter](https://git-scm.com/docs/git-diff) for additional options)
```
> git diff --dirstat=lines,cumulative,1 pre-tcja:t26..post-tcja:t26 | sort -r

   3.8% s168/
   3.6% s965/
   2.8% s199A/
   2.5% s168/k/
   2.4% s451/
   1.8% s59A/
   1.8% s162/
   1.6% s45Q/
   1.6% s168/k/6/
   1.6% s163/
   1.4% s1/
   1.3% s163/j/
   1.3% s1400Z–2/
   1.1% s6225/
   1.0% s807/
   1.0% s199A/g/
```

## Statistics

Statistic | Command | Value
----------| --------| ---------
Number of subsections added | `git diff --name-only --diff-filter=A pre-tcja:t26..post-tcja:t26 | grep  -E "s[0-9]+/[a-z]+/content"` | 69
Number of sections affected | `git diff --name-only pre-tcja:t26..post-tcja:t26 | awk -F'/' 'NF!=1{print $1}' | uniq | wc -l` | 526
Section with the most change | `git diff --dirstat=lines,cumulative pre-tcja:t26..post-tcja:t26` | [§ 168](https://www.law.cornell.edu/uscode/text/26/168)



## Next Steps

