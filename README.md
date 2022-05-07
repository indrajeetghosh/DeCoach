**Abstract**

Wearable devices have gained immense popularity among various pervasive computing and Internet-of-Things (IoT) applications in the past decade. Sports analytics researchers recently focused on improving a player's performance to help devise a winning strategy based on the player's gameplay. Especially in a racquet-based badminton sport, it is assumed that handling the racquet during the gameplay is one of the primary reasons to influence the players' performance. On the contrary, we posit that the players' stance, body movements, and posture are equally significant in evaluating a player's performance during the game. A shot characterized by a recommended posture, stance, and body movements allows a player to play a stroke efficiently, thus aiding the player in guiding the shuttle to strategic spots and making it difficult for the opponent to return the shot and score a point. Relying on this hypothesis, we propose DeCoach, a data-driven framework that leverages the stance and posture of the players and ranks them based on their performances. In this effort, we first employ a deep learning-based algorithm to classify the strokes and stances of the players. Secondly, we propose a distance-based methodology to compare the obtained stance of a player with that of a professional player. Finally, we devise a deep learning-based regressor to predict the player's performance which commences with ranking based on their performance. We evaluate DeCoach using our in-house dataset, Badminton Activity Recognition (BAR) Dataset that is collected using inertial measurement unit (IMU) sensors by placing them on the upper and lower limbs of the players. The BAR dataset is collected from 11 players in the controlled and uncontrolled environment settings for 12 frequently played shots in the game. Empirical results indicate that DeCoach achieves 89.09% accuracy for strokes detection and r-squared score of 88.84% in estimating the players' performance.

**Overall Pipeline**

![Overall_flowchart](https://user-images.githubusercontent.com/41083383/167263910-0b694ac5-e0e5-4d1a-88b5-83a8de777112.png)


**Classification Module**

![Classification](https://user-images.githubusercontent.com/41083383/167264731-48d8cc47-0225-4472-9804-d8d3eb00a668.png)

We design a convolution neural networks (CNNs)-based classifier, for recognizing 12 different types of badminton strokes. We implemented and compared several traditional machine learning algorithms such as random forest, multilayer perceptron, decision tree and support vector machine. Furthermore, the proposed deep learning-based classifier comprises two components. First is the feature extraction component, followed by the classification component. The feature extraction component is responsible for hierarchically extracting high-level features from the raw data. We employed CNNs layers followed by max-pooling layers for the feature representation learning and followed by a softmax layer responsible for classifying the strokes. Each convolution layer 1D comprises the following operations in the sequence mentioned: convolution, rectilinear activation function, dropout and time-based decay learning rate schedule (where scaling factor = 1) shown below: 

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; <img width="400" alt="Screen Shot 2022-05-07 at 1 19 58 PM" src="https://user-images.githubusercontent.com/41083383/167264978-a94aed93-de62-4dd3-a3c7-e37d7f032841.png">

**Error Learning for Stance Retrieval Module**

To compute the ideal stance that the participant players could play, we leverage the lower limb data of the professional. We compute the euclidean distance between each player and the professional player where X_p represent the professional player, and X_L represents participant player leg data. The motivation behind employing the euclidean distance metric as it shows better results for instance-based learning across a vast range of problems. We extracted k closest data instances from the professional's data for each player data instance. Moreover, to extract k closest data instances, we employed the broadcasting function for arithmetic operations. The broadcasting function's advantage is handling different dataset size problems while performing arithmetic operations. We further performed synchronous averaging of the k retrieved data instances. The notion is that performing synchronous averaging causes a filtering effect on the retrieved k stances of the professional and removes the noise, leaving behind the ideal stance's core pattern. During the retrieval of k instances, the labels of the professional's and the intermediate/novice player's data were matched. By employing distance-based approach, we obtained the newly predicted values where X_k represent the synchronous averaging of the participant player data. Finally, we hypothesize that the obtained pattern is the ideal stance for playing any stroke based on the stance is retrieved from the professional's data.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<img width="400" alt="Screen Shot 2022-05-07 at 1 33 11 PM" src="https://user-images.githubusercontent.com/41083383/167265397-c086f370-542a-4d06-84fb-1ad88e76d07b.png">


Following the computation of the ideal stance for each shot played by the participant players, we compute the error metrics. The detailed explanation of each error metric along with the mathematical equations. To obtain the error metrics for each activity, we preserve the labels and compute the error respective to the activities by implementing standard matrix operations on the resulting data from the distance-based model described in section. Our experiment extracted the closest k instances from professional players to other participants discussed in the above section. By performing distance-based, we obtained the newly predicted values. For learning the error between the newly predicted values and actual data, we calculated 13 error metrics and mathematical notations shown in the below papers. Lastly, we plotted the probability density function plots for each stroke considered in the study to measure the error during the data sessions. 

Let E_t represent the error between the actual participant data X_L and newly predicted values $X_k$. Error Metrics (EM) represents the handcrafted error metrics matrix shown below, where n represent number of data instances.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<img width="300" alt="Screen Shot 2022-05-07 at 1 38 39 PM" src="https://user-images.githubusercontent.com/41083383/167265709-ca65bb14-4092-484f-908a-8b16ed58e1d6.png">


Dataset Link/ DOI: https://dx.doi.org/10.21227/n1e0-7c60


Please cite:

a) I. Ghosh, S. R. Ramamurthy and N. Roy, "StanceScorer: A Data Driven Approach to Score Badminton Player," 2020 IEEE International Conference on Pervasive Computing and Communications Workshops (PerCom Workshops), 2020, pp. 1-6, doi: 10.1109/PerComWorkshops48775.2020.9156220.

b) Indrajeet Ghosh, Sreenivasan Ramasamy Ramamurthy, Avijoy Chakma, Emon Dey, Zahid Hasan, Nirmalya Roy, July 23, 2020, "Badminton Activity Recognition (BAR)", IEEE Dataport, doi: https://dx.doi.org/10.21227/n1e0-7c60.

License:

The current version of this repository is released under the GNU General Public License v3.0 unless otherwise stated. The authors of the repository retains their respective rights. The published paper and published dataset is governed by a separate license and the authors retain their respective rights.
