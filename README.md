# Title: Search papers by author names
## Author: Xueli Pan
## City: Amsterdam
## Country: Netherlands


#### Video Demo:  <https://youtu.be/EmLQVUqLlQY>
#### This project aims at providing user with all publications of authors with a certain name. For example, if a student would like to apply for a PhD position, he/she would like to know about all publications by the professor of the corresponding research group. Given the professor's name, we could fetch the publications by authors with the same name through Semantic Search API. To distinguish different author with the same name, we catogorize different author by their authorID and print out their corresponding publications.
#### The input should be a name in string format, without digits and puncturation.
#### The first output is the total number of authors with the same name
#### Then output each author with their correspongding publication, for each publication, we list the paperID and title.
#### Semantic Scholar API introduction: The Semantic Scholar REST API allows you to find and explore scientific publication data about authors, papers, citations, venues, and more. The API is organized into the following services:Academic Graph: Provides data about authors, papers, citations, venues, SPECTER2 embeddings, and more that allows you to link directly to the corresponding page on semanticscholar.org for more information.Recommendations: Provides recommended papers similar to a given paper.Datasets: Provides downloadable links of datasets in the academic graph.Conference Peer Review: Provides utilities to help conference organizers with the problem of assigning reviewers to conference submissions. Includes detection of conflict of interest, based on co-author relationships, and computation of a matching score between a reviewer and a submission's topic, based on the reviewer's publication history.