from django.db import models
from django.contrib.auth.models import User

# table format source data
from djangotailoring.models import SubjectData

# Create your models here.

# python ../manage.py makemtsmodel > MODEL.OUT (results go below here)

INT_PROBLEMSOLVINGSTEPS_CHOICES = (
    ('0', "I don't struggle with any of them."),
    ('1', 'I struggle with correctly identifying the problem.'),
    ('2', 'I struggle with figuring out what the most important pieces of information are in the problem.'),
    ('3', "I struggle with finding examples that are similar to the paroblem that I'm working on."),
    ('4', "I struggle with determining how the problem I'm working on differs from example problems."),
    ('5', 'I struggle with determining which equation I should be using to solve the problem.'),
    ('6', 'I struggle with using the equation correctly.'),
    ('7', 'I struggle with effectively double-checking my solution.'),
    ('99', 'I struggle with all the steps.'),
)

TEXT_SLC_INTEREST_CHOICES = (
    ('Signed_Up', "Yes, I'm already signed up."),
    ('Yes_Not_Signed_Up', 'Yes, but I have not signed up yet.'),
    ('Not_Interested', "No, I'm not interested."),
    ('IDK', "What's the Science Learning Center?"),
)

CTEXT_CLASS_STANDING_CHOICES = (
    ('Freshman', 'Freshman'),
    ('Sophomore', 'Sophomore'),
    ('Junior', 'Junior'),
    ('Senior', 'Senior'),
)

TEXT_PROBLEMTOPIC_140_CHOICES = (
    ('none', "I don't struggle with any of them"),
    ('vectors', 'vectors'),
    ('straightline', 'straight line motion'),
    ('2D', '2D and 3D motion'),
    ('circular', 'circular motion'),
    ('relative', 'relative motion'),
    ('Newtonlaws', "Newton's laws"),
    ('applyingnewton', "applying Newton's laws"),
    ('everything', 'I struggle with everything'),
)

INT_GOAL_GRADE_CHOICES = (
    ('8', 'A'),
    ('7', 'A-'),
    ('6', 'B+'),
    ('5', 'B'),
    ('4', 'B-'),
    ('3', 'C+'),
    ('2', 'C'),
    ('1', 'C- or below'),
)

TEXT_PTPREVIOUSSTUDY_CHOICES = (
    ('none', "I haven't"),
    ('lecturenotes', 'I have read over some of the lecture notes'),
    ('lecturevideos', 'I have watched some of the lecture videos'),
    ('readbook', 'I have read over some of the book'),
    ('bookprobs', 'I have worked through some of the problems from the book'),
    ('masteringphysics', 'I have reviewed and/or reworked some of the mastering physics problems'),
    ('officehours', 'I have gone to office hours'),
    ('physicshelproom', 'I have gone to the physics help room'),
    ('studygroup', 'I have gone to a study group'),
    ('problemroulette', 'I have used problem roulette'),
    ('practiceexam', 'I have solved some of the problems from the practice exams'),
    ('outsideresource', 'I have used resources outside of the course'),
)

INT_HS_MATH_CHOICES = (
    ('1', 'Algebra'),
    ('2', 'Geometry'),
    ('3', 'Precalc/Analysis'),
    ('4', 'Non-AP Calculus'),
    ('5', 'AP Calculus AB'),
    ('6', 'AP Calculus BC'),
    ('7', 'The equivalent of Math 115 (Calc 1) at a College/University'),
    ('8', 'The equivalent of Math 116 (Calc 2) at a College/University'),
    ('9', 'The equivalent of Math 215 (Calc 3: Multivariable Calculus) at a College/University'),
    ('10', 'The equivalent of Math 216 (Calc 4: Differential Equations) at a College/University'),
    ('0', 'Other'),
)

TEXT_PROBLEMTOPIC_235_CHOICES = (
    ('none', "I don't struggle with any of them."),
    ('coulombslaw', "Coulomb's Law"),
    ('conductors', 'conductors'),
    ('insulators', 'insulators'),
    ('electricfield', 'electric fields'),
    ('electricpotentialenergy', 'electric potential energy'),
    ('electricpotential', 'electric potential'),
    ('capacitors', 'capacitors and dielectrics'),
    ('current', 'current and current density'),
    ('resistance', 'resistance and resistivity'),
    ('energypower', 'energy and power in circuits'),
    ('parallelvsseries', 'resistors in series and parallel'),
    ('Kirchoffsrules', "Kirchoff's rules"),
    ('transientsincircuits', 'transients in circuits'),
    ('RCtime', 'RC time'),
    ('biological', 'biological applications'),
    ('everything', 'I struggle with everything'),
)

