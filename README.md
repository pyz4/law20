# Law 2.0 Spring 2019 Final Project - Peter Zhu
Title 26 of the United States Code before and after the TCJA

This repository holds several branches, each containing a version of the Internal Revenue Code. The branches and their descriptions are as follows:

- pre-tcja (Internal Revenue Code as of January 2018)
- post-tcja (Internal Revenue Code as of April 2019)

Each segment of the code (i.e. section, subsection, paragraph, subparagraph, clause, subclause) are stored as individual directories.

You can leverage `git` to find changes and differences between these two versions of the Code. For example, the following command will show you all new provisions added as a result of the Tax Cut and Jobs Act.

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
t26/s1/j/2/A/content
t26/s1/j/2/A/heading
t26/s1/j/2/B/content
t26/s1/j/2/B/heading
t26/s1/j/2/C/content
t26/s1/j/2/C/heading
t26/s1/j/2/D/content
t26/s1/j/2/D/heading
t26/s1/j/2/E/content
t26/s1/j/2/E/heading
t26/s1/j/2/F/content
t26/s1/j/2/F/heading
t26/s1/j/2/heading
t26/s1/j/3/A/content
t26/s1/j/3/A/heading
t26/s1/j/3/B/chapeau
t26/s1/j/3/B/heading
t26/s1/j/3/B/i/content
t26/s1/j/3/B/ii/content
t26/s1/j/3/B/iii/content
t26/s1/j/3/heading
t26/s1/j/4/A/content
t26/s1/j/4/A/heading
t26/s1/j/4/B/chapeau
t26/s1/j/4/B/heading
t26/s1/j/4/B/i/I/content
t26/s1/j/4/B/i/II/content
t26/s1/j/4/B/i/chapeau
t26/s1/j/4/B/i/heading
t26/s1/j/4/B/ii/I/content
t26/s1/j/4/B/ii/II/content
t26/s1/j/4/B/ii/chapeau
t26/s1/j/4/B/ii/heading
t26/s1/j/4/B/iii/I/content
t26/s1/j/4/B/iii/II/content
t26/s1/j/4/B/iii/chapeau
t26/s1/j/4/B/iii/heading
t26/s1/j/4/C/chapeau
t26/s1/j/4/C/heading
t26/s1/j/4/C/i/I/content
t26/s1/j/4/C/i/II/content
t26/s1/j/4/C/i/chapeau
...
```
