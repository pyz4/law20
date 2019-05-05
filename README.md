# Law 2.0 Spring 2019 Final Project - Peter Zhu
Title 26 of the United States Code before and after the TCJA

This repository holds several branches, each containing a version of the Internal Revenue Code. The branches and their descriptions are as follows:

- pre-tcja (Internal Revenue Code as of January 2018)
- post-tcja (Internal Revenue Code as of April 2019)

Each segment of the code (i.e. section, subsection, paragraph, subparagraph, clause, subclause) are stored as individual directories.

You can leverage `git` to find changes and differences between these two versions of the Code. For example, the following command will show you all new provisions added as a result of the Tax Cut and Jobs Act.

```
git diff --name-only --diff-filter=A pre-tcja..post-tcja
```
