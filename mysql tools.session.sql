drop table if exists StudentInfo, AcademicFactors, StressIndicators;


CREATE TABLE StudentInfo (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    gender VARCHAR(10)
);

CREATE TABLE AcademicFactors (
    factor_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    academic_performance INT,
    study_load INT,
    future_career_concerns INT,
    FOREIGN KEY (student_id) REFERENCES StudentInfo(student_id)
);

CREATE TABLE StressIndicators (
    indicator_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    anxiety_level INT,
    self_esteem INT,
    depression INT,
    sleep_quality INT,
    social_support INT,
    peer_pressure INT,
    bullying INT,
    stress_level INT,
    FOREIGN KEY (student_id) REFERENCES StudentInfo(student_id)
);

INSERT INTO StudentInfo (name, age, gender) VALUES
('Alice', 20, 'Female'),
('Bob', 22, 'Male'),
('Charlie', 21, 'Male'),
('David', 23, 'Male'),
('Eva', 20, 'Female');

INSERT INTO AcademicFactors (student_id, academic_performance, study_load, future_career_concerns) VALUES
(1, 3, 2, 3),
(2, 1, 4, 5),
(3, 2, 3, 2),
(4, 2, 4, 4),
(5, 4, 3, 2);

INSERT INTO StressIndicators 
(student_id, anxiety_level, self_esteem, depression, sleep_quality, social_support, peer_pressure, bullying, stress_level) 
VALUES
(1, 14, 20, 11, 2, 2, 3, 2, 1),
(2, 15, 8, 15, 1, 1, 4, 5, 2),
(3, 12, 18, 14, 2, 2, 3, 2, 1),
(4, 16, 12, 15, 1, 1, 4, 5, 2),
(5, 16, 28, 7, 5, 1, 5, 5, 1);

select * from StudentInfo;
select * from AcademicFactors;
select * from StressIndicators;

-- Questions 

-- 1. Stress distribution (kitne students kis stress_level par hain)
select stress_level, count(*) as student_count
from StressIndicators
group by stress_level
order by stress_level;

-- 2. Average stress level by gender
select s.gender, avg(i.Stress_level) as avg_stree
from StudentInfo as s
join stressindicators as i on s.student_id = i.student_id
group by s.gender;

-- 3. Stress vs Academic performance
SELECT a.academic_performance, AVG(i.stress_level) AS avg_stress
FROM AcademicFactors a
JOIN StressIndicators i ON a.student_id = i.student_id
GROUP BY a.academic_performance
ORDER BY academic_performance;

-- 4. Top 3 factors highly associated with high stress
SELECT AVG(anxiety_level) AS avg_anxiety,
       AVG(depression) AS avg_depression,
       AVG(peer_pressure) AS avg_peer_pressure,
       AVG(bullying) AS avg_bullying
FROM StressIndicators
WHERE stress_level < 3;

-- 5. Correlation between study load and stress
SELECT a.study_load, AVG(i.stress_level) AS avg_stress
FROM AcademicFactors a
JOIN StressIndicators i ON a.student_id = i.student_id
GROUP BY a.study_load
ORDER BY a.study_load;

