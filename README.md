Wearable devices have gained immense popularity among various pervasive computing and Internet-of-
Things (IoT) applications in the past decade, including sports analytics. Sports analytics researchers re-
cently focused on improving a player’s performance to help devise a winning strategy based on the player’s
gameplay. Especially in a racquet-based sport, it is assumed that handling of the racquet during the game-
play is one of the primary reasons to influence the players’ performance. On the contrary, we posit that the
players’ stance, body movements, and posture are equally significant in evaluating a players’ performance
during the gameplay. A shot characterized by a perfect posture, stance, and body movements allows a player
to play a stroke efficiently, thus aiding the player in directing the shuttle to strategic spots and making it
difficult for the opponent to return the shot and score a point. Relying on this hypothesis, we propose
DeCoach, a data-driven framework that leverages the stance and posture of a player and ranks them based
on their performances in badminton sports. In this effort, we first employ a deep learning-based algorithm to
classify the strokes and stances of the players. Next, we propose a distance-based methodology to compare
the obtained stance of a player (novice and intermediate) with that of a professional player. Finally, we
devise a deep learning-based regressor to predict the performance of a shot which commence to rank the
players and assess the player’s performance. We evaluate DeCoach using an in-house dataset, Badminton
Activity Recognition Dataset (BAR) that was collected using inertial measurement units (IMU) wearable
sensors by placing them on both upper and lower limbs of the players. The BAR dataset was collected from
11 players in controlled and uncontrolled environment settings for 12 frequently played shots considered.
Empirical results indicate that DeCoach achieves 89.09% accuracy for strokes classification and an R2 value
for 88.84% in predicting the performance of a player.


Dataset Link/ DOI: https://dx.doi.org/10.21227/n1e0-7c60


Please cite:

a) I. Ghosh, S. R. Ramamurthy and N. Roy, "StanceScorer: A Data Driven Approach to Score Badminton Player," 2020 IEEE International Conference on Pervasive Computing and Communications Workshops (PerCom Workshops), 2020, pp. 1-6, doi: 10.1109/PerComWorkshops48775.2020.9156220.

b) Indrajeet Ghosh, Sreenivasan Ramasamy Ramamurthy, Avijoy Chakma, Emon Dey, Zahid Hasan, Nirmalya Roy, July 23, 2020, "Badminton Activity Recognition (BAR)", IEEE Dataport, doi: https://dx.doi.org/10.21227/n1e0-7c60.

License:

The current version of this repository is released under the GNU General Public License v3.0 unless otherwise stated. The authors of the repository retains their respective rights. The published paper and published dataset is governed by a separate license and the authors retain their respective rights.
