**Abstract**

Wearable devices have gained immense popularity among various pervasive computing and Internet-of-Things (IoT) applications in the past decade. Sports analytics researchers recently focused on improving a player's performance to help devise a winning strategy based on the player's gameplay. Especially in a racquet-based badminton sport, it is assumed that handling the racquet during the gameplay is one of the primary reasons to influence the players' performance. On the contrary, we posit that the players' stance, body movements, and posture are equally significant in evaluating a player's performance during the game. A shot characterized by a recommended posture, stance, and body movements allows a player to play a stroke efficiently, thus aiding the player in guiding the shuttle to strategic spots and making it difficult for the opponent to return the shot and score a point. Relying on this hypothesis, we propose DeCoach, a data-driven framework that leverages the stance and posture of the players and ranks them based on their performances. In this effort, we first employ a deep learning-based algorithm to classify the strokes and stances of the players. Secondly, we propose a distance-based methodology to compare the obtained stance of a player with that of a professional player. Finally, we devise a deep learning-based regressor to predict the player's performance which commences with ranking based on their performance. We evaluate DeCoach using our in-house dataset, Badminton Activity Recognition (BAR) Dataset that is collected using inertial measurement unit (IMU) sensors by placing them on the upper and lower limbs of the players. The BAR dataset is collected from 11 players in the controlled and uncontrolled environment settings for 12 frequently played shots in the game. Empirical results indicate that DeCoach achieves 89.09% accuracy for strokes detection and R**^2** score of 88.84% in estimating the players' performance.


Dataset Link/ DOI: https://dx.doi.org/10.21227/n1e0-7c60


Please cite:

a) I. Ghosh, S. R. Ramamurthy and N. Roy, "StanceScorer: A Data Driven Approach to Score Badminton Player," 2020 IEEE International Conference on Pervasive Computing and Communications Workshops (PerCom Workshops), 2020, pp. 1-6, doi: 10.1109/PerComWorkshops48775.2020.9156220.

b) Indrajeet Ghosh, Sreenivasan Ramasamy Ramamurthy, Avijoy Chakma, Emon Dey, Zahid Hasan, Nirmalya Roy, July 23, 2020, "Badminton Activity Recognition (BAR)", IEEE Dataport, doi: https://dx.doi.org/10.21227/n1e0-7c60.

License:

The current version of this repository is released under the GNU General Public License v3.0 unless otherwise stated. The authors of the repository retains their respective rights. The published paper and published dataset is governed by a separate license and the authors retain their respective rights.