INT_SAT_MATH_CHOICES = (
    ('0', 'I did not take the SAT'),
    ('-99', 'I do not remember my SAT math score'),
    ('400', '400 or below'),
    ('410', '410'),
    ('420', '420'),
    ('430', '430'),
    ('440', '440'),
    ('450', '450'),
    ('460', '460'),
    ('470', '470'),
    ('480', '480'),
    ('490', '490'),
    ('500', '500'),
    ('510', '510'),
    ('520', '520'),
    ('530', '530'),
    ('540', '540'),
    ('550', '550'),
    ('560', '560'),
    ('570', '570'),
    ('580', '580'),
    ('590', '590'),
    ('600', '600'),
    ('610', '610'),
    ('620', '620'),
    ('630', '630'),
    ('640', '640'),
    ('650', '650'),
    ('660', '660'),
    ('670', '670'),
    ('680', '680'),
    ('690', '690'),
    ('700', '700'),
    ('710', '710'),
    ('720', '720'),
    ('730', '730'),
    ('740', '740'),
    ('750', '750'),
    ('760', '760'),
    ('770', '770'),
    ('780', '780'),
    ('790', '790'),
    ('800', '800'),
)

CTEXT_COLLEGE_CHOICES = (
    ('LSA', 'LSA'),
    ('Engineering', 'Engineering'),
    ('Kinesiology', 'Kinesiology'),
    ('Other', 'Other'),
)

INT_PAST_PHYSICS_EXPERIENCE_CHOICES = (
    ('2', 'Positive'),
    ('0', 'Neutral'),
    ('-2', 'Negative'),
)

OPT_OUT_CHOICES = (
    ('0', 'Opt in'),
    ('1', 'Opt out'),
)

CTEXT_GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

INT_ATTITUDE_MATH_CHOICES = (
    ('2', 'yes'),
    ('0', 'maybe, but I wish there was a math review'),
    ('-2', 'no'),
)

TEXT_PROBLEMTOPIC_135_CHOICES = (
    ('none', "I don't struggle with any of them"),
    ('vectors', 'vectors'),
    ('displacement', 'displacement'),
    ('force', 'force'),
    ('velocity', 'velocity'),
    ('Newtonslaws', "Newton's Laws and Forces"),
    ('friction', 'friction'),
    ('freebodydiagram', 'free body diagram'),
    ('tension', 'tension'),
    ('forcetransmission', 'force transmission'),
    ('simplemachines', 'simple machines'),
    ('torque', 'torque'),
    ('rotationalequil', 'rotational equilibrium'),
    ('stressstrain', 'stress and strain'),
    ('posvelacc', 'position, velocity, and acceleration'),
    ('everything', 'I struggle with everything'),
)

CINT_SEMSESTERS_COMPLETED_CHOICES = (
    ('9', 'More than 8 semesters'),
)

CTEXT_COLLEGE_CONCENTRATE_CHOICES = (
    ('Engineering', 'Engineering'),
    ('Physics', 'Physics/Astrophysics'),
    ('Chemistry', 'Chemistry'),
    ('Biology', 'Biology'),
    ('Biology_MCDB', 'Biology MCDB'),
    ('Biology_EEB', 'Biology EEB'),
    ('Health', 'Health-related Field (Physical Therapy, Pharmacology, Nursing, etc.)'),
    ('Humanities', 'Humanities'),
    ('Math', 'Mathematics'),
    ('Stats', 'Statistics'),
    ('Neurosci', 'Neuroscience'),
    ('Social_Science_not_Psych', 'Social Science (excluding Psychology)'),
    ('Psych_BBCS', 'Psychology or BBCS'),
    ('Education', 'Education'),
    ('IDK', 'I do not know'),
    ('Other', 'Other'),
)

CTEXT_POST_COLLEGE_CHOICES = (
    ('Employment', 'Employment'),
    ('Med_School', 'Medical School or other Health-related Professional School'),
    ('Dent_School', 'Dental School'),
    ('Education', 'Education (teaching, policy, or a certification program)'),
    ('Grad_Life_Sci', 'Graduate School in a Life Science discipline'),
    ('Grad_Other', 'Graduate School in another discipline'),
    ('IDK', "Unsure/I don't know"),
    ('Other', 'Other'),
)

