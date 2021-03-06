**Abstract:-** Wearable devices have gained immense popularity among various pervasive computing and Internet-of-Things (IoT) applications in the past decade. Sports analytics researchers recently focused on improving a player's performance to help devise a winning strategy based on the player's gameplay. Especially in a racquet-based badminton sport, it is assumed that handling the racquet during the gameplay is one of the primary reasons to influence the players' performance. On the contrary, we posit that the players' stance, body movements, and posture are equally significant in evaluating a player's performance during the game. A shot characterized by a recommended posture, stance, and body movements allows a player to play a stroke efficiently, thus aiding the player in guiding the shuttle to strategic spots and making it difficult for the opponent to return the shot and score a point. Relying on this hypothesis, we propose DeCoach, a data-driven framework that leverages the stance and posture of the players and ranks them based on their performances. In this effort, we first employ a deep learning-based algorithm to classify the strokes and stances of the players. Secondly, we propose a distance-based methodology to compare the obtained stance of a player with that of a professional player. Finally, we devise a deep learning-based regressor to predict the player's performance which commences with ranking based on their performance. We evaluate DeCoach using our in-house dataset, Badminton Activity Recognition (BAR) Dataset that is collected using inertial measurement unit (IMU) sensors by placing them on the upper and lower limbs of the players. The BAR dataset is collected from 11 players in the controlled and uncontrolled environment settings for 12 frequently played shots in the game. Empirical results indicate that DeCoach achieves 89.09% accuracy for strokes detection and r-squared score of 88.84% in estimating the players' performance.

**Overall Pipeline:-**

