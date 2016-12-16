# Bioinformatics D3 Visualizations

# Background
Data-Driven Prediction of Drug Effects and Interactions (by Prof Tatonetti et al)
http://stm.sciencemag.org/content/4/125/125ra31

We also present a comprehensive database of drug effects (OFFSIDES) and a database of drug-drug interaction side effects (TWOSIDES). To demonstrate the biological use of these new resources, we used them to identify drug targets, predict drug indications, and discover drug class interactions. We then corroborated 47 (P < 0.0001) of the drug class interactions using an independent analysis of electronic medical records. Our analysis suggests that combined treatment with selective serotonin reuptake inhibitors and thiazides is associated with significantly increased incidence of prolonged QT intervals. 

We conclude that confounding effects from covariates in observational clinical data can be controlled in data analyses and thus improve the detection and prediction of adverse drug effects and interactions.


# Graphs

## Force-Directed
This is a graph of nodes that links drugs and reactions.  Multiple drugs can share similar reactions, graphically showing intersection relationships among drug reactions.

### Data-set
This graph uses the off-sides dataset.  We have four different views based on the number of data points we started with.  After our filtering and sanitization, the amount of good data points are significantly fewer than what we started with.  We used datasets that originally had 1,500, 2,000, 5,000, and 10,000 points.

## Adjacency-Matrix
This graph uses the two-sides dataset.  This graph shows drug-drug-effect relationships, where the rows and columns are both organized by ATC values.  

# Data Sources

## Offsides
Drug side effects were mined from publicly available data. Offsides is a database of drug side-effects that were found, but are not listed on the official FDA label.
Links drugs to adverse reactions

## Twosides
Drug interactions were mined from publicly available sources. Twosides is the only comprehensive database drug-drug-effect relationships.

## Download link
http://tatonettilab.org/resources.html

## Running Server
binf-visualizations.herokuapp.com/