TEXT_HS_ACTIVITY_CHOICES = (
    ('Music', 'Music'),
    ('Sports', 'Sports'),
    ('Theater', 'Theater'),
    ('None', 'None of the above'),
)

INT_PAST_PHYSICS_CHOICES = (
    ('7', "I've taken physics at U of M"),
    ('6', "I've taken an online physics course at a different university"),
    ('5', "I've taken physics at a community college"),
    ('4', 'AP Physics C'),
    ('3', 'AP Physics B'),
    ('2', 'Honors High School Physics'),
    ('1', 'High School Physics'),
    ('0', 'I have never taken a physics class'),
)

INT_ACT_MATH_CHOICES = (
    ('0', 'I did not take the ACT'),
    ('-99', 'I do not remember my ACT math score'),
    ('15', '15 or below'),
)

INT_YES_NO_CHOICES = (
    ('1', 'yes'),
    ('0', 'no'),
)

TEXT_LEARNER_CHOICES = (
    ('auditory', 'I learn best when I hear the information (as I do in lecture or when a friend explains it).  I digest information best by talking.'),
    ('diagram', "I learn best when there's a picture or diagram involved.  I digest information best by creating a visual representation."),
    ('text', "I learn best when there's a written description for me to read.  I digest information best by writing."),
    ('none', "I'm not really a particular type of learner."),
)

TEXT_MOVIE_CHOICES = (
    ('StarWars', 'Star Wars (ep. 4-6 with references to 1-3)'),
    ('StarTrek', 'Star Trek (J.J. Abrams movies with references to previous shows and movies)'),
    ('LOTR', 'Lord of the Rings (Trilogy with references to "The Hobbit")'),
    ('Harry', 'Harry Potter (All movies)'),
    ('no', "I don't like any of these movies"),
    ('none', 'I have not seen any of these movies'),
)

TEXT_PHYSICSHELPROOMREASON_CHOICES = (
    ('OH', 'Office Hours'),
    ('tutors', 'Help from the Physics Help Room staff (learning assistants, graduate students, etc)'),
    ('teamwork', 'Work with others'),
    ('other', 'Other'),
)

INT_CONFIDENCE_CHOICES = (
    ('4', 'Very confident'),
    ('3', 'Confident'),
    ('2', 'Somewhat confident'),
    ('1', 'Not confident'),
)

TEXT_REASON_CHOICES = (
    ('Physics_req', 'I am considering majoring in physics.'),
    ('Concentration_req', 'This physics course is required by my major.'),
    ('Grad_req', 'I need to take physics to prepare for my graduate/professional program.'),
    ('NS_Credit', 'For Natural Science credit.'),
    ('Interest', "I'm taking this class because of my interest in physics."),
)

TEXT_PARTNER_CHOICES = (
    ('Perfect_Partner', 'Yes, I have a perfect study partner.'),
    ('Know_Like_To', "I know someone and I'd like to study with them."),
    ('Know_Alone', "I know someone, but I'd like to study alone."),
    ('No', "No, I don't know anyone in this course."),
)

CINT_GPA_CHOICES = (
    ('20', '2.0 or lower'),
    ('21', '2.1'),
    ('22', '2.2'),
    ('23', '2.3'),
    ('24', '2.4'),
    ('25', '2.5'),
    ('26', '2.6'),
    ('27', '2.7'),
    ('28', '2.8'),
    ('29', '2.9'),
    ('30', '3.0'),
    ('31', '3.1'),
    ('32', '3.2'),
    ('33', '3.3'),
    ('34', '3.4'),
    ('35', '3.5'),
    ('36', '3.6'),
    ('37', '3.7'),
    ('38', '3.8'),
    ('39', '3.9'),
    ('40', '4.0'),
)

CTEXT_EMPLOYMENT_STATUS_CHOICES = (
    ('No_Job', 'I do not have a job'),
    ('Part_Time', 'I work a part-time job (20 hours or less a week)'),
    ('Full_Time', 'I work a full-time job (more than 20 hours a week)'),
)

CTEXT_YES_NO_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