![Overall_flowchart](https://user-images.githubusercontent.com/41083383/167263910-0b694ac5-e0e5-4d1a-88b5-83a8de777112.png)
We exhibit and discuss the overall architecture of the DeCoach Framework. The above figure depicts the overview of the proposed framework, and each module of the overall framework. We categorize the proposed framework into four main modules: stroke classification, error learning for stance retrieval, error metrics computing and score prediction. Since badminton involves coordinated movements and both upper and lower limbs, it is essential to capture the movements of all the limbs. First, we collected the data from 4 and 7 participants in controlled and uncontrolled environment settings, respectively. The first component of the proposed work involves using the wearables in the upper limb to train a classifier where we aim to predict the stroke played by the player. Once the player's stroke is determined, we use the stroke information to determine the possible ways in which a player could use their lower limbs to execute the shot. We propose a distance-based error metrics module to extract such possible stances to address this problem. The second component of this proposed work addresses instance-based template matching for ideal stance learning. Finally, we compare the ideal stances learned using the professional player's data with other participants. Furthermore, we believe that the error learned here between the professional player and other players can be used for scoring. We investigated various error metrics that can be useful to determine players' performance based on the professional player's performance and can be used as a good representation of the error made by the player. We employed feature selection on the various error metrics obtained to eliminate correlated error metrics. The new feature space of uncorrelated error metrics will refer to as an error matrix. Consequently, we propose a deep learning-based regressor convolution neural network (CNNs) to predict an overall score based on their performance. Besides, we also demonstrate the robustness of the proposed methodology by introducing another professional player's data.


**Classification Module:-**
We design a time-based decay learning rate CNNs-based classifier, for recognizing 12 different types of badminton strokes. We implemented and compared several traditional machine learning algorithms such as random forest, multilayer perceptron, decision tree and support vector machine. Furthermore, the proposed deep learning-based classifier comprises two components. First is the feature extraction component, followed by the classification component. The feature extraction component is responsible for hierarchically extracting high-level features from the raw data. We employed CNNs layers followed by max-pooling layers for the feature representation learning and followed by a softmax layer responsible for classifying the strokes. Each convolution layer 1D comprises the following operations in the sequence mentioned: convolution, rectilinear activation function, dropout and time-based decay learning rate schedule (where scaling factor = 1) shown below: 

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; <img width="400" alt="Screen Shot 2022-05-07 at 1 19 58 PM" src="https://user-images.githubusercontent.com/41083383/167264978-a94aed93-de62-4dd3-a3c7-e37d7f032841.png">

**Error Learning for Stance Retrieval Module:-**
To compute the ideal stance that the participant players could play, we leverage the lower limb data of the professional. We compute the euclidean distance between each player and the professional player where X<sub>p</sub> represent the professional player, and X<sub>L</sub> represents participant player leg data. The motivation behind employing the euclidean distance metric as it shows better results for instance-based learning across a vast range of problems. We extracted k closest data instances from the professional's data for each player data instance. Moreover, to extract k closest data instances, we employed the broadcasting function for arithmetic operations. The broadcasting function's advantage is handling different dataset size problems while performing arithmetic operations. We further performed synchronous averaging of the k retrieved data instances. The notion is that performing synchronous averaging causes a filtering effect on the retrieved k stances of the professional and removes the noise, leaving behind the ideal stance's core pattern. During the retrieval of k instances, the labels of the professional's and the intermediate/novice player's data were matched. By employing distance-based approach, we obtained the newly predicted values where X<sub>k</sub>  represent the synchronous averaging of the participant player data. Finally, we hypothesize that the obtained pattern is the ideal stance for playing any stroke based on the stance is retrieved from the professional's data.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<img width="400" alt="Screen Shot 2022-05-07 at 1 33 11 PM" src="https://user-images.githubusercontent.com/41083383/167265397-c086f370-542a-4d06-84fb-1ad88e76d07b.png">


**Error Computing Module:-**
Following the computation of the ideal stance for each shot played by the participant players, we compute the error metrics. The detailed explanation of each error metric along with the mathematical equations. To obtain the error metrics for each activity, we preserve the labels and compute the error respective to the activities by implementing standard matrix operations on the resulting data from the distance-based model described in section. Our experiment extracted the closest k instances from professional players to other participants discussed in the above section. By performing distance-based, we obtained the newly predicted values. For learning the error between the newly predicted values and actual data, we calculated 13 error metrics and mathematical notations shown in the below papers. Lastly, we plotted the probability density function plots for each stroke considered in the study to measure the error during the data sessions. 

Let E<sub>t</sub> represent the error between the actual participant data X<sub>L</sub> and newly predicted values X<sub>k</sub>. Error Metrics (EM) represents the handcrafted error metrics matrix shown below, where n represent number of data instances.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<img width="300" alt="Screen Shot 2022-05-07 at 1 38 39 PM" src="https://user-images.githubusercontent.com/41083383/167265709-ca65bb14-4092-484f-908a-8b16ed58e1d6.png">

**Score Prediction Module:-**
![Reg](https://user-images.githubusercontent.com/41083383/167265851-58e3ca5d-a191-4b3c-bf13-985ba7a60c97.png)
We design a convolution neural network (CNNs)-based regressor shown in the above figure to predict each participant's score for the handcrafted error vector features. Further, we assigned handcrafted scores to each stroke played by the participants'. We define the handcrafted score as referring to the ideal stance. The motivation behind developing a deep regressor convolution neural network (CNNs) is that the ability to extract high-level features from input feature space hierarchically gives a cutting-edge advantage over the traditional regression algorithms. This motivated us to design an automated deep score predictor pipeline. Our deep regressor model comprises three main components. The first component is the handcrafted computed error metrics used as the input feature space, followed by the dimensionality reduction block, which helped us to extract the most uncorrelated error features with a correlation (greater than 0.90) to obtain better feature representation from the input data. The third component is the deep feature extraction layers, comprising two 1D convolution layers (responsible for hierarchically extracting high-level features from the input space), followed by a flattened layer to reduce the features' dimensionality. Furthermore, the regression component consists of one fully connected layer, followed by the regressor layer consisting of 1 neuron as the output layer.

Let f<sub>i</sub>, y, E<sub>t</sub>, f<sub>i</sub>(E<sub>t</sub>) and Y represents feature selection correlation score, activities, error, score associated with each error metric and kernel size explained in below equation, respectively. 

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<img width="400" alt="Screen Shot 2022-05-07 at 1 49 56 PM" src="https://user-images.githubusercontent.com/41083383/167265938-71d27e05-5d1e-4452-a91f-751660ac4fad.png">


**Instructions and Installation:-** 

This repo was tested with Ubuntu 20.04, Python 3.8.10 and CUDA 11.2

To use the Src codes folder, please follow the steps below-

a) To extract csv files from gzip folder, please use the Extract_gzip_to_csv_files.py file.

**Preprocessing Steps:-**  

Please use the Pre-processing.ipynb notebook. First you need to provide the correct **path** of all the extracted csv files. The notebook constitute normalization of the raw data (Normalize.py) and sliding windowing steps (windowfunction.py). The sliding window function perform and give three outputs - the windowed segment (size of the segment depends on the window size and overlap parameters), the acticity labels and average handcrafted scores of each segment. We would encourage you to save all the preprocessed csv files for each participant's limbs separately.

**Classification Module:-**  
Shallow_Classification_Algorithms_Baseline.ipynb and Classification_Pipeline_Module.ipynb notebooks constitutes reading the raw csv for each participant and corresponding all the limbs by using Raw_Data_Read.py file. You will find various shallow classification algorithms used in this study in the Shallow_Classification_Algorithms_Baseline.ipynb notebook. The Classification_Pipeline_Module.ipynb notebook constitutes the proposed time-based decay learning rate CNNs-based classifier defined in the notebook.

**Error Learning for Stance Retrieval Module:-**  
Distance-based error learning Framework_Module.ipynb notebook constitutes KNN-based error estimation (DBEL.py) and handcrafted error computing (Errors.py). Lastly, you can visualize all the handcrafted errors as pdfs plot.    

**Score Prediction Module:-** 
Scoring_Pipeline.ipynb notebook constitutes the error selection (formula shown in Score Prediction Module) and bivarate correlation analysis on predicted vs handcrafted scores. The CNNs-based regressor is defined in Scoring.py file. To visualize the predicted vs handcrafted scores, please use violin plot function in Visualization.ipynb notebook.   

**Additional:-**
Provided t-SNE plot function to visualize the learned features representation and raw feature representation 2D space.

**BAR Dataset DOI**: https://dx.doi.org/10.21227/n1e0-7c60


**Please read and cite:-**

a) I. Ghosh, S. R. Ramamurthy and N. Roy, "StanceScorer: A Data Driven Approach to Score Badminton Player", 2020 IEEE International Conference on Pervasive Computing and Communications Workshops (PerCom Workshops), 2020, pp. 1-6, doi: 10.1109/PerComWorkshops48775.2020.9156220.

b) I. Ghosh, S. R. Ramamurthy, A Chakma and N. Roy, "DeCoach: Deep Learning-based Coaching for Badminton Player Assessment", 2022 Pervasive and Mobile Computing. **[To be Appear]**.

c) Indrajeet Ghosh, Sreenivasan Ramasamy Ramamurthy, Avijoy Chakma, Emon Dey, Zahid Hasan, Nirmalya Roy, July 23, 2020, "Badminton Activity Recognition (BAR)", IEEE Dataport, doi: https://dx.doi.org/10.21227/n1e0-7c60.

**License:-**
The current version of this repository is released under the GNU General Public License v3.0 unless otherwise stated. The authors of the repository retains their respective rights. The published paper and published dataset is governed by a separate license and the authors retain their respective rights.
 
**Acknowledgements:-**
This research is supported by NSF CAREER grant 1750936 and U.S. Army grant W911NF2120076

**Contact:-**
If you have any questions, please feel free to reach out over email via indrajeetghosh@umbc.edu
