# Predicting Best Picture Winners Nominees
### _Preliminary Findings_

*Based on a first regression of basic movie factors:*
 1. **Parental Guidance (MPAA) ratings** in general appear to be **poor (insignificant) predictors** of Best Picture success
 
 2. The **number of movies nominated in a given year** is a significant, but **weak predictor**
 
 3. **User ratings** show a clear (significant) trend towards **higher rated movies performing better**, but is also relatively **weak predictor** because not all highly rated movies are nominated
 
 ![Score by User Rating](https://github.com/sosier/Predicting_Best_Picture_Winners_Nominees/blob/master/img/score_by_user_rating.png?raw=true "Score by User Rating")

 4. **Movie runtime** also shows a **clear "sweet spot"** of suitable movie length for Best Picture success, but again is a fairly **weak predictor**
 
 ![Score by Runtime](https://github.com/sosier/Predicting_Best_Picture_Winners_Nominees/blob/master/img/score_by_runtime.png?raw=true "Score by Runtime")
 
 5. The key participants in the making of the movie, the **directors, actors, and actresses**, show the clearest impact and are the **most significant and useful predictors** of Best Picture success
 ![People matter!](https://github.com/sosier/Predicting_Best_Picture_Winners_Nominees/blob/master/img/avg_score_with_and_without.png?raw=true "People matter!")
 
 6. Finally, **genres** are by and large relativley **weak predictors** as well  

---

*Methodological Notes:*
 - Best Picture success is modeled with a _**Best Picture Status Score**_. A score of **5 indicates a nomination**, and a score of **10 indicates a win**
 - Data is from 1990 - 2014 (which is why George Lucas does not perform so well)
 
