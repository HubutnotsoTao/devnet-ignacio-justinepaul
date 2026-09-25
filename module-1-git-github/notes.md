# Module 1 — Git & GitHub

**Student:** Ignacio, Justine Paul T.
**Date:** 9-26-2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

Git is the tool and GitHub is the platform. Git allows you to create changes and see the differences with the current project, stage them by using "add", and leave notes via "commit" before making it a part of the actual product by using "push". Git gives you the option to create "branches" that creates an isolated version of your project where you can apply experimental features before applying it to the main product of the project. GitHub is the platform that showcases the actual project, it acts as the house that allows developers and users to explore the project being developed.

---

## Key vocabulary (in your own words)

- repository: repositories are the containers for your project, it has a copy of every push made, and access to it is configured by the owner. 
- commit: this allows the developers to add messages before applying the changes to the actual project.
- branch: a separate part of the main project within the same repository that isolates changes made to it allowing for development in multiple branches without affecting the main branch unless intended.
- push / pull: push applies the commited changes to the target branch and pull retrieves the latest version of the target branch.
- pull request: pull requests are changes the other developers are requesting to be made in a repository that is owned by another developer.
- merge conflict: merge conflicts are differences between branches that need to be resolved through rebasing before merging two branches.

---

## Walking through what I did

[Describe, step by step, a real branch → commit → push → PR you did. Include the actual commands you used.]
First, I added the changes I made the the main branch. Second, I committed the files I added to the staging area and added a message. Third, I pushed the committed changes. Lastly, I verified that the changes have been reflected in the remote repository.

```
# paste your actual commands here
```
git add .
git commit -m "Updated READme and added initial py file"
git push

---

## A mistake I made (or one I want to avoid)

I once tried to merge "jeremiah" branch with "justine" branch while the "jeremiah" branch had an older version of the main project file, I had to resolve the merge conflict through rebasing and deciding what to keep before being able to merge the two branches.

---

## How this connects to something else

Version control allows the developers to track changes made over the span of the project.