INT_ATTITUDE_EXAMS_CHOICES = (
    ('1', 'yes'),
    ('0', 'no'),
)

CTEXT_INVOLVED_IN_CHOICES = (
    ('Greek', 'Greek Life (Sororities/Fraternities)'),
    ('Sports', 'Sports/Club Sports'),
    ('Religious', 'Religious Organizations'),
    ('Research', 'Research (Thesis, UROP, Lab work)'),
    ('Volunteering', 'Volunteering'),
    ('Music_Art', 'Music/Art'),
    ('Other', 'Other Student Clubs/Organzations'),
)

TEXT_PROBLEMTOPIC_240_CHOICES = (
    ('none', "I don't struggle with any of them."),
    ('coulombslaw', "Coulomb's Law"),
    ('electricfield', 'electric fields'),
    ('fieldlines', 'field lines and dipoles'),
    ('fluxgauss', "flux and Gauss's law"),
    ('applicationsGauss', "applications of Gauss's law"),
    ('electricpotential', 'electric potential'),
    ('capacitance', 'capacitance'),
    ('fieldenergy', 'field energy and dielectrics'),
    ('current', 'current and resistance'),
    ('everything', 'I struggle with everything'),
)

INT_ATTITUDE_PHYSICS_EXP_CHOICES = (
    ('-4', 'I am not at all confident in my ability to learn physics.'),
    ('-2', 'I am not confident in my ability to learn physics.'),
    ('2', 'I am confident in my ability to learn physics.'),
    ('4', 'I am very confident in my ability to learn physics.'),
)

INT_COURSE_CHOICES = (
    ('135', 'Physics 135'),
    ('235', 'Physics 235'),
    ('140', 'Physics 140'),
    ('240', 'Physics 240'),
)

INT_PAST_PHYSICS_WHEN_CHOICES = (
    ('1', 'last year'),
    ('2', '2 years ago'),
    ('3', '3 years ago'),
    ('4', '4 years ago'),
    ('5', '5 or more years ago'),
)

