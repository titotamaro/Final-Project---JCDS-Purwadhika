# Final-Project

Dataset Source: https://www.kaggle.com/c/GiveMeSomeCredit

Final Project Title: Personal Loan Default Risk Management with Credit Scoring

<h2>Problems:</h2>
1. Pemberian credit pada customer selalu memberikan potensi resiko bagi bank, dibutuhkan pemodelan dengan tingkat akurasi yang tinggi agar diperoleh resiko sekecil-kecilnya<br>
2. Dibutuhkan tools yang dapat mengklasifikasi customer berdasarkan kemungkinan default-nya<br>
3. Identifikasi faktor-faktor yang paling mempengaruhi kemungkinan default pada customer<br>

<h2>Goals:</h2>
1. Pemodelan yang dapat memprediksi default dengan target AUC ROC > 0.84<br> 
2. Pengelompokkan customer berdasarkan default probability  menjadi 5 tingkatan yaitu poor, fair, good, very good dan exceptional (mirip dengan yang ada pada FICO score)<br>
3. Analisa setiap features pada dataset dan hubungannya dengan tingkat default customer<br> 

<h2>Conclusion:</h2>

1. Diperoleh pemodelan dengan AUC ROC sebesar 0.854 dengan tingkat precision 0.54, algoritma yang digunakan adalah XGBoost Classifier dengan Hyper Tuning dimana parameter yang digunakan adalah : <br>

- N_estimator : 1000 <br>
- Min_child_weight : 1 <br>
- Max depth : 10 <br>
- Learning Rate : 0.03162277660168379 <br>
2. Pengelompokkan data menjadi 5 kelompok resiko yaitu poor, fair, good, very good dan exceptional dengan interval probabilitas sebagai berikut :<br>

- Exceptional  	  (proba : 0 - 0.000561) 
- Very Good    	  (proba : 0.000561 - 0.248171)
- Good          	(proba : 0.248172 - 0.496342)
- Fair          	(proba : 0.496343 - 0.744513)
- Poor          	(proba : 0.744514 -1)

3. Customer yang mengalami default memiliki median RevolvingUtilizationOfUnsecuredlines sebesar 83%, sementara yang tidak mengalami default memiliki median RevolvingUtilizationOfUnsecuredlines sebesar 13.3%.<br>

4. Dari hasil pengelompokkan dapat dilihat bahwa kelompok usia 41-50 tahun paling banyak mengalami gagal bayar dengan persentase 19.1% terhadap keseluruhan data <br>

5. Kelompok customer dengan nilai NumberOfTime30-59DaysPastDueNotWorse 0-3 merupakan yang paling banyak mengalami default<br>

6. Kelompok customer dengan nilai DebtRatio 0-2 merupakan kelompok customer yang paling banyak mengalami gagal bayar yaitu sebanyak 5.5% dari keseluruhan data<br>

7. Kelompok customer dengan NumberOfOpenCreditLinesAndLoans 0-10 memiliki jumlah default paling banyak yaitu 5.1%<br>

8. Setelah dikelompokkan, customer dengan nilai NT90 0-3 memiliki jumlah default paling banyak yaitu 6.4%<br>

9. Setelah pengelompokkan customer dengan nilai NRELL 0-10 memiiki jumlah customer yang paling banyak mengalami default yaitu 6.67%<br>

10. Pada features ini kelompok customer dengan nilai NT6089 0-3 yang memiliki jumlah default paling banyak yaitu sebesar 6.5%<br>

11. Kelompok customer dengan nilai ND 0-5 memiliki jumlah default paling banyak yaitu 6.7%.<br>

12. Korelasi positif terkuat terhadap target terdapat pada features NumberOfTime30-59DaysPastDueNotWorse yaitu sebesar 0.13. Selain itu kekuatan korelasi yang sama ditemukan juga pada features NumberOfTimes90DaysLate sebesar 0.12 dan NumberOfTime60-89DaysPastDueNotWorse sebesar 1. Dari hal ini dapat disimpulkan bahwa adanya keterlambatan pembayaran kredit memiliki korelasi yang kuat dengan customer yang default<br>

13. Korelasi negatif terkuat terhadap terget terdapat pada features age yaitu sebesar -0.12. Hal ini menandakan bahwa semakin besar usia seorang customer maka semakin jumlahnya yang mengalami default<br>