CINT_BDAY_MONTH_CHOICES = (
    ('-1', 'Month'),
    ('1', 'January'),
    ('2', 'February'),
    ('3', 'March'),
    ('4', 'April'),
    ('5', 'May'),
    ('6', 'June'),
    ('7', 'July'),
    ('8', 'August'),
    ('9', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
)

CTEXT_PARENT_ED_CHOICES = (
    ('Less_HS', 'Less than High School'),
    ('HS', 'High School/GED'),
    ('Some_College', 'Some College'),
    ('2_Year_College', '2-Year College Degree (Associates)'),
    ('4_Year_College', '4-Year College Degree (BA, BS)'),
    ('Masters', "Master's Degree"),
    ('Doctoral', 'Doctoral Degree'),
    ('Professional', 'Professional Degree (MD, JD)'),
)

INT_ATTITUDE_PHYSICS_NOEXP_CHOICES = (
    ('-4', 'I am not at all confident in my ability to learn physics.'),
    ('-2', 'I am not confident in my ability to learn physics.'),
    ('0', 'Since I have had no prior physics experience, I honestly do not know what to expect.'),
    ('2', 'I am confident in my ability to learn physics.'),
    ('4', 'I am very confident in my ability to learn physics.'),
)

INT_GOAL_GRADE_RESET_CHOICES = (
    ('8', 'A'),
    ('7', 'A-'),
    ('6', 'B+'),
    ('5', 'B'),
    ('4', 'B-'),
    ('3', 'C+'),
    ('2', 'C'),
    ('1', 'C- or below'),
    ('0', 'No thanks'),
)


class Source1(SubjectData):
    # add meta property
    class Meta: 
        db_table = 'mydata_source1'
    Reg_Enrolled = models.IntegerField(null=True, blank=True)
    Reg_GPA = models.FloatField(null=True, blank=True)
    Reg_Gender = models.CharField(max_length=5, null=True, blank=True)
    Reg_Acad_Level = models.CharField(max_length=20, null=True, blank=True)
    Reg_Course = models.IntegerField(null=True, blank=True)
    ssg_group = models.IntegerField(null=True, blank=True)
    Signup_Opt_Out = models.IntegerField(null=True, blank=True)
    HS_Activity = models.CharField(max_length=7, choices=TEXT_HS_ACTIVITY_CHOICES, null=True, blank=True)
    HS_Activity_Other = models.CharField(max_length=20, null=True, blank=True)
    Movie = models.CharField(max_length=8, choices=TEXT_MOVIE_CHOICES, null=True, blank=True)
    Movie_Other = models.CharField(max_length=50, null=True, blank=True)
    Course = models.IntegerField(null=True, blank=True)
    Another_Hard_Class = models.CharField(max_length=1, choices=INT_YES_NO_CHOICES, null=True, blank=True)
    Learner = models.CharField(max_length=8, choices=TEXT_LEARNER_CHOICES, null=True, blank=True)
    MP_Name = models.CharField(max_length=20, null=True, blank=True)
    Attitude_Exams = models.IntegerField(null=True, blank=True)
    Attitude_Anxiety = models.IntegerField(null=True, blank=True)
    Attitude_Physics_Noexp = models.IntegerField(null=True, blank=True)
    Attitude_Physics_Exp = models.IntegerField(null=True, blank=True)
    Attitude_Math = models.IntegerField(null=True, blank=True)
    SAT_Math = models.IntegerField(null=True, blank=True)
    ACT_Math = models.IntegerField(null=True, blank=True)
    HS_Math = models.IntegerField(null=True, blank=True)
    Past_Physics = models.IntegerField(null=True, blank=True)
    Past_Physics_Experience = models.IntegerField(null=True, blank=True)
    Past_Physics_When = models.IntegerField(null=True, blank=True)
    HS_Math_Other = models.TextField(null=True, blank=True)
    Goal_Grade = models.IntegerField(null=True, blank=True)
    Confidence = models.IntegerField(null=True, blank=True)
    Partner = models.CharField(max_length=15, choices=TEXT_PARTNER_CHOICES, null=True, blank=True)
    Reason = models.CharField(max_length=17, choices=TEXT_REASON_CHOICES, null=True, blank=True)
    SLC_Interest = models.CharField(max_length=17, choices=TEXT_SLC_INTEREST_CHOICES, null=True, blank=True)
    FCI_PreTest = models.FloatField(null=True, blank=True)
    FCI_PostTest = models.FloatField(null=True, blank=True)
    PreMathTest = models.FloatField(null=True, blank=True)
    redo_exam1 = models.IntegerField(null=True, blank=True)
    redo_exam2 = models.IntegerField(null=True, blank=True)
    redo_exam3 = models.IntegerField(null=True, blank=True)
    vote_exam1 = models.IntegerField(null=True, blank=True)
    vote_exam2 = models.IntegerField(null=True, blank=True)
    vote_exam3 = models.IntegerField(null=True, blank=True)
    Exam_1_Score = models.FloatField(null=True, blank=True)
    Exam_2_Score = models.FloatField(null=True, blank=True)
    Exam_3_Score = models.FloatField(null=True, blank=True)
    Exam_Final_Score = models.FloatField(null=True, blank=True)
    MP_PreExam_1 = models.FloatField(null=True, blank=True)
    MP_PreExam_2 = models.FloatField(null=True, blank=True)
    MP_Time_PreExam_2 = models.FloatField(null=True, blank=True)
    MP_PreExam_3 = models.FloatField(null=True, blank=True)
    MP_Time_PreExam_3 = models.FloatField(null=True, blank=True)
    Participation_PreExam_1 = models.FloatField(null=True, blank=True)
    Participation_PreExam_2 = models.FloatField(null=True, blank=True)
    Participation_PreExam_3 = models.FloatField(null=True, blank=True)
    ProblemRoulette_PreExam_2 = models.FloatField(null=True, blank=True)
    ProblemRoulette_Time_PreExam_2 = models.FloatField(null=True, blank=True)
    ProblemRoulette_PreExam_3 = models.FloatField(null=True, blank=True)
    ProblemRoulette_Time_PreExam_3 = models.FloatField(null=True, blank=True)
    Confidence_PreExam1 = models.CharField(max_length=100, null=True, blank=True)
    Confidence_PreExam2 = models.CharField(max_length=100, null=True, blank=True)
    Confidence_PreExam3 = models.CharField(max_length=100, null=True, blank=True)
    Confidence_PreFinal = models.CharField(max_length=100, null=True, blank=True)
    Goal_PreExam1_1 = models.TextField(null=True, blank=True)
    Goal_PreExam1_2 = models.TextField(null=True, blank=True)
    Goal_PreExam1_3 = models.TextField(null=True, blank=True)
    Goal_PreExam2_1 = models.TextField(null=True, blank=True)
    Goal_PreExam2_2 = models.TextField(null=True, blank=True)
    Goal_PreExam2_3 = models.TextField(null=True, blank=True)
    Goal_PreExam3_1 = models.TextField(null=True, blank=True)
    Goal_PreExam3_2 = models.TextField(null=True, blank=True)
    Goal_PreExam3_3 = models.TextField(null=True, blank=True)
    Goal_PreFinal_1 = models.TextField(null=True, blank=True)
    Goal_PreFinal_2 = models.TextField(null=True, blank=True)
    Goal_PreFinal_3 = models.TextField(null=True, blank=True)
    Reflection_PreExam2_1 = models.TextField(null=True, blank=True)
    Reflection_PreExam2_2 = models.TextField(null=True, blank=True)
    Reflection_PreExam3_1 = models.TextField(null=True, blank=True)
    Reflection_PreExam3_2 = models.TextField(null=True, blank=True)
    Reflection_PreFinal_1 = models.TextField(null=True, blank=True)
    Reflection_PreFinal_2 = models.TextField(null=True, blank=True)
    PT1_PreviousStudy__none = models.NullBooleanField()
    PT1_PreviousStudy__lecturenotes = models.NullBooleanField()
    PT1_PreviousStudy__lecturevideos = models.NullBooleanField()
    PT1_PreviousStudy__readbook = models.NullBooleanField()
    PT1_PreviousStudy__bookprobs = models.NullBooleanField()
    PT1_PreviousStudy__masteringphysics = models.NullBooleanField()
    PT1_PreviousStudy__officehours = models.NullBooleanField()
    PT1_PreviousStudy__physicshelproom = models.NullBooleanField()
    PT1_PreviousStudy__studygroup = models.NullBooleanField()
    PT1_PreviousStudy__problemroulette = models.NullBooleanField()
    PT1_PreviousStudy__practiceexam = models.NullBooleanField()
    PT1_PreviousStudy__outsideresource = models.NullBooleanField()
    PT1_ProbStruggle_135 = models.CharField(max_length=17, choices=TEXT_PROBLEMTOPIC_135_CHOICES, null=True, blank=True)
    PT1_ProbStruggle_140 = models.CharField(max_length=14, choices=TEXT_PROBLEMTOPIC_140_CHOICES, null=True, blank=True)
    PT1_ProbStruggle_235 = models.CharField(max_length=23, choices=TEXT_PROBLEMTOPIC_235_CHOICES, null=True, blank=True)
    PT1_ProbStruggle_240 = models.CharField(max_length=17, choices=TEXT_PROBLEMTOPIC_240_CHOICES, null=True, blank=True)
    PT1_ProbConfident_135 = models.CharField(max_length=17, choices=TEXT_PROBLEMTOPIC_135_CHOICES, null=True, blank=True)
    PT1_ProbConfident_140 = models.CharField(max_length=14, choices=TEXT_PROBLEMTOPIC_140_CHOICES, null=True, blank=True)
    PT1_ProbConfident_235 = models.CharField(max_length=23, choices=TEXT_PROBLEMTOPIC_235_CHOICES, null=True, blank=True)
    PT1_ProbConfident_240 = models.CharField(max_length=17, choices=TEXT_PROBLEMTOPIC_240_CHOICES, null=True, blank=True)
    PT1_ProbSolvingStep = models.IntegerField(null=True, blank=True)
    PT1_ProbStruggleImprovedConf = models.IntegerField(null=True, blank=True)
    PT1_ProbStruggle2_135 = models.CharField(max_length=17, choices=TEXT_PROBLEMTOPIC_135_CHOICES, null=True, blank=True)
    PT1_ProbStruggle2_140 = models.CharField(max_length=14, choices=TEXT_PROBLEMTOPIC_140_CHOICES, null=True, blank=True)
    PT1_ProbStruggle2_235 = models.CharField(max_length=23, choices=TEXT_PROBLEMTOPIC_235_CHOICES, null=True, blank=True)
    PT1_ProbStruggle2_240 = models.CharField(max_length=17, choices=TEXT_PROBLEMTOPIC_240_CHOICES, null=True, blank=True)
    PT1_ApplyingMath = models.IntegerField(null=True, blank=True)
    PT1_ConceptualProbs = models.IntegerField(null=True, blank=True)
    PT1_Notecard = models.IntegerField(null=True, blank=True)
    PT1_Timelimit = models.IntegerField(null=True, blank=True)
    Writing_Prompt_1 = models.TextField(null=True, blank=True)
    Writing_Prompt_2 = models.TextField(null=True, blank=True)
    Writing_Prompt_3 = models.TextField(null=True, blank=True)
    Writing_Prompt_4 = models.TextField(null=True, blank=True)
    Writing_Prompt_5 = models.TextField(null=True, blank=True)
    Writing_Prompt_6 = models.TextField(null=True, blank=True)
    Writing_Prompt_7 = models.TextField(null=True, blank=True)
    Writing_Prompt_8 = models.TextField(null=True, blank=True)
    Writing_Prompt_9 = models.TextField(null=True, blank=True)
    FeedbackExam1_ECoach_StudyHabits = models.IntegerField(null=True, blank=True)
    FeedbackExam1_ECoach_ExamPrep = models.IntegerField(null=True, blank=True)
    FeedbackExam1_ECoach_Helpful = models.TextField(null=True, blank=True)
    FeedbackExam1_ECoach_Change = models.TextField(null=True, blank=True)
    FeedbackExam1_StudyGroup_Attend = models.IntegerField(null=True, blank=True)
    FeedbackExam1_StudyGroup_New = models.IntegerField(null=True, blank=True)
    FeedbackExam1_StudyGroup_Helpful = models.TextField(null=True, blank=True)
    FeedbackExam1_StudyGroup_Change = models.TextField(null=True, blank=True)
    FeedbackExam1_PhysicsHelpRoom_Attend = models.IntegerField(null=True, blank=True)
    FeedbackExam1_PhysicsHelpRoom_Reason = models.CharField(max_length=8, choices=TEXT_PHYSICSHELPROOMREASON_CHOICES, null=True, blank=True)
    FeedbackExam1_PhysicsHelpRoom_Reason_Other = models.CharField(max_length=50, null=True, blank=True)
    FeedbackExam1_PhysicsHelpRoom_Helpful = models.TextField(null=True, blank=True)
    FeedbackExam1_PhysicsHelpRoom_Change = models.TextField(null=True, blank=True)
    FeedbackExam1_PeerAdvice = models.TextField(null=True, blank=True)
    FeedbackExam2_PeerAdvice = models.TextField(null=True, blank=True)
    FeedbackExam3_PeerAdvice = models.TextField(null=True, blank=True)
    FeedbackFinal_PeerAdvice = models.TextField(null=True, blank=True)
    FeedbackFinal_StudyHabits = models.IntegerField(null=True, blank=True)
    FeedbackFinal_ExamPrep = models.IntegerField(null=True, blank=True)
    FeedbackFinal_Helpful = models.TextField(null=True, blank=True)
    FeedbackFinal_Change = models.TextField(null=True, blank=True)
    FeedbackFinal_OtherCourses_YesNo = models.IntegerField(null=True, blank=True)
    FeedbackFinal_OtherCourses_Text = models.TextField(null=True, blank=True)
    FeedbackFinal_Confidence = models.IntegerField(null=True, blank=True)
    FeedbackFinal_Major = models.IntegerField(null=True, blank=True)
    Writing_Prompt_10 = models.TextField(null=True, blank=True)
    Writing_Prompt_11 = models.TextField(null=True, blank=True)
    Writing_Prompt_12 = models.TextField(null=True, blank=True)
    Writing_Prompt_13 = models.TextField(null=True, blank=True)
    Writing_Prompt_14 = models.TextField(null=True, blank=True)
    Goal_Grade_Reset_initial = models.IntegerField(null=True, blank=True)
    Goal_Grade_Reset_postexam1 = models.IntegerField(null=True, blank=True)
    Goal_Grade_Reset_postexam2 = models.IntegerField(null=True, blank=True)
    Goal_Grade_Reset_postexam3 = models.IntegerField(null=True, blank=True)
    Pred_Grade_Initial_135 = models.FloatField(null=True, blank=True)
    Pred_Grade_Initial_235 = models.FloatField(null=True, blank=True)
    Pred_Grade_Initial_140 = models.FloatField(null=True, blank=True)
    Pred_Grade_Initial_240 = models.FloatField(null=True, blank=True)
    Pred_Grade_Exam1 = models.FloatField(null=True, blank=True)
    Pred_Grade_Exam2 = models.FloatField(null=True, blank=True)
    Pred_Grade_Exam3 = models.FloatField(null=True, blank=True)
    Pred_Grade_Final = models.FloatField(null=True, blank=True)
    Distribution_ID_135 = models.CharField(max_length=20, null=True, blank=True)
    Distribution_ID_235 = models.CharField(max_length=20, null=True, blank=True)
    Distribution_ID_140 = models.CharField(max_length=20, null=True, blank=True)
    Distribution_ID_240 = models.CharField(max_length=20, null=True, blank=True)
    GradeDistribution = models.TextField(null=True, blank=True)
    GradeDistribution_Peak = models.CharField(max_length=20, null=True, blank=True)
    GradeDistribution_LeftShade = models.CharField(max_length=20, null=True, blank=True)
    GradeDistribution_RightShade = models.CharField(max_length=20, null=True, blank=True)

class EmptySource(SubjectData):
    pass

class Common1(SubjectData):
    # add meta property
    class Meta: 
        db_table = 'mydata_common1'
    First_Name = models.CharField(max_length=20, null=True, blank=True)
    Last_Name = models.CharField(max_length=20, null=True, blank=True)
    uniqname = models.CharField(max_length=20, null=True, blank=True)
    Gender = models.CharField(max_length=1, choices=CTEXT_GENDER_CHOICES, null=True, blank=True)
    BirthDay = models.IntegerField(null=True, blank=True)
    BirthMo = models.IntegerField(null=True, blank=True)
    BirthYr = models.IntegerField(null=True, blank=True)
    Semesters_Completed = models.IntegerField(null=True, blank=True)
    College = models.CharField(max_length=11, choices=CTEXT_COLLEGE_CHOICES, null=True, blank=True)
    College_Other = models.CharField(max_length=30, null=True, blank=True)
    Concentrate__Engineering = models.NullBooleanField()
    Concentrate__Physics = models.NullBooleanField()
    Concentrate__Chemistry = models.NullBooleanField()
    Concentrate__Biology = models.NullBooleanField()
    Concentrate__Biology_MCDB = models.NullBooleanField()
    Concentrate__Biology_EEB = models.NullBooleanField()
    Concentrate__Health = models.NullBooleanField()
    Concentrate__Humanities = models.NullBooleanField()
    Concentrate__Math = models.NullBooleanField()
    Concentrate__Stats = models.NullBooleanField()
    Concentrate__Neurosci = models.NullBooleanField()
    Concentrate__Social_Science_not_Psych = models.NullBooleanField()
    Concentrate__Psych_BBCS = models.NullBooleanField()
    Concentrate__Education = models.NullBooleanField()
    Concentrate__IDK = models.NullBooleanField()
    Concentrate__Other = models.NullBooleanField()
    Concentrate_Other = models.CharField(max_length=30, null=True, blank=True)
    Declared = models.CharField(max_length=3, choices=CTEXT_YES_NO_CHOICES, null=True, blank=True)
    Class_Standing = models.CharField(max_length=9, choices=CTEXT_CLASS_STANDING_CHOICES, null=True, blank=True)
    Cum_GPA_Survey = models.IntegerField(null=True, blank=True)
    Employment = models.CharField(max_length=9, choices=CTEXT_EMPLOYMENT_STATUS_CHOICES, null=True, blank=True)
    Involved_In__Greek = models.NullBooleanField()
    Involved_In__Sports = models.NullBooleanField()
    Involved_In__Religious = models.NullBooleanField()
    Involved_In__Research = models.NullBooleanField()
    Involved_In__Volunteering = models.NullBooleanField()
    Involved_In__Music_Art = models.NullBooleanField()
    Involved_In__Other = models.NullBooleanField()
    Other_Commitment = models.CharField(max_length=30, null=True, blank=True)
    Post_College = models.CharField(max_length=13, choices=CTEXT_POST_COLLEGE_CHOICES, null=True, blank=True)
    Parent_Ed = models.CharField(max_length=14, choices=CTEXT_PARENT_ED_CHOICES, null=True, blank=True)
    High_School_CumGPA = models.IntegerField(null=True, blank=True)


